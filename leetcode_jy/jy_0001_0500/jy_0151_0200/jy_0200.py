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
title_jy = "Number-of-Islands(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a 2d grid map of '1's (land) and '0's  (water), count the number of islands. An
island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
"""


from typing import List
from collections import deque

class Solution:
    """
解法1: 遍历矩阵, 如果值为 1 则表示发现一个岛屿, 同时使用深度优先搜索将与其相连的上下左右四个方
向的 1 标记为已访问过;
    """
    def numIslands_v1(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        # jy: m 行 n 列的二维矩阵, 用于记录元素是否被访问, 均初始化为 False;
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        # jy: 遍历矩阵, 如果碰到 1, 则 count 加 1, 并将所有相邻的 1 都标记已访问; 不相邻的 1 则仍
        #    是未访问状态, 后续循环中也会被访问到, 并再次在 count 的基础上加 1;
        for i in range(m):
            for j in range(n):
                # jy: 如果矩阵所在元素为 1(即表示岛屿) 且暂未被访问过, 则 count 加 1;
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    # jy: 深度优先搜索将上下左右四个方向上相邻的 1 标记为已访问过;
                    self._dfs(grid, i, j, visited)

        return count

    def _dfs(self, grid, row, column, visited):
        m, n = len(grid), len(grid[0])
        # jy: 如果行或列超出范围, 或者 grid[row][column] 不为 1 或已经被访问过了, 则返回, 终止递归;
        if row < 0 or row >= m or column < 0 or column >= n or grid[row][column] != '1' or visited[row][column]:
            return
        # jy: 将当前 grid[row][column] 标记为已访问;
        visited[row][column] = True
        # jy: 将 grid[row][column] 上下左右四个方向上相邻的 1 标记为已访问过(如果四个方向上的值不
        #    为 1, 会终止递归); 以下四个 direction 分别表示 grid[row][column] 的 [上, 左, 下, 右]
        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            # jy: 如果得到的新 row 或 column 超出范围, 也会在新的一轮调用中终止递归;
            self._dfs(grid, row + direction[0], column + direction[1], visited)


    """
解法2: 同理还可使用广度优先搜索
    """
    def numIslands_v2(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        # jy: m 行 n 列的二维矩阵, 用于记录元素是否被访问, 均初始化为 False;
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        # jy: 遍历矩阵, 如果碰到 1, 则 count 加 1, 并将所有相邻的 1 都标记已访问; 不相邻的 1 则仍
        #    是未访问状态, 后续循环中也会被访问到, 并再次在 count 的基础上加 1;
        for i in range(m):
            for j in range(n):
                # jy: 如果对应的行列下标值为 1 且原先没有被访问过, 则 count 加 1, 并将其行列下标添加
                #    到队列中, 队列中的行列下标值表示该下标对应的是值为 1 且需要将该值的上下左右的 1
                #    标记为已访问过;
                #
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    visited[i][j] = True
                    queue = deque([(i, j)])
                    # jy: 如果队列不为空, 表示需要将队列中的下标的上下左右的 1 标记为已访问过; 直到队
                    #    列为空, 表明与原先的 grid[i][j] == '1' 相邻的 1 都已经被标记为已访问过状态;
                    while queue:
                        cell = queue.popleft()
                        row, column = cell[0], cell[1]

                        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                            next_row = row + direction[0]
                            next_column = column + direction[1]
                            # jy: 如果新的行列不满足要求, 或者对于的值不为 1 或已经被访问了, 则不跳过后续
                            #    逻辑, 不需要将该值加入队列中;
                            if next_row < 0 or next_row >= m or next_column < 0 or next_column >= n \
                                    or grid[next_row][next_column] != '1' or visited[next_row][next_column]:
                                continue
                            # jy: 如果执行到此处, 表明对应的相邻新行列值为 1, 且未被访问过, 则将其加入队列中,
                            #    并标记为已访问; 后续队列中会继续将该新行列值的上下左右相邻的 1 设置为已访问状态;
                            queue.append((next_row, next_column))
                            visited[next_row][next_column] = True

        return count

grid = [
"11110",
"11010",
"11000",
"00000",
]
# Output: 1
res = Solution().numIslands_v1(grid)
print(res)

grid = [
"11000",
"11000",
"00100",
"00011",
]
# Output: 3
res = Solution().numIslands_v2(grid)
print(res)


