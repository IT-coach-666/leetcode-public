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
title_jy = "Minimum-Remove-to-Make-Valid-Parentheses(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string s of '(' , ')' and lowercase English characters. Your task is to remove
the minimum number of parentheses —— '(' or ')' in any positions, so that the resulting
parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:'
1) It is the empty string, contains only lowercase characters, or
2) It can be written as AB (A concatenated with B), where A and B are valid strings, or
3) It can be written as (A), where A is a valid string.


Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


Constraints:
1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""


class Solution:
    """
核心思想同 020_Valid-Parentheses.py, 使用一个栈记录遇到的左括号的位置, 遍历字符串:
1) 如果遇到左括号则入栈 left_parentheses
2) 如果遇到右括号:
   a) 如果存放左括号的栈 left_parentheses 为空, 则当前位置的右括号需要删除, 用列表记录待删除的右括号位置;
   b) 如果存放左括号的栈 left_parentheses 不为空, 则出栈一个左括号

遍历完成后, 剩余的左括号加上已删除的右括号就是所有要删除的字符;
    """
    def minRemoveToMakeValid(self, s: str) -> str:
        # jy: 记录左括号对应的位置的栈;
        left_parentheses = []
        # jy: 记录需要删除的右括号的对应位置;
        removed_right_parentheses = []
        for i, c in enumerate(s):
            if c == '(':
                left_parentheses.append(i)
            elif c == ')':
                if not left_parentheses:
                    removed_right_parentheses.append(i)
                else:
                    left_parentheses.pop()

        removed = set(left_parentheses + removed_right_parentheses)

        # jy: version-1: ---------------------------------
        # valid_string = []
        # for i, c in enumerate(s):
        #     if i not in removed:
        #         valid_string.append(c)
        # return ''.join(valid_string)

        # jy: version-2: ---------------------------------
        return ''.join([str_ for i, str_ in enumerate(s) if i not in removed])



s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
res = Solution().minRemoveToMakeValid(s)
print(res)


s = "a)b(c)d"
# Output: "ab(c)d"
res = Solution().minRemoveToMakeValid(s)
print(res)


s = "))(("
# Output: ""
res = Solution().minRemoveToMakeValid(s)
print(res)


s = "(a(b(c)d)"
# Output: "a(b(c)d)"
res = Solution().minRemoveToMakeValid(s)
print(res)


