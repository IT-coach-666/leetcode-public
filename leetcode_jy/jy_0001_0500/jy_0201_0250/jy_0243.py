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
title_jy = "Shortest-Word-Distance(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of strings ``wordsDict`` and two different strings that already exist
in the array ``word1`` and ``word2``, return the shortest distance between these two
words in the list.


Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"],
       word1 = "coding", word2 = "practice"
Output: 3

Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"],
       word1 = "makes", word2 = "coding"
Output: 1


Constraints:
1 <= wordsDict.length <= 3 * 10^4
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
"""


import sys
from typing import List


class Solution:
    """
记录上一个 word1 或者 word2 出现的位置, 如果上一个位子的单词和当前位置的
单词不同, 更新两个单词的最短距离
    """
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # jy: prev_index 记录上一个 word1 或 word2 的下标, 初始化为 -1;
        prev_index = -1
        min_distance = sys.maxsize

        for i, word in enumerate(wordsDict):
            # jy: 如果当前遍历的 word 既不是 word1 又不是 word2, 则跳过, 进行下一轮遍历;
            if word != word1 and word != word2:
                continue
            # jy: 如果代码执行到此处, 则表明当前遍历的单词 word 是 word1 或 word2 (其中一个);
            # jy: 如果 prev_index 不为 -1 (表明之前已经遍历过 word1 或 word2), 且之前遍历
            #     的 prev_index 对应的单词 wordsDict[prev_index] 与当前 word 不相同, 即表
            #     明上一个遍历的单词与当前的单词不同, 即上一个和当前单词就是 word1 和 word2
            #     这两个单词, 求其距离, 并判断是否对最短距离进行更新; 如果上一个单词和当前
            #     单词 word 相同, 则是相同单词, 不能更新两个不同单词的距离, 直接更新 prev_index 即可;
            if prev_index != -1 and wordsDict[prev_index] != word:
                min_distance = min(min_distance, i - prev_index)
            # jy: prev_index 记录上一个 word1 或 word2 的下标(即离当前单词最近的 word1 或 word2
            #     的下标);
            prev_index = i

        return min_distance


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
# Output: 3
res = Solution().shortestDistance(wordsDict, word1, word2)
print(res)


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
# Output: 1
res = Solution().shortestDistance(wordsDict, word1, word2)
print(res)


