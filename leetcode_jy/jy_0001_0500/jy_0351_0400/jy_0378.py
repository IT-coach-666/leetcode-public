# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
assert project_name == "leetcode_jy" and project_name == "leetcode_jy" and \
       url_ == "www.yuque.com/it-coach"
from typing import List, Dict
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Kth-Smallest-Element-in-a-Sorted-Matrix(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an ``n x n`` matrix where each of the rows and columns are sorted in ascending
order, return the ``kth`` smallest element in the matrix. Note that it is the kth
smallest element in the sorted order, not the ``kth`` distinct element.


Example 1:
Input: matrix =
[[1,  5,  9],
 [10, 11, 13],
 [12, 13, 15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1, 5, 9, 10, 11, 12, 13, 13, 15],
             and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5


Constraints:
n == matrix.length
n == matrix[i].length
1 <= n <= 300
-10^9 <= matrix[i][j] <= 10^9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n^2
"""


import bisect
from heapq import heappush, heappop
from typing import List
import sys



class Solution:
    """
解法1: 该题等价于从 n 个有序数组中找到第 k 小的数, n 个有序数组就是矩阵的每一行;
初始化一个最小堆, 保存矩阵第一列的数字, 然后遍历 k-1 次, 每次弹出堆顶的元素, 将
该元素对应矩阵行中的下一个元素放入堆中; k-1 次操作后, 堆顶的元素就是第 k 小的元素;
    """
    def kthSmallest_v1(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        # jy: 初始化一个最小堆, 保留矩阵第一列的数值; 以元组的形式保留, 元组格式如下:
        #     (第一列的元素值, 列号, 行元素列表)
        #     如果 k 值比列数还小, 则没必要保留第一列的所有元素, 保留第一列的前 k 个元
        #     素即可, 因为后面的元素肯定不在第 k 小的范围内了
        for i in range(min(k, len(matrix))):
            heappush(min_heap, (matrix[i][0], 0, matrix[i]))
        # jy: 遍历 k-1 次, 每次弹出堆顶元素(即最小值), 并将该元素所在的行中的下一个元素
        #     加入堆中, 确保截止当前为止, 除去已出堆元素之外的最小的元素在堆中(出堆后剩
        #     余元素中的最小值只可能是出堆元素所在行的下一个元素或出堆元素所在列或该列之
        #     前的列中的元素) 该逻辑确保每次出堆的元素值将是严格按照二维数组中数值的从小
        #     到大进行出堆, 即出堆 k-1 次后, 前 k-1 小的元素都出堆了, 此时的堆顶元素即为
        #     第 k 小的元素;
        for _ in range(k-1):
            # jy: i 为当前最小值元素所在的列下标, row 为当前最小值元素所在的行的所有元素;
            _num, i, row = heappop(min_heap)
            # jy: 如果 i+1 仍为有效的下标, 则将该下标对应的元素入堆;
            if i+1 < len(row):
                heappush(min_heap, (row[i+1], i+1, row))
        # jy: 经过以上 k-1 次循环后, 最小堆的堆顶即为第 k 小的元素;
        return min_heap[0][0]

    """
解法2: 使用二分查找法, 初始定义 low 和 high 为矩阵的第一个和最后一个元素, 每次求得 middle
时计算矩阵中有多少个数值小于等于 middle (注意, 此处的 middle 不是下标中值, 是最大数与最小
数的中值), 如果该数小于 k, 则将 low 置为 middle+1, 否则将 high 置为 middle; 需注意:
1) 由于 middle 不一定存在于矩阵中, 故 count == k 时不能就直接返回 middle;
2) 最后返回的 low 一定存在矩阵中吗? 这个问题要结合第一个问题来看, 当 count == k 时, 虽然 middle 不一定
   存在于矩阵中, 但可以确定的是矩阵中存在 k 个数小于等于 middle, 而实际第 k 小的数必然是矩阵中比 middle 小
   的数中的最大值, 所以需要缩小 middle 的值来定位实际第 k 小的数, 故通过移动 high 到 middle 来实现, 即不断
   缩小 [low, high] 区间的范围来定位实际第 k 小的数, 当 low == high 时, 就定位到了这个数, 即循环中断, 而循
   环中断前要么是 low 移动到 middle+1, 要么是 high 移动到 middle, 最终肯定出现 low = high 的情况, 即中止;
    """
    def kthSmallest_v2(self, matrix: List[List[int]], k: int) -> int:
        # jy: m 行 n 列;
        m, n = len(matrix), len(matrix[0])
        # jy: 获取二维数组中的最小值和最大值;
        low, high = matrix[0][0], matrix[m-1][n-1]

        while low < high:
            # jy: 求最小值与最大值之间的中值(该值不一定在二维数组中存在);
            middle = low + (high - low) // 2
            # jy: 找出二维数组 matrix 中小于或等于 middle 值的个数
            count = self._get_count_less_than_target_v2(matrix, m, n, middle)
            # jy: 如果二维数组中小于或等于 middle 值的个数小于 k, 表明该二维数组中第 k 小
            #     的元素肯定是大于 middle 的, 则将 low 赋值为 middle+1 后进行下一轮循环;
            if count < k:
                low = middle + 1
            # jy: 如果二维数组中小于或等于 middle 值的个数大于或等于 k, 表明该二维数组中第
            #     k 小的元素肯定是小于或等于 middle 的, 此时将 high 赋值为 middle, 进行下一
            #     轮循环;
            else:
                high = middle
        return low

    def _get_count_less_than_target_v2(self, matrix, m, n, middle):
        """
        找出行列均有序的二维数组 matrix 中小于或等于 middle 值的个数;
        传入值 m 和 n 分别为 matrix 二维矩阵的行和列;
        """
        count = 0
        # jy: j 为二维矩阵最后一列的下标值;
        j = n-1
        # jy: 遍历矩阵的行;
        for i in range(m):
            # jy: 如果 j 是有效列下标(大于等于 0), 且当前行的该列值大于 middle,
            #     则将 j 向左移, 直到该行中对应的该列值小于或等于 middle; 该外层
            #     for 循环即找出二维数组中小于或等于 middle 的值的个数;
            '''
            while j >= 0 and matrix[i][j] > middle:
                j -= 1
            '''
            # jy: 以上 while 循环是在 matrix[i] 中找到小于或等于 middle 值的下标,
            #     由于 matrix[i] 是有序的, 故可采用二分查找优化(基于 bisect 实现);
            j = bisect.bisect_right(matrix[i], middle) - 1
            # jy: 补充优化: 当 j < 0 时, 即可结束循环, 因为 j 列以下的值大于当前
            #     值, 当 j < 0 时, 后续的行已经不需要再进行判断, 肯定是没有小于或
            #     等于当前值的数了;
            if j < 0:
                break
            # jy: 由于 j 代表列下标, 该下标以及之前的元素总共有 j+1 个;
            count += j+1
        return count

    """
解法3: 对解法 2 进行优化: 当 count == k 时直接返回小于等于 middle 的数中的最大
值(在获取小于或等于 target 数的个数同时也获取小于等于 target 中的最大值);
    """
    def kthSmallest_v3(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        low, high = matrix[0][0], matrix[m-1][n-1]
        # jy: 注意, 此时 low = hight 时还不能终止循环, 还得继续找, 直到 low > high 才能终止循环;
        while low <= high:
            middle = low + (high - low) // 2
            # jy: 找出二维数组 matrix 中小于或等于 middle 值的个数, 并找出小于或等于 middle 的最大值;
            count, max_num = self._get_count_less_than_target_v3(matrix, m, n, middle)
            # jy: 如果二维数组中小于或等于 middle 值的个数小于 k, 表明该二维数组中第 k 小
            #     的元素肯定是大于 middle 的, 则将 low 赋值为 middle+1 后进行下一轮循环;
            if count < k:
                low = middle + 1
            # jy: 如果二维数组中小于或等于 middle 值的个数正好等于 k, 则直接返回小于或等于 middle 的
            #     最大值即为第 k 小元素;
            elif count == k:
                return max_num
            # jy: 如果二维数组中小于或等于 middle 值的个数大于 k, 表明该二维数组中第 k 小的元
            #     素肯定是小于 middle 的, 此时将 high 赋值为 middle-1, 进行下一轮循环;
            else:
                high = middle - 1

        return low

    def _get_count_less_than_target_v3(self, matrix, m, n, middle):
        """
        找出行列有序的二维数组 matrix 中小于或等于 middle 值的个数, 并找出小于或等
        于 middle 的最大值; 传入值 m 和 n 分别为 matrix 二维矩阵的行和列;
        """
        count = 0
        max_num = -sys.maxsize
        j = n-1
        for i in range(m):
            # jy: 如果 j 是有效列下标(大于等于 0), 且当前行的该列值大于 middle,
            #     则将 j 向左移, 直到该行中对应的该列值小于或等于 middle; 该外层
            #     for 循环即找出二维数组中小于或等于 middle 的值的个数;
            '''
            while j >= 0 and matrix[i][j] > middle:
                j -= 1
            '''
            # jy: 以上 while 循环是在 matrix[i] 中找到小于或等于 middle 值的下标,
            #     由于 matrix[i] 是有序的, 故可采用二分查找优化(基于 bisect 实现);
            j = bisect.bisect_right(matrix[i], middle) - 1
            # jy: 补充优化: 当 j < 0 时, 即可结束循环, 因为 j 列以下的值大于当前
            #     值, 当 j < 0 时, 后续的行已经不需要再进行判断, 肯定是没有小于或
            #     等于当前值的数了;
            if j < 0:
                break
            max_num = max(max_num, matrix[i][j])
            count += j+1
        return count, max_num


matrix = [
[1,  5,  9],
[10, 11, 13],
[12, 13, 15]]
k = 8
# Output: 13
res = Solution().kthSmallest_v1(matrix, k)
print(res)

matrix = [[-5]]
k = 1
# Output: -5
res = Solution().kthSmallest_v2(matrix, k)
print(res)


