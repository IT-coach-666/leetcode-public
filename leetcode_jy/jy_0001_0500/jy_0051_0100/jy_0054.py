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
tag_jy = "基于矩阵 4 个边界指针实现 | IMP | 相似题: 0059"


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


Constraints:
1) m == matrix.length
2) n == matrix[i].length
3) 1 <= m, n <= 10
4) -100 <= matrix[i][j] <= 100
"""


class Solution:
    """
解法 1: 顺时针顺序一层层遍历 (不太好理解)

共需遍历 math.ceil(min(m, n) / 2) 圈, 以示例 2 中的数组为例进行思考
[ [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]]
    """
    def spiralOrder_v1(self, matrix: List[List[int]]) -> List[int]:
        import math

        if not matrix:
            return []
        result = []
        # jy: m 行 n 列
        m, n = len(matrix), len(matrix[0])
        # jy: 共需遍历 math.ceil(min(m, n) / 2) 圈
        for i in range(math.ceil(min(m, n)/2)):
            # jy: 遍历第 i 圈的上面一排 (从左往右)
            for j in range(i, n-i):
                result.append(matrix[i][j])

            # jy: 遍历第 i 圈的右边一列(从上往下)
            for j in range(i+1, m-i):
                result.append(matrix[j][n-i-1])

            # jy: 遍历第 i 圈的下面一排 (从右往左, 因此需倒序遍历)
            #     注意: 如果去除该 if 判断, 则示例 2 中的矩阵的输出结果为:
            #     [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7, 6] (最后多了一个 6)
            if i != m-i-1:
                for j in range(n-i-2, i-1, -1):
                    result.append(matrix[m-i-1][j])

            # jy: 遍历第 i 圈的左边一列 (从下往上, 因此需倒序遍历)
            #     注意: 如果去除该 if 判断, 则 matrix = [[7], [9], [6]] 时
            #     输出结果为: [7, 9, 6, 9]
            if i != n-i-1:
                for j in range(m-i-2, i, -1):
                    result.append(matrix[j][i])
        return result


    """
解法 2: 基于 4 个边界指针进行遍历, 时间复杂度 O(m * n), 空间复杂度 O(1)

顺时针打印矩阵的顺序是 "从左向右、从上向下、从右向左、从下向上" 循环,
因此可设定矩阵的 "左、上、右、下" 四个边界, 模拟以上矩阵遍历顺序

算法流程:
1) 当 matrix 为空时, 直接返回空列表 []
2) 初始化矩阵 左、右、上、下 四个边界 left、right、top、bottom、结果列表 ls_res
3) 循环打印: "从左向右、从上向下、从右向左、从下向上" 四个方向循环打印
   a) 根据边界打印, 将元素按顺序添加至列表 ls_res 尾部
   b) 边界向内收缩 1 (代表已被打印)
   c) 判断边界是否相遇 (是否打印完毕), 若打印完毕则跳出
4) 返回 res 即可
    """
    def spiralOrder_v2(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        # jy: 初始化边界下标
        left, right, top, bottom, ls_res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            # jy: 从左到右打印 (left to right)
            for i in range(left, right + 1): 
                ls_res.append(matrix[top][i])
            # jy: 打印完一圈之后, top 边界向内收缩 1 (top 往下走)
            top += 1
            # jy: 如果收缩后 top 边界大于 bottom 边界, 则退出循环
            if top > bottom:
                break

            # jy: 从上到下打印 (top to bottom), 打印完后 right 边界向内收缩 1
            #     (right 往左走), 如果收缩后 left 边界大于 right, 则退出循环
            for i in range(top, bottom + 1):
                ls_res.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            # jy: 从右到左打印 (right to left), 打印完后 bottom 边界向内收缩 1
            #     (bottom 往上走), 如果收缩后 top 边界大于 bottom, 则退出循环
            for i in range(right, left - 1, -1):
                ls_res.append(matrix[bottom][i]) 
            bottom -= 1
            if top > bottom:
                break

            # jy: 从下到上打印 (bottom to top), 打印完后 left 边界向内收缩 1
            #     (left 往右走), 如果收缩后 left 边界大于 right, 则退出循环
            for i in range(bottom, top - 1, -1):
                ls_res.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return ls_res


    """
解法 3: 基于 zip 内置函数与列表倒序实现
    """
    def spiralOrder_v3(self, matrix: List[List[int]]) -> List[int]:
        """
        以如下矩阵为例进行说明:
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9,10,11,12]]
        """
        result = []
        while matrix:
            # jy: 取出矩阵第一行; 注意: [1, 2, 3, 4] 不能直接与 (8, 12) 相加,
            #     即如果 a = [1, 2, 3, 4], b = (8, 12), 则执行 a = a + b 时会
            #     报错, 但执行 a += b 时可正常执行, 且结果为: [1, 2, 3, 4, 8, 12] 
            result += matrix.pop(0)
            # jy: 旋转矩阵, 当 matrix 为如下矩阵时:
            #     [[5, 6, 7, 8],
            #      [9,10,11,12]]
            #     list(zip(*matrix)) 的结果为:
            #     [(5, 9), (6, 10), (7, 11), (8, 12)]
            #     倒序后结果为: 
            #     [(8, 12), (7, 11), (6, 10), (5, 9)]
            # jy: 当 matrix 为 [(7, 11), (6, 10), (5, 9)] 时:
            #     list(zip(*matrix)) 的结果为:
            #     [(7, 6, 5), (11, 10, 9)]
            #     倒序后结果为:
            #     [(11, 10, 9), (7, 6, 5)]
            matrix = list(zip(*matrix))[::-1] 
        return result



matrix = [ 
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9,10,11,12]]
res = Solution().spiralOrder_v1(matrix)
# jy: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(res)


matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]
res = Solution().spiralOrder_v2(matrix)
# jy: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(res)


matrix = [
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9,10,11,12]]
res = Solution().spiralOrder_v3(matrix)
# jy: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(res)
