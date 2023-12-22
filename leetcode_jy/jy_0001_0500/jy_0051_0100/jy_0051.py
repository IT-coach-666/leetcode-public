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
from typing import List, Dict, Set
# jy: 记录该题的难度系数
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "N-Queens(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


# https://www.yuque.com/frederick/dtwi9g/rc5a65
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],
 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""


class Solution:
    """
核心解法就是一个个去试, 但是尝试的过程中可以过滤掉一些无需考虑的组合;
首先从第一行开始, 对于第一行的每一列, 假设该列放了棋子, 则采用深度优先
搜索递归判断后续行的棋子应该放在哪里;

对于某个放了棋子的位置 (row, column) 来说, 有四个方向是不能再放置棋子的:
同一行, 同一列, 左斜对角线和右斜对角线;

同一行不用判断, 因为每次深度优先搜索都是往下一层
同一列很好判断, 只要看 column 是否相等即可;
同对角线的判断很巧妙, 利用了一个隐藏的性质: 对于 (a, b) 和 (c, d) 两个点来说
  1) 如果是同一左斜对角线, 则有 a + b = c + d
  2) 如果是同一右斜对角线, 则有 a - b = c - d

所以, 可以使用 Set 来保存分别不能放置的行, 左斜对角线, 右斜对角线;
当递归的深度达到了 n, 就说明我们找到了一组解;
    """
    def solveNQueens_v1(self, n: int) -> List[List[str]]:
        result = []
        self._dfs(0, n, set(), set(), set(), [], result)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in solution]
                for solution in result]

    def _dfs(self, row: int, n, columns: Set[int], left_diagonals: Set[int],
             right_diagonals: Set[int], solution: List[int],
             result: List[List[int]]) -> None:
        if row == n:
            result.append(solution)
            return
        for column in range(n):
            if column in columns or row + column in left_diagonals \
                    or row - column in right_diagonals:
                continue
            columns.add(column)
            left_diagonals.add(row + column)
            right_diagonals.add(row - column)
            self._dfs(row + 1, n, columns, left_diagonals,
                      right_diagonals, solution + [column], result)
            columns.remove(column)
            left_diagonals.remove(row + column)
            right_diagonals.remove(row - column)


n = 4
res = Solution().solveNQueens_v1(n)
print(res)


