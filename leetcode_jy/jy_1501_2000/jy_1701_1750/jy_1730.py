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
title_jy = "Shortest-Path-to-Get-Food(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are starving and you want to eat food as quickly as possible. You want to find
the shortest path to arrive at any food cell.  You are given an ``m x n`` character
matrix ``grid`` of these different types of cells:
1) '*' is your location. There is exactly one '*' cell.
2) '#' is a food cell. There may be multiple food cells.
3) 'O' is free space, and you can travel through these cells.
4) 'X' is an obstacle, and you cannot travel through these cells.

You can travel to any adjacent cell north, east, south, or west of your current location
if there is not an obstacle. Return the length of the shortest path for you to reach any
food cell. If there is no path for you to reach food, return -1.


Example 1:
grid = [
["X","X","X","X","X","X"],
["X","*","O","O","O","X"],
["X","O","O","#","O","X"],
["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.

Example 2:
grid = [
["X","X","X","X","X"],
["X","*","X","O","X"],
["X","O","X","#","X"],
["X","X","X","X","X"]]
Output: -1
Explanation: It is not possible to reach the food.

Example 3:
grid =[
["X","X","X","X","X","X","X","X"],
["X","*","O","X","O","#","O","X"],
["X","O","O","X","O","O","X","X"],
["X","O","O","O","O","#","O","X"],
["X","X","X","X","X","X","X","X"]]
Output: 6
Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.

Example 4:
grid = [
["O","*"],
["#","O"]]
Output: 2

Example 5:
grid = [
["X","*"],
["#","X"]]
Output: -1


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[row][col] is '*', 'X', 'O', or '#'.
The grid contains exactly one '*'.
"""


from collections import deque
from typing import List


class Solution:
    """
广度优先搜索, 遇到第一个 # 就是最短路径;
    """
    def getFood(self, grid: List[List[str]]) -> int:
        if not grid:
            return -1

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        # jy: 找出起始位置坐标, 将起始位置坐标的距离设置为 0, 返回一个元组: (start_i, start_j, 0)
        queue = deque([self._find_start_point(grid, m, n)])
        # print(queue)

        while queue:
            row, column, distance = queue.popleft()
            visited[row][column] = True
            # jy: 如果当前位置的值为 '#', 表明找到目标位置, 直接返回对应的距离 distance;
            if grid[row][column] == '#':
                return distance
            # jy: 左上右下四个方向进行遍历;
            for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                next_row = row + direction[0]
                next_column = column + direction[1]
                # jy: 如果坐标位置不在正常范围内, 或者对应位置为障碍物, 或者已访问过, 则跳过该位置;
                if next_row < 0 or next_row >= m or next_column < 0 or next_column >= n \
                        or grid[next_row][next_column] == 'X' or visited[next_row][next_column]:
                    continue

                queue.append((next_row, next_column, distance + 1))
                visited[next_row][next_column] = True

        return -1

    def _find_start_point(self, grid, m, n):
        """逐行遍历, 找出起始位置坐标, 将起始位置坐标的距离设置为 0"""
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    return i, j, 0


grid = [
["X","X","X","X","X","X"],
["X","*","O","O","O","X"],
["X","O","O","#","O","X"],
["X","X","X","X","X","X"]]
# Output: 3
res = Solution().getFood(grid)
print(res)


grid = [
["X","X","X","X","X"],
["X","*","X","O","X"],
["X","O","X","#","X"],
["X","X","X","X","X"]]
# Output: -1
res = Solution().getFood(grid)
print(res)


grid =[
["X","X","X","X","X","X","X","X"],
["X","*","O","X","O","#","O","X"],
["X","O","O","X","O","O","X","X"],
["X","O","O","O","O","#","O","X"],
["X","X","X","X","X","X","X","X"]]
# Output: 6
res = Solution().getFood(grid)
print(res)


grid = [
["O","*"],
["#","O"]]
# Output: 2
res = Solution().getFood(grid)
print(res)


grid = [
["X","*"],
["#","X"]]
# Output: -1
res = Solution().getFood(grid)
print(res)


