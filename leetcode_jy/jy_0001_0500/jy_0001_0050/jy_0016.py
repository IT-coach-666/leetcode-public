# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
from typing import List
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "3Sum-closest(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "类似 0015（条件略作转换: 与目标值的差值最小为目标）"



"""
Given an array `nums` of `n` integers and an integer `target`, find three
integers in `nums` such that the sum is closest to `target`. Return the sum
of the three integers. You may assume that each input would have exactly
one solution.


Example:
nums = [-1, 2, 1, -4]
target = 1
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    """
解法同 0015, 也是先将数组排序, 然后将问题转化为 Two Sum, 使用双指针求解

双指针循环时, 判断当前三数之和与 target 之差的绝对值是否比当前记录最小的
绝对值小, 如果是则更新最小的绝对值
    """
    def threeSumClosest_v1(self, nums: List[int], target: int) -> int:
        # jy: 对列表进行排序
        nums.sort()
        min_diff = sys.maxsize
        n = len(nums)
        ans = -1
        # jy: 遍历 nums 至倒数第三个元素 (遍历至倒数第三个元素时, 对应的
        #     双指针即为最后两个数值)
        for i in range(n - 2):
            # jy: 优化 1: 如果当前数值与前一数值相同, 则跳过, 防止重复计算
            if i and nums[i] == nums[i-1]:
                continue

            # jy: 优化 2: 如果后三个数的值大于目标值 target, 则可终止后续的
            #     遍历, 因为后续的三个数的值只会更大; 同时需判断当前的后三
            #     个数之和与目标值的差是否更小, 如果是则直接返回
            s3num = nums[i] + nums[i+1] + nums[i+2]
            if s3num > target:
                diff = s3num - target
                if diff < min_diff:
                    return s3num

            # jy: 优化 3: 如果当前数值与最后两个数的和仍小于目标值, 则当前数值
            #     加上其后的两个数只会更小, 包含当前数值的三个数中, 剩余两个数
            #     为最后两个较大的数时是更接近目标值的, 此时判断与目标值之差是
            #     否更小, 如果更小则更新最终结果为这三数之和
            s3num = nums[i] + nums[-2] + nums[-1]
            if s3num < target:
                diff = target - s3num
                if diff < min_diff:
                    min_diff = diff
                    ans = s3num
                continue

            # jy: 双指针, 基于双指针找出两数与当前数组成三数之和, 并计算其结果
            #     与目标值的差距, 如果与目标值相等, 则直接返回; 否则计算与目标
            #     的差距, 差距更小时, 则更新相应指针和最终返回结果
            low, high = i+1, n-1
            while low < high:
                s3num = nums[i] + nums[low] + nums[high]
                if s3num == target:
                    return s3num
                elif s3num > target:
                    diff = s3num - target
                    if diff < min_diff:
                        min_diff = diff
                        ans = s3num
                    high -= 1
                else:
                    diff = target - s3num
                    if diff < min_diff:
                        min_diff = diff
                        ans = s3num
                    low += 1
        return ans



nums = [-1, 2, 1, -4]
target = 1
res = Solution().threeSumClosest_v1(nums, target)
print(nums, " === ", target, " === ", res )


