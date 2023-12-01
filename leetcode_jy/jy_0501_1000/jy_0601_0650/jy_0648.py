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
title_jy = "Replace-Words(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
In English, we have a concept called ``root``, which can be followed by some other word to form
another longer word - let's call this word ``successor``. For example, when the ``root`` "an" is
followed by the ``successor`` word "other", we can form a new word "another".

Given a dictionary consisting of many ``roots`` and a sentence consisting of words separated by
spaces, replace all the ``successors`` in the sentence with the ``root`` forming it. If a ``successor``
can be replaced by more than one ``root``, replace it with the ``root`` that has the shortest length.
Return the sentence after the replacement.



Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"

Example 3:
Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
Output: "a a a a a a a a bbb baba a"

Example 4:
Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 5:
Input: dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
Output: "it is ab that this solution is ac"



Constraints:
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 10^6
``sentence`` consists of only lower-case letters and spaces.
The number of words in ``sentence`` is in the range [1, 1000]
The length of each word in ``sentence`` is in the range [1, 1000]
Each two consecutive words in ``sentence`` will be separated by exactly one space.
``sentence`` does not have leading or trailing spaces.
"""



from typing import List


class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}


class Solution:
    """
Trie 的应用: 首先将字典中的单词放入 Trie 中, 然后遍历句子中的单词, 在 Trie 中查找是否存
在单词为当前单词的前缀, 如果存在则替换;
    """
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # jy: 初始化 Trie, 赋值给 root;
        root = TrieNode()
        words = []
        # jy: 将字典中的单词放入 Trie 中;
        for word in dictionary:
            self._insert(root, word)
        # jy: 遍历句子中的单词, 在 Trie (即 root) 中查找是否存在单词为当前句子中的单词的
        #    前缀, 如果存在, 则替换;
        for word in sentence.split(' '):
            word_in_dictionary = self._search(root, word)

            if word_in_dictionary:
                words.append(word_in_dictionary)
            else:
                words.append(word)

        return ' '.join(words)


    def _insert(self, root, word: str) -> None:
        current = root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.end_of_word = True


    def _search(self, root, word: str) -> str:
        current = root
        # jy: 记录词根(即单词前缀)
        path = ''
        # jy: 遍历单词中的字符, 如果字符不在字典对应的 Trie 中, 则返回空字符串; 如果碰
        #    到某字符是 Trie 中的结尾字符, 则直接终止遍历, 并将该字符为止的前缀部分返
        #    回(即返回 path), 如果没有一个字符是 Trie 中的结尾字符, 最终仍返回空字符串;
        for c in word:
            if c not in current.children:
                return ''

            current = current.children[c]
            path += c

            if current.end_of_word:
                break

        return path if current.end_of_word else ''


dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
res = Solution().replaceWords(dictionary, sentence)
print(res)


dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
res = Solution().replaceWords(dictionary, sentence)
print(res)


dictionary = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
# Output: "a a a a a a a a bbb baba a"
res = Solution().replaceWords(dictionary, sentence)
print(res)

dictionary = ["catt","cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
res = Solution().replaceWords(dictionary, sentence)
print(res)


dictionary = ["ac","ab"]
sentence = "it is abnormal that this solution is accepted"
# Output: "it is ab that this solution is ac"
res = Solution().replaceWords(dictionary, sentence)
print(res)



