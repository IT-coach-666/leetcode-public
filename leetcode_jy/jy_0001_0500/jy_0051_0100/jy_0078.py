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
title_jy = "subsets(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "子集问题 (元素无重复、不可复选) IMP | 相似题: 参考 permutation_combination_subset"


"""
Given an integer array `nums` of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution
in any order.

 
Example 1:
Input: nums = [1,2,3]
Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

Example 2:
Input: nums = [0]
Output: [[], [0]]
 

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of `nums` are unique.
"""


class Solution:
    """
解法 1: 在做全排列的过程中本身就存在子集, 只是没有保存; 如果在结束条件处略
作修改, 改为没有条件, 每次节点的值本身就是子集, 将其加入到结果中即可; 但这
样还存在重复: 假如对 [a, b] 进行全排列, 在全排列过程中可能会出现选择 b 作为
开头时后续还可以选 a, 所以结果会出现 [a, b] 和 [b, a], 在组合中这二者是重复
的; 规避方式也很简单: 每次从当前元素的下一个元素开始选

回溯算法关键: 不合适就退回上一步, 然后通过约束条件, 减少时间复杂度
    """
    def subsets_v1(self, nums: List[int]) -> List[List[int]]:
        ls_res, track = [], []
        self._dfs_v1(nums, 0, track, ls_res)
        return ls_res

    def _dfs_v1(self, nums, start, track, ls_res):
        # jy: 每个节点的值都是一个子集, 加入子集; 注意加入的是 track[:] (即
        #     深拷贝, 列表切片是深拷贝), 而不是 track (浅拷贝), 如果是浅拷
        #     贝, 则递归过程中对 track 的操作会影响到当前加入的结果
        ls_res.append(track[:])
        # jy: 选择列表中的每个选择
        for i in range(start, len(nums)):
            track.append(nums[i])
            # jy: 递归
            self._dfs_v1(nums, i+1, track, ls_res)
            # jy: 撤销选择, 回溯
            track.pop()

    """
解法 2: 基于库函数 itertools.combinations 求解
    """
    def subsets_v2(self, nums: List[int]) -> List[List[int]]:
        import itertools

        ls_res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                ls_res.append(tmp)
        return ls_res


    """
解法 3: 循环/迭代
    """
    def subsets_v3(self, nums: List[int]) -> List[List[int]]:
        # jy: 空集是任何集合的子集
        ls_res = [[]]
        for i in nums:
            ls_res += [[i] + ls_num for ls_num in ls_res]
        return ls_res


    """
解法 4: 解法 1 的另一种写法
    """
    def subsets_v4(self, nums: List[int]) -> List[List[int]]:
        ls_res = []
        n = len(nums)
        
        def helper(i, tmp, ls_res, n):
            ls_res.append(tmp)
            for j in range(i, n):
                helper(j+1, tmp + [nums[j]], ls_res, n)
        helper(0, [], ls_res, n)
        return ls_res  



nums = [1, 2, 3]
res = Solution().subsets_v1(nums)
# jy: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(res)


nums = [0]
res = Solution().subsets_v1(nums)
# jy: [[], [0]]
print(res)


nums = [1, 2, 3]
res = Solution().subsets_v3(nums)
# jy: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(res)


nums = [1, 2, 3]
res = Solution().subsets_v4(nums)
# jy: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(res)




