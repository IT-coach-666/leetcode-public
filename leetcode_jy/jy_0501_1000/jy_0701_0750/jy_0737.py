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
title_jy = "Sentence-Similarity-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
We can represent a sentence as an array of words, for example, the sentence
"I am happy with leetcode" can be represented as arr = ["I", "am", "happy",
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
relation is transitive. For example, if the words ``a`` and ``b`` are similar, and
the words ``b`` and ``c`` are similar, then ``a`` and ``c`` are similar.


Example 1:
sentence1 = ["great","acting","skills"]
sentence2 = ["fine","drama","talent"]
similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
Output: true
Explanation: The two sentences have the same length and each word of ``sentence1`` is also
             similar to the corresponding word in ``sentence2``.

Example 2:
sentence1 = ["I","love","leetcode"]
sentence2 = ["I","love","onepiece"]
similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
Output: true
Explanation: "leetcode" --> "platform" --> "anime" --> "manga" --> "onepiece".  Since "leetcode"
             is similar to "onepiece" and the first two words are the same, the two sentences are similar.

Example 3:
sentence1 = ["I","love","leetcode"]
sentence2 = ["I","love","onepiece"]
similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
Output: false
Explanation: "leetcode" is not similar to "onepiece".


Constraints:
1 <= sentence1.length, sentence2.length <= 1000
1 <= sentence1[i].length, sentence2[i].length <= 20
sentence1[i] and sentence2[i] consist of lower-case and upper-case English letters.
0 <= similarPairs.length <= 2000
similarPairs[i].length == 2
1 <= xi.length, yi.length <= 20
xi and yi consist of English letters.
"""


import collections
from typing import List


class Solution:
    """
在 734_Sentence-Similarity.py 的基础上增加了相似的传导性;
为什么在 _is_similar 中只需要判断 (word1, word2) 的关系而不用考虑 (word2, word1) 的组合?
因为在构造 similarities 时已经将 (a, b) 和 (b, a) 的组合都放到 Map 中了
    """
    def areSentencesSimilarTwo_v1(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # jy: 句子长度不等则直接返回 False;
        if len(sentence1) != len(sentence2):
            return False

        # jy: 用一个字典({word: set_of_similar_words})记录单词之间的相似性;
        similarities = collections.defaultdict(set)
        for a, b in similarPairs:
            similarities[a].add(b)
            similarities[b].add(a)

        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            # jy: 如果两个单词不相同, 且根据相似字典判断得知两个单词不相似, 则表明句子的当前单词
            #     不相似, 直接返回 False;
            if word1 != word2 and not self._is_similar_v1(word1, word2, similarities, set()):
            # if word1 != word2 and not self._is_similar_v2(word1, word2, similarities):
            # if word1 != word2 and not self._is_similar(word1, word2, similarities, collections.defaultdict(bool)):
                return False
        return True

    def _is_similar(self, word1, word2, similarities, visited):
        """
        基于 similarities 中的相似单词映射关系(similarities 中的映射关系没体现相似单词的传递性), 判
        断 word1 和 word2 是否相似; 每次判断两个单词是否相似时, 初始传入的 visited 总是一个空字典(内
        部递归判断时则不再是空字典);
        """
        if (word1, word2) in visited:
            return visited[(word1, word2)]
        # jy: 如果 word1 在 word2 的相似单词集合中, 则表明 word1 和 word2 相似(不需要传导判断, 直接
        #     判断其相似), 直接返回 True;
        if word1 in similarities[word2]:
            visited[(word1, word2)] = True
            return True
        # jy: 如果 word1 不在 word2 的相似单词集合中, 表明不能直接判断其相似与否, 需依据单词相似传导
        #     性做进一步判断; 于是先标记 word1 和 word2 已被访问过且记录为 False(表明其不直接相似), 表明不能确定
        #     其是否相似;  后续的传导性判断中, 如果经过传导判断其相似, 则会直接返回 True;
        else:
            visited[(word1, word2)] = False

        # jy: 判断与 word1 相似的单词中, 是否有与 word2 相似的, 有则返回 True (递归进行相似传递性判断)
        for word in similarities[word1]:
            if self._is_similar(word, word2, similarities, visited):
                return True
        return False

    def _is_similar_v1(self, word1, word2, similarities, visited):
        """
        JY: 该方法待 LeetCode 上全面验证;
        基于 similarities 中的相似单词映射关系(similarities 中的映射关系没体现相似单词的传递性), 判
        断 word1 和 word2 是否相似; 初始传入的 visited 为一个空集合, 用于记录已访问过且不相似的单词;

        注意, 调用该方法传入的 word1 和 word2 确保是不同的, 如果相同则在上层逻辑中不会再调用该方法;
        """
        # jy: 如果单词组合在 visited 中, 表明其已访问过且不相似, 直接返回 False;
        if (word1, word2) in visited:
            return False
        # jy: 如果 word1 与 word2 直接相似, 则直接返回 True; 不管是在初始调用还是递归调用中, 一旦此
        #     处返回 True, 则表明原始的两个单词相似, 会直接退出递归调用;
        if word1 in similarities[word2]:
            return True
        # jy: 如果两个单词不直接相似, 暂设定其为不相似的单词, 加入到 visited 集合中; 如果其是间接相
        #     似, 则在以下的 for 循环进行递归调用时, 会直接返回 True;
        else:
            visited.add((word1, word2))
        for word in similarities[word1]:
            if self._is_similar_v1(word, word2, similarities, visited):
                return True
        return False

    def _is_similar_v2(self, word1, word2, similarities):
        """
        注意: 去掉 visited 会出现递归死循环, 出错, 举例如下:
        假设 similarities 如下:
        {'manga': {'onepiece', 'anime'},
         'onepiece': {'manga'},
         'platform': {'leetcode', 'anime'},
         'anime': {'platform', 'manga'},
         'leetcode': {'platform'}}
         则当 word1 和 word2 分别为 leetcode 和 onepiece 时, 按以上的 similarities 会陷入死循环(是否
         陷入死循环, 也取决于 similarities 中集合元素的相对顺序, 偶发);
        """
        # jy: 如果 word1 在 word2 的相似单词集合中, 则表明 word1 和 word2 相似(不需要传导判断, 直接
        #     判断其相似), 直接返回 True;
        if word1 in similarities[word2]:
            return True
        # jy: 判断与 word1 相似的单词中, 是否有与 word2 相似的, 有则返回 True (递归进行相似传递性判断)
        for word in similarities[word1]:
            if self._is_similar_v2(word, word2, similarities):
                return True
        # for word in similarities[word2]:
        #     if self._is_similar_v2(word1, word, similarities):
        #         return True
        return False


sentence1 = ["great","acting","skills"]
sentence2 = ["fine","drama","talent"]
similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
# Output: true
res = Solution().areSentencesSimilarTwo_v1(sentence1, sentence2, similarPairs)
print(res)


sentence1 = ["I","love","leetcode"]
sentence2 = ["I","love","onepiece"]
similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
# Output: true
res = Solution().areSentencesSimilarTwo_v1(sentence1, sentence2, similarPairs)
print(res)


sentence1 = ["I","love","leetcode"]
sentence2 = ["I","love","onepiece"]
# similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
similarPairs = [["hunterXhunter", "manga"], ["anime", "platform"], ["platform", "leetcode"], ["manga", "anime"]]
# Output: false
res = Solution().areSentencesSimilarTwo_v1(sentence1, sentence2, similarPairs)
print(res)


