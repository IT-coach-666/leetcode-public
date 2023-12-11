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
title_jy = "Single-Number(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?


Example 1:
Input: [2, 2, 1]
Output: 1

Example 2:
Input: [4, 1, 2, 1, 2]
Output: 4
"""


from typing import List


class Solution:
    """
位运算(异或运算)的应用:
1) 两个相等的数做异或操作返回 0
2) 0 和任何数做异或操作返回这个数本身
3) 异或操作支持交换律(A ^ B ^ A ^ D ^ B = A ^ A ^ B ^ B ^ D)

遍历数组做异或操作, 最后的结果就是只出现一次的数;
    """
    def singleNumber(self, nums: List[int]) -> int:
        number = nums[0]
        for i in range(1, len(nums)):
            number ^= nums[i]
        return number


nums = [2, 2, 1]
res = Solution().singleNumber(nums)
print(res)


nums = [4, 1, 2, 1, 2]
res = Solution().singleNumber(nums)
print(res)


