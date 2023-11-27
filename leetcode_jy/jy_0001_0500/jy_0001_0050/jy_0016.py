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
tag_jy = "类似 0015（）"



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
        # jy: 遍历 nums 至倒数第三个元素 (遍历至倒数第三个元素时, 对应的
        #     双指针即为最后两个数值)
        for i in range(n - 2):
            # jy: 优化 1
            if i and nums[i] == nums[i - 1]:
                continue

            # jy: 记录 two sum 的最优目标值 k (two sum 越接近 k 值越好),
            #     后续双指针需基于该值进行移动
            k = target - nums[i]
            low, high = i+1, n-1
            while low < high:
                # jy: 计算 3 数之和与目标值之间的差值
                diff = nums[i] + nums[low] + nums[high] - target
                # jy: 如果差值小于已知差值的最小差值 (注意是绝对值之间进
                #     行比较), 则更新最小差值 (更新时是更新原值, 而非绝对值)
                if abs(diff) < abs(min_diff):
                    min_diff = diff

                # jy: 如果当前 2 数之和等于最优目标值 k, 则直接退出循环
                if nums[low] + nums[high] == k:
                    return target + min_diff

                # jy: 如果小于 k, 则 low 指针往前移, 如果大于 k, 则 high 指针
                #     往左移, 使得两数之和往接近最优目标值的方向靠
                if nums[low] + nums[high] < k:
                    low += 1
                else:
                    high -= 1
        # jy: 最后返回的目标值与最小差值的和即为最接近的值;
        return target + min_diff


    def threeSumClosest_v2(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = sys.maxsize
        for i in range(n - 2):
            # jy: 如果当前数值与前一数值相同, 则跳过, 防止重复计算
            if i and nums[i] == nums[i-1]:
                continue 

            # jy: 如果后三个数的值大于目标值 target, 则可终止后续的遍历, 因
            #     为后续的三个数的值只会更大; 同时需判断当前的后三个数之和与
            #     目标值的差是否更小, 如果是, 则更新最终结果为当前三个数之和
            s = nums[i] + nums[i+1] + nums[i+2]
            if s > target: 
                if s - target < min_diff:
                    ans = s 
                break

            # jy: 如果当前数值与最后两个数的和仍小于目标值, 则当前数值加上其后
            #     的两个数只会更小, 包含当前数值的三个数中, 剩余两个数为最后两
            #     个较大的数时是更接近目标值的, 此时判断与目标值之差是否更小,
            #     如果更小则更新最终结果为这三数之和
            s = nums[i] + nums[-2] + nums[-1]
            if s < target: 
                if target - s < min_diff:
                    min_diff = target - s
                    ans = s
                continue

            # 双指针
            low, high = i+1, n-1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if s == target:
                    return s
                if s > target:
                    if s - target < min_diff:  # s 与 target 更近
                        min_diff = s - target
                        ans = s
                    high -= 1
                else:  # s < target
                    if target - s < min_diff:  # s 与 target 更近
                        min_diff = target - s
                        ans = s
                    low += 1
        return ans


nums = [-1, 2, 1, -4]
target = 1
res = Solution().threeSumClosest_v1(nums, target)
print(nums, " === ", target, " === ", res )


res = Solution().threeSumClosest_v2(nums, target)
print(nums, " === ", target, " === ", res )



