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
title_jy = "Fibonacci-Number(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such
that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0,   F(1) = 1
F(N) = F(N-1) + F(N-2), for N > 1.

Given N, calculate F(N).

Example 1:
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.


Example 3:
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Note:
0 ≤ N ≤ 30.
"""



class Solution:
    """
循环求解, 使用两个变量记录之前的两个值;
    """
    def fib_v1(self, N: int) -> int:
        if N <= 1:
            return N

        prev_prev = 0
        prev = 1
        current = 0

        for _ in range(2, N+1):
            current = prev_prev + prev
            prev_prev = prev
            prev = current

        return current


    def fib_v2(self, N):
        if N <=1:
            return N

        return self.fib_v2(N-1) + self.fib_v2(N-2)



res = Solution().fib_v1(2)
print(res)
res = Solution().fib_v2(2)
print(res)

res = Solution().fib_v1(3)
print(res)
res = Solution().fib_v2(3)
print(res)

res = Solution().fib_v1(4)
print(res)
res = Solution().fib_v2(4)


