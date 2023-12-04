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
title_jy = "divide-two-integers(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two integers `dividend` and `divisor`, divide two integers without
using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its 
fractional part. For example, 8.345 would be truncated to 8, and -2.7335
would be truncated to -2.

Return the quotient(商) after dividing `dividend` by `divisor`.


Note: Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem,
if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and
if the quotient is strictly less than -2^31, then return -2^31.

 

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
"""


class Solution:
    """
解法 1: 列竖式算除法
    """
    def divide_v1(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        # jy: 把除数不断左移, 直到它大于被除数
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                # jy: 这里的移位运算是把二进制 (第 count+1 位上的 1) 转换
                #     为十进制
                result += 1 << count
                dividend -= divisor
        if sign: result = -result
        return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1 


dividend = 10
divisor = 3
res = Solution().divide_v1(dividend, divisor)
# jy: 3
print(res)


dividend = 7
divisor = -3
res = Solution().divide_v1(dividend, divisor)
# jy: -2
print(res)



