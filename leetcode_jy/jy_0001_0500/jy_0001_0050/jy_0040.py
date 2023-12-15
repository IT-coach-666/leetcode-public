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
title_jy = "Combination-Sum-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "UNDO 组合问题 (元素有重复、不可复选) | 递归 | 相似题: 参考 permutation_combination_subset"


"""
Given a collection of candidate numbers `candidates` and a target number
`target`, find all unique combinations in `candidates` where the candidate
numbers sum to `target`.

Each number in `candidates` may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.


Example 1:
Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
Output:
[[1, 1, 6],
 [1, 2, 5],
 [1, 7],
 [2, 6]]

Example 2:
Input: candidates = [2, 5, 2, 1, 2], target = 5
Output:
[[1, 2, 2],
 [5]]


Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


class Solution:
    """
解法 1:  0039 (Combination-Sum) 中输入元素没有重复, 本题中 candidates 中的
数字有可能重复

candidates 中当前数字等于前一个数字, 则跳过
    """
    def combinationSum2_v1(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        # jy: 传入已排序的列表, 列表起始下标(在列表中的该下标位置之后的元素中找), 要查
        #    找的目标值, 当前的组合记录, 结果列表;
        self._dfs(sorted(candidates), 0, target, [], result)
        return result


    def _dfs(self, candidates, start, target, combination, result):
        """
        传入的参数为已排序的列表, 列表起始下标(在列表中的该下标位置之后的元素中找), 要查
        找的目标值, 当前的组合记录, 结果列表;
        """
        # jy: 如果剩余要查找的 target 为 0, 表明当前的 combination 已经满足要求, 将其加入
        #    到结果列表
        if target == 0:
            result.append(combination)
            return
        # jy: 从候选数组中的下标为 start 的位置开始找组合中的元素;
        for i in range(start, len(candidates)):
            n = candidates[i]
            # jy: 如果该元素大于目标值 target, 则直接跳出循环, 终止;
            if n > target:
                break
            # jy: 如果 i > start (确保 i-1 有效, 即有前一个值), 且当前值与前一个值相等, 则跳过
            #    当前数值, 防止后续递归中出现相同组合 (深度思考: 因为假如有两个连续位置数值相
            #    同的, 且最终两个相同的数值可以结合其它数值构成一个满足条件的组合, 则当遍历第
            #    一个位置的数值时, 加入候选列表后进行下一轮递归, 则下一轮递归时肯定会把第二个
            #    数值考虑到, 使得两个数都被放入组合, 此时当前此轮的 for 循环的下一轮循环时, 就
            #    不应该再把相同的第二个数值放入并递归查找了, 否则就会有相同组合结果, 导致重复)
            if i > start and candidates[i] == candidates[i-1]:
                continue
            # jy: 遍历完当前数值后, 下一个目标值为原目标值减去当前数值, 且从下一个数值位置开始遍
            #    历查找(如果下一个数值对应的下标不存在, 则会跳出循环)
            self._dfs(candidates, i+1, target - n, combination[:] + [n], result)
            #self._dfs(candidates, i+1, target - n, combination + [n], result)


    def combinationSum2_v2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        # jy: 优先对数组进行排序
        candidates.sort()
        n = len(candidates)
        res = []
        
        def backtrack(i, tmp_sum, tmp_list):
            if tmp_sum == target:
                res.append(tmp_list)
                return 
            for j in range(i, n):
                if tmp_sum + candidates[j]  > target : break
                if j > i and candidates[j] == candidates[j-1]:continue
                backtrack(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])
        backtrack(0, 0, [])    
        return res



candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
res = Solution().combinationSum2(candidates, target)
print(res)
"""
[[1, 1, 6],
 [1, 2, 5],
 [1, 7],
 [2, 6]]
"""

candidates = [2, 5, 2, 1, 2]
target = 5
res = Solution().combinationSum2(candidates, target)
print(res)
"""
[[1, 2, 2],
 [5]]
"""

