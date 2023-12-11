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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Island-Perimeter(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given ``row x col grid`` representing a map where grid[i][j] = 1 represents
land and grid[i][j] = 0 represents water. Grid cells are connected horizontally/vertically
(not diagonally). The grid is completely surrounded by water, and there is exactly one
island (i.e., one or more connected land cells). The island doesn't have "lakes",
meaning the water inside isn't connected to the water around the island. One cell is
a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.


Example 1:  https://www.yuque.com/frederick/dtwi9g/ptp76y
Input: grid = [
[0,1,0,0],
[1,1,1,0],
[0,1,0,0],
[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4


Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
"""




from typing import List



class Solution:
    """
直接遍历
1) 如果遇到 1, 则先将周长加 4, 如果格子上方也是1, 则周长需要减去两个格子重
合的边, 即 2, 如果格子左边也是 1, 同理;
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # jy: m 行 n 列;
        m, n = len(grid), len(grid[0])
        # jy: island 的周长统计
        perimeter = 0
        # jy: 遍历二维矩阵;
        for i in range(m):
            for j in range(n):
                # jy: 如果坐标位置的值为 1, 则周长先加 4, 再判断:
                #    a) 格子的上方是否也为 1, 如果是则周长减 2;
                #    b) 格子的左侧是否也为 1, 如果是则周长减 2;
                #    注意:
                #    version-1: 只需要判断左上即可, 因为右下方的如果有重叠的, 会在遍历到相应元素时也成为那个元素的左上;
                #    version-2: 也可以判断右下, 不判断左上, 因为左上重叠的部分也将会是某个位置的右下;
                if grid[i][j] == 1:
                    perimeter += 4
                    # version-1: 只判断左上版本 ================================================
                    """
                    # jy: 由于要判断上方, 需确保上方位置存在, 即确保 i > 0 才能确保 i-1 对应的下标为有效的上方;
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    # jy: 由于要判断左方, 需确保左方位置存在, 即确保 j > 0 才能确保 j-1 对应的下标为有效的左方;
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
                    """

                    # version-2: 只判断右下版本 ================================================
                    if i+1 < m and grid[i+1][j] == 1:
                        perimeter -= 2
                    # jy: 由于要判断左方, 需确保左方位置存在, 即确保 j > 0 才能确保 j-1 对应的下标为有效的左方;
                    if j+1 < n and grid[i][j+1] == 1:
                        perimeter -= 2


        return perimeter


grid = [
[0,1,0,0],
[1,1,1,0],
[0,1,0,0],
[1,1,0,0]]
# Output: 16
res = Solution().islandPerimeter(grid)
print(res)


grid = [[1]]
# Output: 4
res = Solution().islandPerimeter(grid)
print(res)


grid = [[1,0]]
# Output: 4
res = Solution().islandPerimeter(grid)
print(res)


