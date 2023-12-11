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
title_jy = "Reverse-Words-in-a-String(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an input string, reverse the string word by word.


Example 1:
Input: "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:
1) A word is defined as a sequence of non-space characters.
2) Input string may contain leading or trailing spaces. However, your reversed string should not
   contain leading or trailing spaces.
3) You need to reduce multiple spaces between two words to a single space in the reversed string.
"""


class Solution:
    """
使用一个指针不断移动, 过滤掉空格并解析出单词, 将单词放入一个数组中, 最后反转数组, 以空格分割拼接字符串;
    """
    def reverseWords_v1(self, s: str) -> str:
        words = []
        i = 0
        # jy: 以下 while 循环将字符串中的单词放入 words 列表;
        while i < len(s):
            # jy: 忽略字符串中的空格字符;
            while i < len(s) and s[i] == ' ':
                i += 1

            # jy: 将非空格字符拼接成单词(每次拼接一个单词), 如果拼接结果非空, 则加入单词列表;
            word = ''
            while i < len(s) and s[i] != ' ':
                word += s[i]
                i += 1
            if word:
                words.append(word)

        # jy: 以下将 words 列表中的单词进行反转(使用双指针法, 头尾不断调换);
        low, high = 0, len(words)-1
        while low < high:
            words[low], words[high] = words[high], words[low]
            low += 1
            high -= 1

        return ' '.join(words)


    def reverseWords_jy(self, s: str) -> str:
        """结合 python 中对字符串的处理方式进行反转"""
        ls_word = [i for i in s.split(" ") if i != ""]
        ls_word.reverse()
        return " ".join(ls_word)

s = "the sky is blue"
# Output: "blue is sky the"
res = Solution().reverseWords_v1(s)
print(res)


s = "  hello world!  "
# Output: "world! hello"
res = Solution().reverseWords_v1(s)
print(res)


s = "a good   example"
# Output: "example good a"
res = Solution().reverseWords_v1(s)
print(res)


res = Solution().reverseWords_jy(s)
print(res)


