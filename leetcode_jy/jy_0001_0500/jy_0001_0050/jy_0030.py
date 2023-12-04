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
title_jy = "Substring-with-Concatenation-of-All-Words(sring)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given a string ``s`` and an array of strings ``words`` of the same length.
Return all starting indices of substring(s) in ``s`` that is a concatenation of each
word in ``words`` exactly once, in any order, and without any intervening characters.
You can return the answer in any order.


Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
             The output order does not matter, returning [9,0] is fine too.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]



Constraints:
1 <= s.length <= 10^4
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
"""

import collections
from typing import List


class Solution:
    """
暴力求解, 遍历 s, 从当前字符开始, 依次遍历 len(words) 次, 求得 len(words) 个长度为
len(words[0]) 的字符串, 判断所有的字符串出现的次数是否等于 words 中所有字符串出现的次数
    """
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # jy: 统计 words 中的字符串的出现次数;
        counter = collections.Counter(words)
        # jy: words 中的字符串长度相同, 用 word_length 记录;
        word_length = len(words[0])
        positions = []
        # jy: 暴力求解, 从字符串的起始位置逐个判断其后续的连续 len(words)*word_length 个
        #    字符是否可由 words 中的字符串构成(列表中的每个字符串只能使用一次); 仅需循环
        #    到字符串的第 len(s) - len(words) * word_length 个位置即可, 因为后续位置开始
        #    已经不足 len(words) * word_length 个字符串了, 肯定不满足条件;
        for start in range(len(s) - len(words) * word_length + 1):
            current_counter = collections.defaultdict(int)
            # jy: 基于 start 构建 word 范围, 并统计该 word 出现的次数; 如果构建的 word 不在
            #    counter 字典中或者该 word 的出现次数大于 counter 中的出现次数, 则直接终止
            #    当前内循环, 继续字符串的下一个字符开始判断;
            for i in range(len(words)):
                word_start, word_end = start + i * word_length, start + (i+1) * word_length
                word = s[word_start:word_end]
                current_counter[word] += 1

                if word not in counter:
                    break

                if current_counter[word] > counter[word]:
                    break
            # jy: 如果遍历得到的 word 均满足条件, 则将当前字符串的起始位置存放到目标列表;
            if current_counter == counter:
                positions.append(start)

        return positions


s = "barfoothefoobarman"
words = ["foo","bar"]
# Output: [0,9]
res = Solution().findSubstring(s, words)
print(res)


s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
# Output: []
res = Solution().findSubstring(s, words)
print(res)


s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
# Output: [6,9,12]
res = Solution().findSubstring(s, words)
print(res)


