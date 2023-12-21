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
tag_jy = "排列问题 (元素可重复、不可复选) | 相似题: 参考 permutation_combination_subset"


"""
Given a collection of numbers ``nums``, that might contain duplicates, return all
possible unique permutations in any order.


Example 1:
Input: nums = [1,1,2]
Output:
[[1, 1, 2],
 [1, 2, 1],
 [2, 1, 1]]

Example 2:
Input: nums = [1,2,3]
Output: 
[[1, 2, 3],
 [1, 3, 2],
 [2, 1, 3],
 [2, 3, 1],
 [3, 1, 2],
 [3, 2, 1]]


Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""


class Solution:
    """
解法 1: 递归

在 0046 (Permutations) 的基础上将数组排序, 遍历时, 如果当前数字等
于前一个数字, 则跳过
    """
    def permuteUnique_v1(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        # jy: 先对列表进行排序
        nums.sort()
        self._permute(len(nums), nums, [], permutations)
        return permutations

    def _permute(self, count, nums, permutation, permutations):
        if count == 0:
            permutations.append(permutation)
            return

        for i, n in enumerate(nums):
            # jy: 如果当前数字等于前一个数字, 则跳过 (避免排列重复)
            if i > 0 and nums[i] == nums[i-1]:
                continue

            self._permute(count - 1, 
                          nums[0:i] + nums[i+1:], 
                          permutation + [n], 
                          permutations)


    """
解法 2: 类似解法 1
    """
    def permuteUnique_v2(self, nums):
        if not nums:
            return []

        # jy: 先对列表进行排序
        nums.sort()
        n = len(nums)
        ls_res = []

        # jy: 用于 helper1 递归函数中, 防止数值被重复使用
        visited = [0] * n
        def helper1(temp_list, length):
            if length == n:
                ls_res.append(temp_list)

            for i in range(n):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue

                visited[i] = 1
                helper1(temp_list + [nums[i]], length + 1)
                visited[i] = 0

        def helper2(nums, temp_list, length):
            if length == n and temp_list not in ls_res:
                ls_res.append(temp_list)

            for i in range(len(nums)):
                helper2(nums[:i] + nums[i+1: ], temp_list + [nums[i]], length + 1)

        # jy: 基于 helper1 递归函数
        helper1([], 0)
        # jy: 基于 helper2 递归函数 (执行效率没 helper1 高)
        # helper2(nums, [], 0)
        return ls_res


nums = [1, 1, 2]
res = Solution().permuteUnique_v1(nums)
print(res)
"""
[[1, 1, 2],
 [1, 2, 1],
 [2, 1, 1]]
"""


nums = [1, 2, 3]
res = Solution().permuteUnique_v2(nums)
print(res)
"""
[[1, 2, 3],
 [1, 3, 2],
 [2, 1, 3],
 [2, 3, 1],
 [3, 1, 2],
 [3, 2, 1]]
"""


