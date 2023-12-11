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
title_jy = "Number-of-Distinct-Islands-II(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You
may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same
as another if they have the same shape, or have the same shape after rotation
(90, 180, or 270 degrees only) or reflection (left/right direction or up/down
direction).



Example 1:
11000
10000
00001
00011
Given the above grid map, return 1.
Notice that:
11
1
and
 1
11
are considered same island shapes. Because if we make a 180 degrees clockwise rotation
on the first island, then two islands will have the same shapes.


Example 2:
11100
10001
01001
01110
Given the above grid map, return 2.
Here are the two distinct islands:
111
1
and
1
1
Notice that:
111
1
and
1
111
are considered same island shapes. Because if we flip the first array in the up/down
direction, then they have the same shapes.



Note: The length of each dimension in the given grid does not exceed 50.
"""







from typing import List
from collections import deque



class Solution:
    """
解法1: 和 694_Number-of-Distinct-Islands.py 的基本思想一致, 只是要处理更多的岛屿路径变
种, 不过这道题没有使用自定义的路径表示, 因为涉及到路径旋转的操作, 为方便实现, 直接使用
岛屿的坐标即 (i, j) 作为岛屿路径, 例如一个岛屿的完整路径可能为 [(0, 0), (0, 1), (1, 0)],
要判断两个岛屿是否相等, 只要求得其中某个岛屿的所有路径变种, 然后判断这些路径变种是否存
在和另一个岛屿路径相等即可;
    """
    def numDistinctIslands2_v1(self, grid: List[List[int]]) -> int:
        paths = set()
        # jy: m 行 n 列;
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        # jy: 遍历数组;
        for i in range(m):
            for j in range(n):
                # jy: 如果位置坐标属于岛屿的一部分(值为 1)且没有被访问过, 则递归查找该位置坐
                #    标及其相邻坐标中属于岛屿的部分, 将坐标路径存放入 path 列表;
                if grid[i][j] == 1 and not visited[i][j]:
                    path = []

                    self._dfs(i, j, grid, visited, path)
                    # jy: 对岛屿坐标路径进行标准化: 对于不经过旋转就形状一致的岛屿, 坐标排序
                    #    后, 其它坐标位置的值减去第一个坐标位置的值后形成的列表是相等的;
                    path = self._normalize(path)
                    # jy: 判断路径变种后, 是否在 paths 中不存在(即路径旋转后是否唯一), 如果唯一,
                    #    则将其以元组的形式加入 paths 集合;
                    if self._is_all_path_variation_unique(path, paths):
                        paths.add(tuple(path))
        # jy: 最终返回 paths 集合的长度即为不同类型的岛屿个数;
        return len(paths)


    def _dfs(self, row, column, grid, visited, path):
        # jy: m 行 n 列;
        m, n = len(grid), len(grid[0])
        # jy: 如果遇到不满足条件的坐标位置, 则直接返回, 终止递归
        if row < 0 or row >= m or column < 0 or column >= n or grid[row][column] != 1 or visited[row][column]:
            return
        # jy: 如果坐标位置属于岛屿的一部分, 则将其加入 path 列表, 并设置为已访问;
        visited[row][column] = True
        path.append((row, column))
        # jy: 遍历当前作为的左上右下相邻的四个方向, 将属于岛屿的相邻部分递归的加入到 path 列表中;
        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            self._dfs(row + direction[0], column + direction[1], grid, visited, path)

    # jy: 以下方法在解法 1 和 2 中共用 - Begin
    def _normalize(self, path):
        """
        对岛屿坐标路径进行标准化: 对于不经过旋转就形状一致的岛屿, 坐标排序后, 其它坐标
        位置的值减去第一个坐标位置的值后形成的列表是相等的;
        """
        sorted_path = sorted(path)
        return [(x - sorted_path[0][0], y - sorted_path[0][1]) for x, y in sorted_path]


    def _is_all_path_variation_unique(self, path, paths):
        """判断路径变种后, 是否在 paths 中不存在(即路径旋转后是否唯一)"""
        # jy: 将当前 path 经过各种旋转/反转变种, 并判断变种后的结果对应的元组格式是否
        #    在 paths 集合中出现, 如果有一种变种出现, 则直接返回 False;
        #    1) 三个角度旋转: 判断当前坐标位置以及经过 90*n 旋转(3 个角度的旋转)后的
        #       坐标位置元组是否在 paths 集合中出现, 出现则返回 False;
        if tuple(path) in paths or not self._is_rotation_unique(path, paths):
            return False
        #    2) 竖直方向上反转, 旋转: 判断竖直方向上反转后的坐标位置, 以及反转后 3 个
        #       角度旋转后的坐标位置元组是否在 paths 集合中出现, 出现则返回 False;
        horizontal_path = self._normalize([(-x, y) for x, y in path])
        if tuple(horizontal_path) in paths or not self._is_rotation_unique(horizontal_path, paths):
            return False
        #    3) 水平方向上反转, 旋转: 判断水平方向上反转后的坐标位置, 以及反转后 3 个
        #       角度旋转后的坐标位置元组是否在 paths 集合中出现, 出现则返回 False;
        vertical_path = self._normalize([(x, -y) for x, y in path])
        if tuple(vertical_path) in paths or not self._is_rotation_unique(vertical_path, paths):
            return False

        return True


    def _is_rotation_unique(self, path, paths):
        """判断位置坐标旋转后是否唯一"""
        # jy: 3 个角度旋转: 循环 3 次, 每次旋转 90 度, 下一次在上一次的基础上旋转 90 度,
        #    即三次循环分别为 90, 180, 270 度;
        for i in range(3):
            path = self._normalize([(y, -x) for x, y in path])

            if tuple(path) in paths:
                return False

        return True
    # jy: 以上方法在解法 1 和 2 中共用 - End


    """
解法2: 广度优先搜索版本;
    """
    def numDistinctIslands2_v2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        paths = set()
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # jy: 如果碰到当前坐标位置为岛屿的一部分, 则将其加入队列中, 并设置为已访
                #    问(加入队列的元素都认为是已访问状态, 因为后续肯定是要出队的), 在后
                #    续队列出队后遍历出队位置的相邻四个方向上的位置, 并把属于岛屿的部分
                #    继续入队, 当队列元素全部出队后, 队列为空, 此时表明属于一个岛屿的全
                #    部坐标位置已经遍历完成, 此时得到该岛屿的 path 列表(即一次 if 判断成
                #    立结合内部 while 循环遍历完成后, 得到一个完整的岛屿路径; 当二维数组
                #    元素全部遍历完成后, 即得到所有的岛屿路径), 得到岛屿路径后, 后续的操
                #    作与解法 1 中的相同;
                if grid[i][j] == 1 and not visited[i][j]:
                    path = [(i, j)]
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

                            path.append((next_row, next_column))
                            queue.append((next_row, next_column))
                            visited[next_row][next_column] = True

                    path = self._normalize(path)
                    if self._is_all_path_variation_unique(path, paths):
                        paths.add(tuple(path))

        return len(paths)



grid = [
[1, 1, 0, 0, 0],
[1, 0, 0, 0, 0],
[0, 0, 0, 0, 1],
[0, 0, 0, 1, 1]]
# return 1.
res = Solution().numDistinctIslands2_v1(grid)
print(res)


grid = [
[1, 1, 1, 0, 0],
[1, 0, 0, 0, 1],
[0, 1, 0, 0, 1],
[0, 1, 1, 1, 0]]
# return 2.
res = Solution().numDistinctIslands2_v2(grid)
print(res)


