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
title_jy = "Fraction-to-Recurring-Decimal(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 4, denominator = 333
Output: "0.(012)"
 

Constraints:
1) -2^31 <= numerator, denominator <= 2^31 - 1
2) denominator != 0
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/fraction-to-recurring-decimal/solutions/18788/ji-lu-yu-shu-by-powcai/
    """
    def fractionToDecimal_v1(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        res = []
        # 首先判断结果正负, 异或作用就是 两个数不同 为 True 即 1 ^ 0 = 1 或者 0 ^ 1 = 1
        if (numerator > 0) ^ (denominator > 0):
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        # 判读到底有没有小数
        a, b = divmod(numerator, denominator)
        res.append(str(a))
        # 无小数
        if b == 0:
            return "".join(res)
        res.append(".")
        # 处理余数
        # 把所有出现过的余数记录下来
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            # 余数前面出现过,说明开始循环了,加括号
            if b in loc:
                res.insert(loc[b], "(")
                res.append(")")
                break
            # 在把该位置的记录下来
            loc[b] = len(res)
        return "".join(res)

    
numerator = 1
denominator = 2
res = Solution().fractionToDecimal_v1(numerator, denominator)
# jy: "0.5"
print(res)


numerator = 2
denominator = 1
res = Solution().fractionToDecimal_v1(numerator, denominator)
# jy: "2"
print(res)


numerator = 4
denominator = 333
res = Solution().fractionToDecimal_v1(numerator, denominator)
# jy: "0.(012)"
print(res)