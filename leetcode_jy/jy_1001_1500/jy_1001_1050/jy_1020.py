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
title_jy = "Number-of-Enclaves(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an m x n binary matrix ``grid``, where 0 represents a sea cell and 1
represents a land cell. A move consists of walking from one land cell to another
adjacent (4-directionally) land cell or walking off the boundary of the grid.

Returnthe number of land cells in grid for which we cannot walk off the boundary of
the grid in any number of moves.



Example 1:   https://www.yuque.com/frederick/dtwi9g/ewmwm0
nput: grid = [
[0,0,0,0],
[1,0,1,0],
[0,1,1,0],
[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:
Input: grid = [
[0,1,1,0],
[0,0,1,0],
[0,0,1,0],
[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.



Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""


from typing import List
from collections import deque


class Solution:
    """
解法1: 在 695_Max-Area-of-Island.py 的基础上, 计算岛屿的面积时, 判断当前的岛屿是否和边界相连;
    """
    def numEnclaves_v1(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        enclaves = 0
        # jy: m 行 n 列;
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        # jy: 遍历二维矩阵;
        for i in range(m):
            for j in range(n):
                # jy: 如果当前位置下标为 land, 且没被访问过, 则计算与其相连接的陆地面积, 并返
                #    回陆地是否包含边界, 如果不包含, 则 enclaves 加上陆地块面积;
                if grid[i][j] == 1 and not visited[i][j]:
                    area, has_boundary = self._dfs(grid, i, j, visited)

                    if not has_boundary:
                        enclaves += area

        return enclaves

    def _dfs(self, grid, row, column, visited):
        # jy: m 行 n 列;
        m, n = len(grid), len(grid[0])
        # jy: 如果行或列对应的下标无效, 或对应位置已被访问过或者不为 land, 则直接返回 (0, False)
        if row < 0 or row >= m or column < 0 or column >= n or grid[row][column] != 1 or visited[row][column]:
            # print("==== ", row < 0 or row >= m or column < 0 or column >= n)
            # return 0, row < 0 or row >= m or column < 0 or column >= n
            return 0, False

        area = 1
        visited[row][column] = True
        has_boundary = self._is_boundary(m, n, row, column)
        # jy: 遍历数组的左上右下四个方向;
        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            neighbour_area, neighbour_has_boundary = self._dfs(grid, row + direction[0], column + direction[1], visited)
            area += neighbour_area
            has_boundary = has_boundary or neighbour_has_boundary

        return area, has_boundary


    def _is_boundary(self, m, n, row, column):
        """判断对应位置是否是二维数组的边界"""
        return row == 0 or row == m-1 or column == 0 or column == n-1


    """
解法2: 广度优先搜索版本;
    """
    def numEnclaves_v2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        enclaves = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = 1
                    visited[i][j] = True
                    queue = deque([(i, j)])
                    has_boundary = self._is_boundary(m, n, i, j)

                    while queue:
                        cell = queue.popleft()
                        row, column = cell[0], cell[1]

                        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                            next_row = row + direction[0]
                            next_column = column + direction[1]

                            if next_row < 0 or next_row >= m or next_column < 0 or next_column >= n \
                                    or grid[next_row][next_column] != 1 or visited[next_row][next_column]:
                                continue

                            area += 1
                            queue.append((next_row, next_column))
                            visited[next_row][next_column] = True
                            has_boundary = has_boundary or self._is_boundary(m, n, next_row, next_column)

                    if not has_boundary:
                        enclaves += area

        return enclaves



grid = [
[0,0,0,0],
[1,0,1,0],
[0,1,1,0],
[0,0,0,0]]
# Output: 3
res = Solution().numEnclaves_v1(grid)
print(res)


grid = [
[0,1,1,0],
[0,0,1,0],
[0,0,1,0],
[0,0,0,0]]
# Output: 0
res = Solution().numEnclaves_v1(grid)
print(res)


