# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
from typing import List
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Zigzag-Conversion(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "巧用 flag | 根据题目特点寻找技巧"



"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this (you may want to display this pattern in a fixed font for
better legibility):
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a
number of rows:
string convert(string s, int numRows);
 
字符串 s 是以 N 字形(Z 字形)为顺序存储的字符串, 目标是按行打印


Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
 

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


class Solution:
    """
解法1: 巧用 flag, 时间复杂度和空间复杂度均为 O(N)

设 n 行字符串分别为 s1, s2, ..., sn
容易发现: 按顺序遍历字符串 s 时，每个字符 c 在 N 字形中对应的行索引先
从 s1 增大至 sn, 再从 sn 减小至 s1, ... 如此反复

解决方案: 模拟这个行索引的变化, 在遍历 s 中把每个字符填到正确的行 res[i]

算法流程：
创建 n 行字符串, 初始值均为空串, 并初始化行索引以及其变动的方向标签; 按
顺序遍历字符串 s, 并将遍历的字符存放到指定行索引的所在行, 并基于行索引的
变化方向更新行索引(如果碰到第一行和最后一行, 则及时改变行索引的变化方向),
供存储下一个字符使用
    """
    def convert_v1(self, s: str, numRows: int) -> str:
        # jy: 如果行数小于 2, 直接返回原字符串即可
        if numRows < 2:
            return s
        # jy: 创建 n 行字符串(初始值均为空串)
        res = ["" for _ in range(numRows)]
        # jy: 初始化行索引和 flag (flag 的值表示行索引要减小/增大的幅度)
        #     flag 初始化为 -1, 表明行索引要减小 1, 当碰到第一行或最后一
        #     行时, 行索引的变化方向要作出改变
        i, flag = 0, -1
        for c in s:
            # jy: 先将当前字符放入行索引为 i 的行
            res[i] += c
            # jy: 碰到第一行或最后一行时, 及时调整行索引的变化方向
            if i == 0 or i == numRows - 1: 
                flag = -flag
            # jy: 计算下一个行索引的值, 用于确定下一个字符存放在哪一行
            i += flag
        return "".join(res)


s = "PAYPALISHIRING"
numRows = 3
res = Solution().convert_v1(s, numRows)
# jy: "PAHNAPLSIIGYIR"
print(res)

s = "PAYPALISHIRING"
numRows = 4
res = Solution().convert_v1(s, numRows)
# jy: "PINALSIGYAHRPI"
print(res)

s = "A"
numRows = 1
res = Solution().convert_v1(s, numRows)
# jy: "A"
print(res)


