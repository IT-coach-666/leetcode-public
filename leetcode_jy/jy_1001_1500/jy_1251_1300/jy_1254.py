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
title_jy = "Number-of-Closed-Islands(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal
4-directionally connected group of 0s and a closed island is an island totally
(all left, top, right, bottom) surrounded by 1s. Return the number of closed islands.


Example 1:    https://www.yuque.com/frederick/dtwi9g/pg4vsl
Input: grid = [
[1,1,1,1,1,1,1,0],
[1,0,0,0,0,1,1,0],
[1,0,1,0,1,1,1,0],
[1,0,0,0,0,1,0,1],
[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [
[0,0,1,0,0],
[0,1,0,1,0],
[0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [
[1,1,1,1,1,1,1],
[1,0,0,0,0,0,1],
[1,0,1,1,1,0,1],
[1,0,1,0,1,0,1],
[1,0,1,1,1,0,1],
[1,0,0,0,0,0,1],
[1,1,1,1,1,1,1]]
Output: 2


Constraints:
1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""


from typing import List
from collections import deque


class Solution:
    """
解法1: 和 200_Number-of-Islands.py 类似, 不同的是本题是以 0 为中心进行搜索, 遇到 0 时,
对四个方向进行搜索, 只有当四个方向都返回 1 时, 表示当前的 0 被 1 包围, 注意这里有个技
巧是如果当前是合法的 0 (即不是在边线上的 0), 则将当前置为 1, 这是为了方便处理下一个挨
着的 0;
    """
    def closedIsland_v1(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # jy: m 行 n 列;
        m = len(grid)
        n = len(grid[0])
        # jy: 统计目标结果的个数;
        count = 0
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                # jy: 如果当前位置对应的数值是 0 (代表陆地), 且没被访问过, 同时通过深度优先搜索
                #    判断该位置被 1 包围, 则 count 数加 1;
                if grid[i][j] == 0 and not visited[i][j] and self._dfs(i, j, grid, visited):
                    count += 1

        return count


    def _dfs(self, row, column, grid, visited):
        # jy: m 行 n 列;
        m = len(grid)
        n = len(grid[0])
        # jy: 如果传入的坐标位置无效, 则直接返回 False 终止递归;
        if row < 0 or row >= m or column < 0 or column >= n:
            return False
        # jy: 如果当前坐标位置值为 1 (表示水域), 或者已经被访问过(即被访问过的陆地 0), 则直接返回 1;
        if grid[row][column] == 1 or visited[row][column]:
            return 1

        # jy: 先初始化默认被水包围;
        closed = True
        visited[row][column] = True
        # jy: 从上下左右四个方向深度递归判断(判断当前 0 是否被 1 包围, 只需递归判断其上下左右四个方
        #    向对应的数值是否为 1, 或者不为 1 但也被 1 包围);
        for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            closed &= self._dfs(row + direction[0], column + direction[1], grid, visited)

        return closed


    """
解法2: 广度优先搜索版本: 解法 1 中的递归过程换成了入队遍历过程
    """
    def closedIsland_v2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                # jy: 如果当前位置对应的数值是 0 (代表陆地), 且没被访问过, 则先设置为已访问,
                #    并入队, 初始化默认被水包围;  一轮 if + while 循环即对应解法 1 中的一次
                #    深度优先搜索过程;
                if grid[i][j] == 0 and not visited[i][j]:
                    visited[i][j] = True
                    queue = deque([(i, j)])
                    closed = True

                    while queue:
                        cell = queue.popleft()
                        row, column = cell[0], cell[1]

                        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                            next_row = row + direction[0]
                            next_column = column + direction[1]
                            # jy: 如果对应的坐标位置已经超出正常下标范围, 则表示 closed 为 False (即上
                            #    一个遍历的坐标位置已经是在边界上, 边界上的值不可能被包围)
                            if next_row < 0 or next_row >= m or next_column < 0 or next_column >= n:
                                closed = False
                                # jy: 注意此处不能是 break, 否则会有个别测试用例不通过; 因为当前方向对应
                                #    的坐标位置不符合要求时, 仍要对其它方向进行遍历判断并设置已访问, 否
                                #    则影响后续的判断结果【待深入思考原因】;
                                continue

                            if visited[next_row][next_column] or grid[next_row][next_column] == 1:
                                continue

                            queue.append((next_row, next_column))
                            visited[next_row][next_column] = True

                    if closed:
                        count += 1

        return count


grid = [
[1,1,1,1,1,1,1,0],
[1,0,0,0,0,1,1,0],
[1,0,1,0,1,1,1,0],
[1,0,0,0,0,1,0,1],
[1,1,1,1,1,1,1,0]]
# Output: 2
res = Solution().closedIsland_v1(grid)
print(res)


grid = [
[0,0,1,0,0],
[0,1,0,1,0],
[0,1,1,1,0]]
# Output: 1
res = Solution().closedIsland_v2(grid)
print(res)


grid = [
[1,1,1,1,1,1,1],
[1,0,0,0,0,0,1],
[1,0,1,1,1,0,1],
[1,0,1,0,1,0,1],
[1,0,1,1,1,0,1],
[1,0,0,0,0,0,1],
[1,1,1,1,1,1,1]]
# Output: 2
res = Solution().closedIsland_v1(grid)
print(res)


