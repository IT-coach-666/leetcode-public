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
title_jy = "Contains-Duplicate(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array nums, return true if any value appears at least twice in the array, and
return false if every element is distinct.


Example 1:
Input: nums = [1, 2, 3, 1]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true


Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List

class Solution:
    """
判断转成 Set 后的长度是否等于 nums;
    """
    def containsDuplicate_v1(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def containsDuplicate_v2(self, nums: List[int]) -> bool:
        dict_ = {}
        for num in nums:
            if num in dict_:
                return True
            else:
                dict_[num] = 1

        return False



nums = [1, 2, 3, 1]
# Output: true
res = Solution().containsDuplicate_v1(nums)
print(res)
res = Solution().containsDuplicate_v2(nums)
print(res)


nums = [1, 2, 3, 4]
# Output: false
res = Solution().containsDuplicate_v1(nums)
print(res)
res = Solution().containsDuplicate_v2(nums)
print(res)


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true
res = Solution().containsDuplicate_v1(nums)
print(res)
res = Solution().containsDuplicate_v2(nums)
print(res)


