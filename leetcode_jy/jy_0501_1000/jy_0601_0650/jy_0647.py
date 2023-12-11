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
title_jy = "Palindromic-Substrings(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""


class Solution:
    """
解法1
使用动态规划求解, 记 dp[i][j] 表示 s[i: j + 1] 是否是回文, 则:
1. 如果 s[i] == s[j], dp[i][j] 是否为真取决于 dp[i + 1][j - 1] 是否为真
在构造 dp 时, 如果遇到 dp[i][j] 为真, 则对计数加1, 最后返回总的计数
    """
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = True if i + 1 > j - 1 else dp[i + 1][j - 1]

                if dp[i][j]:
                    count += 1

        return count


class Solution:
    """
解法2
遍历字符串, 以当前字符为中心(当前字符, 或者当前字符加上下一个字符), 向外发散判断是否是回文
    """
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            count += self._count_palindrome(s, i, i, n)
            count += self._count_palindrome(s, i, i + 1, n)

        return count

    def _count_palindrome(self, s, low, high, n):
        count = 0

        while low >= 0 and high < n and s[low] == s[high]:
            low -= 1
            high += 1
            count += 1

        return count


