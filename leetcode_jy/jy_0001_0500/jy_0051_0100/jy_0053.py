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
title_jy = "Maximum-Subarray(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array nums, find the contiguous subarray (containing at least one
number) which has the largest sum and return its sum.

Example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.
"""


from typing import List
class Solution:
    """
此题类似: 152_Maximum_Product_Subarray.py

解法1: 使用动态规划求解, 用 dp[i] 表示以 nums[i] 结尾的子数组的最大和, 则:
dp[i] = max(dp[i-1] + nums[i], nums[i])

最大连续子数组即 dp 中的最大值;
    """
    def maxSubArray_v1(self, nums: List[int]) -> int:
        # jy: 初始化 dp, 值均为 0;
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        #print(dp)
        return max(dp)

    """
解法2: 类似解法1, 使用一个临时变量记录以 nums[i] 结尾的子数组的最大和, 同时与迄今为
止的最大子数组和进行比较并更新, 减少了空间复杂度;
    """
    def maxSubArray_v2(self, nums: List[int]) -> int:
        max_sum = nums[0]
        max_sum_so_far = nums[0]
        for i in range(1, len(nums)):
            max_sum_so_far = max(max_sum_so_far + nums[i], nums[i])
            max_sum = max(max_sum_so_far, max_sum)
        return max_sum

    """
解法3: 原理同解法2, 此处同时获取最大子数组的下标信息;
    """
    def maxSubArray_jy(self, nums: List[int]) -> int:
        max_sum = nums[0]
        idx_b = idx_e = 0
        max_sum_so_far = nums[0]
        for i in range(1, len(nums)):
            if max_sum_so_far + nums[i] >= nums[i]:
                max_sum_so_far = max_sum_so_far + nums[i]
                if max_sum_so_far > max_sum:
                    max_sum = max_sum_so_far
                    idx_e = i
            else:
                max_sum_so_far = nums[i]
                if max_sum_so_far > max_sum:
                    max_sum = max_sum_so_far
                    idx_b = idx_e = i
        return max_sum, idx_b, idx_e



nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#nums = [-2]
#nums = [-2, 1, -3]

res = Solution().maxSubArray_v1(nums)
print(res)

res = Solution().maxSubArray_v2(nums)
print(res)


res, idx_b, idx_e = Solution().maxSubArray_jy(nums)
print(res, " === ", sum(nums[idx_b: idx_e+1]))
print(nums[idx_b: idx_e+1])


