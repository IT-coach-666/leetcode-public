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
tag_jy = "位运算 | 问题转换为 0084 | 相似题: 0084"



"""
Given a `rows x cols` binary `matrix` filled with 0's and 1's, find the 
largest rectangle containing only 1's and return its area.


Example 1: 示例图参考: https://www.yuque.com/it-coach/leetcode/bdsyqgsg9dx7wrnn
Input: matrix = [
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Example 4:
Input: matrix = [["0","0"]]
Output: 0


Constraints:
1) rows == matrix.length
2) cols == matrix[i].length
3) 1 <= row, cols <= 200
4) matrix[i][j] is '0' or '1'.
"""


class Solution:
    """
解法 1: 问题转换为 0084, 时间复杂度 O(m * n), 空间复杂度 O(n)

尝试以矩阵的每一行为基线, 并向上统计该行往上的列中相邻值为 1 的个数, 记录
到 heights 列表中, 即可将问题转化为 0084 (Largest-Rectangle-in-Histogram)

该问题同样可延伸为: 矩阵中值可以大于 1, 求数值最大的矩形
    """
    def maximalRectangle_v1(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        # jy: m 行 n 列
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        # jy: 遍历二维数组的每一行, 每遍历一行时累计该行往上的列中相邻值
        #     为 1 的个数, 并记录到 heights 列表中 (heights 列表记录了上
        #     一行及该行以上所有列中相邻值为 1 的统计信息, 即 heights[j]
        #     表示上一行的第 j 列中相邻的 1 的个数)
        #
        #    列的 1 相邻的 1 的总和(如果当前行的所在列值为 0, 则为 0); 每遍历完一行后,
        #    求最大面积并更新;
        for i in range(m):
            for j in range(n):
                # jy: 如果当前行的第 j 列的值为 "1", 则第 j 列当前行以上
                #     的行中, 累计的相邻 1 值为 heights[j] + 1; 如果当前
                #     行的第 j 列的值为 "0", 则该列往上的相邻的 "1" 为 0
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            max_area = max(max_area, self._get_max_area(heights))

        return max_area

    def _get_max_area(self, heights):
        """
        同 0084 (Largest-Rectangle-in-Histogram)
        """
        stack = []
        max_area = 0
        len_ = len(heights)
        i = 0

        while i <= len_:
            current_height = 0 if i == len_ else heights[i]

            if not stack or current_height >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                high = heights[stack.pop()]
                width = i if not stack else i - 1 - stack[-1]
                max_area = max(max_area, high * width)

        return max_area


    """
解法 2: 基于位运算 (新颖解法, 但时间复杂度并非最优)
    """
    def maximalRectangle_v2(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        # jy: 将每一行看作一个二进制数, 然后转化为一个整数
        nums = [int(''.join(row), base=2) for row in matrix]
        ans, N = 0, len(nums)
        # jy: 遍历所有行
        for i in range(N):
            j, num = i, nums[i]
            # jy: 将第 i 行, 连续的, 和接下来的所有行, 做与运算
            while j < N:
                # jy: 经过与运算后, num 转化为二进制中的 1, 表示从 i 到 j 行
                #     可以组成一个矩形的那几列
                num = num & nums[j]
                if not num:
                    break
                l, curnum = 0, num
                # jy: 这个循环最精彩: 每次循环将 curnum 和其左移一位的数做与
                #     运算最终的循环次数 l 表示, 最宽的有效宽度
                while curnum:
                    l += 1
                    curnum = curnum & (curnum << 1)
                ans = max(ans, l * (j - i + 1))
                j += 1
        return ans



matrix = [
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]]
res = Solution().maximalRectangle_v1(matrix)
# jy: 6
print(res)


matrix = [["0"]]
res = Solution().maximalRectangle_v1(matrix)
# jy: 0
print(res)


matrix = [["1"]]
res = Solution().maximalRectangle_v1(matrix)
# jy: 1
print(res)


matrix = [["0","0"]]
res = Solution().maximalRectangle_v1(matrix)
# jy: 0
print(res)

