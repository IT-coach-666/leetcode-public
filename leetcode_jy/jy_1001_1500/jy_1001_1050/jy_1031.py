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
title_jy = "Maximum-Sum-of-Two-Non-Overlapping-Subarrays(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given an array nums of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths firstLen and secondLen.  (For clarification, the firstLen-length subarray could occur before or after the secondLen-length subarray.)
Formally, return the largest V for which V = (nums[i] + nums[i+1] + ... + nums[i+firstLen-1]) + (nums[j] + nums[j+1] + ... + nums[j+secondLen-1]) and either:
0 <= i < i + firstLen - 1 < j < j + secondLen - 1 < nums.length, or
0 <= j < j + secondLen - 1 < i < i + firstLen - 1 < nums.length.

Example 1:
Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

Example 2:
Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

Example 3:
Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
Note:
1. firstLen >= 1
2. secondLen >= 1
3. firstLen + secondLen <= nums.length <= 1000
4. 0 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    """
首先计算出数组的前缀和 prefix_sum, prefix_sum[i] = nums[0] + nums[1] + ... + nums[i - 1], 然后遍历数组, 对位置 i 来说, prefix_sum[i] - prefix_sum[i - secondLen] 为长度为 secondLen 的子数组和, 需要找到在这之前的长度为 firstLen 的最大子数组和, 两者相加为至今的最大子数组和, 而之前的长度为 firstLen 的子数组和为 prefix_sum[i - secondLen] - prefix_sum[i - firstLen - secondLen]; 因为满足条件的子数组不应定是 firstLen 在前, secondLen 在后, 所以需要调用两次方法, 求其中的较大值;
    """
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int,
                           secondLen: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)

        for i, n in enumerate(nums):
            prefix_sum[i + 1] = prefix_sum[i] + n

        return max(self._max_sum(prefix_sum, firstLen, secondLen),
                   self._max_sum(prefix_sum, secondLen, firstLen))

    def _max_sum(self, prefix_sum, first_length, second_length):
        max_left_sum = 0
        max_sum = 0

        for i in range(first_length + second_length, len(prefix_sum)):
            current_left_sum = prefix_sum[i - second_length] \
                               - prefix_sum[i - first_length - second_length]
            max_left_sum = max(max_left_sum, current_left_sum)
            right_sum = prefix_sum[i] - prefix_sum[i - second_length]
            max_sum = max(max_sum, max_left_sum + right_sum)

        return max_sum


