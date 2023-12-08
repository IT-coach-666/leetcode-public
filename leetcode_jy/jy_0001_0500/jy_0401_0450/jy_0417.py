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
title_jy = "Pacific-Atlantic-Water-Flow(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There is an ``m x n`` rectangular island that borders both the Pacific Ocean and
Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the
Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an ``m x n``
integer matrix ``heights`` where ``heights[r][c]`` represents the height above sea
level of the cell at coordinate (r, c). The island receives a lot of rain, and the
rain water can flow to neighboring cells directly north, south, east, and west if the
neighboring cell's height is less than or equal to the current cell's height. Water
can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain
water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


Example 1:    https://www.yuque.com/frederick/dtwi9g/fl1u7b

Input: heights = [
[1,2,2,3,5],
[3,2,3,4,4],
[2,4,5,3,1],
[6,7,1,4,5],
[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [
[2,1],
[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]


Constraints:
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5
"""


from typing import List
from collections import deque


class Solution:
    """
解法1: 因为矩阵的四条边是可以流入海洋的, 所以如果某个点 (i, j) 可以到达海洋则最后必然
会经过四条边的某个点, 所以对于两个大洋, 分别从四条边开始递推, 计算出哪些点和两个大洋相
连, 最后公共的部分就是结果;
注意到因为是从海洋向陆地推导, 所以需要满足条件(这样陆地上的雨水才能流向海洋):
heights[row][column] <= heights[new_row][new_column]
    """
    def pacificAtlantic_v1(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m = len(heights)
        n = len(heights[0])
        # jy: 记录二维数组中的指定位置坐标是否可以流入 pacific / atlantic
        pacific_connected = [[False] * n for _ in range(m)]
        atlantic_connected = [[False] * n for _ in range(m)]
        result = []

        for i in range(m):
            # jy: 第一列的所有坐标位置均能入 pacific, 递归判断与其相邻的坐标位置是否也能
            #     入 pacific, 如果可以, 将 pacific_connected 中的相应坐标位置设置为 True;
            self._dfs(heights, i, 0, pacific_connected, m, n)
            # jy: 最后一列的所有坐标位置均能入 atlantic, 递归判断与其相邻的坐标位置是否也
            #     能入 atlantic, 如果可以, 将 atlantic_connected 中的相应坐标位置设置为 True;
            self._dfs(heights, i, n-1, atlantic_connected, m, n)

        for i in range(n):
            # jy: 第一行的所有坐标位置均能入 pacific, 递归判断与其相邻的坐标位置是否也能
            #     入 pacific, 如果可以, 将 pacific_connected 中的相应坐标位置设置为 True;
            self._dfs(heights, 0, i, pacific_connected, m, n)
            # jy: 最后一行的所有坐标位置均能入 atlantic, 递归判断与其相邻的坐标位置是否也
            #     能入 atlantic, 如果可以, 将 atlantic_connected 中的相应坐标位置设置为 True;
            self._dfs(heights, m-1, i, atlantic_connected, m, n)

        # jy: 遍历二维数组中的所有位置坐标, 如果该位置坐标既可以流入 pacific 又可以流入 atlantic,
        #     则将其加入到结果列表中;
        for i in range(m):
            for j in range(n):
                if pacific_connected[i][j] and atlantic_connected[i][j]:
                    result.append([i, j])
        return result

    def _dfs(self, heights, row, column, connected, m, n):
        """
        传入该递归方法中的 row 和 column 对应的坐标位置是确保可以流入海洋的, 因此将
        connected 中的该位置坐标值设置为 True, 并递归判断该位置的相邻位置是否可以流入海洋;

        传入该递归方式中的 m 和 n 是固定不变的, 即为二维数组 heights 的行数和列数, 由于其
        可以通过 heights 确定, 故该递归方法中可以去掉最后两个参数, 并在方法内部通过 len()
        获取相应的 m 和 n 的值, 但这样的话每一次递归都会调用 len() 方法, 相对于直接传入而
        言, 性能有所损失(也可以在类中定义 __init__ 方法, 初始化时传入 heights 并求得 self.m
        和 self.n 的值, 后续即可直接调用, 可避免递归方法中传入的同时, 也避免重复运算)
        """
        connected[row][column] = True
        # jy: 递归判断当前位置 (row, column) 的相邻四个方向上的位置是否可以入海;
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_column = row + direction[0], column + direction[1]
            # jy: 如果新的坐标位置超出岛屿范围, 或者之前已经确认可以入海(即 connected[new_row][new_column]
            #     为 True), 或者确定不能入海(即 heights[row][column] > heights[new_row][new_column]), 则跳
            #     过当前位置的判断, 继续下一个相邻位置的判断;
            if new_row < 0 or new_row >= m or new_column < 0 or new_column >= n \
                    or connected[new_row][new_column] or heights[row][column] > heights[new_row][new_column]:
                continue
            # jy: 如果新的坐标位置能入海(且之前没有判断过, 即 connected[new_row][new_column] 为 False; 目
            #     的是避免重复运算), 则递归判断新坐标位置的相邻位置是否可入海;
            self._dfs(heights, new_row, new_column, connected, m, n)

    """
解法2: 广度优先搜索版本
    """
    def pacificAtlantic_v2(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m = len(heights)
        n = len(heights[0])
        # jy: 将第一列和第一行的坐标位置均加入到 pacific_connected 集合中, 表示可以流
        #     入 pacific 的坐标位置;
        pacific_connected = set([(i, 0) for i in range(m)] + [(0, i) for i in range(n)])
        # jy: 将最后一列和最后一行的坐标位置均加入到 atlantic_connected 集合中, 表示可
        #     以流入 atlantic 的坐标位置;
        atlantic_connected = set([(i, n-1) for i in range(m)] + [(m-1, i) for i in range(n)])
        result = []

        pacific_connected = self._bfs(pacific_connected, heights, m, n)
        atlantic_connected = self._bfs(atlantic_connected, heights, m, n)

        for i in range(m):
            for j in range(n):
                if (i, j) in pacific_connected and (i, j) in atlantic_connected:
                    result.append([i, j])

        return result

    def _bfs(self, connected, heights, m, n):
        # jy: 基于 connected 构造队列(初始传入的 connected 中的坐标位置均表示可以流入指
        #     定海洋的坐标位置), 即此时的队列中的坐标位置为可以流入指定海洋的坐标位置;
        queue = deque(connected)
        # jy: 如果队列不为空, 则不断出队, 并判断出队的坐标位置的相邻位置是否可以流入指定
        #     海洋, 如果可以, 则将对应的位置加入队列, 同时也加入 connected 中, 最终返回
        #     的 connected 即为所有可以流入该指定海洋的坐标位置;
        while queue:
            row, column = queue.popleft()

            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_column = row + direction[0], column + direction[1]

                if new_row < 0 or new_row >= m or new_column < 0 or new_column >= n \
                        or (new_row, new_column) in connected or heights[row][column] > heights[new_row][new_column]:
                    continue

                queue.append((new_row, new_column))
                connected.add((new_row, new_column))

        return connected


heights = [
[1, 2, 2, 3, 5],
[3, 2, 3, 4, 4],
[2, 4, 5, 3, 1],
[6, 7, 1, 4, 5],
[5, 1, 1, 2, 4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
res = Solution().pacificAtlantic_v1(heights)
print(res)


heights = [
[2, 1],
[1, 2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
res = Solution().pacificAtlantic_v1(heights)
print(res)


