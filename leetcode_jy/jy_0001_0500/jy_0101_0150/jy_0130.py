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
title_jy = "Surrounded-Regions(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an m x n matrix `board` containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1: 图示参考: https://www.yuque.com/it-coach/leetcode/qd9tapagg6dksa5n
Input: board = [
["X", "X", "X", "X"],
["X", "O", "O", "X"],
["X", "X", "O", "X"],
["X", "O", "X", "X"]]
Output: [
["X", "X", "X", "X"],
["X", "X", "X", "X"],
["X", "X", "X", "X"],
["X", "O", "X", "X"]]
Explanation: Notice that an 'O' should not be flipped if:
             1) It is on the border, or
             2) It is adjacent to an 'O' that should not be flipped.
             The bottom 'O' is on the border, so it is not flipped.
             The other three 'O' form a surrounded region, so they are flipped.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
 

Constraints:
1) m == board.length
2) n == board[i].length
3) 1 <= m, n <= 200
4) board[i][j] is 'X' or 'O'.
"""


class Solution:
    """
解法 1: DFS

参考: https://www.yuque.com/it-coach/leetcode/qd9tapagg6dksa5n
    """
    def solve_v1(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = "B"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tmp_i = i + x
                tmp_j = j + y
                if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == "O":
                    dfs(tmp_i, tmp_j)

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                dfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                dfs(row - 1, j)

        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                dfs(i, 0)
            # 最后一列
            if board[i][col-1] == "O":
                dfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                # O 变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # B 变成 O
                if board[i][j] == "B":
                    board[i][j] = "O"

    """
解法 2: BFS
    """
    def solve_v2(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def bfs(i, j):
            from collections import deque
            queue = deque()
            queue.appendleft((i, j))
            while queue:
                i, j = queue.pop()
                if 0 <= i < row and 0 <= j < col and board[i][j] == "O":
                    board[i][j] = "B"
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        queue.appendleft((i + x, j + y))

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                bfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                bfs(row - 1, j)

        for i in range(row):

            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][col - 1] == "O":
                bfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"

                    
    """
解法 3: 并查集
    """
    def solve_v3(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        f = {}
        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
        def union(x, y):
            f[find(y)] = find(x)

            
            
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        dummy = row * col
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                union(i * col + j, (i + x) * col + (j + y))
        for i in range(row):
            for j in range(col):
                if find(dummy) == find(i * col + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

                    
board = [
["X", "X", "X", "X"],
["X", "O", "O", "X"],
["X", "X", "O", "X"],
["X", "O", "X", "X"]]
res = Solution().solve_v1(board)
print(res)
""" 
[["X", "X", "X", "X"],
 ["X", "X", "X", "X"],
 ["X", "X", "X", "X"],
 ["X", "O", "X", "X"]]
"""


board = [["X"]]
res = Solution().solve_v2(board)
print(res)
"""
[["X"]]
"""
