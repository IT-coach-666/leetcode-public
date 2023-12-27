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
title_jy = "Shortest-Palindrome(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given a string `s`. You can convert `s` to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:
0 <= s.length <= 5 * 10^4
`s` consists of lowercase English letters only.
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/shortest-palindrome/solutions/1396220/by-flix-be4y/
    """
    def shortestPalindrome_v1(self, s: str) -> str:

        MOD = 10**9+7   # 模底
        base = 31       # 进制
        
        '''字符编码'''
        def encode(ch):
            return ord(ch) - ord('a') + 1
        
        n = len(s)
        prefix, suffix = 0, 0
        mul = 1         # 存储base的幂
        best = 0        # 记录s中最长回文前缀的长度
        for i in range(n):
            prefix = ( prefix * base + encode(s[i]) ) % MOD     # 前缀哈希值
            suffix = ( suffix + encode(s[i]) * mul ) % MOD    # 前缀反序哈希值
            mul = mul * base % MOD
            
            if prefix == suffix:
                best = i+1      # best是递增的
        
        if best == n:           # s本身为回文串
            return s
        else:
            return s[best:][::-1] + s


    """
解法 2: KMP 算法
    """
    def shortestPalindrome_v2(self, s: str) -> str:
        def prefix_function(s):
            """
            KMP 模板
            """
            n = len(s)
            pi = [0] * n

            j = 0
            for i in range(1, n):
                while j>0 and s[i] != s[j]:     # 当前位置s[i]与s[j]不等
                    j = pi[j-1]                 # j指向之前位置，s[i]与s[j]继续比较

                if s[i] == s[j]:                # s[i]与s[j]相等，j+1，指向后一位
                    j += 1
                
                pi[i] = j
            return pi
        

        '''主程序'''
        pi = prefix_function(s+'#'+s[::-1])     # s+'#'+s[n-1,...,0]的前缀函数
        if pi[-1] == len(s):                    # 前缀函数的最后一位即为s的最长回文前缀的长度
            return s
        else:
            return s[pi[-1]:][::-1] + s



