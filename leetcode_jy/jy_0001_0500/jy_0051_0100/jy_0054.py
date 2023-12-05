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
title_jy = "Spiral-Matrix(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a matrix of m x n elements (m rows, n columns), return all
elements of the matrix in spiral order.

Example 1:
Input:
[[ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Example 2:
Input:
[ [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
"""


import math
from typing import List
class Solution:
    """
按顺时针顺序一层层遍历即可, 一共有 math.ceil(min(m, n) / 2) 层;
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result = []
        # jy: m 行 n 列
        m, n = len(matrix), len(matrix[0])
        # jy: 顺时针层层遍历, 只需要遍历 math.ceil(min(m, n) / 2) 层;
        for i in range(math.ceil(min(m, n)/2)):
            # jy: 遍历第 i 层的上面一排(从左往右);
            for j in range(i, n-i):
                result.append(matrix[i][j])
            # jy: 遍历第 i 层的右边一列(从上往下);
            for j in range(i+1, m-i):
                result.append(matrix[j][n-i-1])
            # jy: 遍历第 i 层的下面一排(从右往左);
            #"""
            if i != m-i-1:
                for j in range(n-i-2, i-1, -1):
                    result.append(matrix[m-i-1][j])
            """
            for j in range(n-i-2, i-1, -1):
                result.append(matrix[m-i-1][j])
            """
            # jy: 遍历第 i 层的左边一列(从下往上)
            #"""
            if i != n-i-1:
                for j in range(m-i-2, i, -1):
                    result.append(matrix[j][i])
            """
            for j in range(m-i-2, i, -1):
                result.append(matrix[j][i])
            """
        return result

matrix = \
[ [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]]
expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
res = Solution().spiralOrder(matrix)
print(res)
print("Expected: ")
print(expected)

print("\n=======================\n")

matrix = \
[[ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
res = Solution().spiralOrder(matrix)
print(res)
print("Expected: ")
print(expected)

