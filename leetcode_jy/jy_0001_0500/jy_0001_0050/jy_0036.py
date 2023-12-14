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
tag_jy = "九宫格序号计算技巧"


"""
Determine if a `9 x 9` Sudoku board is valid. Only the filled
cells need to be validated according to the following rules:
1) Each row must contain the digits 1-9 without repetition.
2) Each column must contain the digits 1-9 without repetition.
3) Each of the 9 `3 x 3` sub-boxes of the grid must contain the
   digits 1-9 without repetition.
The Sudoku board could be partially filled, where empty cells are
filled with the character '.'


Example 1: 
示例图参考: https://www.yuque.com/it-coach/leetcode/qndu3k
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
Explanation: Same as Example 1, except with the 5 in the top left corner
             being modified to 8. Since there are two 8's in the top left
             `3 x 3` sub-box, it is invalid.

Note:
1) A Sudoku board (partially filled) could be valid but is not necessarily solvable.
2) Only the filled cells need to be validated according to the mentioned rules.


Constraints:
1) board.length == 9
2) board[i].length == 9
3) board[i][j] is a digit 1-9 or '.'
"""


class Solution:
    """
解法 1: 暴力求解, 直接判断每行、每列、每个九宫格即可
    """
    def isValidSudoku_v1(self, board: List[List[str]]) -> bool:
        # jy: 验证每一列是否有效
        for i in range(9):
            column = [row[i] for row in board]
            if not self._is_valid(column):
                return False

        # jy: 验证每一行是否有效
        for row in board:
            if not self._is_valid(row):
                return False

        # jy: 验证每个 3x3 sub-boxes 是否均有效
        #     [0, 3, 6]
        for row in range(0, 9, 3):      
            # jy: [0, 3, 6]
            for column in range(0, 9, 3):
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
解法 2: 解法 1 的更通俗易懂的写法
    """
    def isValidSudoku_v2(self, board: List[List[str]]) -> bool:
        # jy: 判断每一行
        for i in range(9):
            storage = []
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in storage:
                    return False
                else:
                    storage.append(board[i][j])

        # jy: 判断每一列
        for i in range(9): 
            storage = []
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in storage:
                    return False
                else:
                    storage.append(board[j][i])

        # jy: 判断每一个九宫格
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                storage = []
                for x in range(0, 3):
                    for y in range(0, 3):
                        if board[i + x][j + y] == '.':
                            continue
                        if board[i + x][j + y] in storage:
                            return False
                        else:
                            storage.append(board[i + x][j + y])
        return True


    """
解法 3: 一趟循环即可 (空间换时间)

判断元素是否存在可以使用 Map 或 Set 来事先保存遍历过的数字; 因此可以为所有
的行、列、九宫格创建一个 Map, 遍历数字时判断对应的行、列、九宫格里是否已经
有同样的数字

9 * 9 的二维数组可切分为 9 个九宫格, 可从左到右、从上到下给九宫格编号, 则九
宫格的序号可通过 (row, column) 确定: 
(row, column) 对应的九宫格的序号是 (row // 3) * 3 + column // 3
    """
    def isValidSudoku_v3(self, board: List[List[str]]) -> bool:
        # jy: 定义一个列表, 列表中的 9 个字典对应 9 行, 每个字典用于存放对
        #     应行的数字以及其出现的次数
        rows = [{} for _ in range(9)]
        # jy: 定义一个列表, 列表中的 9 个字典对应 9 列, 每个字典用于存放对
        #     应列的数字以及其出现的次数
        columns = [{} for _ in range(9)]
        # jy: 定义一个列表, 列表中的 9 个字典对应 3 x 3 sub-boxes, 每个字
        #     典用于存放对应 sub-boxes 中的数字以及其出现的次数
        boxes = [{} for _ in range(9)]
        # jy: 遍历二维矩阵中的每行每列对应的数值, 将数值记录到对于的 Map 中
        #     并判断是否出现重复, 如有重复直接返回 False
        for row in range(9):
            for column in range(9):
                number = board[row][column]
                if number == '.':
                    continue

                box_index = (row // 3) * 3 + column // 3
                rows[row][number] = rows[row].get(number, 0) + 1
                columns[column][number] = columns[column].get(number, 0) + 1
                boxes[box_index][number] = boxes[box_index].get(number, 0) + 1
                if rows[row][number] > 1 or columns[column][number] > 1 or \
                   boxes[box_index][number] > 1:
                    return False
        return True


    """
解法 4: 解法 3 的更高效的改写
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        nine = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item == ".":
                #if not item.isdigit():
                    continue

                
                if item in row[i]:
                    return False

                if item in col[j]:
                    return False

                nine_idx = (j // 3) * 3 + (i // 3)
                if item in nine[nine_idx]:
                    return False

                row[i].add(item)
                col[j].add(item)
                nine[nine_idx].add(item)
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


