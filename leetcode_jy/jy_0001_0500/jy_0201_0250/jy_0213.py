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
title_jy = "House-Robber-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""

"""
You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed. All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses
have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the
maximum amount of money you can rob tonight without alerting the police.



Example 1:
Input: nums = [2, 3, 2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

Example 2:
Input: nums = [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [0]
Output: 0


Constraints:
1 <= nums.length <= 1000 <= nums[i] <= 1000
"""




from typing import List

class Solution:
    """
由于第一座房子和最后一座房子首尾相连, 等价于抢劫 nums[0] — nums[n-2] 或
者 nums[1] — nums[n-1], 从而将问题变为求解两个 198_House-Robber.py
    """
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return max(self._rob(nums, 0, len(nums) - 2), self._rob(nums, 1, len(nums) - 1))

    def _rob(self, nums, start, end):
        prev_prev = nums[start]
        prev = max(nums[start], nums[start + 1])

        for i in range(start + 2, end + 1):
            prev, prev_prev = max(prev_prev + nums[i], prev), prev

        return prev

nums = [2, 3, 2]
# Output: 3
res = Solution().rob(nums)
print(res)


nums = [1, 2, 3, 1]
# Output: 4
res = Solution().rob(nums)
print(res)


