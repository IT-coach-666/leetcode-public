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
title_jy = "House-Robber(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed, the only constraint stopping you from robbing each of
them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night. Given an
integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police.

JY: 即统计数组中的值的和的最大值(统计的数不能是数组中相邻的两个数)

Example 1:
Input: nums = [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2, 7, 9, 3, 1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

from typing import List
class Solution:
    """
解法1: 使用动态规划求解, 记 dp[i] 为抢劫第 i 家时获得的最大收益, 分两种情况:
1) 刚抢劫了上一家, 由于不能连续抢劫, 所以跳过当前房子, 当前收益为抢劫上一家房子为止的收益, 即 dp[i-1]
2) 没有抢劫上一家, 则当前收益为抢劫当前房子和上上一家房子为止的收益和, 即 dp[i] + dp[i-2] 最后返回 dp 中的最大值;
    """
    def rob_v1(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return max(nums)
        # jy: dp[i] 表示抢劫第 i 家时获得的最大收益(均初始化为 0)
        dp = [0] * len(nums)
        # jy: dp[0] 初始化为 nums[0] (即第一家的储蓄; 默认每家的储蓄都是正数, 否则存在负数应该初始化为 max(0, nums[0]))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return max(dp)

    """
解法2: 这道题的动态规划本质上只使用了两个值, 即抢劫上一家为止的收益, 和抢劫上上一家为止的收益, 所以
用两个变量替代 dp 数组即可;
    """
    def rob_v2(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return max(nums)
        # jy: 记录上上一家为止的收益
        prev_prev = nums[0]
        # jy: 记录上一家为止的收益(该值每循环一次就会被更新为抢劫当前这家时得到的最大收益, 并成为下一轮循环的上一家收益)
        prev = max(nums[0], nums[1])

        # jy: 从 2 (即视为初次循环的当前家, 上一家即为以上初始化的截止第二家的 prev, 上上一家即为以上初始化的第一家
        #    的 prev_prev) 开始循环, 每循环一次 prev 就会被更新为抢劫当前这家时得到的最大收益, 并成为下一轮循环的
        #    上一家收益;
        for i in range(2, len(nums)):
            prev, prev_prev = max(prev_prev + nums[i], prev), prev

        return prev


nums = [1, 2, 3, 1]
# Output: 4
res = Solution().rob_v1(nums)
print(res)

nums = [2, 7, 9, 3, 1]
# Output: 12
res = Solution().rob_v1(nums)
print(res)


