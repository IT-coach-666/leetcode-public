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
title_jy = "Find-Numbers-with-Even-Number-of-Digits(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array nums of integers, return how many of them contain an even number of digits.


Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 12 contains 2 digits (even number of digits).
             345 contains 3 digits (odd number of digits).
             2 contains 1 digit (odd number of digits).
             6 contains 1 digit (odd number of digits).
             7896 contains 4 digits (even number of digits).
             Therefore only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555,901,482,1771]
Output: 1
Explanation: Only 1771 contains an even number of digits.


Constraints:
1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""


from typing import List


class Solution:
    """
直接遍历数组, 将数字转为字符串, 判断字符串的长度是否是偶数;
    """
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda x: len(str(x)) & 1 == 0, nums)))


