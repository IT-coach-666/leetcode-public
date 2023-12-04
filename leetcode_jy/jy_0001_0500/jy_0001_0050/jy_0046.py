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
tag_jy = ""


"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""


from typing import List


class Solution:
    """
记 nums 的长度为 k, 则该题等价于先从 k 个数中取一个数, 然后和 k-1 个数的组合进行组合
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self._permute(len(nums), nums, [], permutations)
        return permutations

    def _permute(self, count, nums, permutation, permutations):
        # jy: count 记录还差一组排列中当前还差几个数; permutation 为当前的排列结果;
        #    nums 记录排列结果中的可选数值列表; permutations 存放所有排列情况; 如果
        #    当前的 count 为 0, 表示已经完成一组排列了, 将其加入到结果列表中; 并返回
        #    终止递归;
        if count == 0:
            permutations.append(permutation)
            return

        # jy: 遍历数组, 将遍历得到的数值作为第排列中的第一个数值, 加入到排列列表中, 随
        #    后后续加入到排列结果中的数值不能再包含当前该值, 故传递给递归调用的参数中
        #    要去除当前数值(即第二个参数);
        for i, n in enumerate(nums):
            self._permute(count - 1, nums[0:i] + nums[i+1:], permutation + [n], permutations)


nums = [1, 2, 3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
res = Solution().permute(nums)
print(res)


nums = [0, 1]
# Output: [[0,1],[1,0]]
res = Solution().permute(nums)
print(res)


nums = [1]
# Output: [[1]]
res = Solution().permute(nums)
print(res)


