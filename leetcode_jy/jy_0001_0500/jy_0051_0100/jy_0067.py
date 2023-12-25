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
title_jy = "Add-Binary(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "二进制加法运算 (逢二进一)"


"""
Given two binary strings `a` and `b`, return their sum as a binary string.


Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"


Constraints:
1) 1 <= a.length, b.length <= 10^4
2) `a` and `b` consist only of '0' or '1' characters.
3) Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    """
解法 1: 逐位相加
    """
    def addBinary_v1(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        m, n = len(a) - 1, len(b) - 1

        while m >= 0 or n >= 0:
            # jy: 当 m 或 n 中有一个小于 0, 但另一个还大于 0 时, 把小于 0 的
            #     那个对应的位作为 0 处理即可
            current_sum = carry + (int(a[m]) if m >= 0 else 0) + (int(b[n]) if n >= 0 else 0)
            # jy: 计算进位, 逢二进一
            carry = current_sum // 2
            # jy: 计算当前位的值, 并拼接上之前的计算结果
            result = str(current_sum % 2) + result
            # jy: 均往高位移动
            m -= 1
            n -= 1

        return result if carry == 0 else '1' + result


    """
解法 2: 基于内置函数 int 和 bin
    """
    def addBinary_v2(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


    """
解法 3: 类似解法 1, 先补齐后统一循环遍历
    """
    def addBinary_v3(self, a: str, b: str) -> str:
        d = len(b) - len(a)
        # jy: 如果 b 比 a 长, 则 d 为正数, 此时会往 a 前面补全 "0", 使得
        #     a 和 b 等长 (-d 为负数, "0" * -d 为 ""); a 比 b 长时同理
        a = "0" * d + a
        b = "0" * -d + b

        result, carry = "", 0
        # jy: 倒序遍历 a 和 b (即优先遍历低位), 将低位的相加结果不断右移
        for i, j in zip(a[::-1], b[::-1]):
            sum_ = int(i) + int(j) + carry
            result = str(sum_ % 2) + result
            carry = sum_ // 2
        return "1" + result if carry else result


    """
解法 4: 解法 1 的另一种写法
    """
    def addBinary_v4(self, a: str, b: str) -> str:
        result, carry = "", 0
        i, j = len(a) - 1, len(b) - 1
        while (i >= 0 or j >= 0 or carry):
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            result = str(carry % 2) + result
            carry //= 2
        return result


a = "11"
b = "1"
res = Solution().addBinary_v1(a, b)
# jy: "100"
print(res)


a = "1010"
b = "1011"
res = Solution().addBinary_v2(a, b)
# jy: "10101"
print(res)


a = "1010"
b = "1011"
res = Solution().addBinary_v3(a, b)
# jy: "10101"
print(res)


