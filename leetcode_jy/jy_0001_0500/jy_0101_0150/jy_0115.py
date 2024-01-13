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
title_jy = "Distinct-Subsequences(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "动态规划 | 递归"



"""
Given two strings `s` and `t`, return the number of distinct subsequences of
`s` which equals `t`.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 
Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation: As shown below, there are 3 ways you can generate "rabbit" from `s`.
             参考: https://www.yuque.com/it-coach/leetcode/ln0m5uondgwo6hgv

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation: As shown below, there are 5 ways you can generate "bag" from `s`.
             参考: https://www.yuque.com/it-coach/leetcode/ln0m5uondgwo6hgv
 

Constraints:
1) 1 <= s.length, t.length <= 1000
2) `s` and `t` consist of English letters.
"""



class Solution:
    """
解法 1: 动态规划

参考: https://www.yuque.com/it-coach/leetcode/ln0m5uondgwo6hgv

dp[i][j] 代表基于 s 的前 j 个字符匹配 t 的前 i 个字符
    """
    def numDistinct_v1(self, s: str, t: str) -> int:
        len_s = len(s)
        len_t = len(t)
        dp = [[0] * (len_s + 1) for _ in range(len_t + 1)]
        for j in range(len_s + 1):
            dp[0][j] = 1

        for i in range(1, len_t + 1):
            for j in range(1, len_s + 1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]  + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        #print(dp)
        return dp[-1][-1]

    """
解法 2: 动态规划改写

dp[i][j] 代表基于 s[i:] 匹配 t[j:]
    """
    def numDistinct_v2(self, s: str, t: str) -> int:
        len_s = len(s)
        len_t = len(t)
        dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]
        for i in range(len_s + 1):
            dp[i][len_t] = 1

        for j in range(len_t - 1, -1, -1):
            for i in range(len_s - 1, -1, -1):
                if t[j] == s[i]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        #print(dp)
        return dp[0][0]


    """
解法 3: 递归 (超时)
    """
    def numDistinct_v3(self, s: str, t: str) -> int:
        
        def dfs(i, j):
            """
            基于字符串 s[i:] 匹配 t[j:] 字符串
            """
            # jy: j == len(t) 表明 t 匹配完了, 返回 1
            if j == len(t): 
                return 1

            # jy: i == len(s) 表明字符串 s 中已经没有可用于匹配的
            #     部分了, 直接返回 0
            if i == len(s):
                return 0
            
            cnt = 0
            
            # jy: 跳过 s[i], 基于字符串 s[i+1: ] 匹配 t[j:] 字符串
            #     (不管 s[i] 是否等于 t[j], 均可选择跳过 s[i])
            cnt += dfs(i+1, j)

            # jy: 只有当 s[i] 等于 t[j] 时, 才能选择用 s[i] 匹配 t[j],
            #     并基于 s[i+1:] 匹配 t[j+1:]
            if s[i] == t[j]: 
                cnt += dfs(i+1, j+1)
            
            return cnt
        # jy: 返回基于 s[0:] 匹配 t[0:] 的最多匹配结果
        return dfs(0, 0) 


    """
解法 4: 递归 + 缓存
    """
    def numDistinct_v4(self, s: str, t: str) -> int:

        dict_ = {}

        def dfs(i, j):
            """
            基于字符串 s[i:] 匹配 t[j:] 字符串
            """
            if (i, j) in dict_:
                return dict_[(i, j)]

            # jy: j == len(t) 表明 t 匹配完了, 返回 1
            if j == len(t):
                return 1

            # jy: i == len(s) 表明字符串 s 中已经没有可用于匹配的
            #     部分了, 直接返回 0
            if i == len(s):
                return 0

            cnt = 0

            # jy: 跳过 s[i], 基于字符串 s[i+1: ] 匹配 t[j:] 字符串
            #     (不管 s[i] 是否等于 t[j], 均可选择跳过 s[i])
            cnt += dfs(i+1, j)

            # jy: 只有当 s[i] 等于 t[j] 时, 才能选择用 s[i] 匹配 t[j],
            #     并基于 s[i+1:] 匹配 t[j+1:]
            if s[i] == t[j]:
                cnt += dfs(i+1, j+1)

            dict_[(i, j)] = cnt
            return cnt
        # jy: 返回基于 s[0:] 匹配 t[0:] 的最多匹配结果
        return dfs(0, 0)
 
   
s = "rabbbit"
t = "rabbit"
res = Solution().numDistinct_v1(s, t)
# jy: 3
print(res)


s = "babgbag"
t = "bag"
res = Solution().numDistinct_v2(s, t)
# jy: 5
print(res)


s = "babgbag"
t = "bag"
res = Solution().numDistinct_v3(s, t)
# jy: 5
print(res)


