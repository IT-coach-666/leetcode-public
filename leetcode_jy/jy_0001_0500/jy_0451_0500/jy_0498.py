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
title_jy = "Diagonal-Traverse(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an m x n matrix ``mat``, return an array of all the elements of the array in a diagonal order.


Example 1:  https://www.yuque.com/frederick/dtwi9g/gx5iig
Input: mat = [
[1,2,3],
[4,5,6],
[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [
[1,2],
[3,4]]
Output: [1,2,3,4]


Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
-10^5 <= mat[i][j] <= 10^5
"""


from typing import List


class Solution:
    """
解法 1(超时): 通过观察可得, 每条对角线上的元素的坐标之和等同于当前对角线的序号(从 0 开始),
所以遍历对角线的序号, 对于对角线序号 i, 在 [0, i] 范围内构造相应矩阵中的数字坐标 (m, n), 注
意当 i 是偶数时, (m, n) 计算后需要互相交换;
    """
    def findDiagonalOrder_v1(self, mat: List[List[int]]) -> List[int]:
        # jy: 如果二维列表为空, 则直接返回空结果;
        if not mat or not mat[0]:
            return []

        result = []
        row, column = len(mat), len(mat[0])
        # jy: 二维矩阵的右下角元素对应的下标数值之和为 (row + column - 2), 从 0 逐渐遍历至该值;
        for i in range(row + column - 1):
            for p in range(i+1):
                # jy: m 代表行下标, n 代表列下标, 同一对角线上的行和列下标之和为 i;
                m, n = p, i - p
                # jy: 如果 i 是偶数, 则变换行列下标值, 使得 p 由 0 递增至 i 时, 对应的 (m, n) 由对
                #    角线的左下至右上遍历; 如果 i 是奇数, 则当 p 由 0 递增至 i 时, 对应的 (m, n)
                #    由对角线的右上至左下遍历;
                if i & 1 == 0:
                    m, n = n, m
                # jy: 如果 m 或 n 超出下标范围, 则跳过当前循环;
                if m >= row or n >= column:
                    continue
                # jy: 遍历时逐个将数值加入到结果列表;
                result.append(mat[m][n])
        return result


    """
解法2: 事先计算好每条对角线上的元素, 构造返回结果时, 如果是偶数序号的对角
线, 则反转当前对角线上的元素;

JY: 相比于解法1, 该方法访问的二维列表位置均为有效位置, 减少了无效位置的遍历;
    """
    def findDiagonalOrder_v2(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        result = []
        row, column = len(mat), len(mat[0])
        diagonal_to_numbers = {}
        # jy: 遍历二维数组的行列下标, 下标之和相同的属于同一个对角线, 将其添加到字典中;
        #    字典的 key 为对角线的序号, value 为该对角线上的元素; 由于遍历时是从左到右,
        #    从上到下进行遍历, 故 value 对应的列表保存的都是对角线右上到左下方向的结果;
        #    因此, 当对角线编号为偶数时, 应该是对角线的左下至右上方向, 故对 value 值进行
        #    反转, 然后添加如 result 列表中;
        for i in range(row):
            for j in range(column):
                p = i + j
                if p not in diagonal_to_numbers:
                    diagonal_to_numbers[p] = []
                diagonal_to_numbers[p].append(mat[i][j])
        # jy: 依据对角线的编号由小到大逐个将对角线的结果加入 result 中;
        for i in sorted(diagonal_to_numbers.keys()):
            if i & 1 == 0:
                result += list(reversed(diagonal_to_numbers[i]))
            else:
                result += diagonal_to_numbers[i]

        return result



mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
res = Solution().findDiagonalOrder_v1(mat)
print(res)

mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
res = Solution().findDiagonalOrder_v2(mat)
print(res)


