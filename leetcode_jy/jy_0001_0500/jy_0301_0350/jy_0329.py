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
title_jy = "Longest-Increasing-Path-in-a-Matrix(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an ``m x n`` integers ``matrix``, return the length of the longest increasing
path in ``matrix``.  From each cell, you can either move in four directions: left,
right, up, or down. You may not move diagonally or move outside the boundary (i.e.,
wrap-around is not allowed).
 

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1
 

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1
"""


class Solution:
    def longestIncreasingPath_v1(self, matrix: List[List[int]]) -> int:
        # jy: 如果矩阵为空, 直接返回 0;
        if not matrix:
            return 0
        # jy: m 行 n 列;
        m, n = len(matrix), len(matrix[0])
        # jy: 初始化一个 m 行 n 列, 数值全为 0 的矩阵, 用于记录以指定位置坐标开始的最
        #     长递增路径;
        record = [[0] * n for _ in range(m)]
        # jy: res 记录了截止当前位置为止的最长增长路径;
        res = 0
        for i in range(m):
            for j in range(n):
                # jy: 如果原先已经计算过位置 (i, j) 开始的最长增长路径, 则不需要重再次复计算;
                if not record[i][j]:
                    # res = max(res, self._dfs(matrix, m, n, i, j, record))
                    res = max(res, self._dfs_v2(matrix, m, n, i, j, record))
        return res

    def _dfs(self, matrix, m, n, i, j, record):
        """
        从二维矩阵的坐标位置 (i, j) 开始递归遍历获取最长递增路径;
        record[i][j] 记录了以位置 (i, j) 开始的最长递增路径
        """
        current_max = 0
        # jy: 从下, 上, 右, 左四个方向逐个遍历;
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            x, y = i + dx, j + dy
            # jy: 如果新下标位置有效, 且比老下标位置的值大, 则计算以位置 (x, y) 开始的最长增长
            #     路径;
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                # jy: 如果 record[x][y] 不为 0, 表明从位置 (x, y) 开始的最长增长路径之前已经计
                #     算得到了, 不需要再次重复计算; 此处需要从 current_max 与 record[x][y] 比较
                #     出一个较大值, 因为当前的 record[x][y] 不一定就是位置 (i, j) 的四个方向上
                #     的增长路径最长的(同理, 也不一定就是 current_max);
                '''
                if record[x][y]:
                    current_max = max(current_max, record[x][y])
                else:
                    current_max = max(current_max, self._dfs(matrix, m, n, x, y, record))
                '''
                # jy: 以上代码可以简化为如下:
                if not record[x][y]:
                    record[x][y] = self._dfs(matrix, m, n, x, y, record)
                current_max = max(current_max, record[x][y])
        # jy: 经过以上四个方向的遍历(含递归过程), current_max 即为位置 (i, j) 开始的最长增长路
        #     径(不包含当前位置本身, 故最终需要进行加 1 处理, 将当前位置本身也算上);
        record[i][j] = current_max + 1 if current_max else 1
        return record[i][j]

    def _dfs_v2(self, matrix, m, n, i, j, record):
        """
        另一解法;
        """
        best = 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                if not record[x][y]:
                    record[x][y] = self._dfs_v2(matrix, m, n, x, y, record)
                best = max(best, record[x][y] + 1)
        # jy: 补充该项能加速运算;
        record[i][j] = best
        return best


matrix = [[9, 9, 4],
          [6, 6, 8],
          [2, 1, 1]]
# Output: 4
res = Solution().longestIncreasingPath_v1(matrix)
print(res)


matrix = [[3, 4, 5],
          [3, 2, 6],
          [2, 2, 1]]
# Output: 4
res = Solution().longestIncreasingPath_v1(matrix)
print(res)


matrix = [[1]]
# Output: 1
res = Solution().longestIncreasingPath_v1(matrix)
print(res)


