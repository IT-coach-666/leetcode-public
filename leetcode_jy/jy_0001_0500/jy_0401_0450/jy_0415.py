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
title_jy = "Add-Strings(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two non-negative integers ``num1`` and ``num2`` represented as string, return
the sum of ``num1`` and ``num2`` as a string.

You must solve the problem without using any built-in library for handling large
integers (such as BigInteger). You must also not convert the inputs to integers directly.


Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:
1 <= num1.length, num2.length <= 10^4
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""

class Solution:
    """
逐位相加, 注意进位;
    """
    def addStrings(self, num1: str, num2: str) -> str:
        # jy: 记录进位数;
        carry = 0
        # jy: 用于保存结果字符串;
        result = ''
        # jy: 两指针均指向字符串末尾;
        i, j = len(num1) - 1, len(num2) - 1
        # jy: 如果有一指针有效, 则循环;
        while i >= 0 or j >= 0:
            # jy: 记录当前位的加和结果, 初始化为进位值;
            current_sum = carry

            if i >= 0:
                current_sum += int(num1[i])
                i -= 1

            if j >= 0:
                current_sum += int(num2[j])
                j -= 1
            # jy: 根据当前加和结果, 获取进位数;
            carry = current_sum // 10
            # jy: 将当前加和结果的个位数部分加入到结果字符串中;
            result = str(current_sum % 10) + result

        return result if carry == 0 else '1' + result


num1 = "11"
num2 = "123"
# Output: "134"
res = Solution().addStrings(num1, num2)
print(res)


num1 = "456"
num2 = "77"
# Output: "533"
res = Solution().addStrings(num1, num2)
print(res)


num1 = "0"
num2 = "0"
# Output: "0"
res = Solution().addStrings(num1, num2)
print(res)


