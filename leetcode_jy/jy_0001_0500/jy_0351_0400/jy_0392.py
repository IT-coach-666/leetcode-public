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
title_jy = "Is-Subsequence(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two strings ``s`` and ``t``, return true if ``s`` is a subsequence of ``t``, or
false otherwise. A subsequence of a string is a new string that is formed from the
original string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde"
while "aec" is not).


Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9,
and you want to check one by one to see if t has its subsequence. In this scenario,
how would you change your code?
"""


class Solution:
    """
使用两个指针分别指向 s 和 t, 如果两个指针指向的字符相等, 则两个指针都向右移动一位, 当
两个指针指向的字符不同时, 仅移动 t 的指针, 直到两个指针指向的字符再次相同, 最后判断 s
的指针是否走完了 s
    """
    def isSubsequence_v1(self, s: str, t: str) -> bool:
        if not s:
            return True
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)


s = "abc"
t = "ahbgdc"
# Output: true
res = Solution().isSubsequence_v1(s, t)
print(res)


s = "axc"
t = "ahbgdc"
# Output: false
res = Solution().isSubsequence_v1(s, t)
print(res)


