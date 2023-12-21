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
title_jy = "Word-Search(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an m x n grid of characters `board` and a string `word`, return true if
word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.
 

Example 1:
Input: board = [
 ["A", "B", "C", "E"],
 ["S", "F", "C", "S"],
 ["A", "D", "E", "E"]]
word = "ABCCED"
Output: true

Example 2:
Input: board = [
 ["A", "B", "C", "E"],
 ["S", "F", "C", "S"],
 ["A", "D", "E", "E"]]
word = "SEE"
Output: true

Example 3:
Input: board = [
 ["A", "B", "C", "E"],
 ["S", "F", "C", "S"],
 ["A", "D", "E", "E"]]
word = "ABCB"
Output: false
 

Constraints:
1) m == board.length
2) n = board[i].length
3) 1 <= m, n <= 6
4) 1 <= word.length <= 15
5) `board` and `word` consists of only lowercase and uppercase English letters.
 

Follow up: 
Could you use search pruning to make your solution faster with a larger `board`?
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/word-search/solutions/2361646/79-dan-ci-sou-suo-hui-su-qing-xi-tu-jie-5yui2/
    """
    def exist_v1(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False


board = [
 ["A", "B", "C", "E"],
 ["S", "F", "C", "S"],
 ["A", "D", "E", "E"]]
word = "ABCCED"
res = Solution().exist_v1(board, word)
# jy: true
print(res)


board = [
 ["A", "B", "C", "E"],
 ["S", "F", "C", "S"],
 ["A", "D", "E", "E"]]
word = "SEE"
res = Solution().exist_v1(board, word)
# jy: true
print(res)


board = [
 ["A", "B", "C", "E"],
 ["S", "F", "C", "S"],
 ["A", "D", "E", "E"]]
word = "ABCB"
res = Solution().exist_v1(board, word)
# jy: false
print(res)


