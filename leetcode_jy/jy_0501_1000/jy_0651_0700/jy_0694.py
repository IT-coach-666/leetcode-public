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
title_jy = "Number-of-Distinct-Islands(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid
are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and
only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.

Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.
Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.


Note: The length of each dimension in the given grid does not exceed 50.
"""


from typing import List
from collections import deque


class Solution:
    """
解法1: 在 200_Number-of-Islands.py 的基础上, 在寻找岛屿的过程中增加记录岛屿的路径, 分别
用 u, l, d, r, c 表示上, 左, 下, 右和当前元素, 最后返回所有不同路径的个数;
    """
    def numDistinctIslands_v1(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # jy: m 行 n 列;
        m, n = len(grid), len(grid[0])
        # jy: 记录哪些位置已经被访问过
        visited = [[False for _ in range(n)] for _ in range(m)]
        paths = set()
        # jy: 遍历矩阵;
        for i in range(m):
            for j in range(n):
                # jy: 如果矩阵对应的位置为 1 , 且没有被访问过, 则从该位置开始深度遍历, 并记
                #    录岛屿的路径; 由于以上遍历元素的时候, 总是会先遍历岛屿的所在行数最小,
                #    且最小行中列最小的值, 如果两个岛屿形状相同, 则相同形状的岛屿的该位置
                #    的行或列的坐标差即为对应其它位置的行或列的坐标差(JY: 因此, 可以将按相
                #    同遍历逻辑, 将同一个岛屿的坐标加入到一个列表中, 后续再判断列表中坐标
                #    个数相同的岛屿是否属于同一形状的岛屿, 如果是则数量减 1);
                if grid[i][j] == 1 and not visited[i][j]:
                    paths.add(self._dfs(grid, i, j, visited))

        return len(paths)

    def _dfs(self, grid, row, column, visited):
        # jy: m 行 n 列;
        m, n = len(grid), len(grid[0])
        # jy: 如果行或列对应的下标超出范围, 或者该行列组成的下标的值不为 1 或已经被访问过
        #    则直接返回空字符(注意, 该条件只有在递归过程中满足, 首次调用时不会满足, 即不
        #    会往以上 paths 集合中添加空字符串)
        if row < 0 or row >= m or column < 0 or column >= n or grid[row][column] != 1 or visited[row][column]:
            return ''
        # jy: 将该位置的值设置为已访问;
        visited[row][column] = True
        # jy: 二维数组中该位置的值由 1 替换为 0;
        #【JY】: 该操作非必须? 去除算法仍然正确? 待验证
        grid[row][column] = 0
        full_path = ''
        # jy: 四个字符, 分别代表 [上, 左, 下, 右], 以下 for 循环中遍历的四个值也即对应这四个方向上
        #    需要做的操作(当前坐标加上相应值即为当前位置的值的四个方向对应的坐标);
        directions = ['u', 'l', 'd', 'r']
        # jy: 循环遍历当前位置的上左下右四个方向, 得到这四个方向上的相应 path, 在此基础上加上该遍历位置
        #    相对原先位置的方位字符串, 最终得到 full_path;
        for i, direction in enumerate([[-1, 0], [0, -1], [1, 0], [0, 1]]):
            path = self._dfs(grid, row + direction[0], column + direction[1], visited)
            full_path += path + directions[i]
        # jy: 返回四个方向上的元素得到的路径后, 再加上当前元素的路径对应的路径表示: "c", 得到真正的全路径;
        return full_path + 'c'

    """
解法2: 广度优先搜索版本;
    """
    def numDistinctIslands_v2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        paths = set()
        directions = ['u', 'l', 'd', 'r']

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    # jy: 设置为已遍历(下面会为当前位置的路径加上 "c" 后缀, 即表示已遍历)
                    visited[i][j] = True
                    # jy: 将当前位置(坐标为 1 ) 的坐标入队;
                    queue = deque([(i, j)])
                    path = ''
                    # jy: 如果队列不为空, 则左侧出队, 获取出队的位置的行和列坐标, 遍历其上下左右
                    #    位置, 并依据相应方位加上相应的字符后缀; 因此, 经过一轮 while 循环, 一个
                    #    岛屿所构成的 path 即可形成;
                    while queue:
                        cell = queue.popleft()
                        row, column = cell[0], cell[1]

                        for index, direction in enumerate([[-1, 0], [0, -1], [1, 0], [0, 1]]):
                            next_row = row + direction[0]
                            next_column = column + direction[1]

                            if next_row < 0 or next_row >= m or next_column < 0 or next_column >= n \
                                    or grid[next_row][next_column] != 1 or visited[next_row][next_column]:
                                continue

                            path += directions[index]
                            queue.append((next_row, next_column))
                            visited[next_row][next_column] = True

                        path += 'c'

                    paths.add(path)

        return len(paths)

    """
JY: 在解法1 的基础上做变种:
由于以上遍历元素的时候, 总是会先遍历岛屿的所在行数最小, 且最小行中列最小的值, 如果两个
岛屿形状相同, 则相同形状的岛屿的该位置的行或列的坐标差即为对应其它位置的行或列的坐标差

因此, 可以将按相同遍历逻辑, 将同一个岛屿的坐标加入到一个列表中, 后续再判断列表中坐标个
数相同的岛屿是否属于同一形状的岛屿, 如果是则数量减 1;

未完成, 还差最后一步处理过程
    """
    def numDistinctIslands_jy(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # jy: m 行 n 列;
        m, n = len(grid), len(grid[0])
        # jy: 记录哪些位置已经被访问过
        visited = [[False for _ in range(n)] for _ in range(m)]
        paths = []
        # jy: 遍历矩阵;
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    paths.append(self._dfs_jy(grid, i, j, visited))
        print("====paths====", paths)
        # jy: 此处还未结束, 还需要对 paths 进行处理: paths 中的元素, 如果是长度相同的, 则
        #    需要进一步判断是否属于同一个类型的岛屿; 或者将该处理逻辑放置到向 paths 添加
        #    元素前进行: 可以将得到的岛屿坐标列表放入字典中, 其长度作为 key, value 为一个
        #    列表, 存在相同长度的所有岛屿, 每得到一个岛屿时坐标列表时, 如果发现有长度相同
        #    的, 就循环判断该岛屿类型是否在列表中了, 不存在再加入;
        return len(paths)

    def _dfs_jy(self, grid, row, column, visited):
        # jy: m 行 n 列;
        m, n = len(grid), len(grid[0])
        if row < 0 or row >= m or column < 0 or column >= n or grid[row][column] != 1 or visited[row][column]:
            return None
        # jy: 将该位置的值设置为已访问;
        visited[row][column] = True
        ls_island_position = []
        for i, direction in enumerate([[-1, 0], [0, -1], [1, 0], [0, 1]]):
            path = self._dfs_jy(grid, row + direction[0], column + direction[1], visited)
            if path:
                ls_island_position += path
        ls_island_position += [row, column]
        return ls_island_position


grid = [
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,0,1,1],
[0,0,0,1,1]]
#return 1.
res = Solution().numDistinctIslands_v1(grid)
print(res)


grid = [
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,0,1,1],
[0,0,0,1,1]]
#return 1.
res = Solution().numDistinctIslands_jy(grid)
print(res)
# a = []
# a.append([1,2])
# print(a)


grid = [
[1,1,0,1,1],
[1,0,0,0,0],
[0,0,0,0,1],
[1,1,0,1,1]]
# return 3.
res = Solution().numDistinctIslands_v1(grid)
print(res)


