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
title_jy = "Majority-Element(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of size n, find the majority element. The majority element is the element
that appears more than ⌊ n/2 ⌋ times. You may assume that the array is non-empty and the
majority element always exist in the array.


Example 1:
Input: [3, 2, 3]
Output: 3

Example 2:
Input: [2, 2, 1, 1, 1, 2, 2]
Output: 2
"""


from typing import List
class Solution:
    """
遇到求个数的, 第一反应可以考虑使用 Map, 记录每个数字出现的次数, 最后遍历 Map, 如果数字的次数大于
数组长度的一半, 则返回这个数, 注意这里不能用整除, 否则类似 [1, 2, 2] 这样, 数组长度整除为 1, 最
后会返回 1 而不是 2;
    """
    def majorityElement(self, nums: List[int]) -> int:
        number_mapping = {}

        for n in nums:
            number_mapping[n] = number_mapping.get(n, 0) + 1

        for key, value in number_mapping.items():
            # jy: 注意, 在 python3 中, "/" 代表非整除, "//" 才代表整除;
            #    而在 python2 中, 如果 "/" 的左右两边都是整数, 则也是整除; 可将其中一个数改成浮点
            #    数, 即可实现非整除运算;
            if value >= len(nums) / 2:
            #if value >= len(nums) / 2.0:
                return key


nums = [3, 2, 3]
# Output: 3
res = Solution().majorityElement(nums)
print(res)


nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2
res = Solution().majorityElement(nums)
print(res)


