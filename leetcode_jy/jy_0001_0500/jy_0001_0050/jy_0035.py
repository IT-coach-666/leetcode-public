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
tag_jy = ""


"""
Given a sorted array of distinct integers and a target value, return the index if the
target is found. If not, return the index where it would be if it were inserted in order.

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

from typing import List
import bisect


class Solution:
    """
二分查找, 等价于:
1) 求解比 target 小的数里最大的数所在位置加 1
2) 求数组中大于或等于 target 的最小数值, 如果该值不存在, 则返回数组长度作为 target 的下标
以上两个角度思考是等价的, 二分查找的代码完全一致;

JY: 不可与以下问题等价:
求比 target 大的最小数所在的位置 (因为 target 可能存在于数组中, 此时要返回其下标, 而不能求比它大的数值)
    """
    def searchInsert_v1(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        # jy: 当 low == high 时会退出循环, 此时的 nums[high || low] >= target (如
        #    果 nums[low] 存在的话, 如果不存在, 则表明 target 比数组中的最后一个
        #    值大, 此时返回的 low 为数组最后一个值的下标加 1)
        while low < high:
            middle = low + (high - low) // 2

            if nums[middle] < target:
                low = middle + 1
            # jy: 以下注释的 elif 部分是对问题的细微优化;
            # elif nums[middle] == target:
            #     return middle
            else:
                high = middle
        return low

    def searchInsert_jy(self, nums: List[int], target: int) -> int:
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
res = Solution().searchInsert_jy(nums, target)
print(res)

nums = [1]
target = 0
# Output: 0
res = Solution().searchInsert_jy(nums, target)
print(res)


