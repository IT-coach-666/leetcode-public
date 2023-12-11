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
title_jy = "Number-of-Longest-Increasing-Subsequence(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.

Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.


Constraints:
1 <= nums.length <= 2000
-10^6 <= nums[i] <= 10^6
"""


from typing import List


class Solution:
    """
在 300. Longest Increasing Subsequence 的基础上增加 counts[i] 表示以 nums[i] 结尾的最大增长子序列的个数
    """
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        counts = [0] * n

        for i in range(n):
            max_length = 1
            max_count = 1

            for j in range(i):
                if nums[j] >= nums[i]:
                    continue

                if dp[j] + 1 == max_length:
                    max_count += counts[j]
                elif dp[j] + 1 > max_length:
                    max_count = counts[j]
                    max_length = dp[j] + 1

            dp[i] = max_length
            counts[i] = max_count

        longest = max(dp)
        count = 0

        for i in range(n):
            if dp[i] == longest:
                count += counts[i]

        return count


