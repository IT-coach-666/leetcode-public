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
title_jy = "N-Queens-II(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 相似题: 0051 | IMP"


"""
The n-queens puzzle is the problem of placing `n` queens on an n×n chessboard
such that no two queens attack each other. Given an integer `n`, return the 
number of distinct solutions to the n-queens puzzle.


Example 1:
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

Example 2:
Input: n = 1
Output: 1
 

Constraints:
1 <= n <= 9
"""


class Solution:
    """
解法 1: 递归 

和 0051 (N-Queens) 一样, 只是在原来返回具体组合的地方返回一个计数
    """
    def totalNQueens_v1(self, n: int) -> int:
        return self._dfs(0, n, set(), set(), set())

    def _dfs(self, row: int, n, columns: Set[int], left_diagonals: Set[int],
             right_diagonals: Set[int]) -> int:
        """
        row: 当前递归过程中尝试在下标为 row 的行的每一列放置 "Q" 
        n: 矩阵维度, 递归过程中该值不变
        columns: 记录递归过程中不能再放置 "Q" 的列
        left_diagonals: 记录递归过程中不能再放置 "Q" 的左下至右上的斜对角线
        right_diagonals: 记录递归过程中不能再放置 "Q" 的左上至右下的斜对角线


        与 0051 相比, 少了两个参数, 因为该题不需存放具体的方案, 只需计算方案
        的个数即可
        """
        if row == n:
            return 1

        # jy: 统计方案数
        count = 0
        for column in range(n):
            if column in columns or row + column in left_diagonals \
                    or row - column in right_diagonals:
                continue

            # jy: 尝试在当前 row 行的 column 列放置 "Q", 并将后续不能放置 "Q"
            #     的列和对角线记录到集合中 
            columns.add(column)
            left_diagonals.add(row + column)
            right_diagonals.add(row - column)
            # jy: 尝试在下一行中的每一列放置 "Q", 并记录不能放置的列和对角线,
            #     不断深度优先递归
            count += self._dfs(row + 1, n, columns, left_diagonals,
                               right_diagonals)
            # jy: 回溯, 确保尝试当前行放置 "Q" 后, 转换到其它行的尝试时不受当
            #     前行放置的影响
            columns.remove(column)
            left_diagonals.remove(row + column)
            right_diagonals.remove(row - column)
        return count


n = 4
res = Solution().totalNQueens_v1(n)
print(res)


n = 6
res = Solution().totalNQueens_v1(n)
print(res)


n = 9
res = Solution().totalNQueens_v1(n)
print(res)

