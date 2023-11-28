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
title_jy = "Valid-Parentheses(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "栈的应用"



"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:    
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""


class Solution:
    """
栈的典型应用: 初始化一个栈, 用于保存遇到的左括号, 然后遍历数组:
1) 如果遇到左括号, 则将其入栈
2) 如果遇到右括号, 则出栈一个左括号判断两者是否匹配, 如果不匹配
   则返回 false, 否则继续循环

当循环结束时, 判断栈是否为空, 如果为空则返回 true, 否则说明有左
括号未匹配, 返回 false
    """
    def isValid_v1(self, s: str) -> bool:
        # jy: 左右括号之间的一一匹配
        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']'}
        stack = []
        for c in s:
            # jy: 如果为左括号, 直接入栈
            if c in parentheses:
                stack.append(c)
            # jy: 如果为右括号, 则需确保栈不为空, 且出栈的左括号必须与当前
            #     右括号匹配, 否则返回 False
            else:
                if not stack or parentheses[stack.pop()] != c:
                    return False
        return not stack

    """
解法 2: 同解法 1, 只是改变字典的 key 与 value 值 (依然要求左括号入栈)
    """
    def isValid_v2(self, s: str) -> bool:
        # jy: dict_ 中的 key 为右括号字符, value 为对应的左括号字符;
        dict_ = {")": "(", 
                 "}": "{", 
                 "]": "["}
        stack = []
        # jy: 遍历字符串中的每个括号字符
        for char in s:
            # jy: 如果字符为右括号字符, 且栈为空, 或出栈的左括号与当前的右
            #     括号不匹配, 则直接返回 False
            if char in dict_:
                if not stack or stack.pop() != dict_[char]:
                    return False
            # jy: 如果为左括号, 则直接入栈
            else:
                stack.append(char)
        return not stack


s = "{[]}"
# Output: true
res = Solution().isValid_v1(s)
print(s, " === ", res)

s = "()"
# Output: true
res = Solution().isValid_v2(s)
print(s, " === ", res)

s = "()[]{}"
# Output: true
res = Solution().isValid_v1(s)
print(s, " === ", res)

s = "(]"
# Output: False
res = Solution().isValid_v2(s)
print(s, " === ", res)

s = "([)]"
# Output: False
res = Solution().isValid_v1(s)
print(s, " === ", res)

