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
title_jy = "Flood-Fill(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
An image is represented by a 2-D array of integers, each integer representing the
pixel value of the image (from 0 to 65535). Given a coordinate (sr, sc) representing
the starting pixel (row and column) of the flood fill, and a pixel value ``newColor``,
"flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected
4-directionally to the starting pixel of the same color as the starting pixel, plus
any pixels connected 4-directionally to those pixels (also with the same color as
the starting pixel), and so on. Replace the color of all of the aforementioned pixels
with the newColor. At the end, return the modified image.


Example 1:
Input:
image = [
[1,1,1],
[1,1,0],
[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output:
[[2,2,2],
 [2,2,0],
 [2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.


Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""


from typing import List
from collections import deque


class Solution:
    """
解法1: 200_Number-of-Islands.py 的简化版;
    """
    def floodFill_v1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return []
        # jy: m 行 n 列;
        m, n = len(image), len(image[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        self._dfs(image, sr, sc, image[sr][sc], newColor, visited)

        return image

    def _dfs(self, image, row, column, current_color, new_color, visited):
        # jy: m 行 n 列
        m, n = len(image), len(image[0])
        # jy: 如果行或列超出范围, 或者对应的坐标已经更新(不再是原有值), 或者该位置已经被访问过,
        #    则直接返回, 终止递归;
        if row < 0 or row >= m or column < 0 or column >= n \
                or image[row][column] != current_color or visited[row][column]:
            return
        # jy: 将该位置值置为新值, 并设置已访问;
        visited[row][column] = True
        image[row][column] = new_color
        # jy: 遍历与当前位置相邻的四个方向, 不断将相邻且值为原值的位置更新为新值;
        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            self._dfs(image, row + direction[0], column + direction[1], current_color, new_color, visited)



    """
解法2: 广度优先搜索版本;
    """
    def floodFill_v2(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return []
        # jy: m 行 n 列
        m, n = len(image), len(image[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        # jy: 获取指定位置的原值, 并将该位置设置为已访问, 且放入队列(放入队列的位置均认为
        #    是已访问的, 因为下一步就会访问)
        current_color = image[sr][sc]
        visited[sr][sc] = True
        queue = deque([(sr, sc)])

        while queue:
            # jy: 左侧出队, 获取位置坐标, 将该坐标的值更新为新值; 并遍历该位置坐标的相邻四个坐标,
            #    如果值与原值相同, 且没被访问过, 则将该坐标也入队, 并也设置为已访问(入队的均认为
            #    是已访问); 后续出队会为相应位置坐标设置为新值, 并把相邻的且值为原值的坐标继续入
            #    队, 不断循环;
            cell = queue.popleft()
            row, column = cell[0], cell[1]
            image[row][column] = newColor

            for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                next_row = row + direction[0]
                next_column = column + direction[1]

                if next_row < 0 or next_row >= m  or next_column < 0 or next_column >= n \
                        or image[next_row][next_column] != current_color or visited[next_row][next_column]:
                    continue

                queue.append((next_row, next_column))
                visited[next_row][next_column] = True

        return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
res = Solution().floodFill_v1(image, sr, sc, newColor)
print(res)


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
res = Solution().floodFill_v2(image, sr, sc, newColor)
print(res)


