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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Maximize-Sum-Of-Array-After-K-Negations(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array nums of integers, we must modify the array in the following way: we choose an i and replace nums[i] with -nums[i], and we repeat this process k times in total.  (We may choose the same index i multiple times.)
Return the largest possible sum of the array after modifying it in this way.

Example 1:
Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose indices (1,) and nums becomes [4,-2,3].

Example 2:
Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

Example 3:
Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
Note:
1. 1 <= nums.length <= 10000
2. 1 <= k <= 10000
3. -100 <= nums[i] <= 100
"""


from typing import List
import heapq


class Solution:
    """
解法1: 首先将数组排序, 遍历数组, 只要 k 大于0且当前数字小于等于0就将当前数字取反, 若经过此操作后 k 仍大于0, 需判断 k 是否为奇数, 因为可以对同一个数字重复取反, 所以如果 k 为偶数则随便找个数字取反偶数次即可不会影响最终结果, 只有当 k 为奇数次时需要做额外的取反操作, 取反时需要比较当前数字和前一个数字的大小(当 k 经过操作后大于0说明数组中的负数的个数小于 k, 此时当前数字为正数, 前一个数字取反后现在也为正数), 取反较小的数最终的数组和才会较大;
    """
    def largestSumAfterKNegations_v1(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        i = 0

        while k > 0 and sorted_nums[i] <= 0:
            sorted_nums[i] = -sorted_nums[i]
            k -= 1
            i += 1

        if k & 1 == 1:
            target = i

            if i > 0 and sorted_nums[i - 1] < sorted_nums[i]:
                target = i - 1

            sorted_nums[target] = -sorted_nums[target]

        return sum(sorted_nums)

    """
解法2: 将数组中的元素放入一个小顶堆, 遍历 k, 每次取出堆顶的元素取反后再放入堆;
    """
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heap = [n for n in nums]
        heapq.heapify(heap)

        for _ in range(k):
            heapq.heappush(heap, -heapq.heappop(heap))

        return sum(heap)


