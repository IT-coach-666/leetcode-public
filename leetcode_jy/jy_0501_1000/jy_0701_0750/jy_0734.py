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
title_jy = "Sentence-Similarity(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
We can represent a sentence as an array of words, for example, the sentence
"I am happy with leetcode" can be represented as arr = ["I", "am", happy",
"with", "leetcode"].

Given two sentences ``sentence1`` and ``sentence2`` each represented as a
string array and given an array of string pairs ``similarPairs`` where
similarPairs[i] = [xi, yi] indicates that the two words ``xi`` and ``yi``
are similar.

Return true if ``sentence1`` and ``sentence2`` are similar, or false if they
are not similar. Two sentences are similar if:
1) They have the same length (i.e., the same number of words)
2) sentence1[i] and sentence2[i] are similar.

Notice that a word is always similar to itself, also notice that the similarity
relation is not transitive. For example, if the words ``a`` and ``b`` are similar,
and the words ``b`` and ``c`` are similar, ``a`` and ``c`` are not necessarily similar.


Example 1:
sentence1 = ["great","acting","skills"]
sentence2 = ["fine","drama","talent"]
similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
Output: true
Explanation: The two sentences have the same length and each word of ``sentence1``
             is also similar to the corresponding word in ``sentence2``.

Example 2:
sentence1 = ["great"]
sentence2 = ["great"]
similarPairs = []
Output: true
Explanation: A word is similar to itself.

Example 3:
sentence1 = ["great"]
sentence2 = ["doubleplus","good"]
similarPairs = [["great","doubleplus"]]
Output: false
Explanation: As they don't have the same length, we return false.


Constraints:
1 <= sentence1.length, sentence2.length <= 1000
1 <= sentence1[i].length, sentence2[i].length <= 20
sentence1[i] and sentence2[i] consist of English letters.
0 <= similarPairs.length <= 1000
similarPairs[i].length == 2
1 <= xi.length, yi.length <= 20
xi and yi consist of lower-case and upper-case English letters.
All the pairs (xi, yi) are distinct.
"""


import collections
from typing import List


class Solution:
    """
将 similarParis 转换为 Map, 遍历单词, 判断单词是否相等或者各自在 Map 中;
    """
    def areSentencesSimilar_v1(self, sentence1: List[str], sentence2: List[str],similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        # jy: 注意, 一个单词可能与多个单词相似, 故用集合保存相似的单词;
        similarities = collections.defaultdict(set)
        for a, b in similarPairs:
            similarities[a].add(b)
            similarities[b].add(a)

        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word1 != word2 and word1 not in similarities[word2] and word2 not in similarities[word1]:
                return False

        return True


sentence1 = ["great","acting","skills"]
sentence2 = ["fine","drama","talent"]
similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
# Output: true
res = Solution().areSentencesSimilar_v1(sentence1, sentence2, similarPairs)
print(res)


sentence1 = ["great"]
sentence2 = ["great"]
similarPairs = []
# Output: true
res = Solution().areSentencesSimilar_v1(sentence1, sentence2, similarPairs)
print(res)


sentence1 = ["great"]
sentence2 = ["doubleplus","good"]
similarPairs = [["great","doubleplus"]]
# Output: false
res = Solution().areSentencesSimilar_v1(sentence1, sentence2, similarPairs)
print(res)



