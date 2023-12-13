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
title_jy = "search-in-rotated-sorted-array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "二分查找 | 相似题: 0081 (数值可重复出现)"



"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand. i.e.: [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2]

You are given a target value to search. If found in the array return its index,
otherwise return -1. You may assume no duplicate exists in the array. Your 
algorithm's runtime complexity must be in the order of O(log n).


Example 1:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4

Example 2:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1

Example 3:
Input: nums = [3, 4, 5, 6, 7, 0, 1, 2], target = 4
Output: 1
"""


class Solution:
    """
解法 1: 二分查找

如果是一个普通升序数组, 只需要 mid 与 target 之间的简单判断:
a) 如果 nums[mid] == target, 则直接返回 mid 值
b) 如果 nums[mid] < target, 则 target 在 mid 的后半部分, low = mid+1
c) 如果 nums[mid] > target, 则 target 在 mid 的前半部分, high = mid-1

旋转升序数组从任意位置劈开后, 至少有一半是有序的, 因此可以先找到有序的一段, 然
后看 target 在不在这一段里, 如果在, 就把另一半丢弃; 如果不在, 就把这一段丢弃

在 nums[mid] 和 target 的基础上再结合 nums[high] 进行判断:
a) 如果 nums[mid] == target, 则直接返回 mid 值
b) 如果 nums[mid] > target, 根据 nums[high] 所处位置不同可分以下 3 种情况:
   1) target < nums[mid] < nums[high], 说明 target 在旋转数组的前半部分, high 移动到 mid-1
   2) nums[high] < target < nums[mid], 说明 target 在旋转数组的前半部分, high 移动到 mid-1
   3) target < nums[high] < nums[mid], 说明 target 在旋转数组的后半部分, low 移动到 mid+1
c) 如果 nums[mid] < target, 根据 nums[high] 所处位置不同可分 3 种情况: 
   1) target > nums[mid] > nums[high], 说明 target 在旋转数组的后半部分, low 移动到 mid+1
   2) nums[high] > target > nums[mid], 说明 target 在旋转数组的后半部分, low 移动到 mid+1
   3) target > nums[high] > nums[mid], 说明 target 在旋转数组的前半部分, high 移动到 mid-1
    """
    def search_v1(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            # jy: 注意 mid 值的计算方式
            mid = low + (high - low) // 2
            # jy: 如果 nums[mid] == target, 则直接返回 mid 值
            if nums[mid] == target:
                return mid

            # jy: 优先判断 nums[mid] 与 target 的值的大小
            #     如果 nums[mid] > target, 则需根据 nums[high] 所处位置判
            #     断 target 所在的区间
            if nums[mid] > target:
                if nums[mid] < nums[high] or nums[high] < target:
                    high = mid - 1
                else:
                    low = mid + 1
            # jy: nums[mid] < target 时对应的逻辑, 仍需根据 nums[high] 所
            #     处位置判断 target 所在的区间
            else:
                if nums[mid] >= nums[high] or nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


    """
解法 2: 同解法 1, 区别在于: 解法 1 中优先判断 nums[mid] 与 target 的大小,
当前解法优先判断 nums[mid] 和 nums[high] 的大小, 以确定哪一半是升序区间,
并判断 target 是否在该区间中, 从而进一步判断是更新 low 还是 high
    """
    def search_v2(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            # jy: 如果 mid 值即为目标值, 直接返回
            if nums[mid] == target:
                return mid

            # jy: 优先判断 nums[mid] 和 nums[high] 的值的大小;
            #     如果 mid 小于 high, 表明后半部分严格升序, 此时判断
            #     target 是否位于后半部分即可更新 low 或 high 值
            if nums[mid] < nums[high]:
                # jy: 当 target == nums[high] 时也更新 low, 使得不会错过正确值
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            # jy: 如果 mid 大于 high, 表明前半部分严格升序; 此时判断
            #     target 是否位于前半部分区间即可更新 low 或 high 值
            elif nums[mid] > nums[high]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # jy: 此处逻辑即 nums[mid] == nums[high], 只有当有序 pivot 数组
            #     中允许数值重复才有可能出现该情况 (如 0081)
            else:
                #high -= 1
                high = mid - 1
        return -1


    """
解法 3: 还可以优先判断 mid 和 low 的值进行分类处理
参见 0081 (Search-in-Rotated-Sorted-Array-II)
    """
    def search_v3(self, nums: List[int], target: int) -> int:
        pass



nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
res = Solution().search_v1(nums, target)
print(nums, " === ", target, " === ", res)

target = 3
res = Solution().search_v1(nums, target)
print(nums, " === ", target, " === ", res)


nums = [3, 4, 5, 6, 7, 0, 1, 2]
target = 4
res = Solution().search_v1(nums, target)
print(nums, " === ", target, " === ", res)


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
res = Solution().search_v2(nums, target)
print(nums, " === ", target, " === ", res)

target = 3
res = Solution().search_v2(nums, target)
print(nums, " === ", target, " === ", res)


nums = [3, 4, 5, 6, 7, 0, 1, 2]
target = 4
res = Solution().search_v2(nums, target)
print(nums, " === ", target, " === ", res)

