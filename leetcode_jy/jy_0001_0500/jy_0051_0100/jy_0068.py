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
title_jy = "Text-Justification(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "字符串的格式处理 | IMP"


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
Input: 
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[  "This    is    an",
   "example  of text",
   "justification.  "]

Example 2:
Input:
words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
Output:
[ "What   must   be",
  "acknowledgment  ",
  "shall be        "]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified because it contains only one word.

Example 3:
Input:
words = ["Science", "is", "what", "we", "understand", "well", "enough", "to",
         "explain", "to", "a", "computer.", "Art", "is", "everything", "else",
         "we", "do"]
maxWidth = 20
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
解法 1: 字符串处理

题意: 给定一堆单词, 让你放在固定长度字符串里; 非末尾行的单词之间的空格尽可能相
同 (均匀的分配), 如果不能均分, 则从左到右尽可能均分

1) 两个单词之间至少有一个空格, 如果单词加空格后长度超过 maxWidth, 说明该单词放
   不下, 比如示例 1: 当 "this is an" 再加入 "example" 变成 "this is an example"
   时, 总长度超过 maxWidth, 所以这一行只能放下 "this"、"is"、"an" 这三个单词
2) "this is an" 长度小于 maxWidth, 因此考虑分配空格, 并保证左边空格数大于右边的
3) 最后一行要尽量靠左, 例如示例 2 的 "shall be "

针对上面三个问题, 有如下解决方案:
1) 先找到一行最多可以容下几个单词
2) 分配空格, 参考代码注解
3) 针对最后一行单独考虑
    """
    def fullJustify_v1(self, words: List[str], maxWidth: int) -> List[str]:
        ls_res = []
        # jy: 总共有 n 个单词
        n = len(words)
        i = 0

        def get_current_row_words(i):
            """
            返回的 left, i 表示当前行的单词为 words[left: i]
            """
            # jy: 题意中表明: words[i].length <= maxWidth, 因此一行至少能放
            #     下一个单词, cur_row_len 用于统计当前行的长度, 初始化为第一
            #     个单词的长度
            left = i
            cur_row_len = len(words[i])

            # jy: 尝试往 cur_row_len 中添加空格和单词, 并统计其长度
            i += 1
            while i < n:
                # jy: 如果当前行长度加上空格以及下一个单词后超过 maxWidth,
                #     则表明不能添加下一个单词, 退出循环; 否则加上 1 (表示
                #     空格的长度) 和下一个单词的长度
                if cur_row_len + 1 + len(words[i]) > maxWidth:
                    break
                cur_row_len += len(words[i]) + 1
                i += 1
            # jy: 返回的 left, i 表示 words[left: i] 为当前行的单词
            return left, i

        while i < n:
            left, i = get_current_row_words(i)
            # jy: 获取当前行可存放的单词列表
            ls_current_word = words[left: i]

            # jy: 如果是最后一行了, 则进行特殊处理: 单词用空格拼接后左对齐,
            #     不足 maxWidth 长度的部分在右侧填充空格
            if i == n :
                ls_res.append(" ".join(ls_current_word).ljust(maxWidth, " "))
                break

            # jy: 统计所有单词的长度
            len_all_word = sum(len(i) for i in ls_current_word)
            # jy: 统计分隔单词所需要的最少空格个数 (即为单词数减 1, 因为两个
            #     单词使用一个空格即可分隔)
            min_seperate_space_num = i - left - 1
            # jy: 一行中的总空格数
            len_all_space = maxWidth - len_all_word

            # jy: 如果 min_seperate_space_num 不为 0 (至少有两个单词), 则所有
            #     的空格需要在单词之间尽可能的均分
            if min_seperate_space_num:
                # jy: seperate_space_num: 尽可能均分的情况下, 单词之间的空格数
                #     num_remain: 不为 0 时, 表明单词之间不能完全均分, 因此左侧
                #                 的单词可多分一个空格, 直到分配完为止
                seperate_space_num, num_remain = divmod(len_all_space, min_seperate_space_num)
                # jy: 当前行的字符串拼接
                tmp = ""
                for word in ls_current_word:
                    if tmp:
                        tmp += " " * seperate_space_num
                        if num_remain:
                            tmp += " "
                            num_remain -= 1
                    tmp += word
                ls_res.append(tmp)
            # jy: 如果当前行只有一个单词, 则以上 min_seperate_space_num 为 0,
            #     该情况下直接使用第一个单词右侧补全空格即可
            else:
                ls_res.append(ls_current_word[0] + " " * (maxWidth - len_all_word))
                #ls_res.append(ls_current_word[0].ljust(maxWidth, " "))

        return ls_res


    """
解法 2: 更简洁的写法
    """
    def fullJustify_v2(self, words: List[str], maxWidth: int) -> List[str]:
        # jy: 存放结果列表
        ls_res = []

        # jy: 记录当前行可存放的单词
        ls_line_word = []
        # jy: 统计当前行存放的单词的长度
        len_words = 0
        # jy: 遍历单词, 不断将单词先往 ls_line_word 添加, 并统计
        for word in words:
            # jy: 如果 "当前行所有单词的长度 + 用于分隔单词所需的最少空格数
            #     + 当前单词的长度" >= maxWidth, 表明如果将当前 word 加入当
            #     前行, 再叠加上一个空格用于分隔该 word, 会使得总体长度超过
            #     maxWidth, 因此表明当前 word 不能再加入当前行中, 此时可对当
            #     前行进行处理并加入结果列表
            if len_words + len(ls_line_word) - 1 + len(word) >= maxWidth:
                # jy: 对当前行进行处理, 并加入结果列表: maxWidth - len_words
                #     即为当前行可存放的所有空格数, 此处即遍历所有空格, 并将
                #     其逐一均分到每个单词的后面 (注意: 最后一个单词之后不添
                #     加空格, 可以假设 ls_line_word 中有 3 个单词, 需在单词间
                #     均分 5 个空格为例进行思考)
                for i in range(maxWidth - len_words):
                    # 循环将每个空格依次加到每个单词之间的间距上
                    ls_line_word[i % max(len(ls_line_word)-1, 1)] += ' '
                # jy: 将所有含空格后缀的单词进行拼接后加入结果列表
                ls_res.append(''.join(ls_line_word))

                # jy: 重新初始化当前行可存放的单词以及所有单词的长度
                ls_line_word, len_words = [], 0       
  
            ls_line_word.append(word)
            len_words += len(word)
        return ls_res + [' '.join(ls_line_word).ljust(maxWidth)]



words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
res = Solution().fullJustify_v1(words, maxWidth)
print(res)
"""
["This    is    an",
 "example  of text",
 "justification.  "]
"""


words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
res = Solution().fullJustify_v1(words, maxWidth)
print(res)
"""
["What   must   be",
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
["Science  is  what we",
 "understand      well",
 "enough to explain to",
 "a  computer.  Art is",
 "everything  else  we",
 "do                  "]
"""

