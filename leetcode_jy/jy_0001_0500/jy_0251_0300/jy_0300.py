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
title_jy = "Longest-Increasing-Subsequence(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an unsorted array of integers, find the length of longest increasing subsequence(LIS).


Example:
Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.


Note: There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.


Follow up: Could you improve it to O(n * logn) time complexity?
"""


from typing import List


class Solution:
    """
解法1: 使用动态规划求解, 记 dp[i] 为以 nums[i] 结尾的最长增长子序列, 则 dp[i] = max(dp[0], dp[1], ... dp[i-1]) + 1,
且对于 i 之前的数 j 需满足 nums[i] > nums[j];
    """
    def lengthOfLIS_v1(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0] * len(nums)

        for i in range(len(nums)):
            dp[i] = max([dp[j] for j in range(i) if nums[j] < nums[i]], default=0) + 1

        return max(dp)


    """
解法2: 额外维护一个最长子序列的数组 lis, 然后遍历 nums, 如果当前数字 number 比 lis 的最后一个数字大,
则追加 number 到 lis 末尾, 否则使用二分查找找到 lis 中大于 number 的数中的最小值, 将它替换成 number;
    """
    def lengthOfLIS_v2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lis = []
        # jy: 遍历 nums
        for number in nums:
            # jy: 如果 lis 为空或者 number 比 lis 中的最后一个大, 则将 number 加入 lis 中;
            if not lis or number > lis[-1]:
                lis.append(number)
            # jy: 如果 number 比 lis 的最后一个值小, 则找出(二分查找) lis 中大于 number 的数中的最小
            #    值, 并将它替换为 number (由于替换的不一定是最后一个数值, 所以替换后的 lis 结果并不
            #    一定遵循原先的数值大小间相对)
            else:
                low, high = 0, len(lis) - 1

                while low <= high:
                    middle = (low + high) // 2

                    if lis[middle] < number:
                        low = middle + 1
                    else:
                        high = middle - 1
                # jy: 经过以上 while 循环后, low 大于 high, 对应的是大于 number 的最小值;
                lis[low] = number
        # jy: lis 结果并非真正的数值相对位置结果
        print(lis)
        return len(lis)

    def lengthOfLIS_jy(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lis = []
        # jy: 遍历 nums
        for idx, number in enumerate(nums):
            ls_tmp = [number]
            for num_tmp in nums[idx+1: ]:
                if num_tmp > ls_tmp[-1]:
                    ls_tmp.append(num_tmp)
            if len(ls_tmp) > len(lis):
                lis = ls_tmp
        # jy: lis 的结果为目标结果(如果有多种结果组合, 则是其中一种)
        print(lis)
        return len(lis)

# nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [10, 9, 2, 5, 1, 7, 101, 18]
# Output: 4
res = Solution().lengthOfLIS_v1(nums)
print(res)

res = Solution().lengthOfLIS_v2(nums)
print(res)


res = Solution().lengthOfLIS_jy(nums)
print(res)


