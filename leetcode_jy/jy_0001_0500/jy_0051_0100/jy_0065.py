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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Valid-Number(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
A valid number can be split up into these components (in order):
1) A decimal number or an integer.
2) (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
1) (Optional) A sign character (either '+' or '-').
2) One of the following formats:
   a) One or more digits, followed by a dot '.'.
   b) One or more digits, followed by a dot '.', followed by one or more digits.
   c) A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):
1) (Optional) A sign character (either '+' or '-').
2) One or more digits.

For example, all the following are valid numbers: 
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1",
 "53.5e93", "-123.456e789"]
while the following are not valid numbers: 
["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

Given a string `s`, return true if `s` is a valid number.

 
Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false
 

Constraints:
1) 1 <= s.length <= 20
2) `s` consists of only English letters (both uppercase and lowercase),
   digits (0-9), plus '+', minus '-', or dot '.'.
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/valid-number/solutions/2361385/65-you-xiao-shu-zi-you-xian-zhuang-tai-z-5lde/

    """
    def isNumber_v1(self, s: str) -> bool:
        states = [
            { ' ': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start with 'blank'
            { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e'
            { 'd': 2, '.': 3, 'e': 5, ' ': 8 }, # 2. 'digit' before 'dot'
            { 'd': 3, 'e': 5, ' ': 8 },         # 3. 'digit' after 'dot'
            { 'd': 3 },                         # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            { 's': 6, 'd': 7 },                 # 5. 'e'
            { 'd': 7 },                         # 6. 'sign' after 'e'
            { 'd': 7, ' ': 8 },                 # 7. 'digit' after 'e'
            { ' ': 8 }                          # 8. end with 'blank'
        ]
        p = 0                           # start with state 0
        for c in s:
            if '0' <= c <= '9': t = 'd' # digit
            elif c in "+-": t = 's'     # sign
            elif c in "eE": t = 'e'     # e or E
            elif c in ". ": t = c       # dot, blank
            else: t = '?'               # unknown
            if t not in states[p]: return False
            p = states[p][t]
        return p in (2, 3, 7, 8)


s = "0"
res = Solution().isNumber_v1(s)
# jy: true
print(res)


s = "e"
res = Solution().isNumber_v1(s)
# jy: false
print(res)


s = "."
res = Solution().isNumber_v1(s)
# jy: false
print(res)

