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
title_jy = "Multiply-Strings(number)"
# jy: 记录不同解法思路的关键词
tag_jy = "乘法运算技巧"


"""
Given two non-negative integers `num1` and `num2` represented as strings,
return the product of `num1` and `num2`, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the 
inputs to integer directly.

 

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:
1) 1 <= num1.length, num2.length <= 200
2) `num1` and `num2` consist of digits only.
3) Both `num1` and `num2` do not contain any leading zero, except the number
   0 itself.
"""


class Solution:
    """
解法 1: for 循环

模拟乘法, 两个数中每一位数相乘时乘上他们各自的进制数, 之后求和; 
例如: "123" * "456" 的求和过程: 3 分别与 6、5、4 相乘, 并乘上 456
各自的进位数 1、10、100, 随后求和

+ 3       * 6     + 3       * 5 * 10  + 3       * 4 * 100
+ 2 * 10  * 6     + 2 * 10  * 5 * 10  + 2 * 10  * 4 * 100
+ 1 * 100 * 6     + 1 * 100 * 5 * 10  + 1 * 100 * 4 * 100
    """
    def multiply_v1(self, num1: str, num2: str) -> str:
        dict_str2num = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, 
                        "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        # jy: 记录 num1 的进位数
        f1 = 1
        ans = 0
        # jy: 倒序遍历数值字符串
        for i in range(len(num1)-1, -1, -1):
            # jy: 记录 num2 的进位数
            f2 = 1
            # jy: num1 中的每一位的数值乘以进位数
            n1 = dict_str2num[num1[i]] * f1

            # jy: 倒序遍历
            for j in range(len(num2)-1, -1, -1):
                # jy: num2 中每一位的数值乘以进位数
                n2 = dict_str2num[num2[j]] * f2
                ans += n1 * n2

                # jy: 内层循环不断遍历 num2 中的数值, 进位数不断更新
                f2 *=10
            # jy: 外层循环不断遍历 num1 中的数值, 相应的进位数不断更新
            f1 *=10
        return str(ans)


    """
解法 2: 不能直接用 int 或类似的大数库, 所以建立字符数到整数的映射, 将 num1 和
num2 转为整型再计算乘积
    """
    def multiply_v2(self, num1: str, num2: str) -> str:
        dict_str2num = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
                        "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        n1 = 0
        n2 = 0
        bit1 = len(num1) - 1
        bit2 = len(num2) - 1
        for i in num1:
            n1 += dict_str2num[i] * (10 ** bit1)
            bit1 -= 1
        for j in num2:
            n2 += dict_str2num[j] * (10 ** bit2)
            bit2 -= 1
        return str(n1 * n2)


    """
解法 3: 解法 2 中可能利用 Python 的 int 支持大数这一特点取巧, 因此再贴一个竖式计算
    """
    def multiply_v3(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        initial = self.one2many_multiply(num1[-1], num2)
        start = 1
        for i in range(len(num1)-2, -1, -1):
            initial = self.many2many_add(initial, self.one2many_multiply(num1[i], num2), start)
            start += 1
        return "".join([str(char) for char in initial[::-1]])

    def one2many_multiply(self, one, many):
        dict_str2num = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
                        "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        res = []
        for i in range(len(many)-1, -1, -1):
            tmp = dict_str2num[one] * dict_str2num[many[i]] + res.pop() if res \
                  else dict_str2num[one] * dict_str2num[many[i]]
            res.append(tmp % 10)
            res.append(tmp // 10)
        return res if res[-1] != 0 else res[:-1]

    def many2many_add(self, many1, many2, start):
        n1, n2 = len(many1), len(many2)
        res = many1[:start]
        i, j = start, 0
        carry = 0
        while i < n1 or j < n2 or carry != 0:
            numMany1 = many1[i] if i < n1 else 0
            numMany2 = many2[j] if j < n2 else 0
            tmp = numMany1 + numMany2 + carry
            res.append(tmp % 10)
            carry = tmp // 10
            i += 1
            j += 1
        return res


    """
解法 4: 类似解法 1
    """
    def multiply_v4(self, num1: str, num2: str) -> str:
        dict_str2num = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
                        "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        num1, num2 = num1[:: -1], num2[:: -1]
        res = 0

        for i, x in enumerate(num2):
            temp_res = 0
            for j, y in enumerate(num1):
                temp_res += dict_str2num[x] * pow(10, i) * dict_str2num[y] * pow(10, j)
            res += temp_res
        return str(res)



num1 = "2"
num2 = "3"
res = Solution().multiply_v1(num1, num2)
# jy: "6"
print(res)


num1 = "123"
num2 = "456"
res = Solution().multiply_v2(num1, num2)
# jy: "56088"
print(res)



num1 = "123"
num2 = "456"
res = Solution().multiply_v3(num1, num2)
# jy: "56088"
print(res)


num1 = "123"
num2 = "456"
res = Solution().multiply_v4(num1, num2)
# jy: "56088"
print(res)

