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
title_jy = "Valid-Palindrome-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string s and an integer k, return true if s is a k-palindrome.
A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

Example 1:
Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.

Example 2:
Input: s = "abbababa", k = 1
Output: true


Constraints:
1 <= s.length <= 1000
s consists of only lowercase English letters.
1 <= k <= s.length
"""


class Solution:
    """
解法1
在 516. Longest Palindromic Subsequence 的基础上只允许删除最多 k 个字符, 在使用动态规划求解最长回文子串的同时记录 s[i] 到 s[j] 构成回文子串需要删除几个字符, 最后判断整个字符串删除的字符个数是否小于等于 k;
    """
    def isValidPalindrome(self, s: str, k: int) -> bool:
        if not s:
            return True

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        removed = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            removed[i][i] = 0

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    removed[i][j] = removed[i + 1][j - 1]
                else:
                    if dp[i + 1][j] > dp[i][j - 1]:
                        dp[i][j] = dp[i + 1][j]
                        removed[i][j] = 1 + removed[i + 1][j]
                    elif dp[i + 1][j] < dp[i][j - 1]:
                        dp[i][j] = dp[i][j - 1]
                        removed[i][j] = 1 + removed[i][j - 1]
                    else:
                        dp[i][j] = dp[i][j - 1]
                        removed[i][j] = 1 + min(
                            removed[i][j - 1], removed[i + 1][j])

        return dp[0][n - 1] > 0 and removed[0][n - 1] <= k

class Solution:
    """
解法2
解法1额外维护二维数组是多余的, 最后直接判断 n - dp[0][n - 1] <= k 即可;
    """
    def isValidPalindrome(self, s: str, k: int) -> bool:
        if not s:
            return True

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return n - dp[0][n - 1] <= k


class Solution:
    """
解法3:
依然是使用动态规划求解, 只是 dp[i][j] 的定义改为需要删除多少个字符才能将 s[i] 到 s[j] 的字符子串变为回文, 最后返回 dp[0][n - 1] <= k 即可;
    """
    def isValidPalindrome(self, s: str, k: int) -> bool:
        if not s:
            return True

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 0

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1] <= k


