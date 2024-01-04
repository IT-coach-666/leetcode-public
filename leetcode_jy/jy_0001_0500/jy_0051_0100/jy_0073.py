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
tag_jy = "逐位置遍历 + 数据结构技巧"


"""
Given an m x n integer matrix `matrix`, if an element is 0, set its entire
row and column to 0's. You must do it in place.


Example 1:
Input:
[[1, 1, 1],
 [1, 0, 1],
 [1, 1, 1]]
Output:
[[1, 0, 1],
 [0, 0, 0],
 [1, 0, 1]]

Example 2:
Input:
[[0, 1, 2, 0],
 [3, 4, 5, 2],
 [1, 3, 1, 5]]
Output:
[[0, 0, 0, 0],
 [0, 4, 5, 0],
 [0, 3, 1, 0]]


Constraints:
1) m == matrix.length
2) n == matrix[0].length
3) 1 <= m, n <= 200
4) -2^31 <= matrix[i][j] <= 2^31 - 1



Follow up:
1) A straight forward solution using O(m*n) space is probably a bad idea.
2) A simple improvement uses O(m+n) space, but still not the best solution.
3) Could you devise a constant space solution?
"""


class Solution:
    """
解法 1: 逐个位置遍历并设置

遍历矩阵, 遇到 0 则将该行、该列的数都置为 0

注意: 置为 0 的过程中需记录原来就为 0 的位置
    """
    def setZeroes_v1(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        # jy: m 行 n 列
        m, n = len(matrix), len(matrix[0])
        # jy: 初始化一个同样大小的矩阵, 用以记录 0 是否被处理过: 将为 0 的位
        #     置设置为 True, 并将该位置的行和列中原先不为 0 但现在已设置为 0
        #     的位置设置为 True; 原先为 0 的位置对应的值为 False
        visited = [[False for _ in range(n)] for _ in range(m)]
        # jy: 遍历矩阵;
        for i in range(m):
            for j in range(n):
                # jy: 如果当前位置为 0 且该位置没被处理 (visited 中该位置的值
                #     为 False), 则设置相应的行列为 0, 且行列中原先不为 0 的
                #     位置对应的 visited 该位置的值为 True, 原先就为 0 的位置
                #     则对应的 visited 仍为 False (表示原先的 0 还未被处理)
                if matrix[i][j] == 0 and not visited[i][j]:
                    # jy: 将第 j 列的非 0 值设置为 0, 并将 visited 中的该相应
                    #     位置的值设置为 True (表示该 0 值已经被处理完)
                    for k in range(m):
                        #if matrix[k][j] != 0:
                        if k != i and matrix[k][j] != 0:
                            matrix[k][j] = 0
                            visited[k][j] = True

                    # jy: 将第 i 行为的非 0 值设置为 0, 并将 visited 中的该相应
                    #     位置的值设置为 True (表示该 0 值已经被处理完)
                    for k in range(n):
                        #if matrix[i][k] != 0:
                        if k != j and matrix[i][k] != 0:
                            matrix[i][k] = 0
                            visited[i][k] = True
                    # jy: 由于以上两个 for 循环中都有 k != i 和 k != j, 所以此处
                    #     需要补充设置 visited 中当前 (i, j) 位置为 True, 表示该
                    #     位置的 0 已经被处理 (如果以上 for 循环中没有 k != i 或
                    #     k != j, 则在 for 循环中就已经设置了该位置, 此处可省略)
                    visited[i][j] = True

    """
解法 2: 优化解法 1 中的空间复杂度

先计算出需要置为 0 的列和行, 然后再遍历一次矩阵将相应的列和行置为 0
    """
    def setZeroes_v2(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        # jy: m 行 n 列
        m, n = len(matrix), len(matrix[0])
        rows, columns = set(), set()
        # jy: 遍历矩阵, 将需要设置为 0 的行和列分别放入 rows 和 columns
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        # jy: 再次遍历矩阵, 将指定的行和列设置为 0
        for i in range(m):
            for j in range(n):
                if i in rows or j in columns:
                    matrix[i][j] = 0

    """
解法 3: 优化解法 2 的空间复杂度至常数级

将解法 2 中需要置为 0 的行和列信息放在矩阵的第一行和第一列中; 由于第一行和第
一列的信息会被修改, 因此不能直接基于第一行或第一列中是否有 0 值来判断第一行或
第一列是否需应设置为 0, 所以需要额外两个变量来标记第一行和第一列是否都要置为 0
    """
    def setZeroes_v3(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        # jy: m 行 n 列
        m, n = len(matrix), len(matrix[0])
        # jy: is_first_row_zero 为 True 时表明第一行要置为 0
        is_first_row_zero = False
        # jy: is_first_column_zero 为 True 时表明第一列需要置为 0
        is_first_column_zero = False

        # jy: 遍历矩阵, 如果矩阵的对应位置值为 0, 如果是第 1 行中的, 表明第 1 行要全置为 0;
        #    如果是第 1 列中的, 则表明第 1 列要全置为 0; 并将第 i 行是否需要置为 0 标记在
        #    第 i 行的第 1 个元素中; 同理, 第 j 列是否需要置为 0 标记在第 j 列的第 1 个元素中;
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # jy: 如果该位置处于第一行, 表明第一行需要置为 0
                    if i == 0:
                        is_first_row_zero = True
                    # jy: 如果该位置处于第一列, 表明第一列需要置为 0
                    if j == 0:
                        is_first_column_zero = True
                    # jy: 表明第 i 行需要设置为 0
                    matrix[i][0] = 0
                    # jy: 表明第 j 列需要设置为 0
                    matrix[0][j] = 0

        # jy: 再次遍历矩阵, 将除第一行和第一列之外的其它行和列的相应位置设置为 0
        #     第一行和第一列是否置为 0 需要基于另外两个变量判断
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # jy: 如果 is_first_row_zero 为 True, 则将第一行设置为 0
        if is_first_row_zero:
            for i in range(n):
                matrix[0][i] = 0

        # jy: 如果 is_first_column_zero 为 True, 则将第一列设置为 0
        if is_first_column_zero:
            for i in range(m):
                matrix[i][0] = 0


    """
解法 4: 简化解法 3 中的代码
    """
    def setZeroes_v4(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        is_first_row_zero = True if 0 in matrix[0][:] else False
        is_first_column_zero = True if 0 in matrix[:][0] else False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

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



matrix = [
 [1, 1, 1],
 [1, 0, 1],
 [1, 1, 1]]
Solution().setZeroes_v1(matrix)
print("\n".join([" " + str(i) for i in matrix]))
"""
[[1, 0, 1],
 [0, 0, 0],
 [1, 0, 1]]
"""

matrix = [
 [0, 1, 2, 0],
 [3, 4, 5, 2],
 [1, 3, 1, 5]]
Solution().setZeroes_v2(matrix)
print(matrix)
"""
[[0, 0, 0, 0],
 [0, 4, 5, 0],
 [0, 3, 1, 0]]
"""


matrix = [
 [0, 1, 2, 0],
 [3, 4, 5, 2],
 [1, 3, 1, 5]]
Solution().setZeroes_v3(matrix)
print(matrix)
"""
[[0, 0, 0, 0],
 [0, 4, 5, 0],
 [0, 3, 1, 0]]
"""


matrix = [
 [0, 1, 2, 0],
 [3, 4, 5, 2],
 [1, 3, 1, 5]]
Solution().setZeroes_v4(matrix)
print(matrix)
"""
[[0, 0, 0, 0],
 [0, 4, 5, 0],
 [0, 3, 1, 0]]
"""

