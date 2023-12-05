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
title_jy = "Add-Binary(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two binary strings a and b, return their sum as a binary string.


Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"


Constraints:
1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    """
逐位相加;
    """
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        m, n = len(a) - 1, len(b) - 1

        while m >= 0 or n >= 0:
            current_sum = carry + (int(a[m]) if m >= 0 else 0) + (int(b[n]) if n >= 0 else 0)
            carry = current_sum // 2
            result = str(current_sum % 2) + result
            m -= 1
            n -= 1

        return result if carry == 0 else '1' + result


    """
JY: 逐位相加后判断;
    """
    def addBinary_jy(self, a: str, b: str) -> str:
        res = ""
        a_idx, b_idx = len(a)-1, len(b)-1
        carry = 0
        while a_idx >= 0 and b_idx >= 0:
            if carry == 0:
                if a[a_idx] == b[b_idx] == "1":
                    res = "0" + res
                    carry = 1
                elif a[a_idx] == b[b_idx] == "0":
                    res = "0" + res
                else:
                    res = "1" + res
            else:
                if a[a_idx] == b[b_idx] == "1":
                    res = "1" + res
                    carry = 1
                elif a[a_idx] == b[b_idx] == "0":
                    res = "1" + res
                    carry = 0
                else:
                    res = "0" + res
                    carry = 1
            a_idx -= 1
            b_idx -= 1

        if a_idx >=0 or b_idx >= 0:
            rest = a if a_idx >= 0 else b
            r_idx = a_idx if a_idx >= 0 else b_idx

            while r_idx >= 0:
                if carry == 1:
                    if rest[r_idx] == "1":
                        res = "0" + res
                        carry = 1
                    else:
                        res = "1" + res
                        carry = 0
                else:
                        res = rest[r_idx] + res
                r_idx -= 1

        if carry == 1:
            res = "1" + res

        return res


a = "11"
b = "1"
# Output: "100"
res = Solution().addBinary(a, b)
print(res)


a = "1010"
b = "1011"
# Output: "10101"
res = Solution().addBinary_jy(a, b)
print(res)


