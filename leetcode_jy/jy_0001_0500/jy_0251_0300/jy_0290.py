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
title_jy = "Word-Pattern(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a pattern and a string str, find if str follows the same pattern. Here follow
means a full match, such that there is a bijection between a letter in pattern and
a non-empty word in str.



Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false



Notes: You may assume pattern contains only lowercase letters, and str contains
lowercase letters that may be separated by a single space.
"""


class Solution:
    """
使用两个 Map 来保存 pattern 到 word 和 word 到 pattern 的映射, 然后遍历 pattern,
判断 word 和 pattern 是否匹配;
    """
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        pattern_to_word = {}
        word_to_pattern = {}

        # jy: 长度不匹配, 直接返回 False
        if len(pattern) != len(words):
            return False

        # jy: 遍历模式字符串, 模式字符串长度与单词个数相同;
        for i, c in enumerate(pattern):
            # jy: 如果模式字符与对应位置的单词均不在相应字典中, 则将其设置为互为映射关系;
            if c not in pattern_to_word and words[i] not in word_to_pattern:
                pattern_to_word[c] = words[i]
                word_to_pattern[words[i]] = c
            # jy: 如果两个字典中的映射关系中, 只是单向映射, 则直接返回 False
            elif (c in pattern_to_word and pattern_to_word[c] != words[i]) or \
                 (words[i] in word_to_pattern and word_to_pattern[words[i]] != c):
                return False

        return True



pattern = "abba"
str = "dog cat cat dog"
# Output: true
res = Solution().wordPattern(pattern, str)
print(res)


pattern = "abba"
str = "dog cat cat fish"
# Output: false
res = Solution().wordPattern(pattern, str)
print(res)


pattern = "aaaa"
str = "dog cat cat dog"
# Output: false
res = Solution().wordPattern(pattern, str)
print(res)


pattern = "abba"
str = "dog dog dog dog"
# Output: false
res = Solution().wordPattern(pattern, str)
print(res)


