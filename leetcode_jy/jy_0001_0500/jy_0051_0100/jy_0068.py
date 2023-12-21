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
title_jy = "Text-Justification(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of strings `words` and a width `maxWidth`, format the text such
that each line has exactly `maxWidth` characters and is fully (left and right)
justified.

You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has
exactly `maxWidth` characters.

Extra spaces between words should be distributed as evenly as possible. If the
number of spaces on a line does not divide evenly between words, the empty 
slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is 
inserted between words.

Note:
1) A word is defined as a character sequence consisting of non-space characters only.
2) Each word's length is guaranteed to be greater than 0 and not exceed `maxWidth`.
3) The input array `words` contains at least one word.
 

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[  "This    is    an",
   "example  of text",
   "justification.  "]

Example 2:
Input: words = ["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth = 16
Output:
[ "What   must   be",
  "acknowledgment  ",
  "shall be        "]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified because it contains only one word.

Example 3:
Input: words = ["Science", "is", "what", "we", "understand", "well", "enough", "to",
                "explain", "to", "a", "computer.", "Art", "is", "everything", "else",
                "we", "do"], maxWidth = 20
Output:
[ "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "]
 

Constraints:
1) 1 <= words.length <= 300
2) 1 <= words[i].length <= 20
3) words[i] consists of only English letters and symbols.
4) 1 <= maxWidth <= 100
5) words[i].length <= maxWidth
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/text-justification/solutions/6314/shun-zhao-si-lu-xiang-by-powcai/

    """
    def fullJustify_v1(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        i = 0

        def one_row_words(i):
            # 至少 一行能放下一个单词, cur_row_len
            left = i
            cur_row_len = len(words[i])
            i += 1
            while i < n:
                # 当目前行 加上一个单词长度 再加一个空格
                if cur_row_len + len(words[i]) + 1 > maxWidth:
                    break
                cur_row_len += len(words[i]) + 1
                i += 1
            return left, i

        while i < n:
            left, i = one_row_words(i)
            # 该行几个单词获取
            one_row = words[left:i]
            # 如果是最后一行了
            if i == n :
                res.append(" ".join(one_row).ljust(maxWidth," "))
                break
            # 所有单词的长度
            all_word_len = sum(len(i) for i in one_row)
            # 至少空格个数
            space_num = i - left - 1
            # 可以为空格的位置
            remain_space = maxWidth - all_word_len
            # 单词之间至少几个空格,还剩几个空格没用
            if space_num:
                a, b = divmod(remain_space, space_num)
            # print(a,b)
            # 该行字符串拼接
            tmp = ""
            for word in one_row:
                if tmp:
                    tmp += " " * a
                    if b:
                        tmp += " "
                        b -= 1
                tmp += word
            #print(tmp, len(tmp))
            res.append(tmp.ljust(maxWidth, " "))
        return res



words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
res = Solution().fullJustify_v1(words, maxWidth)
print(res)
"""
[  "This    is    an",
   "example  of text",
   "justification.  "]
"""


words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
res = Solution().fullJustify_v1(words, maxWidth)
print(res)
"""
[ "What   must   be",
  "acknowledgment  ",
  "shall be        "]
"""


words = ["Science", "is", "what", "we", "understand", "well", "enough", "to",
         "explain", "to", "a", "computer.", "Art", "is", "everything", "else",
         "we", "do"]
maxWidth = 20
res = Solution().fullJustify_v1(words, maxWidth)
print(res)
"""
[ "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "]
"""

