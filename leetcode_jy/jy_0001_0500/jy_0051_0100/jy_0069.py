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
title_jy = "Sqrt_x(number)"
# jy: 记录不同解法思路的关键词
tag_jy = "二分查找 | IMP"


"""
Given a non-negative integer `x`, return the square root of `x` rounded down
to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.
 

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down
             to the nearest integer, 2 is returned.
 

Constraints:
0 <= x <= 2^31 - 1
"""


class Solution:
    """
解法 1: 二分查找

初始化 low = 0, high = x, 计算 middle 值:
1) 如果 middle 的平方大于 x, 则 high = middle - 1
2) 如果 middle 的平方小于 x, 则 low = middle + 1
3) 如果 middle 的平方等于 x, 则 直接返回 middle
    """
    def mySqrt_v1(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            # jy: 计算 middle 时不要简单的两数相加除以 2, 因为当两数大到一定程
            #     度时, 直接相加会溢出 (其它语言有溢出风险, python 中没有)
            middle = low + (high - low) // 2
            square = middle * middle
            if square > x:
                high = middle - 1
            elif square < x:
                low = middle + 1
            else:
                return middle
        # jy: 最后返回 high, 因为结束循环时, high < low, 而题目要求向下取整, 
        #     因此不能返回 low (low 是向上取整的结果)
        return high



    """
解法 2: 使用内置函数 int 和 math.sqrt (不符合题目要求)
    """
    def mySqrt_v2(self, x: int) -> int:
        import math

        num = math.sqrt(x)
        return int(num)


x = 4
res = Solution().mySqrt_v1(x)
print(res)


x = 8
res = Solution().mySqrt_v1(x)
print(res)



