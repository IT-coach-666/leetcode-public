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
title_jy = "Implement-Trie-Prefix_Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A ``trie`` (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings. There are various
applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
Trie() :
    Initializes the trie object.
void insert(String word) :
    Inserts the string word into the trie.
boolean search(String word) :
    Returns true if the string word is in the trie (i.e., was inserted before),
    and false otherwise.
boolean startsWith(String prefix) :
    Returns true if there is a previously inserted string word that has the prefix
    prefix, and false otherwise.


Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true


Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


"""
解法1: 由于题中确保输入只含小写英文字母, 所以 TrieNode 中可直接使用了一个长度为 26 的数组
来存储孩子结点, 对于给定的字符 c, 要确定它应该对应哪个孩子结点就直接使用 ``ord(c)-97`` 即可;

JY: 孩子节点用一个新开辟的固定长度的 list 存储, 会额外占用多余空间; 时间复杂度和空间复杂度均一般;
"""
class TrieNode_v1:
    def __init__(self):
        self.end_of_word = False
        # jy: 孩子节点初始化为 26 个 None, 用于后续存放相应的小写英文字符;
        self.children = [None] * 26

class Trie_v1:
    def __init__(self):
        self.root = TrieNode_v1()

    def _get_child_index(self, c: str) -> int:
        """
        获取字符 c 在孩子节点列表中的下标位置;
        """
        # jy: ord("a") == 97;  ord("A") == 65;
        #     由于题目中说明字母均为小写字母, 故有: ord(c) >= 97
        return ord(c) - 97

    def insert(self, word: str) -> None:
        """
        将 word 插入字典树 Trie 中;
        """
        current = self.root
        for c in word:
            # jy: 获取字母 c 对应的 index('a'的 index 为 0, 'b' 为 1, 如此递增, 'z' 为 25)
            index = self._get_child_index(c)
            child = current.children[index]
            if not child:
                current.children[index] = TrieNode_v1()
            current = current.children[index]
        current.end_of_word = True

    def search(self, word: str) -> bool:
        """
        在 Trie 树中查找 word, 存在则返回 True, 不存在则返回 False;
        """
        current = self.root
        # jy: 遍历待查找单词中的每一个字符(类似往 Trie 树中插入 word, 只是当 child 为
        #     None 时直接返回 False, 表明 word 不存在); 遍历完后, 再判断末尾字符对应的
        #     TrieNode 类的 end_of_word 属性是否为 True (如果是, 表明单词 word 存在);
        for c in word:
            index = self._get_child_index(c)
            child = current.children[index]
            if not child:
                return False
            current = current.children[index]
        return current.end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        判断字典树中是否存在前缀为 prefix 的单词;
        """
        current = self.root
        # jy: 循环遍历前缀字符串中的字符(逻辑过程类似查找单词, 区别为: 只在查找过程中如果没
        #     有返回 False, 则最后返回 True);
        for c in prefix:
            index = self._get_child_index(c)
            child = current.children[index]
            if not child:
                return False
            current = current.children[index]
        return True


"""
解法2: 也可以使用 Map 来保存孩子节点, 从而节省空间;
"""
class TrieNode_v2:
    def __init__(self):
        self.end_of_word = False
        self.children = {}

class Trie_v2:
    def __init__(self):
        # jy: 初始化 Trie 树的根节点, 为一个 TrieNode 类;
        self.root = TrieNode_v2()

    def insert(self, word: str) -> None:
        # jy: current 最初为一个空的 TrieNode 类;
        current = self.root
        for c in word:
            # jy: 如果字符 c 不在当前节点的子节点中, 则将其加入到当前节点的子节点(key 为当
            #     前字符, value 为该字符对应的 TrieNode 类, 即每个字符都对应一个 TrieNode 类;
            if c not in current.children:
                current.children[c] = TrieNode_v2()
            # print(current.children)
            # jy: current 指向的类型总是 TrieNode_v2 类;
            current = current.children[c]
        # print(self.root.children)
        current.end_of_word = True

    def search(self, word: str) -> bool:
        """搜索的逻辑类似插入的逻辑, 只是当判断单词不存在时立即返回 False"""
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        # jy: 经过以上 for 循环后, current 为 word 中的最后一个单词对应的 TrieNode 类, 如果
        #     其 end_of_word 属性为 True, 则表明是最后一个单词;
        return current.end_of_word

    def startsWith(self, prefix: str) -> bool:
        """类似搜索过程, 但不需要判断单词是否是末尾, 只要确保过程中没有返回 False 即可"""
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie_2022_02_27:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True


trie = Trie_v1()
trie.insert("apple")
print(trie.search("apple"))    # returns true
print(trie.search("app"))      # returns false
print(trie.startsWith("app"))  # returns true
trie.insert("app")
print(trie.search("app"))      # returns true


trie = Trie_v2()
trie.insert("apple")
print(trie.search("apple"))    # returns true
print(trie.search("app"))      # returns false
print(trie.startsWith("app"))  # returns true
trie.insert("app")
print(trie.search("app"))      # returns true


