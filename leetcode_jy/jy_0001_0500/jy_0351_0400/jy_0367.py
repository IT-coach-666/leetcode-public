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
title_jy = "Valid-Perfect-Square(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false
"""


class Solution:
    """
解法1: 这道题和 Sqrt(x) 类似, 使用二分法求解;
    """
    def isPerfectSquare_v1(self, num: int) -> bool:
        low, high = 0, num

        while low <= high:
            middle = (low + high) // 2
            square = middle * middle

            if square == num:
                return True
            elif square > num:
                high = middle - 1
            else:
                low = middle + 1

        return False


    """
解法2: 利用了一个数学性质, 如果一个数 n 是完全平方数, 那么 n = 1 + 3 + 5 + ... + (2k - 1), k < n;
初始化 i 等于 1, 不停的从 num 减去 i, 同时 i 更新为下一个奇数, 如果最后 num 等于 0, 则说明 num 是
完全平方数;
    """
    def isPerfectSquare_v2(self, num: int) -> bool:
        i = 1

        while num > 0:
            num -= i
            i += 2

        return num == 0


num = 16
# Output: true
res = Solution().isPerfectSquare_v1(num)
print(res)

num = 14
# Output: false
res = Solution().isPerfectSquare_v2(num)
print(res)



