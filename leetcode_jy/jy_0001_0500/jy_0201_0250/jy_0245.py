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
title_jy = "Shortest-Word-Distance-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of strings ``wordsDict`` and two strings that already exist in the
array ``word1`` and ``word2``, return the shortest distance between these two words
in the list. Note that ``word1`` and ``word2`` may be the same. It is guaranteed that
they represent two individual words in the list.


Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"],
       word1 = "makes", word2 = "coding"
Output: 1

Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"],
       word1 = "makes", word2 = "makes"
Output: 3


Constraints:
1 <= wordsDict.length <= 10^5
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
"""


import sys
from typing import List
from collections import defaultdict


class Solution:
    """
在 243_Shortest-Word-Distance.py 的基础上计算距离时判断两个单词是否相等
    """
    def shortestWordDistance_v1(self, wordsDict: List[str], word1: str, word2: str) -> int:
        prev_index = -1
        min_distance = sys.maxsize

        for i, word in enumerate(wordsDict):
            if word != word1 and word != word2:
                continue

            if prev_index != -1 and (wordsDict[prev_index] != word or word1 == word2):
                min_distance = min(min_distance, i - prev_index)
            prev_index = i

        return min_distance

    """
JY: 参考 244_Shortest-Word-Distance-II.py 中的解法 2 进行实现;
    """
    def shortestWordDistance_jy(self, wordsDict, word1, word2):
        dict_ = defaultdict(list)
        for idx, word in enumerate(wordsDict):
            dict_[word].append(idx)
        min_distance = sys.maxsize
        if word1 == word2:
            ls_position = dict_[word1]
            for i in range(1, len(ls_position)):
                min_distance = min(min_distance, ls_position[i] - ls_position[i-1])
        else:
            ls_position1 = dict_[word1]
            ls_position2 = dict_[word2]
            i, j = 0, 0
            while i < len(ls_position1) and j < len(ls_position2):
                min_distance = min(min_distance, abs(ls_position1[i] - ls_position2[j]))
                if ls_position1[i] < ls_position2[j]:
                    i += 1
                else:
                    j += 1
        return min_distance


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
# Output: 1
res = Solution().shortestWordDistance_v1(wordsDict, word1, word2)
print(res)


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "makes"
# Output: 3
res = Solution().shortestWordDistance_jy(wordsDict, word1, word2)
print(res)


