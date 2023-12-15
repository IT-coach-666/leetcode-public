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
tag_jy = "组合问题 (元素有重复、不可复选) | 递归 | 相似题: 参考 permutation_combination_subset"


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
解法 1:  0039 (Combination-Sum) 中输入列表元素没有重复、可复选, 本题中输入列
表元素有重复, 但不可复选

因此, 在 0039 的基础上补充:
1) 递归时从当前数值的下一个数值的下标位置开始
2) 对数组进行排序, 递归过程中如果当前递归调用的数值与上一个同层级递归调用的数
   值相同, 则跳过, 防止出现重复组合
    """
    def combinationSum2_v1(self, candidates: List[int], target: int) -> List[List[int]]:
        ls_res = []
        # jy: 对原列表进行排序, 递归求解, 从起始下标开始找
        self._dfs(sorted(candidates), 0, target, [], ls_res)
        return ls_res


    def _dfs(self, candidates, start, target, combination, ls_res):
        """
        从 candidates[start:] 中找出一个数值, 使得该数值与 combination 中所有
        数值之和为初始的 target, 如果找到这样的组合, 会在下一轮递归调用中存入
        ls_res
        """
        # jy: 如果剩余要找的数值 target 为 0, 表明当前的 combination 中的数值
        #     总和已经等于初始 target 值, 将其加入到结果列表, 并终止递归
        if target == 0:
            ls_res.append(combination)
            return
        # jy: 从候选数组中的下标为 start 的位置开始找组合中的元素;
        for i in range(start, len(candidates)):
            n = candidates[i]
            # jy: 如果该元素大于目标值 target, 则直接跳出循环, 终止;
            if n > target:
                break
            # jy: 递归过程中如果当前递归调用的数值与上一个同层级递归调用的数
            #     值相同, 则跳过, 防止出现重复组合
            # jy: 深度思考: 因为假如有两个连续位置数值相同的, 且最终两个相同
            #     的数值可以结合其它数值 (与连续相同的数值不同的数值) 构成一
            #     个满足条件的组合, 则当遍历第一个位置的数值时, 能找到一组组
            #     合满足要求; 当下一个同级递归调用遍历的数值与前一个数值相同
            #     时, 同样能找到其它数值 (与连续相同的数值不同的数值) 构成一
            #     个满足要求的组合, 导致重复; 如 candidates 为 [1, 1, 2, 5, 6],
            #     target 为 8, 如果添加该逻辑, 则结果为: [[1, 1, 6], [1, 2, 5], [2, 6]]
            #     如果不添加该逻辑, 则结果为: [[1, 1, 6], [1, 2, 5], [1, 2, 5], [2, 6]] 
            #     因此, 递归求解该题时, 需要先对列表进行排序, 否则按同样的逻
            #     辑仍可能产生重复组合的出现
            if i > start and candidates[i] == candidates[i-1]:
                continue

            # jy: 遍历完当前数值后, 下一个目标值为原目标值减去当前数值, 且从
            #     下一个数值位置开始遍历查找
            self._dfs(candidates, i+1, target - n, combination[:] + [n], ls_res)


    """
解法 2: 循环/迭代
    """
    def combinationSum2_v2(self, candidates: List[int], target: int) -> List[List[int]]:
        # jy: 对数组进行排序
        candidates.sort()
        ls_res = []
        # jy: ls_tmp 用于存放候选子组合, 的初始长度为 1 (1 个空列表)
        ls_tmp = [[]]
        # jy: 遍历有序数组的下标位置
        for i in range(len(candidates)):
            # jy: 遍历 ls_tmp 中的组合, 不断尝试往 ls_tmp 中的所有子组合中加
            #     入当前数值, 如果子组合中加入数值后能使得子组合数值之和正好
            #     为目标值, 则将子组合加入到结果列表; 否则如果加入后子组合中
            #     数值之和比目标值小, 则将其加入到候选子组合列表 ls_tmp 中;
            #     (如果加入后子组合的数值之和大于目标值, 则直接忽略)
            for k in range(len(ls_tmp)): 
                # jy: 初始时, k 为 0, 此处即深拷贝列表 (列表内置 copy 方法为
                #     深拷贝), 等同于列表全切片: ls_tmp[k][:]
                x = ls_tmp[k].copy()
                #x = ls_tmp[k][:]
                
                x.append(candidates[i])
                # jy: 子组合中的数值之和为目标值, 直接加入结果列表 (加入之前
                #     需判断是否有重复)
                if sum(x) == target:
                    if x not in ls_res:
                        ls_res.append(x)
                # jy: 子组合中的数值之和小于目标值, 直接加入候选子组合列表
                #     (加入时也需判断是否重复)
                elif sum(x) < target:
                    if x not in ls_tmp:
                        ls_tmp.append(x)
        return ls_res


    """
动规的朴素思想：target的解空间等于所有小于target值的解加上其与target的差值的集合。
即动规函数：f(n) = set(f(n-1) + 1, f(n-2)+2, ... , f(0)+n)
考虑到candidates的可选值，将函数进行优化，即：
f(n) = set(f(n-a1) + a1, f(n-a2)+a2, ... , f(n-am)+am), 其中a1,...,am属于candidates,且都小于等于n。
另外，考虑到candidates里的值只能用一遍，将candidates每个元素的出现次数进行计数times[am]，然后进行集合化处理，每次f(n)新增一个解时需要判断am是否在其中出现超过times[am]，如果超过，则不放入f(n)的解中。

时间复杂度为：O(nm)
空间复杂度为：O(m)
n是candidates数组长度，m是target的值
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 动规记表从0到target
        # 将candidates中的数出现次数进行计数，每次进行判断

        times = collections.defaultdict(int)
        for k in candidates:
            times[k] += 1
        candidates = list(times.keys())
        candidates.sort()
        n = len(candidates)
        ans = collections.defaultdict(list)
        
        ans[0] = [[]]

        for j in candidates:
            for i in range(j, target + 1):
                for item in ans[i - j]:
                    temp = item.copy()
                    temp.append(j)
                    if temp not in ans[i] and temp.count(j) <= times[j]:
                        ans[i].append(temp.copy())

        return ans[target]


    """
解法 3: 动态规划
    """
    def combinationSum2_v3(self, candidates: List[int], target: int) -> List[List[int]]:
        # jy: 对列表进行排序
        candidates.sort()
        # jy: dp[i] 为一个集合, 集合中存放元组 (即子组合)
        #     dp[i] 用于记录所有值之和为 i 的子组合
        dp = [set() for _ in range(target + 1)]
        # jy: dp[0] 为一个包含空元组的集合: {()}, 表示和为 0 的子组合为空组合
        dp[0].add(())
        # jy: 遍历数组中的数值, 
        for num in candidates:
            # jy: 从大到小遍历 target 至 num, 可避免重复多次使用当前值, 比如 candidates 为
            #     [6, 5, 2, 1, 1], target 为 8, 
            for i in range(target, num-1, -1):
                # jy: i - num 必定是大于等于 0, 小于 target 的数值, 如果存在
                #     和为 i - num 的子组合 sub_tup, 则表明往该组合中添加 num
                #     即可使得组合数值之和为 i, 因此往 dp[i] 集合中加入该组合
                for sub_tup in dp[i - num]:
                    dp[i].add(sub_tup + (num,))
        # jy: 返回 dp[target] 中的所有子组合
        return [list(tup) for tup in dp[target]]




candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
res = Solution().combinationSum2_v1(candidates, target)
print(res)
"""
[[1, 1, 6],
 [1, 2, 5],
 [1, 7],
 [2, 6]]
"""

candidates = [1, 1, 2, 5, 6]
target = 8
res = Solution().combinationSum2_v1(candidates, target)
print(res)
"""
[[1, 1, 6], [1, 2, 5], [2, 6]]
"""

candidates = [2, 5, 2, 1, 2]
target = 5
res = Solution().combinationSum2_v2(candidates, target)
print(res)
"""
[[1, 2, 2],
 [5]]
"""


candidates = [2, 5, 2, 1, 2]
target = 5
res = Solution().combinationSum2_v3(candidates, target)
print(res)
"""
[[1, 2, 2],
 [5]]
"""


