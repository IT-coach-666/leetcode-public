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
title_jy = "Implement-Trie-II_Prefix-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently 
store and retrieve keys in a dataset of strings. There are various applications of this 
data structure, such as autocomplete and spellchecker.

Implement the Trie class:
Trie() : Initializes the trie object.
void insert(String word) : Inserts the string word into the trie.
int countWordsEqualTo(String word) : Returns the number of instances of the string 
                                     word in the trie.
int countWordsStartingWith(String prefix) : Returns the number of strings in the trie
                                            that have the string prefix as a prefix.
void erase(String word) : Erases the string word from the trie.



Example 1:
Trie trie = new Trie();
trie.insert("apple");                 # Inserts "apple".
trie.insert("apple");                 # Inserts another "apple".
trie.countWordsEqualTo("apple");      # There are two instances of "apple" so return 2.
trie.countWordsStartingWith("app");   # "app" is a prefix of "apple" so return 2.
trie.erase("apple");                  # Erases one "apple".
trie.countWordsEqualTo("apple");      # Now there is only one instance of "apple" so return 1.
trie.countWordsStartingWith("app");   # return 1
trie.erase("apple");                  # Erases "apple". Now the trie is empty.
trie.countWordsStartingWith("app");   # return 0



Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 10^4 calls in total will be made to insert, countWordsEqualTo, countWordsStartingWith, and erase.
It is guaranteed that for any function call to erase, the string word will exist in the trie.
"""


class TrieNode:
    def __init__(self):
        self.count = 0
        self.word_count = 0
        self.children = {}


"""
在 208_Implement-Trie_(Prefix-Tree).py 的基础上增加 count 和 word_count 分别表示字符的个
数和单词的个数, countWordsEqualTo 最后返回的是 word_count, countWordsStartingWith 最后返
回的是 count, erase 时如果当前节点的 count 为 0, 则从其父节点中删除当前节点; 
"""
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """将单词插入单词字典树中"""
        current = self.root
        # jy: 遍历单词中的字符, 每遍历一个字符, 该字符对应的 TrieNode 节点的 count 属性值加 1;
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]
            current.count += 1
        # jy: 单词最后一个字符对应的 word_count 属性值加 1;
        current.word_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        """统计单词的个数"""
        current = self.root
        # jy: 遍历单词, 如果出现某单词不存在于递归深度的字典树中, 则直接返回 0, 表明该单词不存在;
        for c in word:
            if c not in current.children:
                return 0

            current = current.children[c]
        # jy: 遍历到单词的最后一个字符时, 直接返回该字符对应的 TrieNode 类的 word_count 属性值(此
        #    时的该属性值也可能是 0, 代表截止当前递归深度的字符串仅仅是某单词的前缀部分);
        return current.word_count


    def countWordsStartingWith(self, prefix: str) -> int:
        """统计指定前缀的单词数"""
        current = self.root
        # jy: 同理 countWordsEqualTo 方法, 只是前缀数用 count 属性记录;
        for c in prefix:
            if c not in current.children:
                return 0
            current = current.children[c]

        return current.count


    def erase(self, word: str) -> None:
        """删除指定单词 word"""
        # jy: 题干中已明确删除的单词 word 肯定存在于字典树中, 故删除该单词时即可逐个遍历
        #    字符并对 count 属性值减 1 处理; 当字符对应的 TrieNode 的 count 属性值为 0
        #    时, 表明该字符应去除(用 prev 记录存放该字符的 TrieNode, 如果该 TrieNode 中
        #    count 属性值为 0, 则直接在 prev 的 children 字典中将该字符去除)
        current = self.root

        for c in word:
            if c not in current.children:
                return

            prev = current
            current = current.children[c]
            current.count -= 1

            if current.count == 0:
                prev.children.pop(c)
        # jy: 遍历到单词最后一个字符后, 该字符对应的 word_count 属性值减 1;
        current.word_count -= 1



trie = Trie()
trie.insert("apple")                        # Inserts "apple".
trie.insert("apple")                        # Inserts another "apple".
print(trie.countWordsEqualTo("apple"))      # There are two instances of "apple" so return 2.
print(trie.countWordsStartingWith("app"))   # "app" is a prefix of "apple" so return 2.
trie.erase("apple")                         # Erases one "apple".
print(trie.countWordsEqualTo("apple"))      # Now there is only one instance of "apple" so return 1.
print(trie.countWordsStartingWith("app"))   # return 1
trie.erase("apple")                         # Erases "apple". Now the trie is empty.
print(trie.countWordsStartingWith("app"))   # return 0



