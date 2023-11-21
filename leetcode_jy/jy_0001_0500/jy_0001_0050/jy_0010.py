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
tag_jy = ""


"""
Given an input string ``s`` and a pattern ``p``, implement regular expression
matching with support for '.' and '*':
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:    
``s`` could be empty and contains only lowercase letters a-z.
``p`` could be empty and contains only lowercase letters a-z, and characters like '.' or '*'.


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
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
s = "aab"
p = "c*a*b"
Output: true
Explanation: 'c' can be repeated 0 times, 'a' can be repeated 1 time. Therefore, it matches "aab".

Example 5:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution:
    """
动态规划; 定义 dp[i][j] = True 表示 s 的前 i 个字符(即 s[:i])和 p 的前 j 个字符(即 s[:j])匹配;
该题与 044_wildcard-matching.py 类似, 只是规则略有不同;
    """
    def isMatch_v1(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # jy: dp 为一个 (m+1, n+1) 二维列表(数组), 最大下标为 dp[m][n], 代表;
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        # jy: s 的前 0 个字符与 p 的前 0 个字符匹配(空字符是匹配的);
        dp[0][0] = True

        # jy: 从 p 的第二个字符开始遍历, 遍历至最后一个字符(即 i 等于 n, 即第 n 个字符);
        for i in range(2, n+1):
            # jy: 由于 i 代表的是第几个字符, 相应的字符下标位置需要减 1; 
            #     如果 p 的第 i 个字符为 '*', 则 s 的前 0 个字符(即空字符) 和 p 的前 i 个字符
            #     的匹配情况 (即 dp[0][i]) 等同于 s 的前 0 个字符(即空字符) 和 p 的前 i-2 个字
            #     符的匹配情况(即 dp[0][i-2]); 因为 '*' 表示可以匹配 0 个或多个该字符之前的字
            #     符;
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]

        # jy: 循环遍历 s 的第一个到最后一个 (即 1 ~ m) 字符;
        for i in range(1, m+1):
            # jy: 循环遍历 p 的第一个到最后一个 (即 1 ~ n) 字符;
            for j in range(1, n+1):
                # jy: 如果 p 的第 j 个字符为 "*", 则 dp[i][j] 在如下情况时为 True (即 s 的前 i 
                #     个字符与 p 的前 j 个字符在如下情况时互相匹配):
                #     1) dp[i][j-2] 为 True  
                #        如果 p 的第 j 个字符 (即 p[j-1]) 为 "*", 且 s 的前 i 个字符与 p 的前 j-2
                #        个字符匹配(即 dp[i][j-2] 为 True), 因为 "*" 可以匹配 0 个或多个该字符之前
                #        的字符, 所以这种情况下 s 的前 i 个字符和 p 的前 j 个字符匹配 (即 dp[i][j]
                #        为 True);
                #     2) (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j]
                #        如果 s 的前 i-1 个字符与 p 的前 j 个字符匹配 (即 dp[i-1][j] 为 True), 则只
                #        需要满足以下条件的其中一个, 即可确定 s 的前 i 个字符与 p 的前 j 个字符匹配:
                #        a) s 的第 i 个字符 (即 s[i-1]) 等于 p 的第 j-1 个字符 (即 p[j-2]) 
                #        b) p 的第 j-1 个字符 (即 p[j-2]) 为 "."; 因为 p 的第 j-1 个字符 "." 可以匹
                #           配 s 的第 i 个字符;  
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
                # jy: 如果 p 的第 j 个字符(即 p[j-1])不为 "*", 此时如果想要 s 的前 i 个字符与 p 的前
                #     j 个字符匹配(即 dp[i][j] 想要为 True), 则只有当 s 的前 i-1 个字符与 p 的前 j-1
                #     个字符匹配 (即 dp[i-1][j-1] 为 True) 的情况下, 同时满足如下的任一一个要求:
                #     a) s 的第 i 个字符等于 p 的第 j 个字符(即 s[i-1] == p[j-1])
                #     b) p 的第 j 个字符为 "." (即 p[j-1] 为 ".")
                else:
                    dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == '.') and dp[i-1][j-1]
        return dp[m][n]

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



