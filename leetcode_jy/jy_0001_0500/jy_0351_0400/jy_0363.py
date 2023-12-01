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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Max-Sum-of-Rectangle-No-Larger-Than-K(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an m x n matrix ``matrix`` and an integer ``k``, return the max sum of a rectangle
in the matrix such that its sum is no larger than k. It is guaranteed that there will be
a rectangle with a sum no larger than k.


Example 1: (图: https://www.yuque.com/frederick/dtwi9g/irl2ku)
Input: matrix = [[1, 0, 1], [0, -2, 3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the
             max number no larger than k (k = 2).

Example 2:
Input: matrix = [[2, 2, -1]], k = 3
Output: 3


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-10^5 <= k <= 10^5


Follow up: What if the number of rows is much larger than the number of columns?
"""


# jy: 该模块用于有序数组的相关操作(二分查找, 插入元素且保持继续有序, )
import bisect
import sys
from typing import List


class Solution:
    """
题解: 虽然是求解二维矩阵和, 但是可以转化为求解一维数组的连续子数组和不超过 k;
将二维数组的每一列相加, 得到的一维数组中连续子数组的和就对应子矩阵的和; 对每
一个可能的矩阵列和, 使用二分查找和前缀和求解最大连续子数组和不超过 k:
1) 遍历矩阵列和, 记当前列为 j
2) 记截止当前行, 各矩阵列相加的和为 sum_so_far
3) 记录各列矩阵和的前缀和, 记前缀和的每一个元素为, ..., 即
4) 使用二分查找在前缀和中查找 sum_so_far - k 应该插入的位置, 记为 i, 有 i <= j
5) 则有, 即, 即, 即, 即找到了一个子数组 [i, j] 满足和不超过 k
6) 将 sum_so_far 插入到前缀和中保持有序
    """
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # jy: 如果二维数组为空(python 中 [[]] 不认为是空, 而 [] 认为是空), 则返回 0;
        if not matrix or not matrix[0]:
            return 0
        # jy: row 行 column 列;
        row, column = len(matrix), len(matrix[0])
        # jy: 初始化最大和为一个很小的数值;
        max_sum = -sys.maxsize
        # jy: 遍历二维数组的每一行(i 从 0 开始); 以下两层 for 循环即构建第 i 行到第 j 行所组
        #    成的子矩阵, 并对属于相同列的元素求和, 形成一行结果: column_sum; 两层 for 循环即
        #    构建了所有连续相邻行的组合(当 i==j 时则表示只针对当前行进行处理)
        for i in range(row):
            # jy: 该行的每一列的值的和均初始化为 0;
            column_sum = [0] * column
            # jy: 遍历第 i 行到最后一行; 每遍历一行时, 将当前行
            for j in range(i, row):
                # jy: 遍历每一行的所有列, 将截止当前行的所有同列元素值进行相加(如果当前行只有一
                #    行, 则 colum_sum 对应的与该行元素等同; 如果有连续多行, 则 column_sum 为所
                #    有行中同列元素的和);
                for c in range(column):
                    column_sum[c] += matrix[j][c]

                max_sum = max(max_sum, self._max_sum(column_sum, k))

        return max_sum

    def _max_sum(self, column_sum, k):
        """
        传入的 column_sum 为所有相邻行中同列元素加和后的结果;
        该函数的作用即: 找出 column_sum 列表中的某一连续片段 column_sum[i:j], 在
        满足 sum(column_sum[i:j]) <= k 的情况下使得 sum(column_sum[i:j]) 尽可能大;
        最后返回的即该最大的 sum(column_sum[i:j]) 值;
        """
        # jy: 记录比 k 小但总和最大的值
        max_sum = -sys.maxsize
        # jy: 记录 column_sum 列表中截止当前位置的数值的总和;
        sum_so_far = 0
        # jy: 初始化 prefix_sums 的值为 [0], 表示 column_sum 中下标位置 0 之前的所有数值
        #    之和为 0;
        prefix_sums = [0]

        for n in column_sum:
            # jy: sum_so_far 记录 column_sum 中截止当前位置对应的数值的总和;
            sum_so_far += n
            # jy: 找出有序数组 prefix_sums 中插入 sum_so_far-k 时的插入位置(如果有序
            #    数组中有相同的数值, 则会返回第一个相同数值的位置下标供当前数值插入)
            #    假如 sum_so_far-k 小于 0, 则最开始插入的位置会是 0 所在的位置, 如果插
            #    入, 0 则往后移(当然, 后续插入时实际上插入的是 sum_so_far 的值, 此处判
            #    断 sum_so_far-k 的插入位置 i 是为了结合 i 判断是否更新 max_sum 的值:
            #    如果 i 小于 len(prefix_sums), 即表明 sum_so_far-k 的插入位置并不是
            #    prefix_sums 数组最后一个数值的后面; 此时根据 i 获取到的 prefix_sums[i]
            #    是个有效的数值, 其含义为 column_sum 中下标位置 i 之前(不含位置 i)的所有
            #    元素之和;
            i = bisect.bisect_left(prefix_sums, sum_so_far - k)
            # jy: 如果 sum_so_far - k 的插入位置 i 小于 len(prefix_sums), 则表明该位置 i 的原
            #    有值 prefix_sums[i] 存在, 且有:  sum_so_far - k <= prefix_sums[i], 即表明
            #    此时 sum_so_far - prefix_sums[i] <= k, 此时如果 sum_so_far - prefix_sums[i]
            #    大于之前的 max_sum, 则表明其为一个更合适的结果, 因此更新 max_sum;
            # jy: 如果 sum_so_far - k 的插入位置 i 大于或等于 len(prefix_sums), 则表明
            #    sum_so_far - k 大于当前 prefix_sums 中的最后一个数值(当前的最大值), 即:
            #    sum_so_far - k > prefix_sums[-1], 即 sum_so_far - prefix_sums[-1] > k,
            #    此时 sum_so_far 减去 prefix_sums 中的任一个数值的结果均会大于 k, 即
            #    sum_so_far - prefix_sums[x] 的结果均非合适的结果, 此时的 max_sum 不需要更新;
            # jy: 此处的 i 必定是大于等于 0 的, 因此以下 if 判断可以进一步省略前半部分 0 <= i 的逻辑
            # if 0 <= i < len(prefix_sums):
            if i < len(prefix_sums):
                max_sum = max(max_sum, sum_so_far - prefix_sums[i])

            # jy: 往有序列表 prefix_sums 中插入新元素 sum_so_far, 并保持插入后有序;
            bisect.insort(prefix_sums, sum_so_far)

        return max_sum


matrix = [[1, 0, 1], [0, -2, 3]]
k = 2
# Output: 2
res = Solution().maxSumSubmatrix(matrix, k)
print(res)

matrix = [[2, 2, -1]]
k = 3
# Output: 3
res = Solution().maxSumSubmatrix(matrix, k)
print(res)


matrix = [[2,2,-1]]
k = 0
res = Solution().maxSumSubmatrix(matrix, k)
print(res)

# jy: bisect 使用示例
"""
arr = [1,3,3,6,8,12,15]
value = 3
print(arr)
idx_left=bisect.bisect_left(arr,value)
print(idx_left)
print(arr)
idx_right=bisect.bisect_right(arr,value)
print(idx_right)
print(arr)
"""


