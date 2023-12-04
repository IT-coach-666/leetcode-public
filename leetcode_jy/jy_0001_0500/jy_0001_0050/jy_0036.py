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
title_jy = "valid-Sudoku(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to
be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

图标示例: https://www.yuque.com/frederick/dtwi9g/ifdr8c

Example 1:
Input:
[['5', '3', '.', '.', '7', '.', '.', '.', '.'],
 ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
 ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
 ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
 ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
 ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
 ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
 ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
 ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
Output: true

Example 2:
Input:
[['8', '3', '.', '.', '7', '.', '.', '.', '.'],
 ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
 ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
 ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
 ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
 ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
 ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
 ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
 ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
• A Sudoku board (partially filled) could be valid but is not necessarily solvable.
• Only the filled cells need to be validated according to the mentioned rules.
• The given board contain only digits 1-9 and the character '.'.
• The given board size is always 9x9.
"""


from typing import List
class Solution:
    """
解法1: 直接按每行, 每列, 每个九宫格判断即可;
    """
    def isValidSudoku_v1(self, board: List[List[str]]) -> bool:
        # jy: 验证每一列是否有效;
        for i in range(9):
            column = [row[i] for row in board]
            if not self._is_valid(column):
                return False
        # jy: 验证每一行是否有效;
        for i, row in enumerate(board):
            if not self._is_valid(row):
                return False
        # jy: 验证每个 3x3 sub-boxes 是否均有效;
        for row in range(0, 9, 3):         # [0, 3, 6]
            for column in range(0, 9, 3):  # [0, 3, 6]
                boxes = board[row][column:column + 3] + \
                        board[row + 1][column:column + 3] + \
                        board[row + 2][column:column + 3]
                if not self._is_valid(boxes):
                    return False
        return True

    def _is_valid(self, numbers: List[str]) -> bool:
        visited = set()
        for n in numbers:
            if n == '.':
                continue
            if n in visited:
                return False
            else:
                visited.add(n)
        return True


    """
解法2: 还可以一趟循环搞定, 判断元素是否存在可以使用 Map 或者 Set 来事先保存遍历过的
数字, 所以可以为所有的行, 列, 九宫格创建一个 Map, 遍历数字时判断对应的行, 列, 九宫格
里是否已经有同样的数字即可; 这里巧妙的地方在于判断九宫格的序号, 对于 (row, column) 数
字来说, 它对应的九宫格的序号是 (row // 3)*3 + column // 3;
    """
    def isValidSudoku_v2(self, board: List[List[str]]) -> bool:
        # jy: 定义一个列表, 列表中为 9 个字典(对应 9 行), 每个字典用于存放对应行的数字
        #    以及其出现的次数;
        rows = [{} for _ in range(9)]
        # jy: 定义一个列表, 列表中为 9 个字典(对应 9 列), 每个字典用于存放对应列的数字
        #    以及其出现的次数;
        columns = [{} for _ in range(9)]
        # jy: 定义一个列表, 列表中为 9 个字典(对应 3x3 sub-boxes), 每个字典用于存放对应
        #    sub-boxes 中的数字以及其出现的次数;
        boxes = [{} for _ in range(9)]
        for row in range(9):
            for column in range(9):
                number = board[row][column]
                if number == '.':
                    continue

                box_index = (row // 3)*3 + column // 3
                rows[row][number] = rows[row].get(number, 0) + 1
                columns[column][number] = columns[column].get(number, 0) + 1
                boxes[box_index][number] = boxes[box_index].get(number, 0) + 1
                if rows[row][number] > 1 or columns[column][number] > 1 or boxes[box_index][number] > 1:
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
res = Solution().isValidSudoku_v1(board)
print(res)

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
res = Solution().isValidSudoku_v2(board)
print(res)


