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
title_jy = "Design-Search-Autocomplete-System(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design a search autocomplete system for a search engine.

You are given a string array ``sentences`` and an integer array ``times`` both of length
``n`` where ``sentences[i]`` is a previously typed sentence and ``times[i]`` is the
corresponding number of times the sentence was typed. For each input character except '#',
return the top 3 historical hot sentences that have the same prefix as the part of the
sentence already typed.  Here are the specific rules:
1) The hot degree for a sentence is defined as the number of times a user typed the exactly
   same sentence before.
2) The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one).
   If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
3) If less than 3 hot sentences exist, return as many as you can.
4) When the input is a special character, it means the sentence ends, and in this case, you need to
   return an empty list.

Implement the ``AutocompleteSystem`` class:
AutocompleteSystem(String[] sentences, int[] times) :
    Initializes the object with the sentences and times arrays.
List<String> input(char c) :
    This indicates that the user typed the character c.
        1) Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
        2) Returns the top 3 historical hot sentences that have the same prefix as the part of the
           sentence already typed. If there are fewer than 3 matches, return them all.


Example 1:
sentences = ["i love you", "island", "iroman", "i love leetcode"]
times = [5, 3, 2, 2]
AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
obj.input("i");   # return ["i love you", "island", "i love leetcode"]. There are four sentences that have
                  # prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree.
                  # Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in
                  # front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will
                  # be ignored.
obj.input(" ");   # return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
obj.input("a");   # return []. There are no sentences that have prefix "i a".
obj.input("#");   # return []. The user finished the input, the sentence "i a" should be saved as a historical
                  # sentence in system. And the following input will be counted as a new search.


Constraints:
n == sentences.length == times.length
1 <= n <= 100
1 <= sentences[i].length <= 100
1 <= times[i] <= 50
``c`` is a lowercase English letter, a hash '#', or space ' '.
Each tested sentence will be a sequence of characters ``c`` that end with the character '#'.
Each tested sentence will have a length in the range [1, 200].
The words in each input sentence are separated by single spaces.
At most 5000 calls will be made to input.
"""



from typing import List


class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}
        # jy: 记录被搜索的次数;
        self.searched_count = 0

"""
Trie 的应用: 对 Trie 节点增加 searched_count 字段表示被搜索的次数, 初始化时将搜索历史添加到 Trie 中;
输入时, 深度优先搜索所有包含当前输入文本的搜素历史, 根据搜索次数倒序排序后返回, 如果当前输入为 #, 则将
当前输入文本添加到 Trie 中, 并清空至今的输入记录;
"""
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        # jy: 记录当前搜索的句子;
        self.current_sentence = ''
        self.root = TrieNode()
        # jy: 将初始化时传入的 sentences 中的每个 sentence 插入到字典树中(即将每个 sentence 视
        #     为 word 插入, self.root 是字典树的根节点);
        for i, sentence in enumerate(sentences):
            self._insert(sentence, times[i])

    def _insert(self, sentence, count):
        """
        将候选句子添加到字典树中(即将 sentence 视为 word 插入, self.root 为 字典树的根节点);
        """
        current = self.root
        # jy: 遍历句子的每个字符, 如果该字符在当前 TrieNode (最开始为字典树的根节点 self.root)
        #     的子节点中, 则将 current 更新为该字符对应的 TrieNode 类(深度搜索); 否则将当前字符
        #     添加到当前 current 的子节点中(即在子节点字典中加入 {char: TrieNode}), 然后将 current
        #     更新为该字符对应的 TrieNode 类;
        for char in sentence:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        # jy: 记录句子的末尾(将整个句子看成一个单词的话, 也即单词的末尾)
        current.end_of_word = True
        # jy: current.searched_count 记录当前句子被搜索的次数(在句子末尾对应的单词中的 TrieNode
        #    类的相应属性中记录);
        current.searched_count += count

    def input(self, c: str) -> List[str]:
        # jy: 如果当前字符是 "#", 表示当前搜索的句子结束, 将当前句子添加
        #    到 Trie (AutocompleteSystem 类) 中, 并更新当前句子为空字符
        #    串, 同时直接返回 [];
        if c == '#':
            self._insert(self.current_sentence, 1)
            self.current_sentence = ''
            return []

        # jy: 如果当前字符不为 "#", 则将该字符添加到当前句子字符串中, 并搜索当前句
        #    子, 同时返回搜索结果;
        self.current_sentence += c

        return self._search(self.current_sentence)

    def _search(self, sentence):
        current = self.root
        # jy: path 用于记录遍历的字符, 最终即表示一个 sentence;
        path = ''
        paths = []
        # jy: 遍历句子中的字符, 如果其不在 current 所指的 TrieNode 中, 表明该句子不能
        #    搜索到, 直接返回 []
        for c in sentence:
            if c not in current.children:
                return []

            path += c
            current = current.children[c]
        # jy: 查找所有以 path 作为前缀的句子, 将其存入 paths 列表中;
        self._find_all(current, path, paths)
        # jy: 对 paths (是一个元组: (当前句子, 被搜索的次数))进行排序, 优先按搜索次数由
        #    高到低(次数的相反数由低到高, 即次数由高到低), 再按句子首字母由小到大;
        paths.sort(key=lambda x: (-x[1], x[0]))
        # jy: 返回排序结果的前 3 个句子;
        return [x[0] for x in paths[:3]]

    def _find_all(self, node, path_so_far, paths):
        """
        查找所有以 path_so_far 作为前缀的句子, 将其存入 paths 列表中;
        """
        # jy: 如果当前节点是句子末尾(将句子看作是单词, 即单词末尾), 则将元组 (当前句子, 被搜索的次数)
        #    加入到 paths 列表中;
        if node.end_of_word:
            paths.append((path_so_far, node.searched_count))
        # jy: 不断遍历 node 节点的子项, 找到所有与原先 path_so_far 为前缀的项, 将其加入到 paths 列表
        #    中(加入该列表的是一个元组: (当前句子, 被搜索的次数), 后续会基于被搜索的次数进行排序)
        for key, child in node.children.items():
            self._find_all(child, path_so_far + key, paths)



sentences = ["i love you", "island", "iroman", "i love leetcode"]
times = [5, 3, 2, 2]
obj = AutocompleteSystem(sentences, times)
print(obj.input("i"))   # return ["i love you", "island", "i love leetcode"]. There are four sentences that have
                        # prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree.
                        # Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in
                        # front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

print(obj.input(" "))   # return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
print(obj.input("a"))   # return []. There are no sentences that have prefix "i a".
print(obj.input("#"))   # return []. The user finished the input, the sentence "i a" should be saved as a historical
                        # sentence in system. And the following input will be counted as a new search.





