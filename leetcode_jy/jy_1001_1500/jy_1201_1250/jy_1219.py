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
title_jy = "Path-with-Maximum-Gold(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
Return the maximum amount of gold you can collect under the conditions:
Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.

Example 1:
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:
Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""

from typing import List


class Solution:
    def __init__(self):
        self.max_gold = 0
    """
解法1
遍历 grid, 以每个不为0的位置为其他开始向四个方向递归搜索, 每次向一个方向搜索完成后需要回溯;
    """
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                self._dfs(grid, i, j, set(), grid[i][j])

        return self.max_gold

    def _dfs(self, grid, row, column, visited, gold_so_far):
        m, n = len(grid), len(grid[0])

        visited.add((row, column))

        self.max_gold = max(self.max_gold, gold_so_far)

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_row = row + direction[0]
            next_column = column + direction[1]

            if next_row < 0 or next_row == m \
                    or next_column < 0 or next_column == n \
                    or grid[next_row][next_column] == 0 \
                    or (next_row, next_column) in visited:
                continue

            self._dfs(grid, next_row, next_column, visited,
                      gold_so_far + grid[next_row][next_column])

            visited.remove((next_row, next_column))

from typing import List


class Solution:
    """
解法2
在解法1的基础上去掉全局变量依赖, 这里为什么在计算 max_gold 时不使用 max(max_gold, current_gold + grid[row][column]), 然后最后直接返回 max_gold? 因为对于给定的 (row, column) 来说, 它的上下左右四个方向不一定能访问到, 所以最后直接返回 max_gold 时会漏掉算上 grid[row][column];
    """
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        max_gold = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                max_gold = max(max_gold, self._dfs(grid, i, j, set()))

        return max_gold

    def _dfs(self, grid, row, column, visited):
        max_gold = 0
        m, n = len(grid), len(grid[0])

        visited.add((row, column))

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_row = row + direction[0]
            next_column = column + direction[1]

            if next_row < 0 or next_row == m \
                    or next_column < 0 or next_column == n \
                    or grid[next_row][next_column] == 0 \
                    or (next_row, next_column) in visited:
                continue

            current_gold = self._dfs(grid, next_row, next_column, visited)
            max_gold = max(max_gold, current_gold)

            visited.remove((next_row, next_column))

        return max_gold + grid[row][column]



