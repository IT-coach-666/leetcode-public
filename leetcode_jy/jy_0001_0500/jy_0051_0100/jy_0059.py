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
title_jy = "Spiral-Matrix-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a positive integer `n`, generate an n x n matrix filled with elements
from 1 to n^2 in spiral order.

 
Example 1:
Input: n = 3
Output: [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]

Example 2:
Input: n = 1
Output: [[1]]
 

Constraints:
1 <= n <= 20
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/spiral-matrix-ii/solutions/12594/spiral-matrix-ii-mo-ni-fa-she-ding-bian-jie-qing-x/
初始化一个 n×n 大小的矩阵 mat，然后模拟整个向内环绕的填入过程：

定义当前左右上下边界 l,r,t,b，初始值 num = 1，迭代终止值 tar = n * n；
当 num <= tar 时，始终按照 从左到右 从上到下 从右到左 从下到上 填入顺序循环，每次填入后：
执行 num += 1：得到下一个需要填入的数字；
更新边界：例如从左到右填完后，上边界 t += 1，相当于上边界向内缩 1。
使用num <= tar而不是l < r || t < b作为迭代条件，是为了解决当n为奇数时，矩阵中心数字无法在迭代过程中被填充的问题。
最终返回 mat 即可。

    """
    def generateMatrix_v1(self, n: int) -> [[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1): # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1): # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1): # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1): # bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat


n = 3
res = Solution().generateMatrix_v1(n)
print(res)
"""
[[1, 2, 3],
 [8, 9, 4],
 [7, 6, 5]]
"""


n = 1
res = Solution().generateMatrix_v1(n)
print(res)
"""
[[1]]
"""

