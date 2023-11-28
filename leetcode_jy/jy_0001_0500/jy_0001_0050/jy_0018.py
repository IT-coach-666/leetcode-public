# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
from typing import List, Dict
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "4Sum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "参考 3Sum、Two Sum"


"""
Given an array `nums` of `n` integers and an integer `target`, are there
elements `a`, `b`, `c`, and `d` in nums such that `a + b + c + d = target`?

Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[ [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]]
"""


from typing import List
class Solution:
    """
有了 3Sum (0015) 的经验, 此题等价于遍历数组, 然后在其余的元素中求解 3Sum, 算
法的时间复杂度是 O(n^3)
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # jy: 对列表进行排序
        nums.sort()
        sums = []
        # jy: 遍历数组元素至倒数第 4 个数 (到倒数第 4 个数后, 剩余的最后 3 个
        #     只能再组成一组四元组)
        for i in range(len(nums)-3):
            # jy: 如果当前数值与前一轮的数值相同, 则直接跳过, 避免重复
            if i and nums[i] == nums[i-1]:
                continue

            # jy: 遍历数组中的剩余数值, 找出满足要求的剩余 3 个数
            for j in range(i+1, len(nums)-2):
                # jy: 如果当前数值与前一轮的数值相同, 则直接跳过, 避免重复
                if j-1 >= i+1 and nums[j] == nums[j-1]:
                    continue

                # jy: 找出两数之和为 k 的结果
                k = target - nums[i] - nums[j]
                # jy: 两数的范围由第二个数的后一个开始算起(下标为 j+1), 到最
                #     后一个;
                low, high = j+1, len(nums)-1
                while low < high:
                    if nums[low] + nums[high] == k:
                        sums.append([nums[i], nums[j], nums[low], nums[high]])
                        # jy: 如果双指针的下一相邻数值与当前相同, 则将指针移动
                        #     至下一数值
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < k:
                        low += 1
                    else:
                        high -= 1
        return sums


nums = [1, 0, -1, 0, -2, 2]
target = 0
res = Solution().fourSum(nums, target)
print(nums, " === ", target, " === ", res)



