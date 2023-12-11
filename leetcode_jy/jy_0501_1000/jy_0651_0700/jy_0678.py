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
title_jy = "Valid-Parenthesis-String(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true


Constraints:
1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""


class Solution:
    """
使用两个栈保存左括号的位置和星号的位置, 遍历字符串, 如果遇到左括号则将其加入到左括号栈中, 如果遇到星号, 则将其加入到星号栈中, 如果遇到右括号, 则从左括号栈或星号栈中出栈一个元素, 如果左括号栈和星号栈都为空, 则返回 False; 最后对左括号栈和星号栈依次出栈, 判断左括号的位置是否小于星号的位置, 如果不是则返回 False, 最后判断左括号栈是否为空
    """
    def checkValidString(self, s: str) -> bool:
        left_parenthesis = []
        stars = []

        for i, c in enumerate(s):
            if c == '(':
                left_parenthesis.append(i)
            elif c == ')':
                if left_parenthesis:
                    left_parenthesis.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            elif c == '*':
                stars.append(i)

        while left_parenthesis and stars:
            if left_parenthesis[-1] < stars[-1]:
                left_parenthesis.pop()
                stars.pop()
            else:
                return False

        return not left_parenthesis


