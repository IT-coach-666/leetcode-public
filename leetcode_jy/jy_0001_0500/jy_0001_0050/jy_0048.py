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
title_jy = "rotate-image(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note: You have to rotate the image in-place, which means you have to modify the
input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix =
[ [1,2,3],
  [4,5,6],
  [7,8,9]]
rotate the input matrix in-place such that it becomes:
[ [7,4,1],
  [8,5,2],
  [9,6,3]]

Example 2:
Given input matrix =
[ [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]]
rotate the input matrix in-place such that it becomes:
[ [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]]
"""



from typing import List
import numpy as np
class Solution:
    """
从矩阵的最外层开始处理, 一共需要处理 n//2 层, 每一层对 matrix[i][i: n-i-1] 这一行的
数字依次进行四次移动, 如对顶点元素的操作:
1. 先暂存左上角的数字
2. 将左下角数字放到左上角
3. 将右下角数字放到左下角
4. 将右上角数字放到右下角
5. 将暂存的左上角数字放到右上角

jy: 即从外圈到内圈, 一圈圈地都顺时针旋转 90 度, 总共只有 n//2 圈;
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # jy: 不断旋转, 共需要旋转 n//2 圈;
        for i in range(n // 2):
            for j in range(i, n-i-1):
                # jy: 暂存左上角的数字
                temp = matrix[i][j]
                # jy: 将左下角数字放到左上角
                matrix[i][j] = matrix[n-1-j][i]
                # jy: 将右下角数字放到左下角
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                # jy: 将右上角数字放到右下角
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                # jy: 将暂存的左上角数字放到右上角
                matrix[j][n-1-i] = temp


matrix = \
[ [1,2,3],
  [4,5,6],
  [7,8,9]]
res = Solution().rotate(matrix)
print(np.array(matrix))

matrix = \
[ [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]]

res = Solution().rotate(matrix)
print(np.array(matrix))


