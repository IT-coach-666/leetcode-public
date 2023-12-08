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
title_jy = "Number-of-Islands-II(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an empty 2D binary grid ``grid`` of size ``m x n``. The grid represents
a map where 0's represent water and 1's represent land. Initially, all the cells of
grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land.
You are given an array ``positions`` where ``positions[i] = [ri, ci]`` is the position
``(ri, ci)`` at which we should operate the ``ith`` operation.

Returnan array of integers ``answer`` where ``answer[i]`` is the number of islands
after turning the cell ``(ri, ci)`` into a land.

An ``island`` is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.



Example 1:
Input: m = 3, n = 3, positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
Output: [1, 1 ,2, 3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.

Example 2:
Input: m = 1, n = 1, positions = [[0, 0]]
Output: [1]



Constraints:
1 <= m, n, positions.length <= 10^4
1 <= m * n <= 10^4
positions[i].length == 2
0 <= ri < m
0 <= ci < n



Follow up: Could you solve it in time complexity O(k log(mn)), where k == positions.length ?
"""


from collections import deque
from typing import List


'''
解法 2 和 解法 3 中使用到该类;
'''
class UnionFind:
    def __init__(self, n: int):
        # jy: 初始化为值为 -1 的列表;
        self.roots = [-1] * n
        self.count = 0

    def add(self, index: int):
        # jy: 如果 index 对应的值为 -1, 则将其更新为 index, 并使 count 属性加 1;
        if self.roots[index] == -1:
            self.roots[index] = index
            self.count += 1

    def get_parent(self, index: int):
        return self.roots[index]

    def find_root(self, index: int) -> int:
        # jy: union 方法中可能会使得 index != self.roots[index], add 方法中使得 index == self.roots[index]
        while index != self.roots[index]:

            # jy: 优化(该行优化代码去除也是正确的), 在执行 find_root 时增加了路径压缩, 避免树的深度太
            #    长, 退化到 O(n), 这里优化为将当前节点的父节点指向原父节点的父节点;
            self.roots[index] = self.roots[self.roots[index]]

            index = self.roots[index]

        return index

    def union(self, p: int, q: int):
        p_root = self.find_root(p)
        q_root = self.find_root(q)

        if p_root == q_root:
            return

        self.roots[p_root] = q_root
        self.count -= 1

    def get_count(self):
        return self.count


class Solution:
    """
解法1(超时): 遍历 positions, 复用 200_Number-of-Islands.py 计算岛屿的个数, 不过会超时;
    """
    def numIslands2_v1(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [['0'] * n for _ in range(m)]
        counts = [0] * len(positions)

        # jy: 将 positions 中的坐标对应位置设置为 1, 随后计算该位置设置为 1 后的 island 的
        #    个数, 并更新到 counts 列表;
        for i, position in enumerate(positions):
            row, column = position[0], position[1]
            grid[row][column] = 1
            counts[i] = self._num_islands(grid)

        return counts


    def _num_islands(self, grid: List[List[str]]) -> int:
        ''' 200_Number-of-Islands.py 中的统计 island 个数的解法 '''
        count = 0
        # jy: m 行 n 列;
        m, n = len(grid), len(grid[0])
        # jy: 初始化遍历矩阵, 将各个位置初始化为 False;
        visited = [[False for _ in range(n)] for _ in range(m)]

        # jy: 遍历矩阵;
        for i in range(m):
            for j in range(n):
                # jy: 如果对应位置代表 island (值为 1), 且没有被遍历过, 则岛屿数加 1;
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1
                    visited[i][j] = True

                    queue = deque([(i, j)])
                    while queue:
                        cell = queue.popleft()
                        row, column = cell[0], cell[1]
                        # jy: 将对应位置的上下左右四个相邻的方向中的 1 设置为已遍历(因为属于同一
                        #    个 island, 后续不需要再次统计);
                        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                            next_row = row + direction[0]
                            next_column = column + direction[1]
                            # jy: 如果该位置超出矩阵边界, 或者值不为 1, 或已经被遍历过, 则跳过;
                            if next_row < 0 or next_row >= m or next_column < 0  or next_column >= n \
                                    or grid[next_row][next_column] != 1 or visited[next_row][next_column]:
                                continue
                            # jy: 将相邻的 1 (即属于同一个 island) 且没有被访问过的位置加入到队列, 使得
                            #    后续会对该位置的上下左右四个方向进行进一步遍历;
                            queue.append((next_row, next_column))
                            visited[next_row][next_column] = True

        # jy: 循环结束后得到的 count 即为 island 的数量;
        return count


    """
解法2: 解法 1 做了许多重复的工作, 因为每次修改 grid 中的元素不一定会影响整个岛屿的数
量, 或仅影响局部岛屿的数量;

该题可转化为一个 Union Find 问题, 遍历 positions, 如果当前元素已经在某个集合中, 说明
该元素已在某个岛屿中; 如果不在, 则添加该元素作为一个新的集合, 然后遍历该元素的邻居, 如
果某个邻居已经在某个集合中了, 说明将当前元素置为 1 后会将两个集合进行合并, 此时岛屿的
数量需要减 1;
    """
    def numIslands2_v2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        counts = []
        # jy: 初始化 UnionFind, 传入的参数为二维数组中数值的个数, 该类初始化后, 其 roots 属性
        #    会初始化为一个值为 -1 的一维数组, 数值的个数即二维数组的数值个数(即二维数组一维
        #    化, 并将对应数值初始化为 -1)
        uf = UnionFind(m * n)
        # jy: 定义上下左右四个相邻方位;
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        # jy: 遍历 positions
        for position in positions:
            # jy: n 为二维数组的列数, 此处得到的 root 为一个数值(即二维数组一维化后的对应位置);
            root = n * position[0] + position[1]
            # print("root===", root)
            # jy: 如果 uf 类中对应的 root 位置数值不为 -1, 则获取 uf 类的 count 属性值并加入到 counts 列表中;
            if uf.get_parent(root) != -1:
                counts.append(uf.get_count())
                continue
            # jy: 如果 uf 类中对应的 root 位置数值为 -1, 则将该位置加入到 uf 类中(如果 uf 类中 root 位置
            #    原值为 -1, 则会更新其值为 root, 并使 count 属性加1)
            uf.add(root)
            # jy: 遍历上下左右四个方位;
            for direction in directions:
                x = position[0] + direction[0]
                y = position[1] + direction[1]
                # jy: 此处得到的 neighbor 二维数组中 position 位置经过一维化(uf 类中 roots 属性)后的相邻位置
                neighbour = n * x + y
                # jy: 如果行或列超出有效范围, 或 uf 类中 neighbor 位置对应的值为 -1(表明该位置还未被加入到 uf 类
                #    中), 则跳过并继续下一轮循环;
                if x < 0 or x >= m or y < 0 or y >= n or uf.get_parent(neighbour) == -1:
                    continue
                # jy: 如果 root 和 neighbor 对应的位置均已经被加入到 uf 类中(属于 positions 中的位置均会被加
                #    入到 uf 中), 则针对这两位置执行 uf 类的 union 方法, 该方法中会判断两个位置如果均为岛屿
                #    是否其属于同一个岛屿上, 如果是, 则 count 会减 1(因为属于重合的岛屿计算, positions 中的
                #    每个元素加入到 uf 类时其 count 属性均会加1, 表示岛屿数加1, 如果两个位置均属于同一岛屿
                #    中, 则岛屿数需减 1)
                uf.union(root, neighbour)
            # jy: 每遍历完 positions 中的一个岛屿数, uf 类中的 count 属性值即为相应 position 被设置为岛屿后
            #    整个二维数组中的岛屿数;
            counts.append(uf.get_count())

        return counts



m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
# Output: [1, 1 ,2, 3]
res = Solution().numIslands2_v1(m, n, positions)
print(res)
res = Solution().numIslands2_v2(m, n, positions)
print(res)

m = 1
n = 1
positions = [[0, 0]]
# Output: [1]
res = Solution().numIslands2_v2(m, n, positions)
print(res)


