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
title_jy = "subsets-ii(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "子集问题 | 相似题: 参考 permutation_combination_subset"


"""
Given an integer array `nums` that may contain duplicates, return all possible
subsets (the power set). The solution set must not contain duplicate subsets. 
Return the solution in any order.


Example 1:
Input: nums = [1, 2, 2]
Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

Example 2:
Input: nums = [0]
Output: [[], [0]]
 

Constraints:
1) 1 <= nums.length <= 10
2) -10 <= nums[i] <= 10
"""



class Solution(object):
    """
解法 1: 递归
    """
    def subsetsWithDup_v1(self, nums):
        if not nums:
            return []

        def helper1(nums, idx, n, combination, ls_res):
            """
            尝试将 nums[idx: n] 中的元素逐个放入组合 combination 中, 并将
            不同的组合放入结果列表 ls_res

            递归函数中的参数 n 其实可以省略, 递归过程中用 len(nums[idx:]) 替
            代, 但这样会导致频繁计算 nums 子集的长度
            """
            # jy: 通过判断组合 (组合中的元素有序) 是否在结果列表中实现去重
            if combination not in ls_res:
                ls_res.append(combination)
            for i in range(idx, n):
                # jy: 将当前元素 nums[i] 加入组合中, 随后从下一个位置开始不断
                #     将元素加入组合
                helper1(nums, i+1, n, combination + [nums[i]], ls_res)

        def helper2(nums, idx, n, combination, ls_res):
            # jy: 直接将组合加入结果列表, 通过 for 循环中的 if 判断实现去重
            ls_res.append(combination)
            for i in range(idx, n):
                # jy: 以 nums = [1, 2, 2] 为例, 为了区别两个不同位置的 2, 写作
                #     nums = [1, 2, 2'], 如果上一轮递归中 combination 为 [1], 
                #     且在下一层更深的递归中传入的 idx 为 1, 即从第一个数值 2 
                #     开始, 当前同层级的 for 循环会遍历两个 2, 如果不加一下的
                #     if 判断逻辑, 则同层级的 for 循环执行完后, 调用下一更深层
                #     级的递归时会将 [1, 2] 和 [1, 2'] 都加入到结果列表, 导致
                #     子集重复; 所以在同层级的递归过程中, 如果当前元素的值与前
                #     一个位置 (需确认前一个位置的元素存在) 的元素值相同, 则应
                #     跳过该元素, 即可达到去重效果 (该判断需要在 nums 已经排序
                #     的情况下进行, 否则判断无效)
                if i > idx and  nums[i] == nums[i-1]:
                    continue
                helper2(nums, i+1, n, combination + [nums[i]], ls_res)

        n = len(nums)
        ls_res = []
        # jy: 先对数组进行排序, 使得后续的子集都有序, 方便判断是否重合
        nums.sort()
        #helper1(nums, 0, n, [], ls_res)
        helper2(nums, 0, n, [], ls_res)
        return ls_res


    """
解法 2: 递归 (解法 1 中 helper2 的另一种实现)

该方式与解法 1 中的区别是: 解法 1 中对 combination 的操作是直接在传参时操
作, 而当前解法中的 combination 会单独拎出来作为一个全局变量操作, 使得递归
过程中对该变量的操作会影响到后续递归过程, 因此递归过程中需要回溯处理
    """
    def subsetsWithDup_v2(self, nums: List[int]) -> List[List[int]]:
        ls_res = []
        combination = []
        nums.sort()
        def backtrack(nums, start):
            ls_res.append(combination[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                combination.append(nums[i])
                backtrack(nums,i+1)
                combination.pop()
        backtrack(nums, 0)
        return ls_res



nums = [1, 2, 2]
res = Solution().subsetsWithDup(nums)
# jy: [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(res)


nums = [0]
res = Solution().subsetsWithDup(nums)
# jy: [[],[0]]
print(res)




