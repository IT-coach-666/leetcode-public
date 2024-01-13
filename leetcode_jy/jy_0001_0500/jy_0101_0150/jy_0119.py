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
title_jy = "Pascals-Triangle-II(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = "相似题: 0018"


"""
Given an integer `rowIndex`, return the rowIndex-th (0-indexed) row of the
Pascal's triangle. In Pascal's triangle, each number is the sum of the two
numbers directly above it.


Example 1:
Input: rowIndex = 3
Output: [1, 3, 3, 1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1, 1]


Constraints:
0 <= rowIndex <= 33

Follow up:
Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

class Solution:
    """
解法 1: 在 0118 (Pascals-Triangle) 的基础上, 先构造出 rowIndex + 1 行的杨
辉三角, 然后返回最后一行的数字
    """
    def getRow_v1(self, rowIndex: int) -> List[int]:
        triangle = self._generate(rowIndex + 1)
        return triangle[rowIndex]

    def _generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle.append(row)
        return triangle


    """
解法 2: 参考 0118 中的解法 2
    """
    def getRow_v2(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        ls_prev = [1]
        while len(ls_prev) < rowIndex + 1:
            ls_prev = [a + b for a, b in zip([0] + ls_prev, ls_prev + [0])]
        return ls_prev


    """
解法 3: 优化解法 1

题目中要求使用 O(rowIndex) 的内存空间, 解法 1 不能满足

杨辉三角的每一行都由上一行构造而来, 所以并不需要一个二维数组, 使用一维数
组保留上一行的结果即可

和 0118 (Pascals-Triangle) 不同的是, 这次构造杨辉三角的行时需要从右往左
构造, 因为在使用一维数组的情况下, 如果从左往右构造, 即: 
row[i] = row[i-1] + row[i]
row[i+1] = row[i] + row[i+1]

在更新 row[i+1] 时, row[i] 已经被替换了, 不再是原来的 row[i]; 从右往左构
造则可避免此问题 (即先构造 row[i+1] 再构造 row[i])
    """
    def getRow_v3(self, rowIndex: int) -> List[int]:
        # jy: 第 n 行共有 n 个元素; 下标为 rowIndex 的行即 rowIndex + 1 行
        row = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            # jy: 从右往左构造;【trick】
            for j in range(i, -1, -1):
                if j == 0 or j == i:
                    row[j] = 1
                else:
                    row[j] = row[j-1] + row[j]
            #print(row)
        return row


    """
解法 4: 对解法 1 进行改写, 维护上一一行结果列表, 空间复杂度满足题目要求
    """
    def getRow_v4(self, rowIndex: int) -> List[int]:

        ls_prev = []
        for i in range(rowIndex + 1):
            ls_cur = []
            for j in range(i+1):
                if j == 0 or j == i:
                    ls_cur.append(1)
                else:
                    ls_cur.append(ls_prev[j-1] + ls_prev[j])
            ls_prev = ls_cur
        return ls_prev


rowIndex = 3
res = Solution().getRow_v1(rowIndex)
# jy: [1, 3, 3, 1]
print(res)


rowIndex = 0
res = Solution().getRow_v2(rowIndex)
# jy: [1]
print(res)


rowIndex = 1
res = Solution().getRow_v3(rowIndex)
# jy: [1, 1]
print(res)


