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
tag_jy = ""



"""
You are given an m x n integer array grid. There is a robot initially located
at the top-left corner (i.e., grid[0][0]). The robot tries to move to the 
bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either 
down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that
the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach
the bottom-right corner.

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
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/unique-paths-ii/solutions/317710/jian-ji-biao-ge-jie-shi-dong-tai-gui-hua-dpsi-lu-f/

    """
    def uniquePathsWithObstacles_v1(self, obstacleGrid: List[List[int]]) -> int:
        #新建矩阵版
        height, width = len(obstacleGrid),len(obstacleGrid[0])
        store = [[0]*width for i in range(height)]

        #从上到下，从左到右
        for m in range(height):#每一行
            for n in range(width):#每一列
                if not obstacleGrid[m][n]: #如果这一格没有障碍物
                    if m == n == 0: #或if not(m or n)
                        store[m][n] = 1
                    else:
                        a = store[m-1][n] if m!=0 else 0 #上方格子
                        b = store[m][n-1] if n!=0 else 0 #左方格子
                        store[m][n] = a+b
        return store[-1][-1]


    def uniquePathsWithObstacles_v2(self, obstacleGrid: List[List[int]]) -> int:
        #原矩阵版
        height, width = len(obstacleGrid),len(obstacleGrid[0])

        #从上到下，从左到右
        for m in range(height):#每一行
            for n in range(width):#每一列
                if obstacleGrid[m][n]: #如果这一格有障碍物
                    obstacleGrid[m][n] = 0
                else:
                    if m == n == 0: #或if not(m or n)
                        obstacleGrid[m][n] = 1
                    else:
                        a = obstacleGrid[m-1][n] if m!=0 else 0 #上方格子
                        b = obstacleGrid[m][n-1] if n!=0 else 0 #左方格子
                        obstacleGrid[m][n] = a+b
        return obstacleGrid[-1][-1]


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

