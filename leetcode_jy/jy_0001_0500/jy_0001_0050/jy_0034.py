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
title_jy = "Find-First-and-Last-Position-of-Element-in-Sorted-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "二分查找 (bisect 模块) | 双指针"



"""
Given an array of integers `nums` sorted in ascending order, find the starting 
and ending position of a given target value. If target is not found in the array, 
return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?


Example 1:
Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]

Example 2:
Input: nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]

Example 3:
Input: nums = [], target = 0
Output: [-1, -1]


Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""


class Solution:
    """
解法 1: 二分查找, 时间复杂度 O(log n), 空间复杂度为 O(1)
当数组元素都相同且目标值在数组中时, 时间复杂度退化到 O(n)

定位到与 target 相同的元素的位置, 然后以该元素为中心向左右两边搜索
    """
    def searchRange_v1(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            # jy: 如果 nums[mid] == target, 则基于 target 向两边延
            #     伸, 找到左右边界
            else:
                start, end = mid, mid
                while start >= 0 and nums[start] == target:
                    start -= 1
                while end < len(nums) and nums[end] == target:
                    end += 1
                # jy: 以上逻辑中的 start 和 end 最终均为不满足条件的下标
                #     位置, 需分别加 1 和减 1 后才是满足条件的边界位置
                return [start + 1, end - 1]
        return [-1, -1]


    """
解法 2: 两次二分查找, 时间复杂度 O(log n), 空间复杂度为 O(1)
该解法优于解法 1, 最坏情况下的时间复杂度也为 O(log n) 

第一次找 target 最左侧下标位置, 第二次找 target 最右侧下标位置
    """
    def searchRange_v2(self, nums: List[int], target: int) -> List[int]:
        start = self._binary_search(nums, target, True)
        end = self._binary_search(nums, target, False)
        return [start, end]

    def _binary_search(self, nums, target, find_first):
        """
        find_first: 为 True 时表明查找最左边的满足条件的值, 为 False 时表明
                    查找最右边的满足条件的值
        """
        # jy: 记录目标位置, 初始化为 -1 (表示不存在)
        obj_idx = -1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2

            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            # jy: nums[mid] == target 时, 不能确保 mid 是目标最左侧或最右侧的
            #     位置, 因此先更新目标位置, 同时缩小范围继续查找, 后续的查找中
            #     如果继续碰到满足要求的目标值, 则目标位置会被不断更新, 直至为
            #     最左侧或最右侧位置
            else:
                obj_idx = mid
                if find_first:
                    high = mid - 1
                else:
                    low = mid + 1
        return obj_idx


    """
解法 3: 进一步优化解法 2

解法 2 中两次二分查找的过程中有重复运算的部分, 此处避免重复运算
    """
    def searchRange_v3(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                idx_left = self._binary_search_boundary(
                        nums, target, low, mid)
                idx_right = self._binary_search_boundary(
                        nums, target, mid, high, False)
                return [idx_left, idx_right]
        return [-1, -1]

    def _binary_search_boundary(self, nums, target, low, high, boundary_left=True):
        """
        二分查找, 找出 nums[low: high+1] 中值为 target 的最左侧/最右侧的下标位置

        boundary_left: 为 True 时表明查找最左侧, 为 False 时表明查找最右侧
        """
        i = -1
        while low <= high:
            mid = low + (high - low) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                i = mid
                if boundary_left:
                    high = mid - 1
                else:
                    low = mid + 1
        return i


    """
解法 4: 逐个查找 (暴力查找), 时间复杂度 O(n), 空间复杂度 O(1) 

当数值大于 target 时可以提前终止查找过程
    """
    def searchRange_v4(self, nums: List[int], target: int) -> List[int]:
        # jy: 标记 start 是否已经找到 (也可去除该变量, 通过 start != -1 判断)
        is_start_found = False
        start = end = -1
        for idx, num in enumerate(nums):
            # jy: 如果当前值大于 target, 可提前终止查找过程
            if num > target:
                return [start, end]

            if num == target and not is_start_found:
                start = end = idx
                is_start_found = True
            elif num == target:
                end = idx
        return [start, end]


    """
解法 5: 同解法 1, 但二分查找基于 bisect 包实现
    """
    def searchRange_v5(self, nums: List[int], target: int) -> List[int]:
        import bisect
        idx_left = bisect.bisect_left(nums, target)
        if idx_left == len(nums) or nums[idx_left] != target:
            return [-1, -1]

        idx_right = idx_left
        while idx_right < len(nums) and nums[idx_right] == target:
            idx_right += 1
        return [idx_left, idx_right - 1]

    """
解法6: 同解法 2, 但二分查找用 bisect 包实现
    """
    def searchRange_v6(self, nums: List[int], target: int) -> List[int]:
        import bisect
        idx_left = bisect.bisect_left(nums, target)
        idx_right = bisect.bisect_right(nums, target)
        if idx_left == len(nums) or nums[idx_left] != target:
            return [-1, -1]
        return [idx_left, idx_right - 1]


    """
解法 7: 双指针法, 时间复杂度 O(n), 空间复杂度 O(1)

当 nums 中目标值范围特别大且比较居中时适合
    """
    def searchRange_v7(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        while low <= high:
            if nums[low] != target:
                low += 1
            if nums[high] != target:
                high -= 1
            if low <= high and nums[low] == nums[high] and nums[low] == target:
                return [low, high]
        return [-1, -1]


nums = [5, 7, 7, 8, 8, 10]
target = 8
res = Solution().searchRange_v1(nums, target)
print(nums, " === ", target, " === ", res)
res = Solution().searchRange_v2(nums, target)
print(nums, " === ", target, " === ", res)

res = Solution().searchRange_v3(nums, target)
print(nums, " === ", target, " === ", res)


target = 6
res = Solution().searchRange_v4(nums, target)
print(nums, " === ", target, " === ", res)
res = Solution().searchRange_v5(nums, target)
print(nums, " === ", target, " === ", res)

nums = []
target = 0
res = Solution().searchRange_v6(nums, target)
print(nums, " === ", target, " === ", res)

nums = [5, 7, 7, 8, 10]
target = 8
res = Solution().searchRange_v7(nums, target)
print(nums, " === ", target, " === ", res)



