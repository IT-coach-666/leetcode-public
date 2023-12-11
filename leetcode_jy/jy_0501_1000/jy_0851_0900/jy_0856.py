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
title_jy = "Score-of-Parentheses(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a balanced parentheses string s, return the score of the string.
The score of a balanced parentheses string is based on the following rule:
"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Example 1:
Input: s = "()"
Output: 1

Example 2:
Input: s = "(())"
Output: 2

Example 3:
Input: s = "()()"
Output: 2

Example 4:
Input: s = "(()(()))"
Output: 6


Constraints:
2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
"""

class Solution:
    """
使用栈维护当前的分值, 如果遇到左括号, 则将当前分值入栈, 并重新初始化分值为0; 如果遇到右括号, 判断当前分值, 如果当前分值为0, 说明没有遇到嵌套的括号, 分值为1, 否则说明遇到嵌套括号将当前分值乘以2, 再弹出栈顶的分值就是同级括号的分值和;
    """
    def scoreOfParentheses(self, s: str) -> int:
        stack, score = [], 0

        for c in s:
            if c == '(':
                stack.append(score)
                score = 0

                continue

            if score == 0:
                score = 1
            else:
                score *= 2

            score += stack.pop()

        return score


