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
title_jy = "Valid-Palindrome-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false


Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.

"""

class Solution:
    """
从字符串的首尾分别向中间遍历, 如果两个指针所在的字符不同, 则尝试删除一端的字符判断剩下的字符串是否是回文
    """
    def validPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1

        while low < high:
            if s[low] != s[high]:
                return self._is_palindrome(s, low + 1, high) \
                       or self._is_palindrome(s, low, high - 1)
            else:
                low += 1
                high -= 1

        return True

    def _is_palindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            else:
                low += 1
                high -= 1

        return True



