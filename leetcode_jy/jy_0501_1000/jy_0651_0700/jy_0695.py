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
title_jy = "Max-Area-of-Island(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid
are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)


Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.


Note:The length of each dimension in the given grid does not exceed 50.
"""


from typing import List
from collections import deque


class Solution:
    """
解法1: 在 200_Number-of-Islands.py 的上稍加修改即可, 每次从一个 1 开始搜索时说明遇到了一个新岛屿, 初始化岛
屿面积为 1, 岛屿面积为对四周进行搜索的面积和;
    """
    def maxAreaOfIsland_v1(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = self._dfs(grid, i, j, visited)
                    max_area = max(area, max_area)

        return max_area

    def _dfs(self, grid, row, column, visited):
        m, n = len(grid), len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n or grid[row][column] != 1 or visited[row][column]:
            return 0

        area = 1
        visited[row][column] = True

        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            area += self._dfs(grid, row + direction[0], column + direction[1], visited)

        return area

    """
解法2: 广度优先搜索版本;
    """
    def maxAreaOfIsland_v2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # jy: 如果遇到当前位置为 1, 则先将 area 设置为 1 , 并将该位置坐标放入双
                #    向队列 queue 中, 双向队列会对该位置的四个方向进行查找, 并将四个方
                #    向上值为 1 的继续加入队列, 不断循环查找相邻的位置上的 1, 并加上相
                #    应的面积; 因此, 一次以下 if 条件成立结合内嵌的 while 循环就找出一
                #    个岛屿的总面积, 并将找到过的位置设置为已访问;
                if grid[i][j] == 1 and not visited[i][j]:
                    area = 1
                    visited[i][j] = True
                    queue = deque([(i, j)])

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
                    # jy: 每次 while 循环完成后, 即找到一个岛屿的总面积, 判断该岛屿是否比当前岛屿面积大, 是则
                    #    更新当前的最大岛屿;
                    max_area = max(area, max_area)

        return max_area

grid = \
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# return 6
res = Solution().maxAreaOfIsland_v1(grid)
print(res)


grid = [[0,0,0,0,0,0,0,0]]
# return 0.
res = Solution().maxAreaOfIsland_v2(grid)
print(res)


