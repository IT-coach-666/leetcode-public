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
tag_jy = "UNDO 子集问题 | 相似题: 参考 permutation_combination_subset"


"""
Given an integer array `nums` that may contain duplicates, return all possible
subsets (the power set). The solution set must not contain duplicate subsets. 
Return the solution in any order.


Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""



class Solution(object):
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        n = len(nums)
        res = []
        nums.sort()
	# 思路1
        def helper1(idx, n, temp_list):
            if temp_list not in res:
                res.append(temp_list)
            for i in range(idx, n):
                helper1(i + 1, n, temp_list + [nums[i]])
	# 思路2
        def helper2(idx, n, temp_list):
            res.append(temp_list)
            for i in range(idx, n):
                if i > idx and  nums[i] == nums[i - 1]:
                    continue
                helper2(i + 1, n, temp_list + [nums[i]])

        helper2(0, n, [])
        return res


    """
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
以 nums = [1,2,2] 为例，为了区别两个 2 是不同元素，写作 nums = [1,2,2']。显然，两条值相同的相邻树枝会产生重复，如都有2：[1,2]，[1,2']，所以需要进行剪枝，如果一个节点有多条值相同的树枝相邻，则只遍历第一条，剩下的都剪掉，不要去遍历：遍历了[1,2]就不再遍历[1,2']。
在代码实现上，先对nums进行排序，在遍历时如果当前元素nums[i]与前一个元素相等nums[i] == nums[i-1]则跳过该元素（注意越界问题）：
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, track = list(), list()
        nums.sort()
        def backtrack(nums,start):
            # 子集问题 不需要判断结束条件 而是要把所有的track都加入res
            res.append(track[:])
            # 对于所有选择
            for i in range(start,len(nums)):
                # 先判断是否满足条件 如果与上一个重复就跳过 此时i > start比避免越界
                if i > start and nums[i] == nums[i-1]:
                    continue
                track.append(nums[i])
                backtrack(nums,i+1)
                track.pop()
        backtrack(nums,0)
        return res



nums = [1, 2, 2]
res = Solution().subsetsWithDup(nums)
# jy: [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(res)


nums = [0]
res = Solution().subsetsWithDup(nums)
# jy: [[],[0]]
print(res)




