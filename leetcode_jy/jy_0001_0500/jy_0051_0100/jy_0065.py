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
title_jy = "Valid-Number(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "有限状态自动机 | 找规律 | 正则表达式 | IMP"



"""
A valid number can be split up into these components (in order):
1) A decimal number or an integer.
2) (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
1) (Optional) A sign character (either '+' or '-').
2) One of the following formats:
   a) One or more digits, followed by a dot '.'.
   b) One or more digits, followed by a dot '.', followed by one or more digits.
   c) A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):
1) (Optional) A sign character (either '+' or '-').
2) One or more digits.

For example, all the following are valid numbers: 
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1",
 "53.5e93", "-123.456e789"]
while the following are not valid numbers: 
["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

Given a string `s`, return true if `s` is a valid number.

 
Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false
 

Constraints:
1) 1 <= s.length <= 20
2) `s` consists of only English letters (both uppercase and lowercase),
   digits (0-9), plus '+', minus '-', or dot '.'.
"""


class Solution:
    """
解法 1: 有限状态自动机

参考解析: https://www.yuque.com/it-coach/leetcode/gax45gle1fbcuowk
    """
    def isNumber_v1(self, s: str) -> bool:
        # jy: ls_state 实际上是一个状态转移矩阵, ls_state[i] 中的 i 的可选
        #     值为 0 至 8, 共 9 个数值, 表示 9 种状态; ls_state[i] 为一个
        #     字典, 其中 keys 为状态 i 下的可选字符模式, values 为已知字符
        #     模式时可迁移至的下一个状态 (每个状态下对应多种可能的字符模式)
        # jy: 例如 ls_state[0] 的值为 { " ": 0, "s": 1, "d": 2, ".": 4 },
        #     表示状态 0 (即开始状态) 下的可选字符模式为:
        #     1) " " (空格): 如果为该字符模式, 则下一个迁移到的状态仍为 0
        #     2) "s" (加减符号): 如果为该字符模式, 则下一个迁移到的状态为 1
        #     3) "d" (数字字符): 如果为该字符模式, 则下一个迁移到的状态为 2
        #     4) "." (小数点符号): 如果为该字符模式, 则下一个迁移到的状态 4
        # jy: 9 个状态说明如下:
        #     0: 开始的空格
        #     1: 幂符号前的正负号
        #     2: 小数点前的数字
        #     3: 小数点、小数点后的数字
        #     4: 当小数点前为空格时，小数点、小数点后的数字
        #     5: 幂符号
        #     6: 幂符号后的正负号
        #     7: 幂符号后的数字
        #     8: 结尾的空格
        ls_state = [
            { " ": 0, "s": 1, "d": 2, ".": 4 },
            { "d": 2, ".": 4 } ,
            { "d": 2, ".": 3, "e": 5, " ": 8 },
            { "d": 3, "e": 5, " ": 8 },
            { "d": 3 }, 
            { "s": 6, "d": 7 }, 
            { "d": 7 }, 
            { "d": 7, " ": 8 }, 
            { " ": 8 } 
        ]

        # jy: 初始状态为 0; ls_state[0] 中定义了该状态下的可选字符模式
        p = 0 
        # jy: 遍历字符串中的每个字符, 并基于该字符设定所属的字符模式
        for c in s:
            # jy: digit
            if "0" <= c <= "9":
                t = "d"
            # jy: sign
            elif c in "+-":
                t = "s"
            # jy: e or E
            elif c in "eE":
                t = "e"
            # jy: "." 和 " " 的字符模式为其本身
            elif c in ". ":
                t = c
            # jy: 其它字符模式 (不在状态转移矩阵的许可范围之内)
            else:
                t = "?" 

            # jy: 如果当前状态下许可的所有字符模式中不包含当前的字符模式,
            #     则直接返回 False
            if t not in ls_state[p]:
                return False

            # jy: 基于字符模式以及当前状态, 更新下一个状态
            p = ls_state[p][t]
        # jy: (2, 3, 7, 8) 为符合最终要求的状态
        return p in (2, 3, 7, 8)


    """
解法 2: 类似解法 1
    """
    def isNumber_v2(self, s: str) -> bool:
        # DFA transitions: dict[action] -> successor
        ls_state = [{},
                  # state 1: 初始状态 (空字符串或纯空格)
                  {"blank": 1, "sign": 2, "digit": 3, "dot": 4},
                  # state 2: 符号位
                  {"digit": 3, "dot": 4},
                  # state 3: 数字位 (形如 -164 可以作为结束)
                  {"digit": 3, "dot": 5, "e|E": 6, "blank": 9},
                  # state 4: 小数点
                  {"digit": 5},
                  # state 5: 小数点后的数字 (形如 .721 或 -123.6 可以作为结束)
                  {"digit": 5, "e|E": 6, "blank": 9},
                  # state 6: 指数 e
                  {"sign": 7, "digit": 8},
                  # state 7: 指数后面的符号位
                  {"digit": 8},
                  # state 8: 指数后面的数字 (形如 +1e-6 可以作为结束)
                  {"digit": 8, "blank": 9},
                  # state 9: 状态 3、5、8 后面多了空格 (主要为了判断 "1 1" 是不合理的)
                  {"blank": 9}]

        def strToAction(st):
            if '0' <= st <= '9':
                return "digit"
            if st in "+-":
                return "sign"
            if st in "eE":
                return "e|E"
            if st == '.':
                return "dot"
            if st == ' ':
                return "blank"
            return None

        currState = 1
        for c in s:
            action = strToAction(c)
            if action not in ls_state[currState]:
                return False
            currState = ls_state[currState][action]

        return currState in {3, 5, 8, 9}


    """
解法 3: 

列举所有的情况是非常困难的, 因为符号之间互相组合的情况实在很多, 一一列举全
且用代码实现的代价很大;

该题的核心是判断浮点数是否合法, 合法的浮点数的情况也是不少的, 这些情况虽然
多, 彼此之间是有联系的, 如果把一个合法的浮点数进行拆分，它大概可以分成以下
几个部分:
1) 首先是符号位, 表示这个数是正数还是负数; 正数用正号表示也是合法的
2) 第二个部分是科学记数法的前半部分, 它可以是一个小数
3) 第三个部分是 e, 即科学记数法当中的 e
4) 最后一个部分是整数部分, 表示 e 的指数

因为这四个部分是有顺序的, 因此只需要判断它们顺序的合理性就可以; 根据顺序的
合理性, 可以进一步推测出每一个符号允许出现的位置, 所有和预期位置不符的符号
都是非法的; 根据这一点可以推导出一些结论:
1) 空格只能出现在首尾, 出现在中间一定是非法的
2) 正负号只能出现在两个地方 (如果出现在其它位置一定也是非法的):
   a) 数字的最前面, 表示符号
   b) e 后面, 表示指数的正负
3) 数字，数字没有特别的判断, 本题当中没有前导 0 的问题
4) e 只能出现一次, 且 e 之后一定要有数字才合法, 123e 这种也是非法的
5) 小数点, 由于 e 之后的指数一定是整数, 所以小数点最多只能出现一次, 并且一定
   要在 e 之前; 所以如果之前出现过小数点或 e, 再次出现小数点就是非法的

当我们把每一个符号合法的情况梳理清楚之后, 会发现其实也没有那么复杂, 情况也没
有那么多; 这其实也是常用套路, 把互相耦合的一些变量拆分开了, 彼此互不影响; 这
样我们就可以单独考虑这其中的每个零件, 而不用面对它们互相耦合的复杂情况了
    """
    def isNumber_v3(self, s: str) -> bool:
        # jy: 去除字符串两边的空格 (后续遍历过程中不再允许出现空格)
        s = s.strip()
        
        # jy: 三个变量分别用于记录 "eE"、"." 和数字符号是否出现
        e_show_up, dot_show_up, num_show_up = False, False, False

        for i in range(len(s)):
            c = s[i]
            # jy: 数字符号出现
            if "0" <= c <= "9":
                num_show_up = True
            # jy: 如果当前字符为 "-+", 且不是第一个字符, 同时前一个字符不
            #     为 "eE", 则不符合要求
            elif c in ('+', '-'):
                if i > 0 and s[i-1] not in ["e", "E"]:
                    return False
            # jy: 如果当前字符为 ".", 且不是第一次出现, 或者是第一次出现, 但
            #     是在 "eE" 之后出现, 则直接返回 False
            elif c == '.':
                if dot_show_up or e_show_up:
                    return False
                dot_show_up = True
            # jy: 如果当前字符为 "eE", 且不是第一次出现, 或之前还没有数值出现,
            #     则直接返回 Fasle; 否则重置 num_show_up 为 False, 表明后续还
            #     需要出现数值才符合规范
            elif c in ["e", "E"]:
                if e_show_up or not num_show_up:
                    return False
                e_show_up = True
                num_show_up = False
            else:
                return False
            
        return num_show_up        
                

    """
解法 4: 基于内置函数 float 和 try 语句 (不符合出题者要求)
    """
    def isNumber_v4(self, s: str) -> bool:
        if s in ["nan", "inf", "-inf", "+inf", "Infinity", "+Infinity", "-Infinity"]:
            return False
        try:
            key = float(s)
            return True
        except: return False


    """
解法 5: 基于正则表达式
    """
    def isNumber(self, s: str) -> bool:
        import re
        s = s.strip()
        pat = re.compile(r'^[\+\-]?(\d+\.\d+|\.\d+|\d+\.|\d+)([e|E][\+\-]?\d+)?$')
        #return True if len(re.findall(pat, s)) else False
        #return True if pat.search(s) else False
        return True if pat.match(s) else False


s = "0"
res = Solution().isNumber_v1(s)
# jy: true
print(res)


s = "e"
res = Solution().isNumber_v1(s)
# jy: false
print(res)


s = "."
res = Solution().isNumber_v1(s)
# jy: false
print(res)

