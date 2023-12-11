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
title_jy = "Longest-Repeating-Substring(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a string s, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

Example 1:
Input: s = "abcd"
Output: 0
Explanation: There is no repeating substring.

Example 2:
Input: s = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.

Example 3:
Input: s = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.

Example 4:
Input: s = "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.


Constraints:
The string s consists of only lowercase English letters from 'a' - 'z'.
1 <= s.length <= 1500
"""


class Solution:
    """
利用 1143. Longest Common Subsequence 的思想, 将该题转化为求两个字符串的最大公共子序列, 不过有点不同:
1. text1[i] == text2[j], 还需要 i != j, 否则是两个相同的字符串
2. text1[i] != text2[j], 则 dp[i][j] = 0, 因为这题中的子串不支持删除字符
    """
    def longestRepeatingSubstring(self, s: str) -> int:
        return self._longest_common_subsequence(s, s)

    def _longest_common_subsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_length = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1] and i != j:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0

                max_length = max(max_length, dp[i][j])

        return max_length

class Solution:
    """
解法2: dp[i][j] 表示以 s[i] 和 s[j] 结尾的子字符串公共部分的长度;
    """
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        max_length = 0

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                max_length = max(max_length, dp[i][j])

        return max_length


