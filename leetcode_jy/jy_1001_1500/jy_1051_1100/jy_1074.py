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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Number-of-Submatrices-That-Sum-to-Target(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a matrix and a target, return the number of non-empty submatrices that sum to target.
A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:
Input: matrix = [[904]], target = 0
Output: 0


Constraints:
1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
"""

import collections
from typing import List


class Solution:
    """
在 363. Max Sum of Rectangle No Larger Than K 的基础上运用 1. Two Sum;
    """
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) \
            -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        count = 0

        for i in range(m):
            column_sum = [0] * n

            for j in range(i, m):
                mapping = collections.defaultdict(int)
                mapping[0] = 1
                sum_so_far = 0

                for column in range(n):
                    column_sum[column] += matrix[j][column]
                    sum_so_far += column_sum[column]
                    count += mapping[sum_so_far - target]
                    mapping[sum_so_far] += 1

        return count



