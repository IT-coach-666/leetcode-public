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
title_jy = "Length-of-Last-Word(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "字符串处理技巧"



"""
Given a string `s` consisting of words and spaces, return the length of the
last word in the string.

A word is a maximal substring consisting of non-space characters only.


Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:
1) 1 <= s.length <= 10^4
2) `s` consists of only English letters and spaces ' '.
3) There will be at least one word in `s`.
"""



class Solution:
    """
解法 1: 去除字符串两边空格, 从右到左遍历并统计
    """
    def lengthOfLastWord_v1(self, s: str) -> int:
        s = s.strip()
        len_last_word = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                return len_last_word
            len_last_word += 1
        return len_last_word


    """
解法 2: 同理解法 1, 但不使用字符串的内置方法 strip()
    """
    def lengthOfLastWord_v2(self, s: str) -> int:
        len_last_word = 0
        right = len(s) - 1
        while s[right] == " ":
            right -= 1
        for i in range(right, -1, -1):
            if s[i] == " ":
                return len_last_word
            len_last_word += 1
        return len_last_word


    """
解法 3: 巧用字符串内置函数 strip 和 split
    """
    def lengthOfLastWord_v3(self, s: str) -> int:
        s = s.strip()
        return len(s.split()[-1])


    """
解法 4: 同解法 1, 但尽量不引入新变量
    """
    def lengthOfLastWord_v4(self, s: str) -> int:
        s = s.strip()
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                return len(s) - 1 - i
        return len(s) - i



s = "Hello World"
res = Solution().lengthOfLastWord_v1(s)
# jy: 5
print(res)


s = "   fly me   to   the moon  "
res = Solution().lengthOfLastWord_v2(s)
# jy: 4
print(res)


s = "luffy is still joyboy"
res = Solution().lengthOfLastWord_v3(s)
# jy: 6
print(res)


s = "luffy is still joyboy"
res = Solution().lengthOfLastWord_v4(s)
# jy: 6
print(res)

