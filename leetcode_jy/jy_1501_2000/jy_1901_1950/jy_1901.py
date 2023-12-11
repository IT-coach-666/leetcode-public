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
title_jy = "Find-a-Peak-Element-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.
Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].
You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

Example 1:    https://www.yuque.com/frederick/dtwi9g/gbrbp3

Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

Example 2:

Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.


Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 10^5
No two adjacent cells are equal.
"""

from typing import List


class Solution:
    """
解法1
直接搜索, 遍历矩阵, 判断四个方向的值, 如果当前位置的值大于四个方向的值则返回当前位置的坐标, 否则将坐标移动到四个位置中值最大的位置继续搜索;
    """
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        row, column = len(mat), len(mat[0])
        i, j = 0, column - 1
        visited = set()

        while 0 <= i < row and 0 <= j < column:
            if (i, j) in visited:
                break

            visited.add((i, j))

            up = -1 if i - 1 < 0 else mat[i - 1][j]
            down = -1 if i + 1 >= row else mat[i + 1][j]
            left = -1 if j - 1 < 0 else mat[i][j - 1]
            right = -1 if j + 1 >= column else mat[i][j + 1]
            current = mat[i][j]

            if current > up and current > down \
                    and current > left and current > right:
                return [i, j]

            max_value = max(up, down, left, right)

            if up == max_value:
                i -= 1
            elif down == max_value:
                i += 1
            elif left == max_value:
                j -= 1
            elif right == max_value:
                j += 1

        return [-1, -1]


from typing import List


class Solution:
    """
解法2
对列进行二分法, 对当前列的元素遍历每一行, 判断峰值可能在左半部分还是右半部分;
    """
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        row, column = len(mat), len(mat[0])
        left, right = 0, column

        while left <= right:
            middle = left + (right - left) # 2
            is_left = False

            for i in range(row):
                if i > 0 and mat[i - 1][middle] >= mat[i][middle]:
                    continue

                if middle > 0 and mat[i][middle - 1] >= mat[i][middle]:
                    is_left = True

                    continue

                if i + 1 < row and mat[i + 1][middle] >= mat[i][middle]:
                    continue

                if middle + 1 < column \
                        and mat[i][middle + 1] >= mat[i][middle]:
                    continue

                return [i, middle]

            if is_left:
                right = middle - 1
            else:
                left = middle + 1

        return [-1, -1]


