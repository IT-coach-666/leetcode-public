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
title_jy = "Palindrome-Partitioning-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given a string s containing lowercase letters and an integer k. You need to :
First, change some characters ofsto other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is a palindrome.
Return the minimal number of characters that you need to change to divide the string.

Example 1:
Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.

Example 2:
Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.

Example 3:
Input: s = "leetcode", k = 8
Output: 0


Constraints:
1 <= k <= s.length <= 100.
s only contains lowercase English letters.
"""


import sys


class Solution:
    """
遍历字符串, 对于字符子串判断 s[i:j + 1] 构成回文需要修改的字符个数, 再加上对于剩下的字符串 s[j + 1:] 组成 k - 1 个回文需要修改的字符个数;
    """
    def palindromePartition(self, s: str, k: int) -> int:
        return self._dfs(s, 0, k, {})

    def _cost(self, s, start, end):
        cost = 0

        while start < end:
            if s[start] != s[end]:
                cost += 1

            start += 1
            end -= 1

        return cost

    def _dfs(self, s, start, k, cache):
        if (start, k) in cache:
            return cache[(start, k)]

        if len(s) - start == k:
            return 0

        if k == 1:
            return self._cost(s, start, len(s) - 1)

        cut = sys.maxsize

        for end in range(start, len(s) - k + 1):
            current_cut = self._dfs(s, end + 1, k - 1, cache) \
                          + self._cost(s, start, end)
            cut = min(cut, current_cut)

        cache[(start, k)] = cut

        return cut


