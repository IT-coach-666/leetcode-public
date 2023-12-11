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
title_jy = "Find-K-Closest-Elements(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a sorted integer array ``arr``, two integers ``k`` and ``x``, return the ``k`` closest
integers to ``x`` in the array. The result should also be sorted in ascending order. An integer
``a`` is closer to ``x`` than an integer ``b`` if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


Constraints:
1 <= k <= arr.length1 <= arr.length <= 10^4
``arr`` is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4
"""


from typing import List

class Solution:
    """
解法1: 维护高低位首尾两个指针, 如果低位与 x 的差值大于高位与 x 的差值, 则低位加 1, 否则高位减 1;
    """
    def findClosestElements_v1(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr) - 1
        # jy: 当 high-low 等于 k 时, 还不能退出循环, 因为此时的 arr[low: high + 1] 共有 k+1 个
        #     数(即 arr[low] 至 arr[high] 共 high-low+1 个, 即 k+1 个数); 同时, 此时也不能就直
        #     接返回 arr[low: high], 虽然这共有 k 个数(即 arr[low] 至 arr[high-1], 相当于把 arr[high]
        #     抛弃), 但此时是不能确定 arr[low] 就是比 arr[high] 更接近 x 的, 还需要进一步比较才
        #     能判断;
        while high - low >= k:
            if abs(arr[low] - x) > abs(arr[high] - x):
                low += 1
            else:
                high -= 1

        return arr[low: high + 1]

    """
解法2: 在解法 1 的基础上, 利用数组的有序性使用二分查找进行优化; 因为需要找 k 个满足条件的
数, 由于数组的有序性, 满足条件的子数组的起始位置位于 0 至 len(arr)-k, 所以对于每一个满足
的 i, 需要在所有 arr[i ... i+k-1] 窗口中找到最符合条件的那个;

对 [0, len(arr)-k] 进行二分查找, 如果: x - arr[middle] > arr[middle + k] - x
说明 arr[middle] 距离 x 比 arr[middle + k] 距离 x 远, 注意 arr[middle] 是当
前窗口的第一个元素, 而 arr[middle + k] 是下一个窗口的最后一个元素, 所以窗口
arr[middle + 1 ... middle + k] 比窗口 arr[middle ... middle + k-1] 更优(因
为这两个窗口只有 arr[middle] 和 arr[middle + k] 不同, 剩下的元素都是相同的),
将 low 移动到 middle + 1 , 反之将 high 移动到 middle;
    """
    def findClosestElements_v2(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr) - k

        while low < high:
            middle = low + (high - low) // 2

            if x - arr[middle] > arr[middle + k] - x:
                low = middle + 1
            else:
                high = middle

        return arr[low: low + k]


arr = [1, 2, 3, 4, 5]
k = 4
x = 3
# Output: [1,2,3,4]
res = Solution().findClosestElements_v1(arr, k, x)
print(res)


arr = [1, 2, 3, 4, 5]
k = 4
x = -1
# Output: [1,2,3,4]
res = Solution().findClosestElements_v2(arr, k, x)
print(res)


