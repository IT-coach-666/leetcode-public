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
title_jy = "Shortest-Word-Distance-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design a data structure that will be initialized with a string array, and then it
should answer queries of the shortest distance between two different strings from
the array. Implement the ``WordDistance`` class:
WordDistance(String[] wordsDict) : initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) : returns the shortest distance between ``word1``
                                           and ``word2`` in the array wordsDict.


wordDistance = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
wordDistance.shortest("coding", "practice") // return 3
wordDistance.shortest("makes", "coding")    // return 1


Constraints:
1 <= wordsDict.length <= 3 * 10^4
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
At most 5000 calls will be made to shortest.
"""

import sys
from typing import List
import collections


"""
解法1: 直接复用 243_Shortest-Word-Distance.py
"""
class WordDistance_v1:
    def __init__(self, wordsDict: List[str]):
        self.words = wordsDict

    def shortest(self, word1: str, word2: str) -> int:
        prev_index = -1
        min_distance = sys.maxsize
        for i, word in enumerate(self.words):
            if word != word1 and word != word2:
                continue
            if prev_index != -1 and self.words[prev_index] != word:
                min_distance = min(min_distance, i - prev_index)
            prev_index = i
        return min_distance


"""
解法2: 在初始化时保存每个单词在数组中的位置，搜索时变为在两个有序数组中搜索距
离最近的两个位置
"""
class WordDistance_v2:
    def __init__(self, wordsDict: List[str]):
        # jy: self.length 属性作用不大(仅用于后续初始化最小距离, 可找一个最大值代替掉)
        self.length = len(wordsDict)
        # jy: 初始化一个默认值为空列表的字典, 随后将单词列表中的单词以及其对应的位置按
        #     key 为单词, value 为保存其出现的位置的列表的方式加入到字典中;
        self.positions = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.positions[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        position1 = self.positions[word1]
        position2 = self.positions[word2]
        i, j = 0, 0
        min_distance = self.length

        while i < len(position1) and j < len(position2):
            min_distance = min(min_distance, abs(position1[i] - position2[j]))
            # jy: 为了求出最小位置距离, 应使得两个单词的位置尽可能的相等, 如果 word1
            #     的单词位置 position1[i] 小于 word2 的单词位置 position2[j], 为了使
            #     得位置尽可能相等, 应找 word1 的下一个位置;
            if position1[i] < position2[j]:
                i += 1
            else:
                j += 1

        return min_distance


wordDistance = WordDistance_v1(["practice", "makes", "perfect", "coding", "makes"])
print(wordDistance.shortest("coding", "practice"))  # return 3
print(wordDistance.shortest("makes", "coding"))     # return 1


wordDistance = WordDistance_v2(["practice", "makes", "perfect", "coding", "makes"])
print(wordDistance.shortest("coding", "practice"))  # return 3
print(wordDistance.shortest("makes", "coding"))     # return 1


