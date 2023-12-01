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
title_jy = "Longest-Uncommon-Subsequence-I(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a group of two strings, you need to find the longest uncommon subsequence of this group of
two strings. The longest uncommon subsequence is defined as the longest subsequence of one of
these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters
without changing the order of the remaining  elements. Trivially, any string is a subsequence
of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon
subsequence. If the longest uncommon subsequence  doesn't exist, return -1.


Example 1:
Input: "aba", "cdc"
Output: 3
Explanation: The longest uncommon subsequence is "aba" (or "cdc"), because "aba" is a subsequence
             of "aba", but not a subsequence of any other strings in the group of two strings.


Note:
Both strings' lengths will not exceed 100.
Only letters from a ~ z will appear in input strings.
"""


class Solution:
    """
实际上就是找字符串 a 的子串, 该子串不是 b 的子串, 输出的是子串的最大长度(a 和 b 反过来同理)

如果两个字符串相等则返回 -1, 否则返回较长的字符串的长度;
    """
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))


a = "aba"
b = "cdc"

res = Solution().findLUSlength(a, b)
print(res)


