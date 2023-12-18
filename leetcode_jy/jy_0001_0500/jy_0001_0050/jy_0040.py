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
tag_jy = "组合问题 (元素有重复、不可复选) | 递归 | 循环迭代 | 动态规划 | 相似题: 参考 permutation_combination_subset"


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

        # jy: 优化: 过滤掉不满足要求的数值, 使得后续流程更轻便
        candidates = [i for i in candidates if i <= target]

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

        # jy: 优化: 过滤掉不满足要求的数值, 使得后续流程更轻便
        candidates = [i for i in candidates if i <= target]

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
解法 3: 动态规划, 时间复杂度 O(n * m), 空间复杂度 O(m)
(n 是 candidates 数组长度, m 是 target 的值)

target 的解空间等于所有小于 target 值的解加上其与 target 的差值的集合
即动规函数: f(n) = set(f(n-1) + 1, f(n-2)+2, ..., f(0)+n)
考虑到 candidates 的可选值, 将函数进行优化为: 
f(n) = set(f(n-a1)+a1, f(n-a2)+a2, ..., f(n-am)+am), 其中 a1, ..., am 属
于 candidates, 且都小于等于 n

考虑到 candidates 里的值只能用一次, 将 candidates 每个元素的出现次数进
行计数 dict_num2count[am], 然后进行集合化处理, 每次 f(n) 新增一个解时需
要判断 am 是否在其中出现超过 dict_num2count[am], 如果超过, 则不放入 f(n)
的解中
    """
    def combinationSum2_v3(self, candidates: List[int], target: int) -> List[List[int]]:
        import collections 

        # jy: 对 candidates 中的数值出现次数进行统计, 每次进行判断
        dict_num2count = collections.defaultdict(int)
        for k in candidates:
            # jy: 优化: 去除值大于 target 的部分, 避免后续对其做些没必要的操作
            if k > target:
                continue
            dict_num2count[k] += 1

        # jy: 对候选值进行排序
        candidates = list(dict_num2count.keys())
        candidates.sort()

        # jy: 记录数值之和为指定值的所有子组合; 数值之和为 0 的子组合为空组合 
        dict_num2res = collections.defaultdict(list)
        # jy: 注意, 子组合的数据类型不能用集合, 因为可能有些数值存在多个; 用
        #     元组或列表即可, 后续需要统计数值的个数, 以判断是否相同数值被重
        #     复使用
        dict_num2res[0] = [[]]

        for num in candidates:
            for i in range(num, target + 1):
                for ls_num in dict_num2res[i - num]:
                    # jy: 对 ls_num 进行深拷贝 (列表的内置方法 copy 为深拷贝, 
                    #     等同于全切片: ls_num[:])
                    ls_num_tmp = ls_num.copy()
                    # jy: 将当前数值加入子组合, 使得子组合中的元素值为 i, 此
                    #     时该组合之前是否出现过(即是否有重复; 由于元素经过排
                    #     序, 因此子组合 (即列表) 也有序, 因此可直接判断列表
                    #     是否相等进而判断是否有重复), 如果没重复, 则将其加入
                    #     到 dict_num2res[i] 中 (注意: 还需判断子组合中的 num
                    #     数值的个数是否小于可使用的个数, 因为数值不可重复使用)
                    ls_num_tmp.append(num)
                    if ls_num_tmp not in dict_num2res[i] and \
                            ls_num_tmp.count(num) <= dict_num2count[num]:
                        dict_num2res[i].append(ls_num_tmp)

        return dict_num2res[target]


    """
解法 4: 动态规划
    """
    def combinationSum2_v4(self, candidates: List[int], target: int) -> List[List[int]]:

        # jy: 优化: 过滤掉不满足要求的数值, 使得后续流程更轻便
        candidates = [i for i in candidates if i <= target]

        # jy: 对列表进行排序
        candidates.sort()
        # jy: dp[i] 为一个集合, 集合中存放元组 (即子组合)
        #     dp[i] 用于记录所有值之和为 i 的子组合
        dp = [set() for _ in range(target + 1)]
        # jy: dp[0] 为一个包含空元组的集合: {()}, 表示和为 0 的子组合为空组合
        dp[0].add(())
        # jy: 遍历数组中的数值, 
        for num in candidates:
            # jy: 如果 num > target, 则此处没有遍历出任何值, 相当于跳过; 如果
            #     num <= target, 则会从 target 主键变小往 num 遍历, 基于值之和
            #     为 i-num 的所有子组合 (即 dp[i-num]), 结合 num 值更新值之和
            #     为 i 的子组合 dp[i]; 每轮外循环中 i 的初始值均为 target, 即
            #     总是优先找出与 num 结合能使得值之和为 target 的子组合, 最后
            #     一轮外循环也是优先更新 dp[target], 最终返回 dp[target] 中的
            #     所有子组合结果
            for i in range(target, num-1, -1):
            # jy: 从 target 逐步变小往 num 遍历可避免重复多次使用当前值; 如
            #     果从 num 逐步遍历至 target, 则 num 可能被重复使用, 比如
            #     candidates 为 [2, 5, 5, 5, 12], target 为 12, 最终结果为正
            #     确结果 [[12], [2, 5, 5]], 如果是从 num 逐步遍历至 target, 
            #     则 num 值可能被重复使用, 因为最开始第一轮外层循环时, num=2,
            #     第一轮内层循环时 i=2, 因此产生 dp[2] = {(2, )}, 当内层循环
            #     i=4 时, 又产生 dp[4] = {(2, 2)}, 同理直到 i=12 (为 target)
            #     时产生 dp[12] = {(2, 2, 2, 2, 2, 2)}, 结合后续其它 num 值的
            #     遍历, 最终结果为: [[12], [2, 5, 5], [2, 2, 2, 2, 2, 2]]
            #for i in range(num, target+1):
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

candidates = [2, 5, 2, 1, 2]
target = 5
res = Solution().combinationSum2_v4(candidates, target)
print(res)
"""
[[1, 2, 2],
 [5]]
"""


candidates = [2, 5, 5, 5, 12]
target = 12
res = Solution().combinationSum2_v4(candidates, target)
print(res)
"""
[[12], [2, 5, 5]]
"""


