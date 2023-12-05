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
title_jy = "Search-a-2D-Matrix(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Write an efficient algorithm that searches for a value in an ``m x n`` matrix.
This matrix has the following properties:
1) Integers in each row are sorted from left to right.
2) The first integer of each row is greater than the last integer of the previous row.


Example 1:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]]
target = 3
Output: true

Example 2:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]]
target = 13
Output: false
"""


from typing import List


class Solution:
    """
解法1: 使用两次二分查找, 第一次在矩阵的第一列中查找比 target 小的最大的数或
等于 target 值的所在行号, 如果该行的第1个数值不为 target 则在该行中使用二分
查找搜索 target;
    """
    def searchMatrix_v1(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        # jy: m 行 n 列;
        m, n = len(matrix), len(matrix[0])
        # jy: 在第一列中找出小于或等于 target 的数的最大值对应的下标(即所在的行号)
        row = self._binary_search([matrix[x][0] for x in range(m)], target)
        if matrix[row][0] == target:
            return True
        else:
            i = self._binary_search(matrix[row], target)
            return matrix[row][i] == target

    def _binary_search(self, numbers: List[int], target: int) -> int:
        """
        从列表中找出小于或等于 target 的最大值下标位置
        """
        low, high = 0, len(numbers)-1
        while low <= high:
            middle = low + (high-low) // 2
            if numbers[middle] == target:
                return middle
            # jy: 如果 middle 位置对应的值大于 target, 则目标值肯定位于 middle 左侧;
            elif numbers[middle] > target:
                high = middle - 1
            # jy: 如果 middle 位置对应的值小于 target, 则 low 加 1, 如果 low 加 1 后
            #     已经大于 high 了, 则表明 high 即为目标位置, 否则表明 low + 1 是更合
            #     适的目标值(更接近目标值);
            else:
                low = middle + 1
        # jy: 由于退出循环时 high < low, 故返回 high
        return high

    """
解法2: 另一种解法是在整个矩阵中进行二分搜索, 需要额外将 middle 转换为矩阵的坐标(技巧);
    """
    def searchMatrix_v2(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        # jy: m 行 n 列;
        m, n = len(matrix), len(matrix[0])
        # jy: 依据矩阵元素总个数确定 low, high 下标;
        low, high = 0, m * n - 1
        while low <= high:
            # jy: 依据 low, high 计算 middle;
            middle = low + (high-low) // 2
            # jy: 将 middle 转换为行列值(技巧), middle 整除列数值即为行下标, middle 对列
            #     数值取余即为列下标;
            row, column = middle // n, middle % n
            # jy: 通过行列下标定位 middle 对应的位置的值, 依据该值判断后续在是 middle 的
            #     左侧还是右侧查找;
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                high = middle - 1
            else:
                low = middle + 1
        return False

    """
解法3: 双指针法; 行指针指向第一行, 列指针指向最后一列, 行列指针对应下标即可定位当前值;
如果当前值等于 target, 则返回 true
如果当前值大于 target, 则列指针向左移动一列
如果当前值小于 target, 则行指针向下移动一行

JY: 复杂度最优;
    """
    def searchMatrix_v3(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        # jy: m 行 n 列;
        m, n = len(matrix), len(matrix[0])
        row, column = 0, n-1
        while row < m and column >= 0:
            if matrix[row][column] == target:
                return True
            # jy: 如果当前值小于 target, 则行往下移动, 否则列往左移动;
            if matrix[row][column] < target:
                row += 1
            else:
                column -= 1
        return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]]
target = 3
res = Solution().searchMatrix_v1(matrix, target)
print("res: ", res)

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]]
target = 13
res = Solution().searchMatrix_v2(matrix, target)
print("res: ", res)


res = Solution().searchMatrix_v3(matrix, target)
print("res: ", res)


