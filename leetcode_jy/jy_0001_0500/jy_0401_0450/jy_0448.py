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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Find-All-Numbers-Disappeared-in-an-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear
twice and others appear once.Find all the elements of [1, n] inclusive that do not appear
in this array.

Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.

Example:
Input: [4,3,2,7,8,2,3,1]
Output: [5,6]
"""


from typing import List


class Solution:
    """
解法1: 额外开辟一个数组用于标记哪些数字存在, 然后遍历数组将对应数字标记为已存在, 最后遍历
用于标记的数组返回不存在的数字;
    """
    def findDisappearedNumbers_v1(self, nums: List[int]) -> List[int]:
        disappeared = []
        appeared = [0] * len(nums)

        for n in nums:
            appeared[n-1] = 1

        for i, n in enumerate(appeared):
            if n == 0:
                disappeared.append(i+1)

        return disappeared


    """
解法2: 如果不能使用额外的内存空间, 那么很可能就需要通过修改原数组来实现;
遍历数组, 将数组中以当前数字减 1 为下标的元素置为负数, 对于不存在的数来说, 以它们减 1 为
下标的元素不会置为负数, 最后再次遍历数组, 正数对应的数组下标加 1 所表示的数字就是缺少的数;
    """
    def findDisappearedNumbers_v2(self, nums: List[int]) -> List[int]:
        disappeared = []

        for n in nums:
            # jy: 注意, 由于可能存在重复出现的数值, 为了确保设置为负数, 需加上绝对值操作(防止
            #   去除绝对值操作后, 负负为正);
            index = abs(n) - 1
            nums[index] = -abs(nums[index])

        for i, n in enumerate(nums):
            if n > 0:
                disappeared.append(i + 1)

        return disappeared


nums = [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [5,6]
res = Solution().findDisappearedNumbers_v1(nums)
print(res)


res = Solution().findDisappearedNumbers_v2(nums)
print(res)


