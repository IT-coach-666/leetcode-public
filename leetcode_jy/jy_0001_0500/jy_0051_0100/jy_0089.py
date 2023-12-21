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
title_jy = "Gray-Code(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
An n-bit gray code sequence is a sequence of 2^n integers where:
1) Every integer is in the inclusive range [0, 2^n - 1],
2) The first integer is 0,
3) An integer appears no more than once in the sequence,
4) The binary representation of every pair of adjacent integers differs by
   exactly one bit, and
5) The binary representation of the first and last integers differs by
   exactly one bit.

Given an integer `n`, return any valid n-bit gray code sequence.

 

Example 1:
Input: n = 2
Output: [0, 1, 3, 2]
Explanation: The binary representation of [0, 1, 3, 2] is [00, 01, 11, 10].
               - 00 and 01 differ by one bit
               - 01 and 11 differ by one bit
               - 11 and 10 differ by one bit
               - 10 and 00 differ by one bit
             [0, 2, 3, 1] is also a valid gray code sequence, whose binary 
             representation is [00, 10, 11, 01].
               - 00 and 10 differ by one bit
               - 10 and 11 differ by one bit
               - 11 and 01 differ by one bit
               - 01 and 00 differ by one bit

Example 2:
Input: n = 1
Output: [0, 1]
 

Constraints:
1 <= n <= 16
"""

class Solution:
    """
解法 1: https://leetcode.cn/problems/gray-code/solutions/13637/gray-code-jing-xiang-fan-she-fa-by-jyd/
    """
    def grayCode_v1(self, n: int) -> List[int]:
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res




n = 2
res = Solution().grayCode_v1(n)
# jy: [0, 1, 3, 2]
print(res)


n = 1
res = Solution().grayCode_v1(n)
# jy: [0, 1]
print(res)


