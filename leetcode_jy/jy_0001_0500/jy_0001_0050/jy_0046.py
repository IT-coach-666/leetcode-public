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
title_jy = "Permutations(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "排列问题 (全排列) | 相似题: 参考 permutation_combination_subset"


"""
Given an array `nums` of distinct integers, return all the possible 
permutations. You can return the answer in any order.


Example 1:
Input: nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

Example 2:
Input: nums = [0, 1]
Output: [[0, 1], [1, 0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of `nums` are unique.
"""


class Solution:
    """
解法 1: 递归

记 nums 的长度为 k, 则该题等价于: 先从 k 个数中取一个数, 然后和 k-1 个数
的组合进行组合
    """
    def permute_v1(self, nums: List[int]) -> List[List[int]]:
        ls_permutation = []
        self._permute(len(nums), nums, [], ls_permutation)
        return ls_permutation

    def _permute(self, count, nums, permutation, ls_permutation):
        """
        count: 由 nums 中的数值构成的一组排列 permutation 中, 还差 count 个
               数值待放入
        nums: 候选数值列表
        permutation: 当前的一组排列中的一部分
        ls_permutation: 记录所有排列情况
        """
        # jy: 如果当前的 count 为 0, 表示排列 permutation 中的数值已经齐全,
        #     因此将 permutation 加入到结果列表中, 并返回, 终止递归
        if count == 0:
            ls_permutation.append(permutation)
            return

        # jy: 遍历数组, 将遍历得到的数值作为第排列中的第一个数值或最后一个数
        #     值, 加入到排列列表中, 后续加入到排列结果中的数值不能再包含当前
        #     数值 (传递给递归调用的参数中要去除当前数值)
        for i, n in enumerate(nums):
            self._permute(count - 1,
                          nums[0:i] + nums[i+1:],
                          # jy: 将 nums 中的数值按顺序正序放入排列列表中
                          permutation + [n],
                          # jy: 将 nums 中的数值反序放入排列列表中
                          #[n] + permutation,
                          ls_permutation)


    """
解法 2: 同解法 1, 但换一种写法
    """
    def permute_v2(self, nums):
        if not nums:
            return
        ls_res = []
        n = len(nums)

        def helper2(nums, temp_list, len_, ls_res):
            # jy: 注意, n 不能换为 len(nums), 因为递归过程中传入
            #     的 nums 不断变化
            if len_ == n:
                ls_res.append(temp_list)
            for i in range(len(nums)):
                helper2(nums[:i] + nums[i+1: ], temp_list + [nums[i]], len_+1, ls_res)
        helper2(nums, [], 0, ls_res)
        return ls_res


    """
解法 3: 递归的另一种思路

图解参考: https://www.yuque.com/it-coach/leetcode/ged0o4
    """
    def permute_v3(self, nums: List[int]) -> List[List[int]]:
        def dfs(x):
            """
            固定第 nums[x] 个元素, 交换其它元素形成不同的排列
            """
            # jy: 如果交换至最后一个元素, 则表明完成一种排列方案, 将排列方
            #     案加入结果列表后 return, 终止递归
            if x == len(nums) - 1:
                ls_res.append(list(nums)) 
                return

            for i in range(x, len(nums)):
                # jy: 将 nums[i] 固定在第 x 位
                nums[i], nums[x] = nums[x], nums[i]
                # jy: 开始固定第 x+1 位的元素
                dfs(x + 1) 
                # jy: 回溯, 恢复交换
                nums[i], nums[x] = nums[x], nums[i]
        ls_res = []
        dfs(0)
        return ls_res


    """
解法 4: 递归求解 nums[1:] 的全排列, 然后将 nums[0] 与 nums[1:] 的全排列再排一次即可
    """
    def permute_v4(self, nums):
        if len(nums) == 1:
            return [nums]

        ls_res = []
        for sub in self.permute_v4(nums[1:]):
            for i in range(len(sub) + 1):
                ls_res.append(sub[:i] + [nums[0]] + sub[i:])
        return ls_res



nums = [1, 2, 3]
res = Solution().permute_v1(nums)
# jy: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(res)


nums = [0, 1]
res = Solution().permute_v2(nums)
# jy: [[0, 1], [1, 0]]
print(res)


nums = [1]
res = Solution().permute_v3(nums)
# jy: [[1]]
print(res)


nums = [1, 2, 3]
res = Solution().permute_v4(nums)
# jy: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(res)

