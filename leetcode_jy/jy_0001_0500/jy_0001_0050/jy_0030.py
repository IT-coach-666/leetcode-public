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
You are given a string ``s`` and an array of strings ``words`` of the same
length. Return all starting indices of substring(s) in ``s`` that is a 
concatenation of each word in ``words`` exactly once, in any order, and 
without any intervening characters. You can return the answer in any order.


Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
             respectively. The output order does not matter, returning [9,0]
             is fine too.

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
解法 1: 暴力求解

注意: 题目中指出 words 中的子串长度均相同

从当前字符开始遍历 s, 依次遍历 len(words) 次, 求得 len(words) 个长度为
len(words[0]) 的字符串, 判断所有的字符串出现的次数是否等于 words 中所
有字符串出现的次数
    """
    def findSubstring_v1(self, s: str, words: List[str]) -> List[int]:
        # jy: 统计 words 中各子串的出现次数
        counter = collections.Counter(words)
        # jy: words 中的字符串长度相同, 用 word_length 记录
        word_length = len(words[0])
        positions = []
        # jy: 从字符串的起始位置开始遍历, 逐个判断后续连续
        #     len(words) * word_length 个字符是否可由 words
        #     中的子串构成 (列表中的每个字符串只能使用一次)
        # jy: 仅需循环到字符串的第 len(s) - len(words) * word_length 个位置
        #     即可, 因为后续的字符数已不足 len(words) * word_length 个字符串
        #     了, 肯定不满足条件
        for start in range(len(s) - len(words) * word_length + 1):
            current_counter = collections.defaultdict(int)
            # jy: 基于 start 构建 word 范围, 并统计该 word 出现的次数; 如果
            #     构建的 word 不在 counter 字典中或该 word 的出现次数大于
            #     counter 中的出现次数, 则直接终止当前内循环, 继续字符串的下
            #     一个字符开始判断
            for i in range(len(words)):
                word_start, word_end = start + i * word_length, start + (i+1) * word_length
                word = s[word_start:word_end]
                if word not in counter:
                    break

                current_counter[word] += 1

                if current_counter[word] > counter[word]:
                    break
            # jy: 如果遍历得到的 word 均满足条件, 则将当前字符串的起始位置存
            #     放到目标列表
            if current_counter == counter:
                positions.append(start)
        return positions

    """
解法 2: 对解法 1 的分割 word 部分进行改写
    """
    def findSubstring_v2(self, s: str, words: List[str]) -> List[int]:
        # jy: 统计 words 中各子串的出现次数
        counter = collections.Counter(words)
        # jy: words 中的字符串长度相同, 用 word_length 记录
        word_length = len(words[0])
        positions = []
        word_num = len(words)
        for start in range(len(s) - word_num * word_length + 1):
            current_counter = collections.defaultdict(int)
            candidate_str = s[start: start + word_num * word_length]
            ls_str = [candidate_str[i * word_length: (i+1) * word_length] for i in range(word_num)]
            if counter == collections.Counter(ls_str):
                positions.append(start)
        return positions


    """
解法 3: 思路同解法 1 和 2, 只是判断是否匹配部分先经过排序后再判断, 性能和
内存占用有所提升
    """
    def findSubstring_v3(self, s: str, words: List[str]) -> List[int]:
        mn, n = len(words) * len(words[0]), len(words[0])
        words.sort()
        return [i for i in range(len(s) - mn + 1) if sorted(findall(r'.{%d}' % n, s[i : i + mn])) == words]


    """
解法 4: 单词化的滑动窗口; 性能极大提升, 但内存占用较多
    """
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ls = len(s)         # 字符串s的长度
        m = len(words)      # 总单词数量
        n = len(words[0])   # 单个单词长度
        res = []
        if ls < m * n:
            return res      # 字符串s的长度小于所有单词拼接起来的长度，直接返回
        # 枚举每一个切分单词的起点，共有[0, n-1]个起点
        for i in range(n):
            diff = {}   # 记录滑动窗口中每个单词和words中对应单词的个数差值，diff为空，说明滑动窗口中的单词与word一致
            # 从起点i开始，将前m个子串单词加入哈希表，前m个单词就是首个滑动窗口里的单词; j表示第几个单词
            for j in range(m):
                if i + (j + 1) * n > ls:    # 当前提取的子串单词右边界越界
                    break
                w = s[i + j * n : i + (j + 1) * n]
                diff[w] = diff.get(w, 0) + 1
            # 遍历words，进行做差
            for word in words:
                diff[word] = diff.get(word, 0) - 1
                if diff[word] == 0:
                    diff.pop(word)  # 单词数目为0，说明这个单词在滑动窗口和words的数目匹配，直接移除；
            # 移动这个长度固定为m*n的滑动窗口，左边界left为每个单词的起点，滑动窗口范围[left, left + m * n)
            for left in range(i, ls - m * n + 1, n):
                # 从第二个单词开始，开始要加入新单词，移除旧单词
                if left > i:
                    w = s[left + (m - 1) * n : left + m * n]    # 从右边界right = left + (m - 1) * n，为要加入滑动窗口的单词的起点
                    diff[w] = diff.get(w, 0) + 1    # 滑动窗口中加入一个单词，相当于差值+1
                    if diff[w] == 0:
                        diff.pop(w)
                    w = s[left - n : left]          # 当前left的前一个单词是要移除的单词
                    diff[w] = diff.get(w, 0) - 1    # 滑动窗口中移除一个单词，相当于差值-1
                    if diff[w] == 0:
                        diff.pop(w)
                # diff为空，说明滑动窗口中的单词与word一致；left即为子串起点
                if not diff:
                    res.append(left)
        return res


s = "barfoothefoobarman"
words = ["foo","bar"]
# Output: [0, 9]
res = Solution().findSubstring_v1(s, words)
print(res)


s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
# Output: []
res = Solution().findSubstring_v1(s, words)
print(res)


s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
# Output: [6, 9, 12]
res = Solution().findSubstring_v1(s, words)
print(res)


s = "barfoothefoobarman"
words = ["foo","bar"]
# Output: [0, 9]
res = Solution().findSubstring_v2(s, words)
print(res)


