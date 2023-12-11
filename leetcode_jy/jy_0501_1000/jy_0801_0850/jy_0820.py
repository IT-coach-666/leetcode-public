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
title_jy = "Short-Encoding-of-Words(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A valid encoding of an array of words is any reference string ``s`` and array of
``indices`` indices such that:
words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to
(but not including) the next '#' character is equal to words[i].

Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

Example 1:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"

Example 2:
Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].


Constraints:
1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] consists of only lowercase letters.
"""


from typing import List


class Solution:
    """
该题等价于求一个新的列表, words 中的每个单词都是新列表中单词的后缀, 将 words 保存到 Set 中, 遍历单词, 从 Set 中删除所有可能的后缀
    """
    def minimumLengthEncoding(self, words: List[str]) -> int:
        word_set = set(words)

        for word in words:
            for i in range(1, len(word)):
                word_set.discard(word[i:])

        return sum(len(word) + 1 for word in word_set)


