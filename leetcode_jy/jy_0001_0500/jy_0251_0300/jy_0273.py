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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Integer-to-English-Words(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 2^31 - 1.


Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand
         Eight Hundred Ninety One"
"""


import math

class Solution:
    def __init__(self):
        self.less_than_10 = {
            '0': 'Zero',
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine'
        }
        self.less_than_20 = {
            '10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '14': 'Fourteen',
            '15': 'Fifteen',
            '16': 'Sixteen',
            '17': 'Seventeen',
            '18': 'Eighteen',
            '19': 'Nineteen'
        }
        self.larger_than_20 = {
            '2': 'Twenty',
            '3': 'Thirty',
            '4': 'Forty',
            '5': 'Fifty',
            '6': 'Sixty',
            '7': 'Seventy',
            '8': 'Eighty',
            '9': 'Ninety'
        }

    def numberToWords(self, num: int) -> str:
        # jy: 将数值字符串化;
        number_string = str(num)
        length = len(number_string)
        i = 0
        # jy: 用于保存数值转换为英文表达的结果, 获取高位数值后, 每 3 位转换一次表达结果;
        words = []
        separators = {
            1: '',
            2: 'Thousand',
            3: 'Million',
            4: 'Billion'
        }
        # jy: 从最高位开始, 每三位解析;
        while i < length:
            high_digits_length = (length - i) % 3
            separator = separators.get(math.ceil((length - i) / 3), '')
            # jy: 获取高位的数值字符串 (获取后确保后续的数值是 3 的倍数)
            high_digits = number_string[i: i + high_digits_length] if high_digits_length != 0 else number_string[i: i+3]
            digits = self._trim_zero(high_digits)
            word = ''

            if len(digits) == 3:
                word = self._parse_three_digits(digits)
            elif len(digits) == 2:
                word = self._parse_two_digits(digits)
            elif len(digits) == 1:
                word = self._parse_one_digit(digits)

            if word:
                words.append(word + (' ' + separator if separator else ''))

            i += len(high_digits)

        return ' '.join(words)


    def _parse_three_digits(self, num: str) -> str:
        """解析三位数值的英文表达"""
        left = int(num[1:])
        return self._parse_one_digit(num[0]) + ' Hundred' + (' ' + self._parse_two_digits(str(left)) if left != 0 else '')


    def _parse_two_digits(self, num: str) -> str:
        """解析两位数值的英文表达"""
        if len(num) == 1:
            return self._parse_one_digit(num)
        elif int(num) < 20:
            return self.less_than_20[num]
        elif num[1] == '0':
            return self.larger_than_20[num[0]]
        else:
            return self.larger_than_20[num[0]] + ' ' + self.less_than_10[num[1]]


    def _parse_one_digit(self, num: str) -> str:
        """解析一位数值的英文表达"""
        return self.less_than_10[num]


    def _trim_zero(self, num: str) -> str:
        """去除数值字符串左边的 '0' 字符"""
        if len(num) == 1:
            return num

        i = 0
        while i < len(num) and num[i] == '0':
            i += 1

        return num[i:]


nums = 123
# Output: "One Hundred Twenty Three"
res = Solution().numberToWords(nums)
print(res)


nums = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
res = Solution().numberToWords(nums)
print(res)


nums = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
res = Solution().numberToWords(nums)
print(res)


nums = 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
res = Solution().numberToWords(nums)
print(res)


