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
title_jy = "Search-in-Rotated-Sorted-Array-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "二分查找 + 去重技巧 | 相似题: 0033"


"""
There is an integer array `nums` sorted in non-decreasing order (not
necessarily with distinct values). Before being passed to your function,
`nums` is rotated at an unknown pivot index `k` (0 <= k < nums.length)
such that the resulting array is (0-indexed):
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]

For example, [0, 1, 2, 4, 4, 4, 5, 6, 6, 7] might be rotated at pivot
index 5 and become [4, 5, 6, 6, 7, 0, 1, 2, 4, 4].

Given the array `nums` after the rotation and an integer `target`, return
true if target is in `nums`, or false if it is not in `nums`.


Example 1:
Input: nums = [2, 5, 6, 0, 0, 1, 2], target = 0
Output: true

Example 2:
Input: nums = [2, 5, 6, 0, 0, 1, 2], target = 3
Output: false


Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4


Follow up: This problem is the same as 0033 (search-in-rotated-sorted-array),
where `nums` may contain duplicates. Would this affect the runtime complexity?
How and why?
"""


from typing import List
class Solution:
    """
解法 1: 二分查找 (该题的任何解法同样可用于 0033 中)

nums 可能包含重复元素, 这会影响到程序的时间复杂度吗?
会, 使用二分查找局部有序时, 当 nums[mid] == nums[low] 时 (或其它类似情况),
无法知道到底是左侧区间还是右侧区间是升序区间, 只能 low 左移一位后继续判断

该题在 0033 (search-in-rotated-sorted-array) 的基础上增加了重复的数字, 
当左端点和右端点(或中间值)相等时, 无法判断 mid 的左半边还是右半边才是
有序数组, 可以在两端不断去除重复的元素后再进一步判断

该解法优先基于 low 和 mid 的值进行判断, 如果值相等, 则 low 往前移, 实
现去重
    """
    def search_v1(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                return True

            # jy: 优先判断 nums[mid] 和 nums[low] 的值的大小;
            #     如果 nums[mid] > nums[low], 表明前半部分严格升序, 此时如
            #     果目标值在 low 和 mid 中间, 则更新 high 为 mid-1, 否则更
            #     新 low 为 mid+1
            if nums[low] < nums[mid]:
                # jy: 注意 "nums[low] <= target" 中的 "=" 必须存在, 因为可
                #     能存在 nums[low] == target, 此时要更新 high; 否则当 
                #     nums[low] == target 时, 会走 else 部分逻辑更新 low,
                #     导致错过正确值【trick】
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # jy: 如果 mid 值小于 low 值, 表明右侧区间升序, 此时可判断目标
            #     值是否在该升序区间, 从而决定更新 low 还是 high 的值
            elif nums[low] > nums[mid]:
                # jy: "target <= nums[high]" 中的 "=" 必须存在, 否则 target
                #     等于 nums[high] 还更新 high 值, 导致错过正确值【trick】
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            # jy: 如果 nums[mid] == nums[low], (但不等于 target, 否则在开头已
            #     经返回), 表明 low 到 mid 之间的值都相等, 此时 low 往前进 1,
            #     即可实现去除重复元素
            else:
                low += 1
        return False


    """
解法 2: 类似解法 1, 但优先基于 low 和 high 去除重复元素
    """
    def search_v2(self, nums: List[int], target: int) -> bool:
        # jy: 当左右两端数值相等时, 不断 pop 出右端元素, 直到两端数值不等;
        #     也可通过以下移动 low 或 high 实现
        #while len(nums) > 1 and nums[0] == nums[-1]:
        #    nums.pop()

        low, high = 0, len(nums) - 1
        # jy: 如果没有以上的 pop 过程, 也可以通过移动 low 或 high 来实现
        #     (注意: low 和 high 不能同时移动, 否则重复的元素可能全部被清除)
        while low <  high and nums[low] == nums[high]:
            # low += 1
            high -= 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True

            # jy: nums[low] <= nums[mid] 时表明左侧区间有序, 如果目标值在该
            #     区间, 则更新 high = mid - 1
            if nums[low] <= nums[mid]:  
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low =  mid + 1
            # jy: nums[low] > nums[mid] 时表明右侧区间有序, 如果目标值在右侧
            #     区间, 则更新 low = mid + 1
            else:            
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False


    """
解法 3: 类似解法 2, 但优先判断 mid 和 high 的值, 从而判断 target 是在
左侧区间还是右侧区间, 进而更新 low 或 high
    """
    def search_v3(self, nums: List[int], target: int) -> bool:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True

            # jy: 如果 low 和 high 相等, 则移动 low 或 high (注意不能同时移
            #     动, 否则可能把重复的元素全部去除, 一个都不保留)
            if nums[low] == nums[high]:
                low += 1
                #high -= 1
                continue

            if nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False


    """
解法 4: 同解法 2, 但修改了去重逻辑
    """
    def search_v4(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            
            # jy: 当 mid、low、high 的值均相等时, 同时移动 low 和 high 也不
            #     会使得重复元素全部被清除 (至少还保留了 mid 位置的值)
            if nums[mid] == nums[low] == nums[high]:
                low += 1
                high -= 1
                continue

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False


    """
解法 5: 同解法 4, 但优先基于 mid 和 high 的值判断升序区间, 进一步判断
target 值是否位于升序区间, 从而确定更新 low 还是 high

其实这道题只需根据 0033 题的搜索改变一点判断就行, 即当
nums[low] == nums[mid] == nums[high] 时不知道该怎么移动,
此时 low += 1, high -= 1 后再去判断即可
    """
    def search_v5(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True

            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            if nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False



nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
res = Solution().search_v1(nums, target)
print(res)

nums = [2, 5, 6, 0, 0, 1, 2]
target = 3
res = Solution().search_v2(nums, target)
print(res)

nums = [1, 0, 1, 1, 1]
target = 0
res = Solution().search_v3(nums, target)
print(res)


nums = [1, 0, 1, 1, 1]
target = 0
res = Solution().search_v4(nums, target)
print(res)


nums = [1, 0, 1, 1, 1]
target = 0
res = Solution().search_v5(nums, target)
print(res)



