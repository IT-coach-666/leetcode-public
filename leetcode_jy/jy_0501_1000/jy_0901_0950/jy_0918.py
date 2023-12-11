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
title_jy = "Maximum-Sum-Circular-Subarray(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:
Input: nums = [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:
Input: nums = [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:
Input: nums = [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1


Constraints:
n == nums.length
1 <= n <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
"""

from typing import List


class Solution:
    """
在 53. Maximum Subarray 的基础上将数组变成了环形数组, 最大连续子数组和有两种情况:
1. 在数组的中间位置
2. 由数组头和数组尾组成
第一种情况就是 53. Maximum Subarray, 第二种情况等价于在数组中间位置求连续的子数组, 其和为最小, 最后返回两种情况下的最大值, 不过要注意一点, 当数组中元素都是负数时, 第二种情况下求得的最大连续子数组和为0, 不应该返回此值;
    """
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, max_sum, max_so_far, min_sum, min_so_far = \
            nums[0], nums[0], nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            max_so_far = max(max_so_far + n, n)
            max_sum = max(max_sum, max_so_far)
            min_so_far = min(min_so_far + n, n)
            min_sum = min(min_sum, min_so_far)
            total += n

        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum



