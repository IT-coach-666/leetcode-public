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
title_jy = "Decode-Ways-II(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the
reverse of the mapping above (there may be multiple ways).

For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

In addition to the mapping above, an encoded message may contain the '*' character, which can
represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may
represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19".
Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

Given a string s containing digits and the '*' character, return the number of ways to decode it.
Since the answer may be very large, return it modulo 10^9 + 7.



Example 1:
Input: s = "*"
Output: 9
Explanation: The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9".
Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G", "H", and "I" respectively.
Hence, there are a total of 9 ways to decode "*".

Example 2:
Input: s = "1*"
Output: 18
Explanation: The encoded message can represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19".
Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be decoded to "AA" or "K").
Hence, there are a total of 9 * 2 = 18 ways to decode "1*".

Example 3:
Input: s = "2*"
Output: 15
Explanation: The encoded message can represent any of the encoded messages "21", "22", "23", "24", "25", "26", "27", "28", or "29".
"21", "22", "23", "24", "25", and "26" have 2 ways of being decoded, but "27", "28", and "29" only have 1 way.
Hence, there are a total of (6 * 2) + (3 * 1) = 12 + 3 = 15 ways to decode "2*".



Constraints:
1 <= s.length <= 10^5
s[i] is a digit or '*'.
"""

class Solution:
    """
在 091_Decode-Ways.py 的基础上额外处理 * :
1) 对于 1 位数, 如果是 *, 则有 1-9 共 9 种组合
2)对于 2 位数, 有三种情况:
   a) * 加数字 : 则 * 处只能是 1 或 2, 如果是 2, 则同时需要数字小于等于 6
   b) 数字加 * : 如果数字是 1, 则 * 有 1-9 共 9 种组合, 如果数字是 2, 则 * 有 1-6 共 6 种组合
   c) 两个 * : 可表示 11-26 (排除 10, 20, 因为 * 只能表示 1-9) 共 15 种组合
    """
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        # jy: 初始化 dp 数组, dp[i] 表示 s[0] 到 s[i] 组成的字符串所拥有的解码组合;
        n = len(s)
        dp = [0] * n
        # jy: 如果第一个字符是 '*', 则 dp[0] 为 9, 表示 s[0] 共有 9 种解码方法;
        if s[0] == '*':
            dp[0] = 9
        # jy: 如果第一个字符不为 '*' 且不为 '0', 则 dp[0] 为 1, 表示有 1 种解码方法;
        #    如果第一个字符为 '0', 则 dp[0] 为 0, 表示该字符没有解码方法(事实上这种情
        #    况不存在, 因为给定的字符串是通过编码得到的, 肯定是有效字符; 如果这种情况
        #    存在, 表示是无效的编码结果, 则整个字符串的解码方式为 0 种; 即如果 s[0] 为
        #    '0', 此处即可直接返回最终结果为 0 了)
        else:
            dp[0] = 1 if s[0] != '0' else 0
        # jy: 从第二位开始遍历字符串;
        for i in range(1, n):
            # jy: 获取当前字符;
            one_digit = s[i: i+1]
            # jy: 获取当前字符以及它的前一个字符(因为解码规则中包含两位数的解码方式, 且每轮循
            #    环都是为了计算 dp[i], 它代表 s[0] 到 s[i] 组成的字符串有多少种解码方式, 显
            #    然计算 dp[i] 时不能将 i 的后一个字符考虑进来, 只能考虑它的前一个字符)
            two_digits = s[i-1: i+1]
            # jy: 计算 dp[i] 时, 将 s[0] 至 s[i] 组成的字符串的解码方式有两种:
            #    1) 将 s[i] 单独拿出来解码, 该字符之前的子串的解码方式即为 dp[i-1], 如果 s[i] 对
            #       应的值为 '*', 表明 s[i] 有 9 种解码方式, 每一种都能与之前的 dp[i-1] 种结合为
            #       整个 s[0] 至 s[i] 组成的字符串解码, 即共有 dp[i-1] * 9 种; 如果 s[i] 的值是 1-9
            #       中的一个数值, 则 s[i] 的解码方式有 1 种, 与之前的 dp[i-1] 种结合仍为 dp[i-1] 种;
            if one_digit == '*':
                dp[i] += dp[i-1] * 9
            elif 1 <= int(one_digit) <= 9:
                dp[i] += dp[i-1]
            # jy: 2) 将 s[i] 和 s[i-1] 拿出来组合成两个数值的子串, 则该子串之前的部分的解码方式有 dp[i-2]
            #       种(如果 i 为 1 时, 则 two_digits 所代表的值为 s[0] 和 s[1] 所组成的两位数值, 此时, 如
            #       果 '*' 不在 two_digits 中, 且 two_digits 的值为 10-26 之间, 则有 1 种解码方法)
            #       a) 如果 '*' 在 two_digits 中, 则需进一步判断 '*' 在左侧还是在右侧;
            if '*' in two_digits:
                count = 0
                # jy: 如果 '*' 在左侧(右侧一位为数值), 则如果当右侧数值小于等于 6 时, 有 2 种解码方式;
                #    如果右侧数值大于 6, 则只有一种解码方式;
                if two_digits[1].isdigit():
                    if int(two_digits[1]) <= 6:
                        count = 2
                    else:
                        count = 1
                # jy: 如果 '*' 在右侧(左侧一位为数值), 则如果当左侧一位为 '1' 时, 有 9 种解码方式, 如果左
                #    侧一位为 '2', 则有 6 种解码方式, 如果为其它数值, 则没有相应的解码方式;
                elif two_digits[0].isdigit():
                    if two_digits[0] == '1':
                        count = 9
                    elif two_digits[0] == '2':
                        count = 6
                # jy: 如果 two_digits 均为 "*" (即 "**"), 则共有 15 种解码方式(11-26, 20 除外);
                else:
                    count = 15
                # jy: 如果 i 大于等于 2 (dp[i] 表示 s[0] 至 s[i] 所组成的字符中的解码方式), 即 s[i]
                #    非第 2 个字符, 且 two_digits 之前还有字符, 且对应的解码方式共有 dp[i-2] 种, 故
                #    结合当前 two_digits 的总数 count, 能组合成 dp[i-2] * count 种; 如果 i 为 1, 则
                #    表明 two_digits 为最开始的两个字符, 其解码方式共有 count 种;
                dp[i] += dp[i-2] * count if i >= 2 else count
            # jy:    b) 如果 '*' 不在 two_digits 中, 且对应的数值范围为 10-26, 则 two_digits 子串之
            #          前的部分的解码方式有 dp[i-2], 结合当前 two_digits 有 1 种解码方式, 整体仍为
            #          dp[i-2] 种(如果 i 为 1 时, 则 two_digits 所代表的值为 s[0] 和 s[1] 所组成的
            #          两位数值, 此时则有 1 种解码方法)
            elif 10 <= int(two_digits) <= 26:
                dp[i] += dp[i-2] if i >= 2 else 1

            dp[i] %= 1000000007

        return dp[-1]


s = "*"
# Output: 9
res = Solution().numDecodings(s)
print(res)


s = "1*"
# Output: 18
res = Solution().numDecodings(s)
print(res)


s = "2*"
# Output: 15
res = Solution().numDecodings(s)
print(res)


