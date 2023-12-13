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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Search-Insert-Position(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "二分查找 (bisect 模块)"


"""
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0


Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""


class Solution:
    """
解法 1: 二分查找

该题有以下两种理解方式: 
1) 求比 target 小的数里最大的数的下一个位置下标
2) 求数组中大于或等于 target 的最小数值, 如果该值不存在, 则返回数组长
   度作为目标下标位置 (当 target 在数组中时, 返回该值的下标位置)
    """
    def searchInsert_v1(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        # jy: 假设列表最后一个值为 target, 则循环过程中的 mid 总是满足
        #     nums[mid] < target, 因此不断更新 low 值, 当且仅当最后一次
        #     循环 low == high 时, nums[mid] == target, 此时再次更新 high
        #     会使得 low > high, 因此退出循环返回的 low 值符合要求; 如果
        #     列表中所有值都比 target 小, 则循环过程会不断更新 low 值, 直
        #     到更新的 low 值大于 high 时退出循环并返回, 即最终 low 值为
        #     初始 high 的下一个位置下标
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] < target:
                low = mid + 1
            # jy: 以下 elif 逻辑可优化提速 (去除也正确); 如果去除该部分, 则
            #     当找到符合要求的 mid 时, 仍去更新 high 值为 mid - 1, 使得
            #     后续循环中得到的中间值 mid_v2 不再满足要求, 因此 low 会不
            #     断更新为 mid_v2 + 1, 直到更新为比原先的 high 值大为止才退
            #     出循环, 而原先的 high 值为 mid-1, 比其大即为 mid, 因此最终
            #     返回的下标位置 low (即原先满足要求的 mid) 对应的值为 target
            elif nums[mid] == target:
                return mid
            else:
                high = mid - 1
        return low


    """
解法 2: 同解法 1, 但使用 bisect 模块
    """
    def searchInsert_v2(self, nums: List[int], target: int) -> int:
        import bisect
        return bisect.bisect_left(nums, target)


nums = [1, 3, 5, 6]
target = 5
# Output: 2
res = Solution().searchInsert_v1(nums, target)
print(res)

nums = [1, 3, 5, 6]
target = 2
# Output: 1
res = Solution().searchInsert_v1(nums, target)
print(res)

nums = [1, 3, 5, 6]
target = 7
# Output: 4
res = Solution().searchInsert_v1(nums, target)
print(res)

nums = [1, 3, 5, 6]
target = 0
# Output: 0
res = Solution().searchInsert_v2(nums, target)
print(res)

nums = [1]
target = 0
# Output: 0
res = Solution().searchInsert_v2(nums, target)
print(res)


