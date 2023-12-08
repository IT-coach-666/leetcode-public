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
tag_jy = ""


"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.


Example:
Input: 5
Output:
[    [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]]
"""


from typing import List
class Solution:
    """
直接循环按照定义构造即可
    """
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        # jy: 循环遍历行;
        for i in range(numRows):
            # jy: 用于存放每行的数值, 第 n 行有 n 个数值, i 代表行的 index, 第 i 行有 i+1 个元素;
            row = []
            for j in range(i+1):
                # jy: 如果是该行的第一个或者最后一个数值, 则为 1; 第一行中只会添加 1 个数值 1;
                if j == 0 or j == i:
                    row.append(1)
                # jy: 第一行只会添加数值 1, 并完成一个 for 循环往 triangle 中加入 row; 到此处
                #    else 逻辑时, i 是一个大于 0 的数值; 即当前行的当前元素为上一行的最近两个
                #    元素的和;
                else:
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle.append(row)
        return triangle


numRows = 5
res = Solution().generate(numRows)
print(res)


