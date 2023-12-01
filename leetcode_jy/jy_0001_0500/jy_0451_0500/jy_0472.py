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
title_jy = "Concatenated-Words(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of strings ``words`` (without duplicates), return all the concatenated words
in the given list of words. A concatenated word is defined as a string that is comprised
entirely of at least two shorter words in the given array.


Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
             "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
             "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]


Constraints:
1 <= words.length <= 10^4
0 <= words[i].length <= 1000
words[i] consists of only lowercase English letters.
0 <= sum(words[i].length) <= 10^5
"""


from typing import List


class Solution:
    """
解法1: 遍历每个单词, 将单词拆成两部分 prefix 和 suffix, 对每一组 prefix 和 suffix,
如果 prefix 和  suffix 都在字典中, 说明两者是独立的单词, 返回 True; 如果 prefix 在
字典中, suffix 没有在字典中, 则需要判断 suffix 是否由几个独立的单词组成; 如果 prefix
在不在字典中, suffix 在字典中, 则需要判断 prefix 是否由几个独立的单词组成
    """
    def findAllConcatenatedWordsInADict_v1(self, words: List[str]) -> List[str]:
        word_set = set(words)
        result = []

        for word in words:
            if self._dfs(word, word_set):
                result.append(word)

        return result

    def _dfs(self, word, words):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            if prefix in words and suffix in words:
                return True

            if prefix in words and self._dfs(suffix, words):
                return True

            if suffix in words and self._dfs(prefix, words):
                return True

        return False

    """
解法2: 首先将单词按照长度遍历, 因为要找的单词是由更短的单词组成, 所以长度比当前
单词长的单词就无需关注; 遍历每个单词, 使用动态规划求解, 记 dp[i] 表示单词 word[0:i]
可以由某几个单词组成
    """
    def findAllConcatenatedWordsInADict_v2(self, words: List[str]) -> List[str]:
        sorted_words = sorted(words, key=lambda x: len(x))
        word_set = set()
        result = []

        for word in sorted_words:
            dp = [False] * (len(word) + 1)
            dp[0] = True

            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True

                        break

            if len(word) > 0 and dp[len(word)]:
                result.append(word)

            word_set.add(word)

        return result



