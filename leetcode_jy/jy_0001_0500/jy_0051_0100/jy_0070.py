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
tag_jy = "循环/迭代 | 递归 + 缓存"


"""
You are climbing a staircase. It takes `n` steps to reach the top. Each time
you can either climb 1 or 2 steps. In how many distinct ways can you climb to
the top?


Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
             1) 1 step + 1 step
             2) 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
             1) 1 step + 1 step + 1 step
             2) 1 step + 2 steps
             3) 2 steps + 1 step


Constraints:
1 <= n <= 45
"""



class Solution:
    """
解法 1: 循环/迭代

走到第 n 级台阶有两种可能:
1) 先走到第 n-1 阶, 然后一步上来
2) 先走到第 n-2 阶, 然后两步上来 

即 f(n) = f(n-1) + f(n-2), 初始值 f(1) = 1, f(2) = 2

由于求 f(n) 需要先求 f(n-1) 和 f(n-2), 即求后面的需要先把前面的求出来,
因此可从前不断往后循环迭代, 直到求解出 f(n)
    """
    def climbStairs_v1(self, n: int) -> int:
        if n <= 2:
            return n

        step = 0
        # jy: 已知 f(1) = 1, f(2) = 2
        prev_prev, prev = 1, 2
        # jy: 不断循环迭代求 f(3) 至 f(n)
        for i in range(3, n+1):
            step = prev_prev + prev
            prev_prev, prev = prev, step
        return step


    """
解法 2: 递归 (超时, 因为 n 比较大时, 很多子问题会不断重复计算)
    """
    def climbStairs_v2(self, n: int) -> int:
        """
        求登到第 n 阶台阶的所有方法数
        """
        # jy: 如果阶数小于 2 时, 方法数等同于阶数
        if n <= 2:
            return n
        # jy: 总共有 n 阶台阶, 每次可以往上踏一个或两个台阶, 因此登上第
        #     n 阶的方法数有以下两种:
        #     1) 登到第 n-1 阶, 让后往上再踏一阶
        #     2) 登到第 n-2 阶, 让后往上再踏两阶
        return self.climbStairs_v2(n-1) + self.climbStairs_v2(n-2)


    """
解法 3: 递归 + 缓存 (优化解法 2)
    """
    dict_ = {}
    def climbStairs_v2(self, n: int) -> int:
        if n <= 2:
            return n
        if n in self.dict_:
            return self.dict_[n]

        self.dict_[n-1] = self.climbStairs_v2(n-1)
        self.dict_[n-2] = self.climbStairs_v2(n-2)
        return self.dict_[n-1] + self.dict_[n-2]


n = 8
res = Solution().climbStairs_v1(n)
print(res)


res = Solution().climbStairs_v2(n)
print(res)


