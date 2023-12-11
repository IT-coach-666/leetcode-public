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
title_jy = "Ugly-Number(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.


Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 8
Output: true
Explanation: 8 = 2 × 2 × 2

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

Example 4:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are
             limited to 2, 3, and 5.


Constraints:
-2^31 <= n <= 2^31 - 1
"""


class Solution:
    """
不断对 n 以 [2, 3, 5] 整除, 最后判断 n 等于 1
    """
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i

        return n == 1


n = 6
# Output: true, Explanation: 6 = 2 × 3
res = Solution().isUgly(n)
print(res)


n = 8
# Output: true, Explanation: 8 = 2 × 2 × 2
res = Solution().isUgly(n)
print(res)


n = 14
# Output: false, Explanation: 14 is not ugly since it includes the prime factor 7.
res = Solution().isUgly(n)
print(res)


n = 1
# Output: true
res = Solution().isUgly(n)
print(res)


