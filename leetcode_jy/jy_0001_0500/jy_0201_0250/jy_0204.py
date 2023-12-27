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
title_jy = " Count-Primes(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer `n`, return the number of prime numbers that are strictly less than `n`.

 

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
 

Constraints:
0 <= n <= 5 * 10^6
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/count-primes/solutions/36629/pythonzui-you-jie-fa-mei-you-zhi-yi-liao-ba-by-bru/
    """
    def countPrimes_v1(self, n: int) -> int:
        """
        求n以内的所有质数个数（纯python代码）
        """
        # 最小的质数是 2
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0   # 0和1不是质数，先排除掉

        # 埃式筛，把不大于根号 n 的所有质数的倍数剔除
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)


    
n = 10
res = Solution().countPrimes_v1(n)
# jy: 4
print(res)


n = 0
res = Solution().countPrimes_v1(n)
# jy: 0
print(res)


n = 1
res = Solution().countPrimes_v1(n)
# jy: 0
print(res)
    