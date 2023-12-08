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
title_jy = "Reverse-Vowels-of-a-String(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.


Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"


Constraints:
1 <= s.length <= 3 * 10^5
s consist of printable ASCII characters.
"""


class Solution:
    """
先求出所有元音所在字符串中的位置，然后使用首尾双指针进行反转元音
    """
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i, c in enumerate(s) if c
                  in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]
        low, high = 0, len(vowels) - 1
        # jy: 由于字符串不支持基于下标进行字符替换, 故先将其转换为列表;
        chars = list(s)

        while low < high:
            chars[vowels[low]], chars[vowels[high]] = chars[vowels[high]], chars[vowels[low]]
            low += 1
            high -= 1
        return ''.join(chars)

    """
JY: 比解法 1 更优;
    """
    def reversevowels_jy(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        low = 0
        high = len(s)-1
        # jy: 由于字符串不支持基于下标进行字符替换, 故先将其转换为列表;
        s = list(s)
        while low < high:
            while low < len(s) and s[low] not in vowels:
                low += 1
            while high >= 0 and s[high] not in vowels:
                high -= 1
            if low < high:
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1
        return "".join(s)


s = "hello"
# Output: "holle"
res = Solution().reverseVowels(s)
print(res)


s = "leetcode"
# Output: "leotcede"
res = Solution().reversevowels_jy(s)
print(res)


