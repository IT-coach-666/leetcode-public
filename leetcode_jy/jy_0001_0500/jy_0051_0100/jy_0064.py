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
title_jy = "Minimum-Path-Sum(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = "动态规划 | 递归 + 缓存 | 相似题: arr_dim_2_path"


"""
Given a m x n `grid` filled with non-negative numbers, find a path from top
left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 
Example 1:
Input: grid = [
 [1, 3, 1],
 [1, 5, 1],
 [4, 2, 1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [
 [1, 2, 3],
 [4, 5, 6]]
Output: 12


Constraints:
1) m == grid.length
2) n == grid[i].length
3) 1 <= m, n <= 200
4) 0 <= grid[i][j] <= 200
"""

class Solution:
    """
解法 1: 动态规划

用更新后的 grid[i][j] 表示从位置 (0, 0) 到位置 (i, j) 的最短路径
    """
    def minPathSum_v1(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # jy: 如果处于左上角开始位置, 则跳过 (保留原值)
                if i == j == 0:
                    continue

                # jy: 经过以上, 表明 i 和 j 不会同时为 0, 此时:
                #     1) 如果 i 为 0, 表明处于第一行, 当前位置 (i, j) 只能从位
                #        置 (i, j-1) 走过来
                #     2) 如果 j 为 0, 表明处于第一列, 当前位置 (i, j) 只能从位
                #        置 (i-1, j) 走过来
                #     3) 如果 i 和 j 均不为 0, 则当前位置 (i, j) 可以从位置
                #        (i-1, j) 或 (i, j-1) 走过来, 此时应选路径更短的一个
                if i == 0:  
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        # jy: 最终返回右下角位置的最短路径
        return grid[-1][-1]


    """
解法 2: 递归 + 缓存 (类似动态规划, 参考 0063 中的解法 3)
    """
    def minPathSum_v2(self, grid: [[int]]) -> int:
        dict_ = {}

        def dfs(grid, i, j):
            if i < 0 or j < 0:
                return 0

            if i == 0 and j == 0:
                return grid[i][j]

            if (i, j) in dict_:
                return dict_[(i, j)]

            if i == 0:
                dict_[(i, j)] = dfs(grid, i, j-1) + grid[i][j]
            elif j == 0:
                dict_[(i, j)] = dfs(grid, i-1, j) + grid[i][j]
            else:
                dict_[(i, j)] = min(dfs(grid, i-1, j), dfs(grid, i, j-1)) + grid[i][j]
            return dict_[(i, j)]


        m, n = len(grid), len(grid[0])
        return dfs(grid, m-1, n-1)


grid = [
 [1, 3, 1],
 [1, 5, 1],
 [4, 2, 1]]
res = Solution().minPathSum_v1(grid)
# jy: 7
print(res)


grid = [
 [1, 2, 3],
 [4, 5, 6]]
res = Solution().minPathSum_v1(grid)
# jy: 12
print(res)


