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
title_jy = "Permutations-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a collection of numbers ``nums``, that might contain duplicates, return all
possible unique permutations in any order.


Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

from typing import List


class Solution:
    """
在 046_Permutations.py 的基础上将数组排序, 遍历时, 如果当前数字等于前一个数字, 则跳过
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self._permute(len(nums), sorted(nums), [], permutations)
        return permutations

    def _permute(self, count, nums, permutation, permutations):
        if count == 0:
            permutations.append(permutation)
            return

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self._permute(count - 1, nums[0:i] + nums[i+1:], permutation + [n], permutations)


nums = [1, 1, 2]
'''
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
'''
res = Solution().permuteUnique(nums)
print(res)


nums = [1, 2, 3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
res = Solution().permuteUnique(nums)
print(res)


