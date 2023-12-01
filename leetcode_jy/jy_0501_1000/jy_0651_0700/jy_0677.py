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
title_jy = "Map-Sum-Pairs(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Implement the MapSum class:
MapSum() :                         Initializes the MapSum object.
void insert(String key, int val) : Inserts the key-val pair into the map. If the key already existed, the
                                   original key-value pair will be overridden to the new one.
int sum(string prefix) :           Returns the sum of all the pairs' value whose key starts with the prefix.


Example 1:
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");             # return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");             # return 5 (apple + app = 3 + 2 = 5)


Constraints:
1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
"""


from typing import Tuple


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        # jy: 记录每个字符的路径(即单词公共前缀的出现总次数)
        self.path_sum = 0
        # jy: 记录每个单词的值(单词出现的次数)
        self.word_value = 0


"""
Trie 的应用, 在 208_Implement-Trie-(Prefix-Tree).py 的基础上, 增加 path_sum 和 word_value 表
示每个字符的路径和以及每个单词的值, 插入时先进行搜索, 如果已经存在, 则对路径上的每个字符的路径和
需要减去已有单词的值, 并加上新的单词的值;
"""
class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        current = self.root
        # jy: 判断 key 对应的单词(或前缀)是否存在, 如果存在, 则返回: (True, 单词 key 出现的次数)
        #    注意是整个单词 key, 如果 key 是某单词的前缀部分, 则返回: (False, 前缀 key 出现的次数)
        exist, word_value = self._search(key)
        # jy: 遍历单词 key 中的字符;
        for c in key:
            # jy: 如果当前字符(单词前缀)不在 Trie 对应的单词前缀中, 则将该字符加入已有前缀的后续子
            #    字典中, 值为对应的 TrieNode 节点, 并将当前节点赋值为该字符对应的 TrieNode 节点;
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
            # jy: 如果 key 作为一个完整单词存在于 Trie 中, 则当前遍历的部分(即 key 的前缀) 对应的
            #    字符节点的 path_sum 属性均要减去该单词 key 出现的次数, 并加上 val (因为该单词 key
            #    出现的次数会由原先的 word_value 次修正为现在的 val 次, 即单词出现的次数会被更新
            #    为新的值, 减 word_value 再加上 val 即表示随着单词次数被更新, 以该单词的前缀部分
            #    的次数也随之被更新)
            if exist:
                current.path_sum = current.path_sum - word_value + val
            # jy: 如果该单词 key 不存在(即并非最为完整单词存在, 如: 只是某单词的前缀), 则当前字符对
            #    应的节点(即截止当前前缀为止的最后一个单词对应的 TrieNode 节点) 的 path_sum 属性值
            #    应为原有该前缀值加上当前 key 要设置的次数;
            else:
                current.path_sum += val
        # jy: 经过以上循环后的 current 即为 key 的最后一个字符对应的 TrieNode 节点, 该节点的 end_of_word
        #    属性表示该字符是 key 单词的结尾字符, word_value 属性即为该单词出现的次数;
        current.end_of_word = True
        current.word_value = val

    def sum(self, prefix: str) -> int:
        """计算所有前缀为 prefix 的单词的出现总次数"""
        current = self.root
        # jy: 前缀为 prefix 的单词的出现总次数即为 Trie 类中, 以 prefix 的最后一个字符串
        #    对应的 TrieNode 节点的 path_sum 数值的值; 此处即不断循环遍历前缀中的字符, 如
        #    果发现该前缀在 Trie 中并没有完整存在, 则直接返回 0, 否则遍历前缀的最后一个
        #    字符, 该字符对应的 path_sum 属性即为最终结果;
        for c in prefix:
            if c not in current.children:
                return 0

            current = current.children[c]

        return current.path_sum

    def _search(self, key: str) -> Tuple[bool, int]:
        """判断 key 所对应的单词是否在 Trie 中, 如果在, 返回 (True, 该单词的出现次数)"""
        current = self.root

        for c in key:
            if c not in current.children:
                return False, 0

            current = current.children[c]

        return current.end_of_word, current.word_value


mapSum = MapSum()
mapSum.insert("apple", 3)
print(mapSum.sum("ap"))              # return 3 (apple = 3)
mapSum.insert("app", 2)
print(mapSum.sum("ap"))              # return 5 (apple + app = 3 + 2 = 5)


def _search(self, key: str) -> Tuple[bool, int]:
    """判断 key 所对应的单词是否在 Trie 中, 如果在, 返回 (True, 该单词的出现次数)"""
    current = self.root

    for c in key:
        if c not in current.children:
            return False, 0

        current = current.children[c]

    return current.end_of_word, current.word_value



