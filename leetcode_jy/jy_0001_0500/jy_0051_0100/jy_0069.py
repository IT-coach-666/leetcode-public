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
tag_jy = ""


"""
Implement int sqrt(int x). Compute and return the square root of ``x``, where
``x`` is guaranteed to be a non-negative integer. Since the return type is an
integer, the decimal digits are truncated and only the integer part of the result
is returned.


Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated,
             2 is returned.
"""


class Solution:
    """
二分查找: 初始化 low = 0, high = x, 计算 middle 值:
1) 如果 middle 的平方大于 x, 则 high = middle - 1
2) 如果 middle 的平方小于 x, 则 low = middle + 1
3) 如果 middle 的平方等于 x, 则 直接返回 middle
最后返回 high (结束循环时, high < low, 因为题目要求的意思也是向下取整, 故不能返回 low, 因
为 low 是向上取整的结果)
    """
    def _sqrt_lower(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            # jy: 计算 middle 时不要简单的两数相加除以 2, 因为当两数大到一定程度时, 直接相加会
            #     溢出(尽管在 python 中不会有这种情况, 因为python 中支持的最大值很大)
            # middle = (low + high) // 2
            middle = low + (high - low) // 2
            square = middle * middle
            if square > x:
                high = middle - 1
            elif square < x:
                low = middle + 1
            else:
                return middle
        return high


x = 4
res = Solution()._sqrt_lower(x)
print(res)


x = 8
res = Solution()._sqrt_lower(x)
print(res)



