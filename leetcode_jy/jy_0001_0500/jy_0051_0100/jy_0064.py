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
title_jy = "Minimum-Path-Sum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right, which minimizes the sum of all numbers along its path.

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
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""

class Solution:
    def minPathSum_v1(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:  
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]



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


