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
title_jy = "Binary-Search(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a
function to search target in nums. If target exists, then return its index. Otherwise, return -1.


Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:
1 <= nums.length <= 104
-9999 <= nums[i], target <= 9999
All the integers in nums are unique.
nums is sorted in an ascending order.
"""


from typing import List
import bisect


class Solution:
    def search_v1(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            middle = low + (high - low) // 2
            mid_value = nums[middle]
            if mid_value > target:
                high = middle - 1
            elif mid_value < target:
                low = middle + 1
            else:
                return middle

        return -1

    """
JY: 基于 bisect 包实现;
    """
    def search_jy(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        if idx == len(nums) or nums[idx] != target:
            return -1
        return idx


nums = [-1, 0, 3, 5, 9, 12]
target = 9
# Output: 4
res = Solution().search_v1(nums, target)
print(res)


nums = [-1, 0, 3, 5, 9, 12]
target = 2
# Output: -1
res = Solution().search_v1(nums, target)
print(res)



