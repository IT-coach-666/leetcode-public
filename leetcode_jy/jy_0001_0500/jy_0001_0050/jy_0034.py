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
tag_jy = ""



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


from typing import List
import bisect


class Solution:
    """
解法1: 二分查找定位到与 target 相同的元素的位置, 然后以该元素为中心向左右两边搜索;
时间复杂度: O(log n); 当数组元素都相同且目标值在数组中时, 时间复杂度退化到 O(n);
空间复杂度: O(1)
    """
    def searchRange_v1(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        while low <= high:
            middle = low + (high - low) // 2
            if nums[middle] > target:
                high = middle - 1
            elif nums[middle] < target:
                low = middle + 1
            # jy: 如果 nums[middle] == target, 则基于 target 向两边延伸, 找到左右边界;
            else:
                start, end = middle, middle
                while start >= 0 and nums[start] == target:
                    start -= 1
                while end < len(nums) and nums[end] == target:
                    end += 1
                # jy: 注意: 以上逻辑中的 start 和 end 最终均为不满足条件的边界的位置, 需
                #     分别加 1 和减 1 后才是满足条件的边界位置;
                return [start + 1, end - 1]
        return [-1, -1]

    """
解法2: 两次二分查找, 第一次找 target 最左侧下标位置, 第二次找 target 最右侧下标位置;
时间复杂度: O(log n)
空间复杂度: O(1)
    """
    def searchRange_v2(self, nums: List[int], target: int) -> List[int]:
        start = self._binary_search(nums, target, True)
        end = self._binary_search(nums, target, False)
        return [start, end]

    def _binary_search(self, nums, target, find_first):
        # jy: 记录 nums 中值为 target 的下标位置, 初始化为 -1, 表示不存在;
        i = -1
        low, high = 0, len(nums)-1
        while low <= high:
            middle = low + (high-low) // 2
            if target > nums[middle]:
                low = middle + 1
            elif target < nums[middle]:
                high = middle - 1
            # jy: 第一次执行到以下 else 逻辑时即 target == nums[middle], 但并不能确保
            #     nums[middle] 是 nums 中的第 1 个还是最后 1 个; 于是先将当前对应值为
            #     target 的下标位置 middle 赋值给 i, 随后根据 find_first 判断是向左或
            #     向右迭代, 直到找出目标位置为止(如果左侧或右侧找不到值为 target 的下标
            #     位置, 则最终会返回 i, 如果找到则会更新 i, 并直到找不到为止将 i 返回);
            else:
                i = middle
                if find_first:
                    high = middle - 1
                else:
                    low = middle + 1
        return i

    """
解法3: 对解法 2 进行优化: 解法 2 中两次二分查找的过程中有重复运算的部分, 此处将避免重复运算;
时间复杂度: O(log n)
空间复杂度: O(1)
    """
    def searchRange_v3(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = low + (high - low) // 2
            if target > nums[middle]:
                low = middle + 1
            elif target < nums[middle]:
                high = middle - 1
            else:
                idx_left = self._binary_search_boundary(nums, target, low, middle)
                idx_right = self._binary_search_boundary(nums, target, middle, high,
                                                         False)
                return [idx_left, idx_right]
        return [-1, -1]

    def _binary_search_boundary(self, nums, target, low, high, boundary_left=True):
        """
        jy: 二分查找, 找出 nums[low: high+1] 中值为 target 的最左侧/最右侧的下标位置;
        """
        i = -1
        while low <= high:
            middle = low + (high - low) // 2
            if target > nums[middle]:
                low = middle + 1
            elif target < nums[middle]:
                high = middle - 1
            else:
                i = middle
                if boundary_left:
                    high = middle - 1
                else:
                    low = middle + 1
        return i

    """
解法 4: 逐个查找, 当数值大于 target 时可以提前终止查找过程;
时间复杂度: O(n)
空间复杂度: O(1)
    """
    def searchRange_v4(self, nums: List[int], target: int) -> List[int]:
        is_start_found = False
        start = end = -1
        for idx, num in enumerate(nums):
            if num > target:
                return [start, end]

            if num == target and not is_start_found:
                start = end = idx
                is_start_found = True
            elif num == target:
                end = idx
        return [start, end]

    """
解法5: 同解法 1, 只是基于 bisect 包实现二分查找;
注意: 在 LeetCode 上执行效率优于解法 1, 可深入解读 bisect 包的具体实现细节;
    """
    def searchRange_v5(self, nums: List[int], target: int) -> List[int]:
        idx_left = bisect.bisect_left(nums, target)
        if idx_left == len(nums) or nums[idx_left] != target:
            return [-1, -1]

        idx_right = idx_left
        while idx_right < len(nums) and nums[idx_right] == target:
            idx_right += 1
        return [idx_left, idx_right - 1]

    """
解法6: 同解法 2, 只是基于 bisect 包实现二分查找;
注意: 在 LeetCode 上执行效率优于解法 2, 可深入解读 bisect 包的具体实现细节;
    """
    def searchRange_v6(self, nums: List[int], target: int) -> List[int]:
        idx_left = bisect.bisect_left(nums, target)
        idx_right = bisect.bisect_right(nums, target)
        if idx_left == len(nums) or nums[idx_left] != target:
            return [-1, -1]
        return [idx_left, idx_right - 1]

    """
解法7: 双指针法;
时间复杂度: O(n)
空间复杂度: O(1)
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



