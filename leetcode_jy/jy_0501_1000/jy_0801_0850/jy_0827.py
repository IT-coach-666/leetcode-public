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
title_jy = "Making-A-Large-Island(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Returnthe size of the largest island in grid after applying this operation. An island is
a 4-directionally connected group of 1s.


Example 1:
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.



Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""


from typing import List
import collections


class Solution:
    """
解法1(超时): 在 695_Max-Area-of-Island.py 的基础上, 依次尝试将 0 置为 1, 然后
求最大的岛屿面积;
    """
    def largestIsland_v1(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    # jy: 构造新的二维数组, 使得 grid[i][j] == 1 (原来是 0)
                    new_grid = self._new_grid(grid, m, n, i, j)
                    area = self._max_area_of_island(new_grid)
                    max_area = max(area, max_area)
        # jy: 注意, 按以上逻辑, max_area 可能会是 0 (当二维数组值全为 1 时, 由于没
        #     有 grid[i][j] == 0 的场景, 故 max_area 不会被更新, 为 0), 此时应该直
        #     接计算岛屿的面积即可(不能直接简单 ``return max_area``);
        return max_area if max_area != 0 else self._max_area_of_island(grid)


    def _max_area_of_island(self, grid: List[List[int]]) -> int:
        """获取二维数组中的最大岛屿面积"""
        max_area = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # jy: 一次 if 判断成立会获取一个岛屿的面积, 二维数组遍历完后, 即获得所
                #    有岛屿的面积, 在该过程中, 获取面积最大的岛屿, 并最终返回;
                if grid[i][j] == 1 and not visited[i][j]:
                    area = self._dfs(grid, i, j, visited)
                    max_area = max(area, max_area)
        return max_area


    def _dfs(self, grid, row, column, visited):
        m, n = len(grid), len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n or grid[row][column] != 1 or visited[row][column]:
            return 0
        # jy: 当前位置为岛屿的一部分, 其面积为 1, 访问后设置该位置已访问;
        area = 1
        visited[row][column] = True
        # jy: 递归遍历岛屿的相邻四个方向, 求得其面积, 并与当前面积相加, 最终返回当前面积;
        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            area += self._dfs(grid, row + direction[0], column + direction[1], visited)

        return area


    def _new_grid(self, grid, m, n, row, column):
        new_grid = [[grid[i][j] for j in range(n)] for i in range(m)]
        new_grid[row][column] = 1

        return new_grid


    """
解法2: 在解法1上进行优化, 将 0 置为 1 时, 如果能知道 0 的四周的 1 所对应的岛屿的面积, 则可直接求得
将 0 置为 1 后总岛屿的面积, 即 1 加上四周岛屿的面积; 故需要两次循环
1) 第一次和 200_Number-of-Islands.py 一样, 只是增加两个额外的信息:
   a) 每个坐标对应的岛屿序号
   b) 每个岛屿序号对应的岛屿面积
2) 第二次循环则是计算将 0 置为 1 时能获得的最大岛屿面积是多少;
    """
    def largestIsland_v2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # jy: m 行 n 列;
        m, n = len(grid), len(grid[0])
        # jy: 记录最大岛屿的面积;
        max_area = 0
        # jy: 记录岛屿的序号(第一个岛屿的序号将会是 1);
        island_index = 0
        # jy: 记录对应序号的岛屿的对应面积(字典格式)
        areas = collections.Counter()
        # jy: 记录二维数组的对应位置是否被访问过;
        visited = [[False for _ in range(n)] for _ in range(m)]
        # jy: 记录二维数组中, 属于岛屿的位置部分, 对应的岛屿编号;
        islands = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # jy: 如果属于岛屿的一部分, 则将该岛屿序号加 1 (避免与之前的岛屿序号重
                #    叠; 因此第一个岛屿的序号为 1), 求得该序号的岛屿对应的面积, 记录
                #    到 areas 字典中, 并在 islands 二维数组中把属于该岛屿的位置用该岛
                #    屿序号进行标记;
                if grid[i][j] == 1 and not visited[i][j]:
                    island_index += 1
                    self._dfs_v2(grid, i, j, visited, island_index, areas, islands)
                    max_area = max(max_area, areas[island_index])
        # jy: 经过以上二维数组的全部元素遍历, areas 保留了岛屿序号以及其对应的面积, islands 则
        #    将对应是岛屿的位置用该岛屿序号标记; 此处调用 _get_max_area_v2 方法, 找出二维数组
        #    中值为 0 的位置, 并判断将该位置置为 1 时, 与周边岛屿构成的最大岛屿面积;
        # jy: 如果二维数组中所有值均为 1, 则 _get_max_area_v2 方法返回的值会是 1, 此时真正的结
        #    果应该是此处的 max_area 值, 故需要该值与 _get_max_area_v2 方法的返回值进行比较;
        return max(max_area, self._get_max_area_v2(m, n, grid, areas, islands))


    def _dfs_v2(self, grid, row, column, visited, island_index, areas, islands):
        m, n = len(grid), len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n or grid[row][column] != 1 or visited[row][column]:
            return

        visited[row][column] = True
        areas[island_index] += 1
        islands[row][column] = island_index

        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            self._dfs_v2(grid, row + direction[0], column + direction[1], visited, island_index, areas, islands)

    def _get_max_area_v2(self, m, n, grid, areas, islands):
        """
        找出二维数组中值为 0 的位置, 并判断将该位置置为 1 时, 与周边岛屿构成的最大岛屿面积
        该方法同时也在解法 3 中应用
        """
        # jy: 先初始化 max_area 为 1 (将二维数组中 0 变为 1 后, 岛屿面积至少为 1)
        max_area = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                # jy: 找出 grid[i][j] == 0 的位置, 假设将该位置置为 1, 计算此时的岛屿面积
                area = 1
                # jy: 记录相邻位置的不同岛屿编号的集合;
                neighbour_islands = set()

                for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    next_row = i + direction[0]
                    next_column = j + direction[1]
                    # jy: 如果相邻四个方向的位置坐标不合规, 直接跳过;
                    if next_row < 0 or next_row >= m or next_column < 0 or next_column >= n:
                        continue
                    # jy: 将相邻位置的不同岛屿编号添加到集合中(如果非岛屿, 则其编号为 -1);
                    neighbour_islands.add(islands[next_row][next_column])
                # print("=========== ", neighbour_islands)
                # jy: 计算如果当前位置由 0 置为 1 后(此时至少面积为 1, 即 area 初始值), 岛屿的面
                #    积(此时加上相邻位置岛屿编号对应的岛屿面积即可)
                for island in neighbour_islands:
                    area += areas[island]
                # jy: 更新保留最大岛屿面积(最终返回);
                max_area = max(max_area, area)

        return max_area


    """
解法3: 广度优先搜索版本
    """
    def largestIsland_v3(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # jy: 以下初始化的变量同解法 2;
        m, n = len(grid), len(grid[0])
        max_area = 0
        island_index = 0
        areas = collections.Counter()
        visited = [[False for _ in range(n)] for _ in range(m)]
        islands = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or visited[i][j]:
                    continue
                # jy: 如果对应位置为原先的岛屿部分, 则岛屿编号加 1 (第一个岛屿编号为 1), 并将
                #    该位置加入队列, 后续出队时不断获取队列中坐标位置的相邻位置, 判断其是否属
                #    于岛屿部分, 如果是则不断使岛屿面积增加, 并记录相应位置的岛屿编号, 同时继
                #    续入队, 不断的判断相邻位置, 直到队列为空, 表明一个岛屿的面积计算完成;
                island_index += 1
                visited[i][j] = True
                queue = [(i, j)]

                while queue:
                    (row, column) = queue.pop(0)
                    areas[island_index] += 1
                    islands[row][column] = island_index

                    for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                        next_row = row + direction[0]
                        next_column = column + direction[1]

                        if next_row < 0 or next_row >= m or next_column < 0 or next_column >= n \
                                or grid[next_row][next_column] != 1 or visited[next_row][next_column]:
                            continue

                        visited[next_row][next_column] = True
                        queue.append((next_row, next_column))

                max_area = max(max_area, areas[island_index])
        # jy: 同解法 2 中的逻辑;
        return max(max_area, self._get_max_area_v2(m, n, grid, areas, islands))


grid = [[1,0],[0,1]]
# Output: 3
res = Solution().largestIsland_v1(grid)
print(res)


grid = [[1,1],[1,0]]
# Output: 4
res = Solution().largestIsland_v2(grid)
print(res)


grid = [[1,1],[1,1]]
# Output: 4
res = Solution().largestIsland_v3(grid)
print(res)



