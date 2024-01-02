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
title_jy = "Combinations(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "组合问题(元素无重复、不可复选) | IMP | 相似题: 参考 permutation_combination_subset"


"""
Given two integers `n` and `k`, return all possible combinations of `k`
numbers out of the range [1, n]. You may return the answer in any order.


Example 1:
Input: n = 4, k = 2
Output:
[ [2, 4],
  [3, 4],
  [2, 3],
  [1, 2],
  [1, 3],
  [1, 4],]

Example 2:
Input: n = 1, k = 1
Output: [[1]]


Constraints:
1 <= n <= 20
1 <= k <= n
"""


class Solution:
    """
解法 1: 递归

从 n 个数里挑 k 个数等价于先挑一个数, 然后在剩下的 n-1 个数里挑 k-1 个数
    """
    def combine_v1(self, n: int, k: int) -> List[List[int]]:
        ls_res = []
        # jy: 候选数值列表
        ls_candidate = list([i+1 for i in range(n)])
        # jy: 深度优先搜索 (递归)
        self._dfs(k, ls_candidate, [], ls_res)
        return ls_res
    
    def _dfs(self, k, ls_candidate, combination, ls_res):
        """
        k: 组合 combination 中还差 k 个数才能构造目标组合
        ls_candidate: 候选数值列表
        combination: 当前组合
        ls_res: 记录所有满足要求的组合的列表
        """
        # jy: 如果 k 为 0, 表明当前组合 combination 已满足条件, 加入结果列表
        if k == 0:
            ls_res.append(combination)
            return

        # jy: 遍历候选集中的元素
        for i in range(len(ls_candidate)):
            # jy: 将当前元素加入到 combination 中, k 同时减 1, 剩余可挑选的
            #     数为 ls_candidate[i+1:] (因为 ls_candidate[:i] 的数都已经
            #     被挑选过, 因此不包含在内, 避免挑选了 [1, 2] 后再次又挑选了
            #     [2, 1], 而实际上对于组合来说, 这两者是一样的)
            self._dfs(k-1, ls_candidate[i+1:], combination[:] + [ls_candidate[i]], ls_res)


    """
解法 2: 优化解法 1
1) 空间复杂度优化: 无需单独维护一个候选数值列表, 在递归调用时记录候选数
   值的起始数字和终止数字 (小于起始数字的数都已经被选过了, 可以跳过)
2) 遍历候选数值时不需遍历到 n, 因为只挑选 k 个数, 如果剩下的数不足 k 个,
   则可直接放弃剩下的数
    """
    def combine_v2(self, n: int, k: int) -> List[List[int]]:
        ls_res = []
        self._dfs(k, 1, n, [], ls_res)
        return ls_res

    def _dfs(self, k, start, end, combination, ls_res):
        """
        k: 表示 combination 中还差多少个数
        start: 可加入到 combination 的候选数值的最小值
        end: 可加入到 combination 的候选数值的最大值
        combination: 记录当前组合元素的列表
        ls_res: 记录满足要求的组合的列表
        """
        if k == 0:
            ls_res.append(combination)
            return
        # jy: 将 i 先加入到 combination 中, 随后在 i+1 到 end 中寻找组合元素;
        #     由于组合中要包含 k 个元素, 且元素值为 1 到 n, 为了保证从小到大
        #     能加满 k 个元素, 起始元素必须不大于 end-k+1, 如果起始值大于该值,
        #     后续已经不足 k 个元素了
        for i in range(start, end - k + 2):
            self._dfs(k-1, i+1, end, combination[:] + [i], ls_res)


    """
解法 3: 递归的另一种写法

包含回溯过程, 需理解与以上递归写法的区别
    """
    def combine_v3(self, n: int, k: int) -> List[List[int]]:
        ls_res = []

        def backtrack(start, n, k, combination):
            """
            组合 combination 中的可选数值的数值范围为 start 到 n, 总共选 k 个
            """
            # jy: 如果组合中个数已经满足 k 个, 则将组合加入结果列表 (注意: 加
            #     入的是深拷贝的结果, 否则后续 combination 的改变仍会影响到当
            #     前加入的结果)
            if len(combination) == k:
                ls_res.append(combination[:])
                return

            # jy: 组合中的可选数值为 start 到 n, 以下尝试将该范围的数值放入组
            #     合, 并从下一个数值范围中递归寻找剩余数值
            for i in range(start, n+1):
                combination.append(i)
                backtrack(i+1, n, k, combination)
                # jy: 回溯, 使得当前的 for 循环中的上一个 i 数值遍历完后, 从组
                #     合中弹出, 寻找下一个不包含该数值的组合; 如果缺少该回溯过
                #     程, 则以上递归找到一个满足要求的组合后, 下一轮 for 循环
                #     会继续往 combination 中加入数值, 使得 combination 中的元
                #     素越来越多, 因此不再会加入到结果列表
                # jy: 为什么前两种解法的递归中都无需回溯, 但当前解法中的递归需
                #     要有该回溯过程? 这是由以上终止递归的 if 判断条件决定的
                combination.pop()
        backtrack(1, n, k, [])
        return ls_res



n = 4
k = 2
res = Solution().combine_v1(n, k)
"""
[ [2, 4],
  [3, 4],
  [2, 3],
  [1, 2],
  [1, 3],
  [1, 4],]
"""
print(res)


n = 1
k = 1
res = Solution().combine_v2(n, k)
print(res)
"""
[[1]]
"""


n = 1
k = 1
res = Solution().combine_v3(n, k)
print(res)
"""
[[1]]
"""

