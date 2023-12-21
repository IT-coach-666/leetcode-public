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
title_jy = "Interleaving-String(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an
interleaving of `s1` and `s2`.

An interleaving of two strings `s` and `t` is a configuration where `s`
and `t` are divided into `n` and `m` substrings respectively, such that:
1) s = s1 + s2 + ... + sn
2) t = t1 + t2 + ... + tm
3) |n - m| <= 1
4) The interleaving is: 
   s1 + t1 + s2 + t2 + s3 + t3 + ... 
   or 
   t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: `a + b` is the concatenation of strings `a` and `b`.

 

Example 1: 
图示参考: https://www.yuque.com/it-coach/leetcode/pgvb5ui8ag9vuzxo
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
1) Split `s1` into: "aa" + "bc" + "c", and `s2` into: "dbbc" + "a"
2) Interleaving the two splits, we get:
   "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac"
3) Since `s3` can be obtained by interleaving `s1` and `s2`, we return true.


Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave `s2` with any other
             string to obtain `s3`.


Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:
1) 0 <= s1.length, s2.length <= 100
2) 0 <= s3.length <= 200
3) `s1`, `s2`, and `s3` consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?
"""


class Solution:
    """
解法 1: 动态规划

https://leetcode.cn/problems/interleaving-string/solutions/48146/dong-tai-gui-hua-zhu-xing-jie-shi-python3-by-zhu-3/
    """
    def isInterleave_v1(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if(len1 + len2 != len3):
            return False

        dp=[[False]*(len2+1) for i in range(len1+1)]
        dp[0][0]=True

        for i in range(1, len1 + 1):
            dp[i][0] = (dp[i-1][0] and s1[i-1] == s3[i-1])

        for i in range(1, len2 + 1):
            dp[0][i] = (dp[0][i-1] and s2[i-1] == s3[i-1])

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or \
                           (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        return dp[-1][-1]



s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
res = Solution().isInterleave_v1(s1, s2, s3)
# jy: true
print(res)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
res = Solution().isInterleave_v1(s1, s2, s3)
# jy: false
print(res)


s1 = ""
s2 = ""
s3 = ""
res = Solution().isInterleave_v1(s1, s2, s3)
# jy: true
print(res)


