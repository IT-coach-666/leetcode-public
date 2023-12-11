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
title_jy = "Valid-Word-Abbreviation(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A string can be abbreviated by replacing any number of non-adjacent substrings with
their lengths. For example, a string such as "substitution" could be abbreviated as
(but not limited to):
  "s10n" ("s ubstitutio n")
  "sub4u4" ("sub stit u tion")
  "12" ("substitution")
  "su3i1u2on" ("su bst i t u ti on")
  "substitution" (no substrings replaced)

Note that "s55n" ("s ubsti tutio n") is not a valid abbreviation of "substitution"
because the replaced substrings are adjacent.

Given a string s and an abbreviation abbr, return whether the string matches with the
given abbreviation.


Example 1:
Input: word = "internationalization", abbr = "i12iz4n"
Output: true

Example 2:
Input: word = "apple", abbr = "a2e"
Output: false


Constraints:
1 <= word.length, abbr.length <= 20
word consists of only lowercase English letters.
abbr consists of lowercase English letters and digits.
"""


class Solution:
    """
将 abbr 解码, 如果解码的结果等于 word, 则返回 true;
    """
    def validWordAbbreviation_v1(self, word: str, abbr: str) -> bool:
        decoded = ''
        digit = 0
        i = 0
        # jy: 记录缩略词中剩余的数值中未处理的数值之前的字符对应的下标;
        index_before_digit = -1
        # jy: 循环遍历 abbr; 由于 i 在内层 while 循环中可能会前进好几位, 故此处
        #    使用 i 作为下标, 然后依据 i 访问 abbr, 而不是直接 for 循环遍历 abbr
        #    中的元素;
        while i < len(abbr):
            # jy: 如果 abbr[i] 是数值字符
            if abbr[i].isdigit():
                # jy: 如果 abbr 中的数值子串以 0 开头, 视为非法缩写, 直接返回 False;
                if int(abbr[i]) == 0:
                    return False
                # jy: 获取以有效数值字符开始(非 '0' 开头)的全数值(因为非个位数数值的字符
                #    串形式长度大于 1, 但不确定长度是多少); 该循环结束后, i 对应的位置
                #    为非数字字符(单词原有字符), digit 对应为缩略的字符个数;
                while i < len(abbr) and abbr[i].isdigit():
                    digit = 10 * digit + int(abbr[i])
                    i += 1

                # jy: 确定当前数值对应的 word 中的起始下标;
                start = index_before_digit + 1
                end = start + digit

                # jy: 如果计算得到的末尾下标大于 word 的长度, 直接返回 False;
                if end > len(word):
                    return False

                decoded += word[start:end]
                # jy: 更新 index_before_digit 为 decoded 的最后一个字符的下标;
                index_before_digit = len(decoded) - 1
                # jy: 重置 digit 为 0, 使得下轮数值可以被正确解读;
                digit = 0
            # jy: 如果 abbr[i] 非数值字符(即单词的原字符), 则将该字符直接添加
            #    到 decoded 字符串之后;
            else:
                decoded += abbr[i]
                index_before_digit += 1
                i += 1

        return word == decoded


    def validWordAbbreviation_jy(self, word, abbr):
        decoded = ''
        digit = 0
        i = 0
        # jy: 遍历缩略词;
        while i < len(abbr):
            if abbr[i].isdigit():
                # jy: 如果 abbr 中的数值子串以 0 开头, 视为非法缩写, 直接返回 False;
                #    若当前 decoded 字符子串与 word 中相同长度的子串不相等, 返回 False;
                if int(abbr[i]) == 0 or decoded != word[: len(decoded)]:
                    return False
                # jy: 该循环结束后, i 对应的位置为非数字字符(单词原有字符), digit 对应为
                #    缩略的字符个数;
                while i < len(abbr) and abbr[i].isdigit():
                    digit = 10 * digit + int(abbr[i])
                    i += 1

                start = len(decoded)
                end = start + digit
                if end > len(word):
                    return False

                decoded += word[start: end]
                digit = 0
            # jy: 如果 abbr[i] 非数值字符(即单词的原字符), 则将该字符直接添加
            #    到 decoded 字符串之后;
            else:
                decoded += abbr[i]
                i += 1

        return decoded == word

    def validWordAbbreviation_jy2(self, word, abbr):
        # jy: 用于记录数值字符串和非数值字符串(数值与非数值分开单独记录)
        ls_ = []
        i = 0
        while i < len(abbr):
            # jy: 获取数值部分, 将其加入到 ls_ 中;
            digit_str = ""
            while i < len(abbr) and abbr[i].isdigit():
                digit_str += abbr[i]
                i += 1
            if digit_str != "":
                ls_.append(digit_str)

            # jy: 获取非数值部分, 将其加入到 ls_ 中;
            str_ = ""
            while i < len(abbr) and not abbr[i].isdigit():
                str_ += abbr[i]
                i += 1
            if str_ != "":
                ls_.append(str_)

        # jy: 基于 ls_ 进行解码,
        decoded = ""
        for i in ls_:
            if i.isdigit():
                start = len(decoded)
                end = start + int(i)
                # jy: 截止当前的 decoded 记录的是上一轮循环解码得到的字符串, 将其与 word 相
                #    同长度的前缀部分比较, 如果不相等则直接返回 False; 如果字符串的结尾下标
                #    也超出了 word 长度, 则也直接返回 False;
                if decoded != word[: len(decoded)] or end > len(word):
                    return False
                # jy: 解码拼接字符串;
                decoded += word[start: end]
            else:
                decoded += i

        return decoded == word


word = "internationalization"
abbr = "i12iz4n"
# Output: true
res = Solution().validWordAbbreviation_v1(word, abbr)
print(res)
res = Solution().validWordAbbreviation_jy(word, abbr)
print(res)
res = Solution().validWordAbbreviation_jy2(word, abbr)
print(res)

word = "apple"
abbr = "a2e"
# Output: false
res = Solution().validWordAbbreviation_v1(word, abbr)
print(res)
res = Solution().validWordAbbreviation_jy(word, abbr)
print(res)
res = Solution().validWordAbbreviation_jy2(word, abbr)
print(res)



