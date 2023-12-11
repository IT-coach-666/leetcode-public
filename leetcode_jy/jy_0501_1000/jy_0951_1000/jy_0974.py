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
title_jy = "Subarray-Sums-Divisible-by-K(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array nums of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by k.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Note:
1. 1 <= nums.length <= 30000
2. -10000 <= nums[i] <= 10000
3. 2 <= k <= 10000
"""

from typing import List


class Solution:
    """
和 523. Continuous Subarray Sum 基本一致, 由判断是否存在变为求解个数
    """
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum_so_far = 0
        mapping = {0: 1}
        count = 0

        for i, n in enumerate(nums):
            sum_so_far += n
            key = sum_so_far if k == 0 else sum_so_far % k
            count += mapping.get(key, 0)
            mapping[key] = mapping.get(key, 0) + 1

        return count


