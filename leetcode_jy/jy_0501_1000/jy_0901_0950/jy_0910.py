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
title_jy = "Smallest-Range-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an integer array nums and an integer k.
For each index i where 0 <= i < nums.length, change nums[i] to be either nums[i] + k or nums[i] - k.
The score of nums is the difference between the maximum and minimum elements in nums.
Return the minimum score of nums after changing the values at each index.

Example 1:
Input: nums = [1], k = 0
Output: 0
Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.

Example 2:
Input: nums = [0,10], k = 2
Output: 6
Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.

Example 3:
Input: nums = [1,3,6], k = 3
Output: 3
Explanation: Change nums to be [4, 6, 3]. The score is max(nums) - min(nums) = 6 - 3 = 3.


Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^4
0 <= k <= 10^4
"""

from typing import List


class Solution:
    """
首先将数组排序, 然后遍历数组, 遍历数组, 比较当前数字加 k 和最后一个数字减 k 作为可能的数组最大值, 比较下一个数字减 k 和第一个数字加 k 作为数组可能的最小值;
    """
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        min_score = sorted_nums[-1] - sorted_nums[0]

        for i in range(len(sorted_nums) - 1):
            big = max(sorted_nums[i] + k, sorted_nums[-1] - k)
            small = min(sorted_nums[i + 1] - k, sorted_nums[0] + k)
            min_score = min(min_score, big - small)

        return min_score


