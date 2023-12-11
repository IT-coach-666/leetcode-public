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
title_jy = "Longest-Common-Subsequence(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""


class Solution:
    """
使用动态规划求解, 记 dp[i][j] 表示 text1[0:i + 1] 和 text2[0:j + 1] 的最长公共子序列, 则:
1. text1[i] == text2[j], 则 text1[i] 和 text2[j] 可以成为公共子序列的一部分, dp[i][j] = dp[i - 1][j - 1] + 1
2. text1[i] != text2[j], 则 text1[i] 和 text2[j] 中只可能有一个有可能成为公共子序列的一部分, dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
实际编码时为了方便处理 dp[i - 1][j - 1] 将 dp 的容量初始化为了 (len(text1) + 1) * (len(text2) + 1)
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_length = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                max_length = max(max_length, dp[i][j])

        return max_length


