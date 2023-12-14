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
1) Each of the digits 1-9 must occur exactly once in each row.
2) Each of the digits 1-9 must occur exactly once in each column.
3) Each of the the digits 1-9 must occur exactly once in each of
   the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.


Example 1:
图例参考: https://www.yuque.com/it-coach/leetcode/akzfg7

Input: board = [
 ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
 ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
 ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
 ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
 ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
 ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
 ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
 ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
 ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

Output: 
[['5', '3', '4', '6', '7', '8', '9', '1', '2'],
 ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
 ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
 ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
 ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
 ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
 ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
 ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
 ['3', '4', '5', '2', '8', '6', '1', '7', '9']]

Explanation: The input board is shown above and the only valid solution is
             shown below: 
             参考: https://www.yuque.com/it-coach/leetcode/akzfg7

Note:
1) The given board contain only digits 1-9 and the character '.'.
2) It is guaranteed that the input board has only one solution.
3) The given board size is always 9 x 9.
"""


import pprint

class Solution:
    """
解法 1: 递归遍历

遍历数独的每一个格子, 从 1 到 9 尝试放入数字, 如果该数字有效 (行、列、九
宫格没有重复数字), 则以当前状态继续递归求解, 如果该数字最后无解, 则将该
位置重新置为 "."
    """
    def solveSudoku_v1(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for column in range(9):
                # jy: 如果对位置的值不为 '.', 表示已有数字, 不需要再填充
                if board[row][column] != '.':
                    continue

                # jy: 如果对应的位置为 '.', 尝试为其添加数字 (数值范围为 1-9)
                for number in range(1, 10):
                    # jy: 如果该数加入后满足行、列、九宫格的要求, 则加入该数
                    #     并进一步递归求解; 如果该数加入后不满足, 则重置为 "."
                    if self._is_valid(board, row, column, str(number)):
                        board[row][column] = str(number)
                        if self.solveSudoku_v1(board):
                            return True
                        else:
                            board[row][column] = '.'
                # jy: 如果 9 个数都尝试完之后还不可以, 则返回 False
                return False
        return True

    def _is_valid(self, board: List[List[str]], row: int, column: int,
                  number: str) -> bool:
        """
        往 board[row][column] 填充 number 后, 判断 board 是否符合要求
        """
        for i in range(9):
            # jy: 判断在指定 column 列中放入 number 后是否有效;
            if board[i][column] == number:
                return False

            # jy: 判断在指定 row 行中放入 number 后是否有效;
            if board[row][i] == number:
                return False

            # jy: 判断在 3 x 3 的 sub-boxes 中放入 number 后是否有效;
            box_row = 3*(row // 3) + i // 3
            box_column = 3*(column // 3) + i % 3
            if board[box_row][box_column] == number:
                return False
        return True


    """
解法 2: 递归回溯 27 个集合, 性能极佳 (空间换时间)
    """
    def solveSudoku_v2(self, board: List[List[str]]) -> None:
        ls_row = [set() for _ in range(9)]
        ls_col = [set() for _ in range(9)]
        ls_box = [set() for _ in range(9)]
        ls_empty = []
        # jy: 遍历 board, 存储初始时行、列、九宫格中的数值, 以及
        #     待填充的位置坐标
        for row, line in enumerate(board):
            for column, char in enumerate(line):
                if char == '.':
                    ls_empty.append((row, column))
                else:
                    ls_row[row].add(char)
                    ls_col[column].add(char)
                    ls_box[(row // 3) * 3 + (column // 3)].add(char)

        # jy: 从 ls_empty 中的开头不断往后尝试填充
        #self.dfs(0, ls_empty, ls_row, ls_col, ls_box, board)
        # jy: 从 ls_empty 中的末尾不断往前尝试填充
        self.dfs2(len(ls_empty)-1, ls_empty, ls_row, ls_col, ls_box, board)

    def dfs(self, k, ls_empty, ls_row, ls_col, ls_box, board):
        """
        往 ls_empty[k] 中尝试填充数值 (递归过程中会从前往后尝试填充)

        ls_empty: 记录了待填充的坐标位置, 坐标位置从左到右、从上到下排序
        ls_row: ls_row[row] 为集合, 记录了第 row 行中已存在的数值
        ls_col: ls_col[column] 为集合, 记录了第 column 行中已存在的数值
        ls_box: ls_box[box_idx] 集合, 记录了第 box_idx 个九宫格中已存在的数值
        board: 9 * 9 矩阵
        """
        # jy: 如果 k == len(ls_empty), 表明之前的所有待填充位置均可正常
        #     填充, 返回 True
        if k == len(ls_empty):
            return True
        row, column = ls_empty[k]
        box_idx = (row // 3) * 3 + column // 3
        for char in '123456789':
            if not (char in ls_row[row] or char in ls_col[column] or char in ls_box[box_idx]):
                ls_row[row].add(char)
                ls_col[column].add(char)
                ls_box[box_idx].add(char)
                # jy: 从 ls_empty 的前面元素不断往后尝试填充, 如果可顺利填充,
                #     则将当前的位置坐标设置为当前的数值 char
                if self.dfs(k+1, ls_empty, ls_row, ls_col, ls_box, board):
                    board[row][column] = char
                    # jy: 注意, 此处必须要有 return True, 否则该递归函
                    #     数应用在该部分的 if 判断时, 即使满足条件也是
                    #     返回 None, 使得后续不会填充满足条件的值
                    return True

                ls_row[row].remove(char)
                ls_col[column].remove(char)
                ls_box[box_idx].remove(char)
        return False

    def dfs2(self, k, ls_empty, ls_row, ls_col, ls_box, board):
        """
        往 ls_empty[k] 中尝试填充数值 (递归过程中会从后往前尝试填充)

        ls_empty: 记录了待填充的坐标位置, 坐标位置从左到右、从上到下排序
        ls_row: ls_row[row] 为集合, 记录了第 row 行中已存在的数值
        ls_col: ls_col[column] 为集合, 记录了第 column 行中已存在的数值
        ls_box: ls_box[box_idx] 集合, 记录了第 box_idx 个九宫格中已存在的数值
        board: 9 * 9 矩阵
        """
        # jy: 如果 k < 0, 表明从后往前填充均可有效填充满, 返回 True 终止递归
        if k < 0:
            return True
        row, column = ls_empty[k]
        box_idx = (row // 3) * 3 + column // 3
        for char in '123456789':
            if not (char in ls_row[row] or char in ls_col[column] or char in ls_box[box_idx]):
                ls_row[row].add(char)
                ls_col[column].add(char)
                ls_box[box_idx].add(char)
                if self.dfs2(k-1, ls_empty, ls_row, ls_col, ls_box, board):
                    board[row][column] = char
                    # jy: 注意, 此处必须要有 return True, 否则该递归函
                    #     数应用在该部分的 if 判断时, 即使满足条件也是
                    #     返回 None, 使得后续不会填充满足条件的值
                    return True

                ls_row[row].remove(char)
                ls_col[column].remove(char)
                ls_box[box_idx].remove(char)
        return False


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
Solution().solveSudoku_v1(board)
pprint.pprint(board)

print("-" * 66)

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
Solution().solveSudoku_v2(board)
pprint.pprint(board)


