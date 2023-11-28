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
from typing import List
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "String-to-Integer（atoi）(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "边界判断 | 字符串遍历细节处理"

"""
Implement the ``myAtoi(string s)`` function, which converts a string to a
32-bit signed integer (similar to C/C++'s ``atoi`` function). The algorithm
for ``myAtoi(string s)`` is as follows:
1) Read in and ignore any leading whitespace.
2) Check if the next character (if not already at the end of the string) is
   '-' or '+'. Read this character in if it is either. This determines if the
   final result is negative or positive respectively. Assume the result is
   positive if neither is present.
3) Read in next the characters until the next non-digit character or the end
   of the  input is reached. The rest of the string is ignored.
4) Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If
   no digits were read, then the integer is 0. Change the sign as necessary
   (from step 2).
5) If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1],
   then clamp the integer so that it remains in the range. Specifically,
   integers less than -2^31 should be clamped to -2^31, and integers greater
   than 2^31 - 1 should be clamped to 2^31 - 1.
6) Return the integer as the final result.

Note:
1) Only the space character ' ' is considered a whitespace character.
2) Do not ignore any characters other than the leading whitespace or the rest
   of the string after the digits.


Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a
             numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a
             numerical digit or a +/- sign. Therefore no valid conversion
             could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit
             signed integer. Thefore INT_MIN (-2^31) is returned.
"""


import re


class Automaton:
    """
    自动机 (应用于解法 4)
    """
    # jy: 有效数值范围为 [-2^31, 2^31 - 1]
    #     最大值为: 2 ** 31 - 1 = 2147483647
    #     最小值为: -2^31 = -2147483648
    INT_MAX = 2 ** 31 - 1
    upper_max = (2 ** 31 - 1) // 10

    def __init__(self):
        # jy: 记录当前的状态, 初始状态为 'start' (状态与字符类型对应)
        self.state = 'start'
        # jy: 记录数值的符号
        self.sign = 1
        # jy: 记录数值绝对值结果
        self.ans = 0
        # jy: 设置状态转移表(4 行 4 列), 每一行的 key 和 value 分别代表上一
        #     状态以及上一状态结合当前字符可以转换到的当前状态( index 为 0
        #     至 3 所对应的状态分别表示当前字符为空格、加减符号、数值、其它
        #     符号时, 应转换为的具体状态)
        self.table = {
            # jy: 如果上一状态为 'start', 则当前状态有四种可能(结合当前字
            #     符而定)
            'start':     ['start', 'signed', 'in_number', 'end'],
            # jy: 如果上一状态为 'signed' (即上一个字符为正负符号), 则如果
            #     当前字符非数值字符, 则当前状态均需更新为 'end' (代表结束),
            #     如果当前字符为数值字符, 则当前状态更新为 'in_number'
            'signed':    ['end',   'end',    'in_number', 'end'],
            # jy: 如果上一个状态为 'in_number' (即上一个字符为数值字符), 则
            #     只有当前字符为数值字符时, 当前状态才为 'in_number', 否则就
            #     将当前状态更新为 'end' (代表结束)
            'in_number': ['end',   'end',    'in_number', 'end'],
            # jy: 如果上一状态为 'end', 则不管当前碰到什么字符, 状态均为 'end'
            #     如果后续逻辑中判断为 'end' 状态时及时退出, 则此部分可注释掉
            #'end':       ['end',   'end',    'end',       'end'],
        }

    def get_new_state(self, c):
        """
        c: 当前碰到的字符

        依据当前字符以及上一个状态, 确定当前状态
        """
        if c.isspace():
            return self.table[self.state][0]
        if c == '+' or c == '-':
            return self.table[self.state][1]
        if c.isdigit():
            return self.table[self.state][2]
        return self.table[self.state][3]

    def get(self, c):
        """
        c: 当前碰到的字符

        根据当前字符和前一个状态, 更新当前状态, 并结合当前状态更新数值 
        """
        # jy: 结合上一状态和当前字符, 确认当前状态
        self.state = self.get_new_state(c)
        # jy: 如果当前状态为 'in_number', 表明当前字符为数值字符
        if self.state == 'in_number':
            # jy: 判断是否 self.ans * 10 + inc(c) 会越界
            #     1) 当 self.ans > self.upper_max 时, self.ans * 10 肯定越界
            #     2) 当 self.ans = self.upper_max 时, 只有数值字符大于 7 时
            #        才会越界
            if self.ans > self.upper_max or (
                    self.ans == self.upper_max and int(c) > 7):
                # jy: 有效数值范围为:
                #     最大值(即 self.INT_MAX): 2 ** 31 - 1 = 2147483647
                #     最小值: -2^31 = -2147483648
                #     如果数值越界, 则当为负值时, 要将 self.ans 设置为负最大
                #     值的相反数 (因为最终返回结果的符号是基于 self.sign 确定
                #     的, self.ans 不应带负号)
                self.ans = self.INT_MAX if self.sign == 1 else (self.INT_MAX + 1)
                # jy: 设置状态为 "end", 表明已经可以结束
                self.state = "end"
            else:
                self.ans = self.ans * 10 + int(c)
        # jy: 如果当前字符为符号字符, 则根据符号字符判断是正数还是负数
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

            
class Solution:
    """
解法 1: 遍历字符串, 忽略所有前置空格, 然后判断是否有正负号(唯有符号位时默认为
正值), 接着继续遍历直到遇到的不是数字为止, 遍历数字时先将截止当前为止的整数乘
以 10, 然后再加上当前数字
    """
    def myAtoi_v1(self, s: str) -> int:
        # jy: 最大值上限: 2^31 - 1
        max_positive = pow(2, 31) - 1
        # max_positive = 2 ** 31 - 1
        # jy: 最小值下限: - 2^31
        min_negative = -max_positive - 1
        # jy: 记录符号位
        negative = False
        # jy: 记录最终结果
        result = 0
        # jy: 记录当前遍历到的位置以及字符串长度
        i, len_s = 0, len(s)

        # jy: 忽略所有前缀空格
        while i < len_s and s[i].isspace():
            i += 1
        # jy: 如果已经遍历完字符串, 则直接返回 0
        if i == len_s:
            return 0

        # jy: 忽略前缀空格后, 如果碰到符号位, 则更新 negative (为 "-" 时
        #     negative 为 True)
        if s[i] == '+' or s[i] == '-':
            negative = s[i] == '-'
            i += 1

        # jy: result 初始值为 0; 处理完所有前缀空格以及符号位后, 如果为数
        #     值, 则不断记录更新到 result 中, 直到碰到的非数值停止即可基
        #     于正负号返回相应结果
        while i < len_s and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        # jy: 如果为负值, 所取负值不能比 min_negative 还小, 否则越界);
        #     如果为正值, 所取正值不能比 max_negative 还大, 否则越界)
        return max(-result, min_negative) if negative else min(result, max_positive)
    

    """
解法 2: 解法 1 中不能保证计算过程中的数值始终在有效数值的范围内; 涉及整数运
算时需要注意溢出; 应做到事前预防, 而非等到真正溢出时再进行判断 
(具体逻辑可参考 jy_0007.py 中的讲解)
    """
    def myAtoi_v2(self, s: str) -> int:
        res = 0
        is_negative = False
        len_s = len(s)
        i = 0

        while i < len_s and s[i] == " ":
            i += 1
        if i == len_s:
            return 0

        if s[i] in "-+":
            is_negative = s[i] == "-"
            i += 1

        max_ = 2 ** 31 - 1
        upper_max = (2 ** 31 - 1) // 10
        while i < len_s and s[i].isdigit():
            int_s_i = int(s[i])
            # jy: 判断 res * 10 + int_s_i 是否会越界
            #     1) 当 res > upper_max 时, res * 10 肯定越界
            #     2) 当 res = upper_max 时, 只有数值字符大于 7 时才会越界
            if res > upper_max or (res == upper_max and int_s_i > 7):
                return - max_ - 1 if is_negative else max_
            res = res * 10 + int_s_i
            i += 1

        return -res if is_negative else res


    """
解法 3: 调用 re 包, 基于正则匹配(非真正意义上考量算法)
    """
    def myAtoi_v3(self, str_: str) -> int:
        # jy: 最大值 2147483647
        INT_MAX = 2 ** 31 - 1
        # jy: 最小值 -2147483648
        INT_MIN = - 2 ** 31
        # jy: 清除左边多余的空格
        str_ = str_.lstrip()
        # jy: 设置正则规则
        num_re = re.compile(r'^[\+\-]?\d+')
        # jy: 查找匹配的内容
        num = num_re.findall(str_)
        # jy: 由于返回的是只含一个元素的列表, 解包并且转换成整数
        #num = int(*num)
        num = int(num[0])
        # jy: 返回值
        return max(min(num, INT_MAX), INT_MIN)


    """
解法4: 自动机解法(官方)
    """
    def myAtoi_v4(self, str: str) -> int:
        # jy: 初始化自动机
        automaton = Automaton()
        for c in str:
            automaton.get(c)
            # jy: 如果 state 已经为 "end", 则可退出, 优化执行效率
            #     如果补充该逻辑, 则 self.table 中的 key 为 'end'
            #     的项可以去除
            if automaton.state == "end":
                break
        return automaton.sign * automaton.ans



s = "42"
res = Solution().myAtoi_v1(s)
print(s, " ===== ", res)

s = "   -42 sada +42"
res = Solution().myAtoi_v2(s)
print(s, " ===== ", res)

s = "4193 with words"
res = Solution().myAtoi_v3(s)
print(s, " ===== ", res)

s = "words and 987"
res = Solution().myAtoi_v4(s)
print(s, " ===== ", res)

s = "-91283472332"
res = Solution().myAtoi_v2(s)
print(s, " ===== ", res)

