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
title_jy = "Spiral-Matrix-II(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = "相似题: 0054"


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
解法 1: 参考 0054 中的解法 2
    """
    def generateMatrix_v1(self, n: int) -> [[int]]:
        left, right, top, bottom = 0, n-1, 0, n-1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num, max_num = 1, n * n
        while num <= max_num:
            for i in range(left, right + 1): 
                matrix[top][i] = num
                num += 1
            top += 1

            for i in range(top, bottom + 1): 
                matrix[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix


    """
解法 2: 解法 1 的改写 (完全参照 0054 的解法 2)
    """
    def generateMatrix_v2(self, n: int) -> List[List[int]]:
        left, right, top, bottom = 0, n-1, 0, n-1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        while True:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            if right < left:
                break

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            if bottom < top:
                break

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            if left > right:
                break
        return matrix


n = 3
res = Solution().generateMatrix_v1(n)
print(res)
"""
[[1, 2, 3],
 [8, 9, 4],
 [7, 6, 5]]
"""


n = 1
res = Solution().generateMatrix_v2(n)
print(res)
"""
[[1]]
"""

