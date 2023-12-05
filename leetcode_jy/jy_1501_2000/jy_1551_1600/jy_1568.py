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
title_jy = "Minimum-Number-of-Days-to-Disconnect-Island(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a 2D grid consisting of 1 s (land) and 0 s (water).  An island is a maximal
4-directionally (horizontal or vertical) connected group of 1 s. The grid is said
to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).
Returnthe minimum number of days to disconnect the grid.



Example 1:  https://www.yuque.com/frederick/dtwi9g/vsvsn6
Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
             Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.

Example 2:
Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.

Example 3:
Input: grid = [[1,0,1,0]]
Output: 0

Example 4:
Input: grid = [
[1,1,0,1,1],
[1,1,1,1,1],
[1,1,0,1,1],
[1,1,0,1,1]]
Output: 1

Example 5:
Input: grid = [
[1,1,0,1,1],
[1,1,1,1,1],
[1,1,0,1,1],
[1,1,1,1,1]]
Output: 2



Constraints:
1 <= grid.length, grid[i].length <= 30
grid[i][j] is 0 or 1.
"""


from typing import List


class Solution:
    """
这里有个技巧, 即一个岛屿最多将两个 1 变为 0 就能拆成两个岛屿, 方法是从岛屿的边角入手,
如下图所示, 一个岛屿的边角最多有两个相邻的 1, 将红色方块变为 0, 就能拆分一个岛屿;
'
借助 200_Number-of-Islands.py, 首先计算岛屿的数量:
1) 如果不为 1, 直接返回 0;
2) 如果为 1, 则遍历岛屿, 如果遇到 1, 先将其置为 0, 然后判断岛屿数量是否不为 1:
   a) 如果不为 1, 则直接返回 1;
   b) 如果仍为 1, 则返回 2 (最多需要将两个 1 改为 0 就能实现拆分)
    """
    def minDays(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # jy: 如果二维数组中的岛屿数多于 1 个, 表示已是分割状态;
        if self._number_of_islands(grid) != 1:
            return 0

        # jy: 以上 if 判断如果没有返回值, 则表明岛屿的个数为 1; 遍历二维数组, 将其原先
        #    为 1 的位置先置为 0, 再次判断岛屿的个数, 如果不为 1, 则表明将一个 1 变为
        #    0 即可拆分岛屿, 即返回 1 即可;
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if self._number_of_islands(grid) != 1:
                        return 1
                    # jy: 将原先置为 0 的结果再次置为 1, 避免干扰后续的结果(回溯);
                    grid[i][j] = 1

        return 2

    def _number_of_islands(self, grid: List[List[int]]) -> int:
        """
        计算二维数组中岛屿的数量
        """
        count = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1
                    # jy: 在二维数组中递归找出当前与当前位置 1 相邻的所有 1, 并设置为已访问状态;
                    self._dfs(grid, i, j, visited)

        return count

    def _dfs(self, grid, row, column, visited):
        m, n = len(grid), len(grid[0])
        # jy: 如果行列下标超出规定范围, 或当前位置值不为 1, 或已访问过, 则返回, 终止递归;
        if row < 0 or row >= m or column < 0 or column >= n or grid[row][column] != 1 or visited[row][column]:
            return

        visited[row][column] = True
        # jy: 递归遍历当前位置的相邻四个方向, 将为 1 的值设置为已访问状态;
        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            self._dfs(grid, row + direction[0], column + direction[1], visited)


grid = [
[0,1,1,0],
[0,1,1,0],
[0,0,0,0]]
# Output: 2
res = Solution().minDays(grid)
print(res)


grid = [[1,1]]
# Output: 2
res = Solution().minDays(grid)
print(res)


grid = [[1,0,1,0]]
# Output: 0
res = Solution().minDays(grid)
print(res)


grid = [
[1,1,0,1,1],
[1,1,1,1,1],
[1,1,0,1,1],
[1,1,0,1,1]]
# Output: 1
res = Solution().minDays(grid)
print(res)


grid = [
[1,1,0,1,1],
[1,1,1,1,1],
[1,1,0,1,1],
[1,1,1,1,1]]
# Output: 2
res = Solution().minDays(grid)
print(res)


