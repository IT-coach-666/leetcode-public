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
title_jy = "Decode-Ways(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into
letters using the reverse of the mapping above (there may be multiple ways). For
example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F'
since "6" is different from "06".

Given a string ``s`` containing only digits, return the number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.


Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
             The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither
             of which start with 0. Hence, there are no valid ways to decode this
             since all digits need to be mapped.

Example 4:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero
             ("6" is different from "06").


Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""


from functools import lru_cache


class Solution:
    """
解法1: 动态规划;
记 dp[i] 表示 s[0] 到 s[i] 组成的字符串的解码数量, 遍历字符串, 考虑两种情况:
1) 将当前字符单独解码(解码为个位数), 则 dp[i] += dp[i-1]
2) 将当前字符和前一个字符一起解码(解码为两位数), 则 dp[i] += dp[i-2]
   该情况下只有 i >= 2 时 dp[i-2] 才是有效的数值, 否则为 1
   至于为什么是与前一个字符而不是后一个字符, 是由 dp[i] 的定义而定: dp[i] 统
   计的是截止位置下标 i 为止的情况, 要构成两个字符只能是 i 和 i-1 对应的字符;
    """
    def numDecodings_v1(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
            # jy: 初始化 dp 长度为 n, 且初始值均为 0;
        n = len(s)
        dp = [0] * n
        # jy: 如果第一个数值不为 0, 则其对应有 1 种解码方式(仅考虑单个字符);
        dp[0] = 1
        # jy: 从第 2 个字符开始遍历字符串;
        for i in range(1, n):
            # jy: 基于当前数值字符, 构造 1 个或 2 个数值字符并转换为整形后进行解码;
            one_digit = int(s[i: i+1])
            two_digits = int(s[i-1: i+1])
            # jy: 将当前字符解码为个位数时, 在当前字符对应的数值为 1 至 9 的情况下, 当前字
            #     符有 1 种解码方法, 故有: dp[i] += dp[i-1] (截止 i 字符的解码方法数等同
            #     于截止 i-1 字符的解码方法数; dp[i] 初始为 0);
            if 1 <= one_digit <= 9:
                dp[i] += dp[i-1]
            # jy: 将当前字符与其前一个字符一起解码(解码为两位数)时, 在确保组成的数值是在
            #     10-26 之间的数值时, 共有 1 种解码方式(非该数值范围内的两位数不能有效解
            #     码); 即截止 i 字符的解码方式共有 dp[i-2] 种(在 i 和 i-1 组成的两位数一
            #     起进行解码的情况下), 当然, 为了确保 dp[i-2] 有效, 需满足 i >= 2, 否则
            #     假如 i 为 1, 则将 i 和 i-1 对应的字符一起解码为有效两位数的解码方式只有
            #     1 种;
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2] if i >= 2 else 1
        return dp[-1]

    """
解法2: 递归求解;
时间复杂度(如果不使用缓存的情况下): O(2^n)
空间复杂度: O(n)
    """
    @lru_cache()
    def numDecodings_v2(self, s: str) -> int:
        if len(s) == 0:
            return 1
        decode_1, decode_2 = 0, 0
        # jy: 将 s 的第一个字符单独解码(解码为个位数; 前提是要保证第一个字符可正常解码)
        if s[0] != "0":
            decode_1 = self.numDecodings_v2(s[1:])
        # jy: 将 s 的前两个字符单独解码(解码为两位数; 前提是要保证前两个字符可正常解码)
        if len(s) > 1 and 10 <= int(s[:2]) <= 26:
            decode_2 = self.numDecodings_v2(s[2:])
        # jy: 两种情况下的解码数相加后返回;
        return decode_1 + decode_2

    """
解法3: 对解法 1 进行优化: 滚动数组, 节省空间;
时间复杂度: O(n)
空间复杂度: O(1)
    """
    def numDecodings_v3(self, s: str) -> int:
        # jy: 如果 s 以 "0" 开头, 表明不能对 s 进行解码;
        if s[0] == '0':
            return 0
        # jy: 如果 s 长度为 1 (执行到此处时已表明 s 不为 "0"), 则只有 1 种解码方法;
        if len(s) == 1:
            return 1

        # jy: a, b, c 分别代表 dp[i-1], dp[i], dp[i+1]; 分别初始化(对应 i 为 0 时的初始
        #     化值)为 1, 1, 0; 其中 a 初始化为 1 是为了后续初次使用到 a 时的场景;
        a, b, c = 1, 1, 0
        for i in range(1, len(s)):
            # jy: 如果当前位置对应的字符不能正常解码(即当前字符为 "0"), 此时:
            #     1) 如果前一个字符为 "1" 或 "2", 则有一种解码方法(a 初始化值为 1);
            #     2) 如果前一个字符不为 "1" 或 "2", 则直接返回 0 (不能对 s 进行解码);
            if s[i] == "0":
                if s[i - 1] in ("1", "2"):
                    c = a
                else:
                    return 0
            # jy: 如果当前位置对应的字符可以正常解码(即当前字符不是 "0"), 表明当前字符可
            #     可以被单独解码; 以下分两种情况:
            #     a) 如果当前字符以及前一字符组成的两个字符可有效解码, 则解码的方式有两种:
            #        1) 将当前字符单独解码(有 dp[i-1] 种, 即 b 的值)
            #        2) 将当前字符与前一字符组成的两个字符一起解码(有 dp[i-1] 种, 即 a 值)
            #     b) 如果当前字符以及其前一字符组成的两个字符不能有效解码, 则只能将当前字符
            #        单独解码, 有 dp[i-1] 种 (即 b 的值)
            #     注意: a 和 b 在还没得到更新时, 对应的值为当前 i 值的前一个值(i-1)的结果,
            #          即 b 对应为 dp[i-1], a 对应为 dp[i-1-1] (dp[i-2]); 以下更新后即对
            #          应当前轮循环后得到的 dp[i-1], dp[i], 但进入下一轮循环时, 由于 i 由
            #          增 1, 上一轮的 dp[i-1] 和 dp[i] 也就又相应变成了当前轮的 dp[i-1]
            #          和 dp[i-1]
            else:
                if 11 <= int(s[i - 1: i + 1]) <= 26:
                    c = b + a
                else:
                    c = b
            a = b
            b = c
        return c


s = "12"
# Output: 2
res = Solution().numDecodings_v1(s)
print(res)


s = "226"
# Output: 3
res = Solution().numDecodings_v2(s)
print(res)


s = "0"
# Output: 0
res = Solution().numDecodings_v3(s)
print(res)


s = "06"
# Output: 0
res = Solution().numDecodings_v1(s)
print(res)


s = "12"
# Output: 2
res = Solution().numDecodings_v2(s)
print(res)


