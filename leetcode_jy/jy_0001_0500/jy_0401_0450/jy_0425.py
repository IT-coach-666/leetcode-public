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
title_jy = "Word-Squares(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of unique strings ``words``, return all the word squares you can build from
``words``. The same word from ``words`` can be used multiple times. You can return the
answer in any order.

A sequence of strings forms a valid word square if the k-th row and column read the same string,
where 0 <= k < max(numRows, numColumns). For example, the word sequence:
["ball",
 "area",
 "lead",
 "lady"]
forms a word square because each word reads the same both horizontally and vertically.


Example 1:
Input: words = ["area", "lead", "wall", "lady", "ball"]
Output: [
["ball",
 "area",
 "lead",
 "lady"],
["wall",
 "area",
 "lead",
 "lady"]]
Explanation: The output consists of two word squares. The order of output does not matter
             (just the order of words in each word square matters).

Example 2:
Input: words = ["abat", "baba", "atan", "atal"]
Output: [
["baba",
 "abat",
 "baba",
 "atal"],
["baba",
 "abat",
 "baba",
 "atan"]]


Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 5
All words[i] have the same length.
words[i] consists of only lowercase English letters.
All words[i] are unique.
"""


from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        # jy: end_of_word 属性用于记录单词的末尾; word 属性用于记录单词末尾时, 此时
        #    对应的具体单词;
        # jy: 其实可以只保留 word 属性即可, 当为空字符串时表示非单词末尾, 否则为相应
        #    单词的末尾;
        self.end_of_word = False
        self.word = ''


class Solution:
    """
Trie 的应用, 在 208_Implement-Trie-(Prefix-Tree).py 的基础上增加方法搜索所有包含指定前缀的单词;
搜索时, 维护一个候选集, 初始候选集为空, 根据候选集确定如何搜索下一个候选者: 假设候选集的长度为 k,
则下一个候选者满足其单词的前缀包含当前所有候选集中的第 k 个字符的组合:
1) 初始化时候选集为空, 前缀为空, 则搜索出的候选集为所有单词
2) 遍历所有候选者, 对每个候选者递归进行搜索, 如当前候选者为 wall, 根据定义, 下一个候选者的第一
   个字母必然是 a, 所以在 Trie 中搜索所有前缀为 a 的单词, 假设为 area, 则当前候选集更新为
   [wall,
    area], 在这个基础上, 下一个候选者必然是以 le 为前缀的单词, 依此类推;
3) 当候选集的长度等于第一个单词的长度时, 说明找到了一组满足条件的单词集合, 因为所有的单词长度相
   同(constraints 中明确表示), 组合成 word square 的单词个数必然等于每个单词字符的个数;
    """
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # jy: 如果为空列表, 直接返回空结果;
        if not words or not words[0]:
            return []
        # jy: 初始化 Trie 字典树的根节点;
        root = TrieNode()
        result = []
        # jy: 将列表中的单词插入到 Trie 字典树中;
        for word in words:
            self._insert(root, word)
        # jy: 在 Trie 字典树(根节点为 root)中寻找 word squares 单词列表(该方法的第二个参数
        #    明确列表的长度为单词字符串长度), 将找到的单词列表存放到 result 列表中, 最终返回;
        # jy: 最开始候选集为空(即第三个参数为 [])
        self._word_squares(root, len(words[0]), [], result)
        return result

    def _insert(self, root, word):
        current = root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.end_of_word = True
        current.word = word


    def _search_prefix(self, root, prefix, candidates):
        """
        在 Trie 字典树(root 为其根节点)中找出所有前缀为 prefix 的单词, 放入 candidates 列表中;
        如果 prefix 为空字符, 会将字典树中的所有单词加入到 candidates 列表;
        """
        current = root
        # jy: 如果当前 TrieNode 节点为单词末尾, 则将当前对应的单词(当前 TrieNode 节点的 word 属
        #    性记录)加入到列表中, 并返回终止递归;
        if current.end_of_word:
            candidates.append(current.word)
            return

        # jy: 循环遍历前缀字符串;
        for c in prefix:
            # jy: 如果字符 c 不在当前节点的 children 属性中, 则直接返回, 终止递归;
            if c not in current.children:
                return
            current = current.children[c]
        # jy: 如果以上循环遍历完前缀字符串后, 前缀字符串的最后一个字符对应的 TrieNode 节点中的
        #    children 字典属性中仍有单词(即为该前缀对应的所有单词), 则将所有以该前缀开头的单词
        #    加入到 candidates 中;
        for child in current.children.values():
            self._search_prefix(child, '', candidates)


    def _word_squares(self, root, size, words, result):
        # jy: 如果候选单词列表的长度已经为单词的长度, 则表示已经找到一组, 将其加入结
        #    果列表中, 并终止递归;
        if len(words) == size:
            result.append(words)
            return

        candidates = []
        # jy: 1) 第一次调用该方法时, 传入的候选集 words 为 [], 此时的 prefix 为 "", 此时调
        #       用 _search_prefix 方法后, candidates 中存放了字典树中的所有单词; 随后逐个
        #       遍历所有单词, 将所有组成 word square 的单词列表都加入到 result 列表中;
        #    2) 第二层递归调用时, 传入的候选者参数 words 列表中开始有一个单词, 如 wall, 根
        #       据定义, 下一个候选者的第一个字母必然是 a (此处的 prefix 逻辑即可获取该字符),
        #       随后在 Trie 中搜索所有前缀为 a 的单词, 假设为 area, 则当前候选集更新为
        #       [wall,
        #        area], 在这个基础上, 下一个候选者必然是以 le 为前缀的单词(此处的 prefix 逻辑
        #       同样依据列表中的单词获取到 le), 依此类推; 当候选集的长度等于第单词的长度时, 说
        #       明找到了一组满足条件的单词列表, 将其加入到结果列表中即可;
        prefix = ''.join([word[len(words)] for word in words])
        self._search_prefix(root, prefix, candidates)
        for candidate in candidates:
            self._word_squares(root, size, words + [candidate], result)



words = ["area", "lead", "wall", "lady", "ball"]
# Output: [["ball", "area", "lead", "lady"], ["wall", "area", "lead", "lady"]]
res = Solution().wordSquares(words)
print(res)


words = ["abat", "baba", "atan", "atal"]
# Output: [["baba", "abat", "baba", "atal"],["baba", "abat", "baba", "atan"]]
res = Solution().wordSquares(words)
print(res)


