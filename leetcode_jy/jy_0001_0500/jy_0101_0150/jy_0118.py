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
title_jy = "Pascals-Triangle(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = "基于定义 | 基于规律技巧 | 相似题: 0019"


"""
Given an integer `numRows`, return the first numRows of Pascal's triangle. 
In Pascal's triangle, each number is the sum of the two numbers directly
above it as shown:


Example 1:
Input: numRows = 5
Output:
[    [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
 

Constraints:
1 <= numRows <= 30
"""


class Solution:
    """
解法 1: 按定义循环构造即可
    """
    def generate_v1(self, numRows: int) -> List[List[int]]:
        ls_res = []
        # jy: 循环遍历行
        for i in range(numRows):
            # jy: 用于存放每行的数值, 第 n 行有 n 个数值 
            #     (i 代表行的 index, 第 i 行有 i+1 个元素)
            row = []
            for j in range(i+1):
                # jy: 如果是该行的第一个或最后一个数值, 则
                #     为 1 (第一行中只会添加 1 个数值 1)
                if j == 0 or j == i:
                    row.append(1)
                # jy: i 为 0 时 (即第一行) 内循环只会执行一次, 此
                #     时 row 为 [1], 因此执行到以下逻辑时, 确保 i
                #     是大于 0 的数值 (j 也同样大于 0), 因此以下的
                #     下标范围有效
                # jy: 基于杨辉三角的特点: 除了当前行的首尾数值为 1
                #     之外, 当前行的当前列的数值等于上一行的当前列
                #     和前一列的数值之和
                else:
                    row.append(ls_res[i-1][j-1] + ls_res[i-1][j])
            ls_res.append(row)
        return ls_res


    """
解法 2: 错位并逐个相加

当前一行只比上一行多一个元素, 且当前行元素等于上一行元素往后错一位再逐位相加
例如第 4 行为 [1, 3, 3, 1], 第 5 行的结果为:
第 4 行:    1 3 3 1 0
错 1 位:    0 1 3 3 1
第 5 行:    1 4 6 4 1

因此只要对最后一行单独处理: 最后一行首、尾分别添加一个零然后对应位置求和就可
以得到新的一行
    """
    def generate_v2(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        ls_res = [[1]]
        while len(ls_res) < numRows:
            newRow = [a + b for a, b in zip([0] + ls_res[-1], ls_res[-1] + [0])]
            ls_res.append(newRow)      
        return ls_res



numRows = 5
res = Solution().generate_v1(numRows)
print(res)


