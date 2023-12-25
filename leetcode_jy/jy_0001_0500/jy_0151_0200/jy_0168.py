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
title_jy = "Excel-Sheet-Column-Title(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer `columnNumber`, return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"
 

Constraints:
1 <= columnNumber <= 2^31 - 1
"""


class Solution:
    """
解法 1:
十进制 6 转二进制 110 的过程:
 2 |_ 6 _                       ^
    2|_ 3 _  ······ 0    |
     2|_ 1 _ ·······1    |
       |_ 0_ ·······1    |


这道题换句话说是十进制转 26 进制, 但有个难点: 如果 26 转成字母是多少?
 26|_ 26 _
    1 ··· 0
        
这里出现了 0, 但是我们 26 字母没有任何一个字母是表示 0, 所以我们可以从 商 借一个给余数
 26|_ 26 _
    0 ··· 26
    """
    def convertToTitle_v1(self, n: int) -> str:
        res = ""
        while n:
            n, y = divmod(n, 26) 
            if y == 0:
                n -= 1
                y = 26
            res = chr(y + 64) + res
        return res

    
    """
解法 2: 先让 n 减一
    """
    def convertToTitle_v2(self, n: int) -> str:
        res = ""
        while n:
            n -= 1
            n, y = divmod(n, 26) 
            res = chr(y + 65) + res
        return res

    
    """
解法 3: 递归
    """
    def convertToTitle_v3(self, n: int) -> str:
        return "" if n == 0 else self.convertToTitle_v3((n - 1) // 26) + chr((n - 1) % 26 + 65)

    

columnNumber = 1
res = Solution().convertToTitle_v1(columnNumber)
# jy: "A"
print(res)


columnNumber = 28
res = Solution().convertToTitle_v1(columnNumber)
# jy: "AB"
print(res)


columnNumber = 701
res = Solution().convertToTitle_v1(columnNumber)
# jy: "ZY"
print(res)
