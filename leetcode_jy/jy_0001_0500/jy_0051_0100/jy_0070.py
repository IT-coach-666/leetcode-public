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
title_jy = "Climbing-Stairs(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct
ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""



class Solution:
    """
走到下一级台阶有两种可能, 一种是一步上来, 另一种是两步上来, 即 T(n) = T(n-1) + T(n-2), 初
始值 T(1) = 1, T(2) = 2, 循环求解即可;
    """
    def climbStairs_v1(self, n: int) -> int:
        if n <= 2:
            return n
        step = 0
        prev_prev, prev = 1, 2
        for i in range(2, n):
            step = prev_prev + prev
            prev_prev, prev = prev, step
        return step

    """
解法2: 递归求解;
    """
    def climbStairs_v2(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs_v2(n-1) + self.climbStairs_v2(n-2)


n = 8
res = Solution().climbStairs_v1(n)
print(res)


res = Solution().climbStairs_v2(n)
print(res)


