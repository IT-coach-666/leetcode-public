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
tag_jy = "动态规划 | 递归 + 缓存 | IMP"


"""
A message containing letters from "A" - "Z" can be encoded into numbers using
the following mapping:
"A" -> "1"
"B" -> "2"
...
"Z" -> "26"

To decode an encoded message, all the digits must be grouped then mapped back
into letters using the reverse of the mapping above (there may be multiple ways).
For example, "11106" can be mapped into:
1) "AAJF" with the grouping (1 1 10 6)
2) "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into
'F' since "6" is different from "06".

Given a string `s` containing only digits, return the number of ways to decode
it. The answer is guaranteed to fit in a 32-bit integer.


Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6),
             or "BBF" (2 2 6).

Example 3:
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
             The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20",
             neither of which start with 0. Hence, there are no valid ways to
             decode this since all digits need to be mapped.

Example 4:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero
             ("6" is different from "06").


Constraints:
1) 1 <= s.length <= 100
2) `s` contains only digits and may contain leading zero(s).
"""


from functools import lru_cache


class Solution:
    """
解法 1: 动态规划, 时间复杂度 O(n), 空间复杂度 O(n)

记 dp[i] 表示 s[0] 到 s[i] 组成的字符串的解码数量
遍历字符串 (假设当前字符的下标位置为 i), 考虑两种情况:
1) 将当前字符单独解码 (解码为个位数), 则 dp[i] += dp[i-1]
2) 将当前字符和前一个字符一起解码 (解码为两位数), 则 dp[i] += dp[i-2]
   注意: 如果当前字符和前一个字符之前已经没有字符了, 则对
   应的解码方式只有 1 种
   
为什么是与前一个字符而不是后一个字符? 这是由 dp[i] 的定义而定:
dp[i] 统计的是截止位置下标 i 为止的解码方式, 要构成两个字符只能
是 i 和 i-1 对应的字符 (因为动态规划需逐步求解, 不是从前往后就是
从后往前, 当前定义属于从前往后的方式)

注意: 当确保数值位数相同时, 字符串的形式也能直接进行比较, 效果等
同于数值形式的比较
    """
    def numDecodings_v1(self, s: str) -> int:
        # jy: 如果字符串的首字符为 "0", 则无法解码, 直接返回 0 
        if not s or s[0] == "0":
            return 0

        n = len(s)
        # jy: 初始化 dp (长度为 n, 初始值均为 0)
        dp = [0] * n
        # jy: 执行到此处表明字符串的第一个字符不为 "0", 因此单独对第一个
        #     字符进行解码的方式有 1 种
        dp[0] = 1
        # jy: 从第 2 个字符开始遍历字符串
        for i in range(1, n):
            # jy: 尝试将当前字符单独进行解码
            #     1) 如果当前字符为 "0", 则无法将其单独解码
            #     2) 如果当前字符为 "1" 到 "9", 则当前字符单独解码的方式
            #        有 1 种, 因此对当前字符以及之前的字符进行解码的方式
            #        等同于前一个字符之前的解码方式, 即: dp[i] = dp[i-1]
            one_digit = s[i: i+1]
            if "1" <= one_digit <= "9":
                # jy: 此处等同于 dp[i] = dp[i-1], 因为 dp[i] 的初始值为 0
                dp[i] += dp[i-1]

            # jy: 尝试将当前字符以及其前一个字符组合在一起进行解码
            #     1) 如果组合后的数值字符不在 "10" 到 "26" 之间, 则表明
            #        无法对其单独解码
            #     2) 如果组合后的数值字符在 "10" 到 "26" 之间, 则表明可
            #        以对其进行解码, 解码方式有 1 种, 因此如果将其组合起
            #        来进行编码, 对当前字符以及之前的字符进行解码的方式
            #        前两个字符之前的解码方式, 即 dp[i] = dp[i-2], 因此
            #        叠加上一种单独字符解码的方法, 有: dp[i] += dp[i-2]
            #        注意: 如果当前字符和前一个字符之前已经没有字符了,
            #        则对应的解码方式只有 1 种
            two_digits = s[i-1: i+1]
            if "10" <= two_digits <= "26":
                dp[i] += dp[i-2] if i >= 2 else 1
        return dp[n-1]

    """
解法 2: 优化解法 1 的空间复杂度至 O(1)

dp[i] 的计算只依赖 dp[i-1] 和 dp[i-2], 因此可以采用与滚动数组类似的思路,
只创建长度为 3 的 dp 数组, 通过取余的方式来复用不再需要的下标
    """
    def numDecodings_v2(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
            
        n = len(s)
        dp = [0] * 3
        dp[0] = 1
        for i in range(1, n):
            # jy: 关键一步: 最新的 dp[i % 3] 是当前一步要更新的对象,
            #     原值需确保重置为 0, 因为后续会基于原值的基础上累加
            dp[i % 3] = 0
            if "1" <= s[i] <= "9":
                dp[i % 3] = dp[(i - 1) % 3]
            if "10" <= s[i-1: i+1] <= "26":
                dp[i % 3] += dp[(i - 2) % 3] if i >= 2 else 1
        return dp[(n-1) % 3]


    """
解法 3: 解法 2 的更简洁改写

输入 "12" 的结果为 2, 如果在 "12" 后面增加一个数字 "3", 输入变成 "123", 结果
是 "12" 的结果 + "1" 的结果 = 3

i 从索引 1 开始逐渐遍历 s, 当前位置对应结果为以下两种结果之和:
a) 上次结果 (如果 i 位置字符和 i-1 位置字符的组合满足条件)
b) 当前结果 (如果 s[i] 不为 0)
    """
    def numDecodings_v3(self, s: str) -> int:
        prev = 1
        current = int(s[0] != "0")
        for i in range(1, len(s)):
            # jy: 完美地展现了有限制的递归公式: dp[i] = dp[i-1] + dp[i-2]
            #     注意, 该公式不能拆开写
            prev, current = current, prev * ("10" <= s[i-1:i+1] <= "26") + current * (s[i] > "0")
        return current


    """
解法 4: 递归; 无缓存时, 时间复杂度 O(2^n), 会超时; 空间复杂度 O(n)
    """
    @lru_cache()
    def numDecodings_v4(self, s: str) -> int:
        # jy: 该判断条件主要是用于后续递归过程中, 用于终止递归 (实际上不能用
        #     于主函数, 但由于题目中明确说明最开始输入的 s 不会为空, 因此用
        #     在主函数上也不影响)
        if len(s) == 0:
            return 1

        if s[0] == "0":
            return 0

        decode_1, decode_2 = 0, 0
        # jy: 将 s 的当前字符 (一个数值字符) 单独解码 (需保证该字符可正常解码)
        if s[0] != "0":
            decode_1 = self.numDecodings_v2(s[1:])

        # jy: 将 s 的前两个字符单独解码 (需保证前两个字符可正常解码)
        if len(s) > 1 and 10 <= int(s[:2]) <= 26:
            decode_2 = self.numDecodings_v2(s[2:])

        # jy: 两种情况下的解码数相加后返回
        return decode_1 + decode_2


    """
解法 5: 递归的另一个写法
    """
    def numDecodings_v5(self, s: str) -> int:
        if s[0] == "0":
            return 0

        @lru_cache(None)
        def dfs(i):
            """
            求 s[i:] 共有几种解码方法
            """
            ans = 0
            # jy: 如果递归过程中 i 已经到 s 的末尾, 表明已经找到一种解码方法
            if i >= len(s):
                return 1

            if i + 2 <= len(s) and "10" <= s[i: i+2] <= "26":
                ans += dfs(i+2)

            if s[i] != "0":
                ans += dfs(i+1)
            return ans

        return dfs(0)



s = "12"
res = Solution().numDecodings_v1(s)
# jy: 2
print(res)


s = "226"
res = Solution().numDecodings_v2(s)
# jy: 3
print(res)


s = "0"
res = Solution().numDecodings_v3(s)
# jy: 0
print(res)


s = "06"
res = Solution().numDecodings_v4(s)
# jy: 0
print(res)


s = "12"
res = Solution().numDecodings_v5(s)
# jy: 2
print(res)


s = "60"
res = Solution().numDecodings_v1(s)
# jy: 0
print(res)

