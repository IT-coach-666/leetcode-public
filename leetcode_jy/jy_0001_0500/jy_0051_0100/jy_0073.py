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
title_jy = "Set-Matrix-Zeroes(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Example 1:
Input:
[ [1,1,1],
  [1,0,1],
  [1,1,1]]
Output:
[ [1,0,1],
  [0,0,0],
  [1,0,1]]

Example 2:
Input:
[ [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]]
Output:
[ [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]]


Follow up:
• A straight forward solution using O(m*n) space is probably a bad idea.
• A simple improvement uses O(m+n) space, but still not the best solution.
• Could you devise a constant space solution?
"""



from typing import List
import numpy as np
class Solution:
    """
解法1: 题目本身比较简单, 遍历矩阵, 遇到 0 则将该行, 该列的数都置为 0, 需要注意置为 0 的
过程中原来就存在矩阵中的 0, 为了区别这些数, 额外开辟了个相同大小的矩阵来保存已经被访问过的 0;
    """
    def setZeroes_v1(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        # jy: m 行 n 列;
        m, n = len(matrix), len(matrix[0])
        # jy: 将当前遍历到为 0 的位置设置为 True, 并将该位置的行和列中原先不为 0, 但现在已设置
        #    为 0 的位置设置为 True; 原先为 0 且还没遍历到的位置对应的值仍为 False;
        visited = [[False for _ in range(n)] for _ in range(m)]
        # jy: 遍历矩阵;
        for i in range(m):
            for j in range(n):
                # jy: 如果遍历到数值 0 且该数值之前没有被处理(visited 中的值为 False), 则设置
                #    相应的行列为 0, 且行列中原先不为 0 的位置对应的 visited 值为 True, 原先
                #    就为 0 的则其对应的 visited 人仍为 False;
                if matrix[i][j] == 0 and not visited[i][j]:
                    # jy: 设置第 j 列为 0, 如果原先就为 0 了, 则其对应的位置的 visited 值仍为 False
                    for k in range(m):
                        #if matrix[k][j] != 0:
                        if k != i and matrix[k][j] != 0:
                            matrix[k][j] = 0
                            visited[k][j] = True
                    # jy: 设置第 i 行为 0, 如果原先就为 0 了, 则其对应的位置的 visited 值仍为 False
                    for k in range(n):
                        #if matrix[i][k] != 0:
                        if k != j and matrix[i][k] != 0:
                            matrix[i][k] = 0
                            visited[i][k] = True
                    # jy: 由于以上两个 for 循环中都有 k != i 和 k != j, 所以此处需要补充设置(否则可
                    #    不设置);
                    visited[i][j] = True

    """
解法2: 为了减少额外空间的消耗, 可以首先计算出哪些列, 哪些行需要置为 0, 然
后再遍历一次矩阵将需要置为 0 的数字置为 0;
    """
    def setZeroes_v2(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        # jy: m 行 n 列;
        m, n = len(matrix), len(matrix[0])
        rows, columns = set(), set()
        # jy: 遍历矩阵, 将需要设置为 0 的行列放入 rows 和 columns 集合中;
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        # jy: 遍历矩阵的行和列, 如果行或列在相应的集合中, 则将矩阵的对应值置为 0;
        for i in range(m):
            for j in range(n):
                if i in rows or j in columns:
                    matrix[i][j] = 0

    """
解法3: 最后题目要求算法的空间复杂度是常数级别, 这里巧妙的将解法 2 中记录哪些行, 列需要
置为 0 的信息放在了矩阵的第一行和第一列中, 由于第一行, 第一列的信息被修改, 所以需要额
外两个变量来标记最后第一行, 第一列是否都要置为0;
    """
    def setZeroes_v3(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        # jy: m 行 n 列;
        m, n = len(matrix), len(matrix[0])
        is_first_row_zero = False
        is_first_column_zero = False

        # jy: 遍历矩阵, 如果矩阵的对应位置值为 0, 如果是第 1 行中的, 表明第 1 行要全置为 0;
        #    如果是第 1 列中的, 则表明第 1 列要全置为 0; 并将第 i 行是否需要置为 0 标记在
        #    第 i 行的第 1 个元素中; 同理, 第 j 列是否需要置为 0 标记在第 j 列的第 1 个元素中;
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        is_first_row_zero = True
                    if j == 0:
                        is_first_column_zero = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # jy: 遍历矩阵, 如果该行或列的第一个元素为 0, 则表明矩阵的该位置需要置为 0;
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if is_first_row_zero:
            for i in range(n):
                matrix[0][i] = 0
        if is_first_column_zero:
            for i in range(m):
                matrix[i][0] = 0

    """
简化 setZeroes_v3 中的代码结构;
    """
    def setZeroes_v4(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        is_first_row_zero = True if 0 in matrix[0][:] else False
        is_first_column_zero = True if 0 in matrix[:][0] else False

        # jy: 找出需要置为 0 的行和列, 并将需要置为 0 的行或列的第一个元素置为 0;
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # jy: 遍历矩阵, 如果相应位置的行或列的第一个元素为 0, 表明该位置需要置为 0;
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # jy: 首行或首列置为 0
        if is_first_row_zero:
            matrix[0][:] = [0] * n    # jy: 只有行可以这么赋值;
            #for i in range(n):
            #    matrix[0][i] = 0
        if is_first_column_zero:
            #matrix[:][0] = [0] * m   # jy: 列不可以这么赋值, 因为其是列表搭建而成的(非真正矩阵类型)
            print(matrix[:][0])
            for i in range(m):
                matrix[i][0] = 0



matrix =\
[ [1,1,1],
  [1,0,1],
  [1,1,1]]
Output =\
[ [1,0,1],
  [0,0,0],
  [1,0,1]]

res = Solution().setZeroes_v3(matrix)
print(" res: \n", np.array(matrix), "\n expected: \n", np.array(Output))

print(" ======================= ")
matrix =\
[ [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]]
Output =\
[ [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]]

res = Solution().setZeroes_v1(matrix)
print(" res: \n", np.array(matrix), "\n expected: \n", np.array(Output))

print(" ======================= ")
matrix =\
[ [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]]
Output =\
[ [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]]
res = Solution().setZeroes_v2(matrix)
print(" res: \n", np.array(matrix), "\n expected: \n", np.array(Output))


print(" ======================= ")
matrix =\
[ [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]]
Output =\
[ [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]]
res = Solution().setZeroes_v4(matrix)
print(" res: \n", np.array(matrix), "\n expected: \n", np.array(Output))


