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
title_jy = "Search-a-2D-Matrix-II(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Write an efficient algorithm that searches for a value in an ``m * n`` matrix.
This matrix has the following properties:
1) Integers in each row are sorted in ascending from left to right.
2) Integers in each column are sorted in ascending from top to bottom.


Example:
[ [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]
Given target = 5, return true.
Given target = 20, return false.
"""


from typing import List


class Solution:
    """
双指针法(同 074_Search-a-2D-Matrix.py 的解法 3): 一个指针指向第一行, 另一个指针指向最后一列
1) 如果当前值等于 target, 则返回 true
2) 如果当前值大于 target, 则列指针向左移动一列
3) 如果当前值小于 target, 则行指针向下移动一行
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        # jy: 双指针, 初始时, row 指向第一行, column 指向第一列;
        row, column = 0, n-1

        while row < m and column >= 0:
            # jy: 如果对应的行列指针的值为目标值, 返回 True;
            if matrix[row][column] == target:
                return True
            # jy: 如果行列指针的值大于目标值, 则列指针向左移动一列;
            elif matrix[row][column] > target:
                column -= 1
            # jy: 如果行列指针的值小于目标值, 则行指针向右移动一列;
            else:
                row += 1

        return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]


target = 5
# return true.
res = Solution().searchMatrix(matrix, target)
print(res)

target = 20
# return false.
res = Solution().searchMatrix(matrix, target)
print(res)



