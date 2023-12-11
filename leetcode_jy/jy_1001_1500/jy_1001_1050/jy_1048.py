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
title_jy = "Longest-String-Chain(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an array of words where each word consists of lowercase English letters.
wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.
For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.


Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
"""


from typing import List


class Solution:
    """
解法1
思想同 300. Longest Increasing Subsequence, 首先将数组按照单词长度排序, 记 dp[i] 表示以以该处的单词结尾的最长字符串链;
    """
    def longestStrChain(self, words: List[str]) -> int:
        sorted_words = sorted(words, key=lambda x: len(x))
        n = len(words)
        dp = [1] * n

        for i in range(1, n):
            j = i - 1
            word_length = len(sorted_words[i])
            max_length = 1

            while j >= 0 and len(sorted_words[j]) == word_length:
                j -= 1

            while j >= 0 and len(sorted_words[j]) + 1 == word_length:
                if self._is_valid(sorted_words[j], sorted_words[i]):
                    max_length = max(max_length, dp[j] + 1)

                j -= 1

            dp[i] = max_length

        return max(dp)

    def _is_valid(self, word1, word2):
        i, j = 0, 0

        while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
            i += 1
            j += 1

        j += 1

        while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
            i += 1
            j += 1

        return i == len(word1) and j == len(word2)


from typing import List


class Solution:
    """
解法2
解法2和解法1类似, 只是 dp 不再是数组, 而是直接将单词作为 key, 值就是以该单词结尾的最长字符串链;
    """
    def longestStrChain(self, words: List[str]) -> int:
        sorted_words = sorted(words, key=lambda x: len(x))
        max_length = 1
        dp = {}

        for word in sorted_words:
            dp[word] = 1

            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]

                if prev in dp:
                    dp[word] = max(dp[prev] + 1, dp[word])
                    max_length = max(max_length, dp[word])

        return max_length


