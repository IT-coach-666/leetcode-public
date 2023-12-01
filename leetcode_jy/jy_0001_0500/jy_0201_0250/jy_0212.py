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
title_jy = "Word-Search-II(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same letter
cell may not be used more than once in a word.


Example:
Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath", "pea", "eat", "rain"]
Output: ["eat", "oath"]



Note:
All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""



from typing import List, Set


class TrieNode_v2:
    def __init__(self):
        self.end_of_word = False
        self.children = {}

class Trie_v2:
    def __init__(self):
        # jy: 初始化 Trie_v2 时, 根节点为一个初始化的 TrieNode_v2 类;
        self.root = TrieNode_v2()

    def insert(self, word: str) -> None:
        # jy: current 最初为一个空的 TrieNode_v2 类;
        current = self.root
        # jy: 遍历单词的每个字符(以 "apple" 为例进行思考);
        '''
        self.root.children 值如下:
        {'a': TrieNode_v2()}
              self.root.children['a'].children 如下:
              {'p': TrieNode_v2()}

        '''
        for c in word:
            # jy: 如果字符 c 不在 children 字典中, 为该字符建立一个 key-value 对, key 为
            #    该字符, value 为一个初始化的 TrieNode_v2 节点; 即每个字符都应该有一个
            #    TrieNode_v2 类与之对应;
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
        # jy: 如果循环结束, 则表明是最后一个单词, 判断该单词是否是原先插入时的末尾即可;
        return current.end_of_word

    def startsWith(self, prefix: str) -> bool:
        """类似搜索过程, 但不需要判断单词是否是末尾, 只要确保过程中没有返回 False 即可"""
        current = self.root

        for c in prefix:
            if c not in current.children:
                return False

            current = current.children[c]

        return True


class Solution:
    """
借助 208_Implement-Trie-Prefix_Tree.py 中的 Trie 来实现, 首先将所有的单词都加入
到 Trie 中, 然后遍历二维字符数组的每一个字符, 递归搜索判断当前累加的字符串是否在
Trie 中, 如果存在, 则继续递归调用当前元素在二维字符数组中的上下左右四个方向;
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # jy: 该类来自 208_Implement-Trie-Prefix_Tree.py 中的解法2;
        trie = Trie_v2()
        result = set()
        rows, columns = len(board), len(board[0])
        # jy: 二维数组, 用以记录 board 中的对应位置的单词是否已经被访问过;
        visited = [[False for _ in range(columns)] for _ in range(rows)]
        # jy: 将单词列表加入到 Trie 中;
        for word in words:
            trie.insert(word)
        # jy: 遍历二维字符数组的每一个字符, 递归搜索判断当前累加的字符串是否在 Trie 中;
        for row in range(rows):
            for column in range(columns):
                # jy: board[row][column] 代表每次遍历的二维数组中的字符;
                self._dfs(row, column, board, '', trie, result, visited)

        return list(result)

    def _dfs(self, row: int, column: int, board: List[List[str]], word: str, trie: Trie_v2, result: Set[str],
             visited: List[List[bool]]) -> None:
        # jy: 如果 row 或 column 值超出了二维字符数组的界限, 则返回, 终止递归;
        if not (0 <= row < len(board) and 0 <= column < len(board[0])):
            return
        # jy: 如果在该递归中字符 board[row][column] 已经被遍历过, 则返回, 因为同一个字符不能被使用两次;
        if visited[row][column]:
            return
        # jy: 如果字符 board[row][column] 没有被使用过, 则将其加入 word 字符中;
        word += board[row][column]
        # jy: 如果当前的 word 字符串不是 Trie 中某单词的前缀, 则直接终止;
        if not trie.startsWith(word):
            return
        # jy: 如果当前的 word 在 Trie 中存在, 则直接将其加入 result 结果列表中;
        if trie.search(word):
            result.add(word)
            return   # jy: 补充, 待确认是否正确;

        # jy: 执行到此处时, 表明 word 作为某单词的前缀出现在 Trie 中, 此时将 board[row][column] 对
        #    应的字符设置为已访问过, 并继续递归调用当前元素在二维字符数组中的上下左右四个方向;
        visited[row][column] = True
        self._dfs(row - 1, column, board, word, trie, result, visited)
        self._dfs(row + 1, column, board, word, trie, result, visited)
        self._dfs(row, column - 1, board, word, trie, result, visited)
        self._dfs(row, column + 1, board, word, trie, result, visited)
        # jy: 递归调用当前元素在二维字符数组中的上下左右四个方向后, 需要重新将当前的 board[row][column]
        #    重新设置为未访问, 因为主方法(findWords 方法)中涉及到多次循环调用 _dfs 方法(存在多次主递归
        #    调用), 完成一轮主递归调用后, 需要恢复 visited[row][column] 为原先状态, 供下一轮主提柜调用
        #    使用;
        visited[row][column] = False

board = \
[ ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']]
words = ["oath", "pea", "eat", "rain"]
# Output: ["eat", "oath"]
res = Solution().findWords(board, words)
print(res)


