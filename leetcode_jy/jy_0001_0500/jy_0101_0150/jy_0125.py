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
title_jy = "Valid-Palindrome(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.


Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""

class Solution:
    """
使用两个指针分别指向字符串的首尾, 同时向中间移动, 判断两个指针指向的字符是否忽略大小
写后相等, 同时过滤掉非法的字符;
    """
    def isPalindrome(self, s: str) -> bool:
        low, high = 0, len(s)-1
        while low < high:
            # jy: 如果左指针碰到无效字符, 则 low 加 1;
            if not self._is_valid_letter(s[low]):
                low += 1
            # jy: 如果右指针碰到无效字符, 则 high 加 1;
            elif not self._is_valid_letter(s[high]):
                high -= 1
            # jy: 如果均为有效字符, 则左右指针对应的字符必须相等, 否则返回 False;
            elif s[low].lower() != s[high].lower():
                return False
            # jy: 经过以上逻辑, 此处即表示左右指针对应字符相等, 此时 low 进 1, high 退 1, 然后进行下一步循环;
            else:
                low += 1
                high -= 1
        return True


    def _is_valid_letter(self, s: str) -> bool:
        """判断是否是有效字符"""
        return 'a' <= s <= 'z' or 'A' <= s <= 'Z' or '0' <= s <= '9'


s = "A man, a plan, a canal: Panama"
res = Solution().isPalindrome(s)
print(res)

s = "race a car"
res = Solution().isPalindrome(s)
print(res)


