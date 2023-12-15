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
tag_jy = "UNDO 组合问题(元素无重复、不可复选) | "


"""
Given two integers `n` and `k`, return all possible combinations of `k`
numbers out of the range [1, n]. You may return the answer in any order.


Example 1:
Input: n = 4, k = 2
Output:
[ [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],]

Example 2:
Input: n = 1, k = 1
Output: [[1]]


Constraints:
1 <= n <= 20
1 <= k <= n
"""

#JY: 该题的以下解法中, 均默认 n >= k, 否则返回空列表;
from typing import List


class Solution:
    """
解法1: 从 n 个数里挑 k 个数等价于先挑一个数, 然后在剩下的 n-1 个数里挑 k-1 个数;
所以可以用递归求解, 初始化 1 到 n 个数作为候选集, 然后遍历候选集, 将当前的数加入
到当前组合中, 然后递归调用求解在剩下的 n-1 个数里挑 k-1 个数, 递归调用时需要从候
选集中删除当前的数, 同时记录上一个候选者的值, 过滤掉当前候选集中小于等于上一个候
选者的数字, 避免重复组合; 当 k 等于 0 时, 说明找到了一组解, 将其放到最终的结果中;
    """
    def combine_v1(self, n: int, k: int) -> List[List[int]]:
        result = []
        # jy: 维护一个候选集, 表示加入 combination 中的数的可能情况;
        candidates = set([i+1 for i in range(n)])
        # jy: 深度优先搜索递归求解;
        self._dfs(k, 0, candidates, [], result)
        return result

    def _dfs(self, k, prev_candidate, candidates, combination, result):
        """
        k: 记录当前 combination 中还差多少个元素
        prev_candidate: 上一个候选者的值
        candidates: 存放可加入到 combination 中的值的列表
        combination: 记录当前组合中的元素
        result: 记录所有符合要求的组合
        """
        # jy: 如果 k 为 0, 表明当前的组合 combination 已经满足条件, 将其加入结果列表;
        if k == 0:
            result.append(combination)
            return
        # jy: 遍历候选集中的元素,
        for n in candidates:
            # jy: 如果当前元素 n 小于或等于 prev_candidate, 表明当前元素已经加入过了, 直接跳过;
            if n <= prev_candidate:
                continue
            # jy: 更新 candidates 候选值(此处不更新正确, 更新可使 candidates 范围缩小, 使得后
            #    续 for 循环次数减少)
            new_candidates = set(candidates)
            new_candidates.remove(n)
            # jy: 将当前元素 n 加入到 combination 中, k 同时减 1, 且 prev_candidate 更新
            #    为 n;
            self._dfs(k-1, n, new_candidates, combination[:] + [n], result)

    """
解法2: 在解法 1 的基础上进行两个优化:
1) 不需要单独维护一个候选集, 造成频繁开辟空间保存候选集, 在递归调用时记录候选集的起始
   数字和终止数字, 因为小于起始数字的数都已经被选过了, 所以可以跳过
2) 遍历候选集时不需要遍历到 n, 因为只挑选 k 个数, 所以如果剩下的数不足 k 个, 则可以直
   接放弃剩下的数
    """
    def combine_v2(self, n: int, k: int) -> List[List[int]]:
        result = []
        self._dfs(k, 1, n, [], result)
        return result

    def _dfs(self, k, start, end, combination, result):
        """
        k: 表示 combination 中还差多少个数
        start: 表示可加入到 combination 的候选集的最小值
        end: 表示可加入到 combination 的候选集的最大值
        combination: 一个记录当前组合元素的列表
        result: 一个记录满足要求的组合的列表
        """
        if k == 0:
            result.append(combination)
            return
        # jy: 将 i 先加入到 combination 中, 随后递归在 i+1 到 end 中寻找组合元素;
        #    由于组合中要包含 k 个元素, 且元素值为 1 到 n, 为了保证从小到大能加满
        #    k 个元素, 起始元素必须不大于 end-k+1, 如果起始值大于该值, 后续已经不
        #    足 k 个元素了;
        for i in range(start, end - k + 2):
            self._dfs(k-1, i+1, end, combination[:] + [i], result)


    """
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。你可以按 任何顺序 返回答案。
这是标准的组合问题，但翻译一下就变成子集问题了：给你输入一个数组 nums = [1,2..,n] 和一个正整数 k，请你生成所有大小为 k 的子集。

还是以 nums = [1,2,3] 为例，刚才78题让求所有子集，就是把所有节点的值都收集起来；现在只需要把第 2 层（根节点视为第 0 层）的节点收集起来，就是大小为 2 的所有组合：

在代码上，只是需要添加结束条件：
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, track = [], []
        def backtrack(n,start,k):
            # 结束条件 遍历到第k层时收集当前结果track
            if len(track) == k:
                res.append(track[:])
                return # 后面的部分是不需要的 所以此处就可以结束了
            # 对于所有选择
            for i in range(start,n): # 选择列表是1到n之间的元素（包括n） 相当于nums = [1,..,n]
                # 做选择
                track.append(i)
                # 递归
                backtrack(n,i+1,k)
                # 撤销选择
                track.pop()
        backtrack(n+1,1,k) # 选择列表是1到n之间的元素（包括n） 所以start从1开始 n+1结束（range是左闭右开）
        return res



n = 4
k = 2
'''
Output:
[ [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],]
'''
res = Solution().combine_v1(n, k)
print(res)


n = 1
k = 1
# Output: [[1]]
res = Solution().combine_v2(n, k)
print(res)


