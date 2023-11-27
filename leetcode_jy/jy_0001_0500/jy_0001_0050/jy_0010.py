# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
from typing import List
# jy: 记录该题的难度系数
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Regular-Expression-Matching(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "动态规划 | UNDO"


"""
Given an input string `s` and a pattern `p`, implement regular expression
matching with support for "." and "*":
1) "." Matches any single character.
2) "*" Matches zero or more of the preceding element.

注意: "." 可匹配任意单个字符, 而 "*" 只能匹配该字符之前的字符(匹配 0 次或多次)

The matching should cover the entire input string (not partial).

Note:    
a) `s` could be empty and contains only lowercase letters a-z.
b) `p` could be empty and contains only lowercase letters a-z, and characters
   like '.' or '*'.


Example 1:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, 
             by repeating 'a' once, it becomes "aa".

Example 3:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more of any character".

Example 4:
s = "aab"
p = "c*a*b"
Output: true
Explanation: 'c' can be repeated 0 times, 'a' can be repeated 1 time.
             Therefore, it matches "aab".

Example 5:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution:
    """
解法 1: 动态规划 (与 0044 类似, 只是规则略有不同)

设 dp[i][j] = True 表示 s 的前 i 个字符(即 s[:i])和 p 的前 j 个字
符(即 s[:j])匹配
    """
    def isMatch_v1(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # jy: dp 为一个 (m+1, n+1) 二维列表(数组), 最大下标为 dp[m][n],
        #     代表 s 的前 m 个字符与 p 的前 n 个字符匹配 (即表示字符串
        #     s 与模式 p 匹配)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        # jy: s 的前 0 个字符与 p 的前 0 个字符匹配 (空字符必定匹配)
        dp[0][0] = True

        # jy: 基于模式字符串的特点, 完成对 dp 的初始化设置; i 代表的是第几个
        #     字符; 以下从 p 的第二个字符开始遍历, 遍历至最后一个字符(即第 n
        #     个字符); 由于 i 代表第 i 个字符, 因此对应的下标位置为 i-1
        for i in range(2, n+1):
            # jy: 因为 '*' 表示可以匹配 0 个或多个该字符之前的字符, 因此如
            #     果 p 的第 i 个字符为 '*', 则 s 的前 0 个字符 (即空字符)
            #     和 p 的前 i 个字符的匹配情况 (即 dp[0][i]) 等同于 s 的前
            #     0 个字符和 p 的前 i-2 个字符的匹配情况 (即 dp[0][i-2])
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]

        # jy: 遍历 s 的每一个字符 (第 i 个字符的下标为 i-1)
        for i in range(1, m+1):
            # jy: 遍历 p 的每一个字符 (第 j 个字符的下标为 j-1)
            for j in range(1, n+1):
                # jy: 如果 p 的第 j 个字符 p[j-1] 为 "*", 则 s 的前 i 个字符与
                #     p 的前 j 个字符在如下情况时互相匹配 (即 dp[i][j] = True):
                #     1) dp[i][j-2] = True, 即 s 的前 i 个字符与 p 的前 j-2 个
                #        字符匹配; 因为 "*" 可以匹配 0 个或多个该字符之前的字符
                #     2) dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.')
                #        如果 dp[i-1][j] = True, 即 s 的前 i-1 个字符与 p 的前
                #        j 个字符匹配, 则只需满足以下其中一个条件即可确定 s 的
                #        前 i 个字符与 p 的前 j 个字符匹配:
                #        a) s 的第 i 个字符 s[i-1] 等于 p 的第 j-1 个字符 p[j-2]
                #        b) p 的第 j-1 个字符 p[j-2] 为 ".", 可匹配 s 的第 i 个字符
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                # jy: 如果 p 的第 j 个字符 p[j-1] 不为 "*", 此时需满足 s 的前
                #     i-1 个字符与 p 的前 j-1 个字符匹配 (即 dp[i-1][j-1] = True)
                #     并满足下的任一要求时才能确保 s 的前 i 个字符与 p 的前 j
                #     个字符匹配:
                #     a) s 的第 i 个字符等于 p 的第 j 个字符(即 s[i-1] == p[j-1])
                #     b) p 的第 j 个字符为 "." (即 p[j-1] 为 ".")
                else:
                    dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == '.') and dp[i-1][j-1]
        return dp[m][n]

    """
解法 2: UNDO
注意: "." 可匹配任意单个字符, 而 "*" 只能匹配该字符之前的字符(匹配 0 次或多次)
    """
    def isMatch_v2(self, s: str, p: str) -> bool:
        i, j = 0, 0
        prev_p = -1
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == "."):
                i += 1
                prev_p = j
                j += 1
            elif j < len(p) and p[j] == "*" and (p[prev_p] == s[i] or p[prev_p] == "."):
                if i + 1 < len(s) and j + 1 < len(p) and s[i + 1] == p[j + 1]:
                    i += 1
                    j += 1
                else:
                    i += 1
            elif j < len(p) and p[j] == "*" and p[prev_p] != s[i]:
                j += 1
            elif j + 1 < len(p) and p[j + 1] == "*":
                j += 2
                prev_p = -1
            else:
                return False
        while j < len(p):
            if p[j] != "*":
                return False
            j += 1
        return True


s = "mississippi"
p = "mis*is*p*."
# Output: false
res = Solution().isMatch_v1(s, p)
print(res)

s = "aa"
p = "a"
# Output: false
res = Solution().isMatch_v1(s, p)
print(res)

s = "aa"
p = "a*"
# Output: true
res = Solution().isMatch_v2(s, p)
print(res)

s = "ab"
p = ".*"
# Output: true
res = Solution().isMatch_v2(s, p)
print(res)

s = "aab"
p = "c*a*b"
# Output: true
res = Solution().isMatch_v2(s, p)
print(res)

# undo
s = "aaa"
p = "ab*a*c*a"
# Output: true
res = Solution().isMatch_v2(s, p)
print(res)



