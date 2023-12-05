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
title_jy = "N-Queens-II(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
The n-queens puzzle is the problem of placing n queens on an n×n
chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],
 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


from typing import List, Set

class Solution:
    """
和 051_N-Queens.py 一样, 在原来返回具体组合的地方返回一个计数;
    """
    def totalNQueens(self, n: int) -> int:
        return self._dfs(0, n, set(), set(), set())

    def _dfs(self, row: int, n, columns: Set[int], left_diagonals: Set[int],
             right_diagonals: Set[int]) -> int:
        if row == n:
            return 1
        count = 0
        for column in range(n):
            if column in columns or row + column in left_diagonals \
                    or row - column in right_diagonals:
                continue
            columns.add(column)
            left_diagonals.add(row + column)
            right_diagonals.add(row - column)
            count += self._dfs(row + 1, n, columns, left_diagonals,
                               right_diagonals)
            columns.remove(column)
            left_diagonals.remove(row + column)
            right_diagonals.remove(row - column)
        return count


n = 4
res = Solution().totalNQueens(n)
print(res)



