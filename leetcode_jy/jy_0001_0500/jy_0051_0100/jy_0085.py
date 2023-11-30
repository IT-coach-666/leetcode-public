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
title_jy = "Maximal-Rectangle(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a ``rows x cols`` binary matrix filled with 0's and 1's, find the largest 
rectangle containing only 1's and return its area.


Example 1:   https://www.yuque.com/frederick/dtwi9g/olg7py
Input: matrix = [
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = []
Output: 0

Example 3:
Input: matrix = [["0"]]
Output: 0

Example 4:
Input: matrix = [["1"]]
Output: 1

Example 5:
Input: matrix = [["0","0"]]
Output: 0


Constraints:
rows == matrix.length
cols == matrix[i].length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""


from typing import List


class Solution:
    """
遍历每一行, 以当前行为基线, 计算向上每一列的和(如果基线处为 0, 则当前列和也为 0), 
即将问题转化为 084_Largest-Rectangle-in-Histogram.py
    """
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        # jy: m 行 n 列;
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        # jy: 遍历二维数组的每一行, 每遍历一行时计算每一列中当前行之上的所有列中与当所在
        #    列的 1 相邻的 1 的总和(如果当前行的所在列值为 0, 则为 0); 每遍历完一行后,
        #    求最大面积并更新;
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            max_area = max(max_area, self._get_max_area(heights))

        return max_area

    def _get_max_area(self, heights):
        """
        同 084_Largest-Rectangle-in-Histogram.py
        """
        stack = []
        max_area = 0
        length = len(heights)
        i = 0

        while i <= length:
            current_height = 0 if i == length else heights[i]
            if not stack or current_height >= heights[stack[-1]]:
                stack.append(i)
                i += 1

            else:
                high = heights[stack.pop()]
                width = i if not stack else i - 1 - stack[-1]
                max_area = max(max_area, high * width)

        return max_area


matrix = [
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]]
# Output: 6
res = Solution().maximalRectangle(matrix)
print(res)


matrix = []
# Output: 0
res = Solution().maximalRectangle(matrix)
print(res)


matrix = [["0"]]
# Output: 0
res = Solution().maximalRectangle(matrix)
print(res)


matrix = [["1"]]
# Output: 1
res = Solution().maximalRectangle(matrix)
print(res)


matrix = [["0","0"]]
# Output: 0
res = Solution().maximalRectangle(matrix)
print(res)



