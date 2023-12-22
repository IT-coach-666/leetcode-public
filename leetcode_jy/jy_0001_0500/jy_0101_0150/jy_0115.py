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
title_jy = "Distinct-Subsequences(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.

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
1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""



class Solution:
    """
解法 1: 动态规划

参考: https://www.yuque.com/it-coach/leetcode/ln0m5uondgwo6hgv
    """
    def numDistinct_v1(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        #print(dp)
        return dp[-1][-1]

    
s = "rabbbit"
t = "rabbit"
res = Solution().numDistinct_v1(s, t)
# jy: 3
print(res)


s = "babgbag"
t = "bag"
res = Solution().numDistinct_v1(s, t)
# jy: 5
print(res)


