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
title_jy = "Design-Add-and-Search-Words-Data-Structure(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design a data structure that supports adding new words and finding if a string matches any
previously added string. Implement the WordDictionary class:
1) WordDictionary():   Initializes the object.
2) void addWord(word): Adds word to the data structure, it can be matched later.
3) bool search(word):  Returns true if there is any string in the data structure that matches word
                       or false otherwise. word may contain dots '.' where dots can be matched with
                       any letter.


Example:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad");  // return False
wordDictionary.search("bad");  // return True
wordDictionary.search(".ad");  // return True
wordDictionary.search("b..");  // return True


Constraints:
1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
"""


class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}

"""
解法1: Trie 的应用, 对 208_Implement-Trie-Prefix_Tree.py 中的 search 方法进行更新,
使其支持基于 "." 进行搜索(深度优先搜索);

JY: 时间/空间复杂度较差
"""
class WordDictionary_v1:
    def __init__(self):
        # jy: 初始化 Trie 树的根节点;
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        往 Trie 树中添加 word;
        """
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.end_of_word = True

    def search(self, word: str) -> bool:
        """
        从 Trie 树的根节点搜索单词 word (word 中支持 "." 表示模糊匹配任一字符);
        """
        return self._search(word, self.root)

    def _search(self, word, node):
        """
        从 Trie 树的 node 节点开始搜索 word (word 中支持 "." 表示模糊匹配任一字符);
        """
        current = node
        # jy: 由于后续可能需要跳过当前字符 c, 因此需要知道当前字符在 word 中的下标位置 i,
        #     随后可通过下标 i+1 开始表示跳过当前字符;
        for i, c in enumerate(word):
            # jy: 深度优先搜索; 如果当前搜索字符为 "." (表示可以匹配任一字符), 则跳过当前字符,
            #     从下一个字符开始搜索(对应的 Trie 节点也需要同步变更为当前节点所对应的下一子节点)
            if c == '.':
                for key, current_child in current.children.items():
                    if self._search(word[i+1:], current_child):
                        return True
                return False
            # jy: 如果搜索字符不为 ".", 且不在当前节点的子节点中, 则返回 False;
            #     注意: 必须先确保字符 c 不为 "." 后才进行当前判断, 否则直接进行当前判断时, 如果碰
            #     到的的字符 "." 会直接返回 False, 不符合预期;
            elif c not in current.children:
                return False
            # jy: 如果搜索字符在当前节点的子节点中, 则进行下一轮循环, 判断下一个搜索
            #     字符是否在 Trie 树的下一相邻层子节点中;
            else:
                current = current.children[c]
        # jy: 经过以上 for 循环后, current 为 word 最后一个字符对应的 TrieNode 节点, 如果
        #     其 end_of_word 属性为 Ture, 表明该单词存在;
        return current.end_of_word

    def _search_2022_02_27(self, word, node):
        """
        从 Trie 树的 node 节点开始搜索 word;
        """
        current = node
        for idx, char in enumerate(word):
            if char == ".":
                for char_i, node in current.children.items():
                    if self._search(word[idx + 1:], node):
                        return True
                return False
            elif char not in current.children:
                return False
            else:
                current = current.children[char]
        return current.end_of_word


"""
解法2: 基于双字典求解(时间复杂度略有提升, 空间复杂度极佳);
"""
class WordDictionary_v2:
    def __init__(self):
        # jy: 记录单词以及单词对应的长度;
        self.word_len = {}
        self.len_words = defaultdict(list)

    def addWord(self, word: str) -> None:
        # jy: 如果单词 word 已经存在于 self.word_len 字典中, 表明之前已经添加过, 不需要
        #     重复添加; 否则基于单词长度添加到 self.len_words 和 self.word_len 中;
        if word not in self.word_len:
            len_ = len(word)
            self.len_words[len_].append(word)
            self.word_len[word] = len_

    def search(self, word: str) -> bool:
        # jy: 如果单词在 self.word_len 字典中, 直接返回 True;
        if word in self.word_len:
            return True

        # jy: 从与 word 长度相同的候选单词列表中查找:
        for w in self.len_words[len(word)]:
            # jy: 如果 "." 在 word 中, 则当前单词 w 可能与 word 匹配(否则不可能匹配, 因为
            #     word 中的每个字符都是确定不变的, 且该长度的单词中之前没找到匹配的结果);
            if '.' in word:
                # jy: length 记录截止当前位置 w 与 word 能相互匹配的下标位置;
                length = 0
                for i in range(len(w)):
                    if w[i] == word[i] or word[i] == '.':
                        length += 1
                    else:
                        break
                if length == len(w):
                    return True
        return False


wordDictionary = WordDictionary_v1()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))   # return False
print(wordDictionary.search("bad"))   # return True
print(wordDictionary.search(".ad"))   # return True
print(wordDictionary.search("b.."))   # return True


