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
title_jy = "Ways-to-Split-Array-Into-Three-Subarrays(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
A split of an integer array is good if:
The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 10^9 + 7.

Example 1:
Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].

Example 2:
Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]

Example 3:
Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.


Constraints:
3 <= nums.length <= 10^5
0 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    """
题解
构造前缀和数组 prefix_sum, prefix_sum[i] = nums[0] + nums[1] + ... + nums[i], 遍历数组, 对当前位置 i, nums[0:i + 1] 为第一段子数组, 需要找到第二段数组的最小可能结束位置 j 和第三段数组的最大可能起始位置 k, 这样 k - j 就是数组的分隔方式; 定位第二段数组的最小可能结束位置 j 时需满足: prefix_sum[i] <= prefix_sum[j] - prefix_sum[i], 即第一段数组的和小于等于第二段数组;
    """
    def waysToSplit(self, nums: List[int]) -> int:
        prefix_sum = [n for n in nums]

        for i in range(1, len(nums)):
            prefix_sum[i] = nums[i] + prefix_sum[i - 1]

        count = 0
        j = k = 0

        for i in range(len(nums) - 2):
            j = max(j, i + 1)

            while j < len(nums) - 1 and prefix_sum[i] \
                    > prefix_sum[j] - prefix_sum[i]:
                j += 1

            k = max(k, j)

            while k < len(nums) - 1 and prefix_sum[k] - prefix_sum[i] \
                    <= prefix_sum[-1] - prefix_sum[k]:
                k += 1

            count = (count + k - j) % 1000000007

        return count


