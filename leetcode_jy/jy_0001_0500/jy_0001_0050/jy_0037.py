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
title_jy = "Sudoku-solver(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the the digits 1-9 must occur exactly once in each of
   the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.

图例: https://www.yuque.com/frederick/dtwi9g/unru1c

Note:
• The given board contain only digits 1-9 and the character '.'.
• You may assume that the given Sudoku puzzle will have a single unique solution.
• The given board size is always 9x9.
"""
# ===============================================================
from typing import List
import pprint

class Solution:
    """
递归遍历求解, 遍历数独的每一个格子, 从 1 到 9 尝试放入数字, 如果该数字有效(行, 列, 九
宫格没有重复数字), 则以当前状态继续递归求解, 如果该数字最后无解, 则将该位置重新置为 "." ;
    """
    def solveSudoku(self, board: List[List[str]]) -> bool:
        return self._solve(board)

    def _solve(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for column in range(9):
                # jy: 如果对应的位置不为 '.', 表示已有数字, 不需要填充;
                if board[row][column] != '.':
                    continue
                # jy: 如果对应的位置为 '.', 尝试为其添加数字(数值范围为 1-9);
                for number in range(1, 10):
                    # jy: 如果该数加入后满足行, 列, box 的要求, 则加入, 并进一步递归求解;
                    if self._is_valid(board, row, column, str(number)):
                        board[row][column] = str(number)
                        if self._solve(board):
                            return True
                        else:
                            board[row][column] = '.'
                return False
        return True

    def _is_valid(self, board: List[List[str]], row: int,
                  column: int, number: str) -> bool:
        for i in range(9):
            # jy: 判断在指定 column 列中放入 number 后是否有效;
            if board[i][column] == number:
                return False

            # jy: 判断在指定 row 行中放入 number 后是否有效;
            if board[row][i] == number:
                return False

            # jy: 判断在指定 3x3 sub-boxes 中放入 number 后是否有效;
            box_row = 3*(row // 3) + i // 3
            box_column = 3*(column // 3) + i % 3
            if board[box_row][box_column] == number:
                return False
        return True


board = \
[['5', '3', '.', '.', '7', '.', '.', '.', '.'],
 ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
 ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
 ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
 ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
 ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
 ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
 ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
 ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
res = Solution().solveSudoku(board)
print(res)
print(pprint.pprint(board))

board = \
[['8', '3', '.', '.', '7', '.', '.', '.', '.'],
 ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
 ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
 ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
 ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
 ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
 ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
 ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
 ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
res = Solution().solveSudoku(board)
print(res)
print(pprint.pprint(board))


