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
title_jy = "01-Matrix(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an m x n binary matrix ``mat``, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.


Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:
m == mat.lengthn == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
There is at least one 0 in ``mat``.
"""


import sys
from typing import List
from collections import deque


class Solution:
    """
解法1 (超时): 使用深度优先遍历搜索;
    """
    def updateMatrix_v1(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []
        # jy: m 行 n 列;
        m, n = len(mat), len(mat[0])
        # jy: 初始化距离矩阵, 值均为 0 (二维矩阵中值为 0 的位置的最近距离即为 0);
        distances = [[0] * n for _ in range(m)]
        # jy: 将二维矩阵中值为 1 的位置的距离先置为最大值;
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    distances[i][j] = sys.maxsize
        # jy: 找出二维数组中值为 0 的位置, 深度递归遍历;
        for i in range(m):
            for j in range(n):
                # jy: 值为 0 的位置的 distance (最后一个参数值) 为 0;
                if mat[i][j] == 0:
                    self._dfs(mat, i, j, distances, 0)

        return distances

    def _dfs(self, mat, row, column, distances, distance):
        # jy: m 行 n 列;
        m, n = len(mat), len(mat[0])
        # jy: 设置当前位置的距离为 distance;
        distances[row][column] = distance
        # jy: 遍历当前位置的左上右下四个相邻方向;
        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            next_row = row + direction[0]
            next_column = column + direction[1]
            # jy: 如果坐标不在规定范围内, 或者距离小于等于当前距离(初始化时距离矩阵除了坐标位
            #    置值为 0 的为 0 外, 其余坐标位置的距离值均为最大值), 则跳过当前位置; 调用该
            #    方法进行递归遍历时, 初始传入的坐标位置的距离均为 0, 而其相邻的四个方向的坐标
            #    中, 如果距离也为 0, 则跳过当前坐标位置, 进行下一个坐标位置的判断;
            if next_row < 0 or next_row >= m or next_column < 0 or next_column >= n \
                    or distances[next_row][next_column] <= distance:
                continue
            # jy: 如果第一次执行到此处, 表明当前位置的距离不为 0 (初始值为最大值), 由于其与 0 相邻,
            #    将该位置的坐标设置为 1 (该值也为该位置的终值), 并进一步递归判断该位置的相邻位置;
            #    根据此逻辑, 距离坐标中距离为 0 的相邻位置中距离大于 0 的距离坐标的距离数值会优先
            #    被设置为 1 (表示与值为 0 的坐标的距离为 1, 即为目标值), 经过此设置后, 递归设置其
            #    周边值: 距离坐标中的相邻位置中, 如果对应的距离值比当前的距离值大, 则表明对应的位
            #    置与 0 的距离要在当前的距离上加 1 (与值为 0 相邻且大于 0 的坐标都被置为 1 了, 与
            #    值为 1 相邻且大于 1 的位置对应的距离需要被置为 2, 因为其不与 0 直接相邻, 且相邻
            #    位置与 0 的距离为 1, 表明当前位置与 0 的距离为 2);
            self._dfs(mat, next_row, next_column, distances, distance + 1)


    """
解法2: 广度优先搜索版本;
    """
    def updateMatrix_v2(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []
        # jy: m 行 n 列;
        m, n = len(mat), len(mat[0])
        # jy: 记录对应位置是否已访问;
        visited = [[False] * n for _ in range(m)]
        # jy: 记录对应位置与坐标为 0 的位置的最小距离;
        distances = [[0] * n for _ in range(m)]
        queue = deque([])
        # jy: 遍历数组, 将值为 0 的位置入队, 并将该位置标记为已访问(值为 0 的位置对
        #    应的目标值已经是目标距离 0);
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = True

        # jy: 先批量将距离值为 0 相邻且未被访问(值不为 0, 因为值为 0 的已经标记已访问) 的坐标的
        #    距离设置为 1, 并且均设置为已访问; 接着批量将距离为 1 相邻且未被访问的坐标的值置为
        #    2, 并设置其已访问, 不断如此, 直到所有位置均被访问;
        while queue:
            # jy: 左侧出队获取一位置坐标, 并基于该坐标的相邻 4 个方向求相邻坐位置;
            #    出队时总是左侧先出, 入队时总是右侧入, 确保了先进先出; 因此, 距离
            #    值为 0 的坐标会优先遍历完成, 即会优先将与距离为 0 的坐标相邻且不
            #    为 0 的位置的距离置为 1, 并将距离值为 1 的坐标入栈; 等距离为 0 的
            #    坐标位置全部遍历完成后, 其相邻的非 0 位置的距离也均被置为 1, 接着
            #    就对距离为 1 的位置逐个出栈, 且对其相邻, 且还没有被访问过的位置的
            #    值置为 2, 如此循环, 最终得到目标距离矩阵;
            row, column = queue.popleft()
            for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                next_row = row + direction[0]
                next_column = column + direction[1]
                # jy: 如果坐标位置超出范围, 或者已访问, 则跳过当前坐标位置;
                if next_row < 0 or next_row >= m or next_column < 0 or next_column >= n or visited[next_row][next_column]:
                    continue
                # jy: 如果坐标有效, 且暂未被访问过, 则将该坐标入队, 并设置已访问, 并将该坐标的值设
                #    置为原坐标的距离值加 1 (因为该坐标是原坐标的相邻坐标, 且值不为 0, 则该坐标与
                #    值为 0 的坐标的距离即为原坐标与 0 的距离加上 1);
                queue.append((next_row, next_column))
                visited[next_row][next_column] = True
                distances[next_row][next_column] = distances[row][column] + 1

        return distances


mat = [
[0,0,0],
[0,1,0],
[0,0,0]]
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
res = Solution().updateMatrix_v1(mat)
print(res)


mat = [
[0,0,0],
[0,1,0],
[1,1,1]]
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]
res = Solution().updateMatrix_v2(mat)
print(res)


