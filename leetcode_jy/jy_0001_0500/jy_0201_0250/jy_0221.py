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
title_jy = "Maximal-Square(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1: 图示参考: https://www.yuque.com/it-coach/leetcode/kgvauwglk5amer88
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0
 

Constraints:
1) m == matrix.length
2) n == matrix[i].length
3) 1 <= m, n <= 300
4) matrix[i][j] is '0' or '1'.
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/maximal-square/solutions/237808/fen-xiang-yi-ge-bu-yong-dong-tai-gui-hua-cai-yong-/
    """
    def maximalSquare_v1(self, matrix: List[List[str]]) -> int:
        nums=[int(''.join(n),base=2) for n in matrix]  #步骤1：每一行当作二进制数
        res,n=0,len(nums)
        for i in range(n):   #步骤2：枚举所有的组合，temp存储相与的结果
            temp=nums[i]
            for j in range(i,n):
                temp&=nums[j]
                w=self.getWidth(temp)
                h=j-i+1
                res=max(res,min(w,h))
        return res*res

    def getWidth(self, num):  #步骤3：求一个数中连续最多的1
        w=0
        while num>0:
            num&=num<<1
            w+=1
        return w
    
    
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
res = Solution().maximalSquare_v1(matrix)
# jy: 4
print(res)



matrix = [["0","1"],["1","0"]]
res = Solution().maximalSquare_v1(matrix)
# jy: 1
print(res)



matrix = [["0"]]
res = Solution().maximalSquare_v1(matrix)
# jy: 0
print(res)

