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
title_jy = "Combination-Sum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "组合问题(元素无重复、可复选) | 递归 | 相似题: 参考 permutation_combination_subset"


"""
Given an array of distinct integers `candidates` and a target integer 
`target`, return a list of all unique combinations of candidates where
the chosen numbers sum to `target`. You may return the combinations in
any order.

The same number may be chosen from candidates an unlimited number of 
times. Two combinations are unique if the frequency of at least one of
the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to
`target` is less than 150 combinations for the given input.


Example 1:
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]
Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can
             be used multiple times. 7 is a candidate, and 7 = 7. These
             are the only two combinations.

Example 2:
Input: candidates = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Example 4:
Input: candidates = [1], target = 1
Output: [[1]]

Example 5:
Input: candidates = [1], target = 2
Output: [[1, 1]]


Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""


class Solution:
    """
解法 1: 递归

该题等价于先从 candidates 中挑选一个数 k, 然后继续在 candidates
中挑选几个数, 其和为 target - k

递归时, 记录当前数值在 candidates 中的序号, 从当前序号开始遍历
candidates 即可避免结果重复;

如果每层递归都对全体 candidates 做遍历会导致如 [2, 2, 3], [3, 2, 2] 这
样的对称重复的答案的产生; 每次更深层的递归都应往后缩小一个 candidates,
即可避免结果重复
    """
    def combinationSum_v1(self, candidates: List[int], target: int) -> List[List[int]]:
        ls_res = []
        self._dfs(candidates, 0, target, [], ls_res)
        return ls_res

    def _dfs(self, candidates, start, target, ls_num, ls_res):
        """
        从 candidates[start: ] 中挑选数值放入 ls_num 中, 如果 ls_num 中
        的数值总和为最初的目标值, 则将 ls_num 加入到 ls_res 中

        递归函数中的 target 值为与最初目标值的差值
        """
        # jy: 由于 candidates 为 1 - 200 的数值, 故 target 不能为负值;
        #     因此 target 为负时即可返回, 终止递归
        if target < 0:
            return

        # jy: target 为 0 表明已经找到一个满足要求的组合
        elif target == 0:
            ls_res.append(ls_num)
            return

        # jy: 遍历候选值, 因为可重复使用同一个值, 因此确定一个值后, 剩余
        #     的值也从位置 i 开始继续找
        for i in range(start, len(candidates)):
            n = candidates[i]
            # jy: 注意此处传入的第 4 个参数为 ls_num[:] + [n], 而不能预先操
            #     作 ls_num.append(n) 之后将 ls_num 直接传入, 因为如果直接传
            #     入 ls_sum, 则相当于浅拷贝, 后续递归过程中对 ls_num 的修改
            #     都会影响到当前的结果; 而 ls_num[:] + [n] 相当于是深拷贝
            self._dfs(candidates, i, target - n, ls_num[:] + [n], ls_res)


    """
解法 2: 解法 1 的另一种写法

递归回溯算法不管怎么优化时间复杂度都不可能低于 O(N!), 因为穷举整棵决策树是无
法避免的; 不像动态规划能重叠子问题, 回溯算法就是纯暴力穷举, 复杂度一般都很高

该题是组合问题, 也是子集问题: candidates 的哪些子集的和为 target ? 想解决这类
问题也得回到回溯树上; 标准的子集/组合问题如何保证不重复使用元素？答案在于递归
时输入的参数 start

start 从 i 开始, 则下一层回溯树就从 i + 1 开始, 从而保证 nums[i] 这个元素不会
被重复使用; 反过来, 如果我想让每个元素被重复使用, 只要把 i + 1 改成 i 即可

这样这棵回溯树会永远生长下去, 所以递归函数需要结束条件, 即路径和大于 target 时
就没必要再遍历下去了
    """
    def combinationSum_v2(self, candidates: List[int], target: int) -> List[List[int]]:
        ls_res = []
        self._dfs_v2(candidates, [], target, 0, ls_res)
        return ls_res

    def _dfs_v2(self, candidates, path, target, start, ls_res):
        if sum(path) == target:
            # jy: 注意此处加入的是 track[:] (即深拷贝), 如果直接加入
            #     track (相当于浅拷贝), 后续对 track 的改变也会影响到
            #     当前已加入的结果
            ls_res.append(path[:])
            return
        if sum(path) > target:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            # jy: 相同元素可重复使用, 因此下一个查找位置仍从
            #     当前位置开始找起
            self._dfs_v2(candidates, path, target, i, ls_res)
            path.pop()


    """
解法 3: 在解法 1 的基础上进行优化: 先将 candidates 排序, 递归搜索时如果当前
数字大于 target, 则可终止搜索
    """
    def combinationSum_v3(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sorted_candidates = sorted(candidates)
        self._dfs_v3(sorted_candidates, 0, target, [], result)
        return result

    def _dfs_v3(self, candidates, start, target, combination, result):
        if target == 0:
            result.append(combination)
            return

        for i in range(start, len(candidates)):
            n = candidates[i]
            # jy: 如果 n > target, 表明后续的数值均使得 target - n 小于 0,
            #     不再满足条件, 直接 break 或 return (break 的含义与 return
            #     相同, 相当于递归函数返回 None), 终止递归
            if n > target:
                break
                #return
            self._dfs_v3(candidates, i, target - n, combination[:] + [n], result)


    """
解法 4: 动态规划

"零钱兑换" 问题输出为凑成总金额所需的最少硬币个数, 此题需输出所有可行解
    """
    def combinationSum_v4(self, candidates: List[int], target: int) -> List[List[int]]:
        # jy: 用 dp[i] 记录 candidates 中的子组合之和为 i 的所有子组合,
        #     因此最终返回 dp[target]
        dp = {i:[] for i in range(target+1)}
        # jy: 和为 0 的子组合为空组合 (注意, dp[0] 应用到 if 判断时结果为 True)
        dp[0] = [[]]
        # jy: 遍历列表中的每一个数值
        for num in candidates:
            # jy: 遍历该数值到 target 数值的所有数值, 如果 num 值大于 target,
            #     则忽略跳过
            for i in range(num, target+1):
                # jy: 如果 i - num 的所有子组合已求解过, 则在已有子组合的基
                #     础上进一步更新和为 i 的子组合结果
                if dp[i - num]:
                    # jy: ls_sub 中的数值之和为 i - num, 因此 ls_sub 中再加
                    #     入 num 后, 数值之和即为 i
                    for ls_sub in dp[i - num]:
                        dp[i].append(ls_sub + [num])
        # jy: 最终返回值为 target 的所有子组合
        return dp[target]




candidates = [2, 3, 6, 7]
target = 7
# Output: [[2, 2, 3], [7]]
res = Solution().combinationSum_v1(candidates, target)
print(res)


candidates = [2, 3, 5]
target = 8
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
res = Solution().combinationSum_v2(candidates, target)
print(res)


candidates = [2]
target = 1
# Output: []
res = Solution().combinationSum_v3(candidates, target)
print(res)


candidates = [1]
target = 1
# Output: [[1]]
res = Solution().combinationSum_v4(candidates, target)
print(res)


candidates = [1]
target = 2
# Output: [[1, 1]]
res = Solution().combinationSum_v1(candidates, target)
print(res)


