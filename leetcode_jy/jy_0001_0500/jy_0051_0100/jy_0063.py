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
title_jy = "Unique-Paths-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "动态规划 | 递归 + 缓存 | 相似题: arr_dim_2_path"



"""
You are given an m x n integer array `grid`. There is a robot initially
located at the top-left corner (i.e., grid[0][0]). The robot tries to move
to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move
either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in `grid`. A path
that the robot takes cannot include any square that is an obstacle. Return
the number of possible unique paths that the robot can take to reach the 
bottom-right corner.

The testcases are generated so that the answer will be less than or equal to
2 * 10^9.

 

Example 1:
Input: obstacleGrid = [
 [0, 0, 0],
 [0, 1, 0],
 [0, 0, 0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
             There are two ways to reach the bottom-right corner:
             1. Right -> Right -> Down -> Down
             2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [
 [0, 1],
 [0, 0]]
Output: 1
 

Constraints:
1) m == obstacleGrid.length
2) n == obstacleGrid[i].length
3) 1 <= m, n <= 100
4) obstacleGrid[i][j] is 0 or 1.
"""


class Solution:
    """
解法 1: 动态规划 (参考 0062 中的解法 2)

记 dp[i][j] 表示机器人从 (0, 0) 走到 (i, j) 的路径数
    """
    def uniquePathsWithObstacles_v1(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]

        # jy: 从上到下遍历每一行, 从左到右遍历每一列
        for i in range(m):
            for j in range(n):
                # jy: 如果当前位置 (i, j) 没有障碍物, 表明可能存在路径能走
                #     到该位置, 尝试更新 dp[i][j]; 如果当前位置有障碍物, 则
                #     无需更新 dp[i][j], 保留其默认值 0
                if not obstacleGrid[i][j]:
                    # jy: 由于可能存在障碍物, 因此不能确定第一行或第一列的所
                    #     有位置的路径走法均为 1 (与 0062 的主要区别)
                    if i == j == 0:
                        dp[i][j] = 1
                    else:
                        # jy: (i-1, j) 为 (i, j) 的上方位置, dp[i-1][j] 即从
                        #     位置 (0, 0) 走到位置 (i-1, j) 的路径数, 如果 i
                        #     为 0, 表明该上方位置不存在, 不能从该上方位置往
                        #     下走到 (i, j)
                        top = dp[i-1][j] if i != 0 else 0
                        # jy: (i, j-1) 为 (i, j) 的左方位置, dp[i][j-1] 即从
                        #     位置 (0, 0) 走到位置 (i, j-1) 的路径数, 如果 j
                        #     为 0, 表明该左方位置不存在, 不能从该左方位置往
                        #     右走到 (i, j)
                        left = dp[i][j-1] if j != 0 else 0
                        # jy: 走到当前位置 (i, j) 的走法是以上两种走法之和
                        dp[i][j] = top + left
        return dp[m-1][n-1]


    """
解法 2: 同解法 1, 但不额外引入 dp 数组, 而是直接使用原矩阵
    """
    def uniquePathsWithObstacles_v2(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]: 
                    obstacleGrid[i][j] = 0
                else:
                    if i == j == 0:
                        obstacleGrid[i][j] = 1
                    else:
                        top = obstacleGrid[i-1][j] if i != 0 else 0 
                        left = obstacleGrid[i][j-1] if j != 0 else 0
                        obstacleGrid[i][j] = top + left
        return obstacleGrid[m-1][n-1]


    """
解法 3: 递归 + 缓存 (类似动态规划, 参考 0062 中的解法 6)
    """
    def uniquePathsWithObstacles_v3(self, obstacleGrid: List[List[int]]) -> int:
        dict_ = {}

        def dfs(obstacleGrid, i, j):
            if i < 0 or j < 0:
                return 0

            if obstacleGrid[i][j]:
                return 0

            if i == 0 and j == 0:
                return 1


            if (i, j) in dict_:
                return dict_[(i, j)]

            dict_[(i, j)] = dfs(obstacleGrid, i-1, j) + dfs(obstacleGrid, i, j-1)
            return dict_[(i, j)]


        m, n = len(obstacleGrid), len(obstacleGrid[0])       
        return dfs(obstacleGrid, m-1, n-1)


obstacleGrid = [
 [0, 0, 0],
 [0, 1, 0],
 [0, 0, 0]]
res = Solution().uniquePathsWithObstacles_v1(obstacleGrid)
# jy: 2
print(res)


obstacleGrid = [
 [0, 1],
 [0, 0]]
res = Solution().uniquePathsWithObstacles_v1(obstacleGrid)
# jy: 1
print(res)

