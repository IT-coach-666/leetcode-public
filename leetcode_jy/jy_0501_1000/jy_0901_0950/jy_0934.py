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
title_jy = "Shortest-Bridge(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)
Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Constraints:
2 <= grid.length == grid[0].length <= 100
grid[i][j] == 0 or grid[i][j] == 1
"""


from typing import List


class Solution:
    """
首先将其中一座小岛标记为2, 然后每次扩充小岛的周边, 标记数字依次递增, 每次扩充小岛周边时判断是否存在和1相邻的格子, 如果存在, 说明连接到了另一座小岛;
    """
    def shortestBridge(self, grid: List[List[int]]) -> int:
        found = False
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                found = self._paint(grid, i, j) > 0

                if found:
                    break

            if found:
                break

        color = 2

        while True:
            for i in range(m):
                for j in range(n):
                    if grid[i][j] != color:
                        continue

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if self._expand(grid, i + dy, j + dx, color):
                            return color - 2

            color += 1

    def _paint(self, grid, i, j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) \
                or grid[i][j] != 1:
            return 0

        grid[i][j] = 2

        return 1 + self._paint(grid, i + 1, j) + self._paint(grid, i - 1, j) \
            + self._paint(grid, i, j + 1) + self._paint(grid, i, j - 1)

    def _expand(self, grid, i, j, color):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
            return False

        if grid[i][j] == 0:
            grid[i][j] = color + 1

        return grid[i][j] == 1


