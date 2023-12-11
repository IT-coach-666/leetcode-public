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
title_jy = "Palindrome-Partitioning-IV(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string s, return trueif it is possible to split the stringsinto three non-empty palindromic substrings. Otherwise, return false.
A string is said to be palindrome if it the same string when reversed.

Example 1:
Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.

Example 2:
Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.


Constraints:
3 <= s.length <= 2000
s consists only of lowercase English letters.
"""

class Solution:
    """
记 dp[i][j] 表示 s[i:j + 1] 是回文, 首先构造出 dp, 如果字符串最后可以拆成3个回文, 那必然是拆成左中右三个部分是回文, 最后遍历 dp 判断左中右三个部分是否是回文;
    """
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] if i + 1 <= j - 1 else True

        for i in range(1, n - 1):
            for j in range(i, n - 1):
                if dp[0][i - 1] and dp[i][j] and dp[j + 1][n - 1]:
                    return True

        return False


