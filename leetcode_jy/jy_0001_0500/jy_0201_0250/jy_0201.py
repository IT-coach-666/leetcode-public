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
title_jy = "Bitwise-AND-of-Numbers-Range(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two integers `left` and `right` that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
 

Constraints:

0 <= left <= right <= 2^31 - 1
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/bitwise-and-of-numbers-range/solutions/384938/shu-zi-fan-wei-an-wei-yu-by-leetcode-solution/
    """
    def rangeBitwiseAnd_v1(self, m: int, n: int) -> int:
        shift = 0   
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift

    
    """
解法 2: 
    """
    def rangeBitwiseAnd_v2(self, m: int, n: int) -> int:
        while m < n:
            # 抹去最右边的 1
            n = n & (n - 1)
        return n

    
left = 5
right = 7
res = Solution().rangeBitwiseAnd_v1(left, right)
# jy: 4
print(res)


left = 0
right = 0
res = Solution().rangeBitwiseAnd_v1(left, right)
# jy: 0
print(res)


left = 1
right = 2147483647
res = Solution().rangeBitwiseAnd_v1(left, right)
# jy: 0
print(res)


