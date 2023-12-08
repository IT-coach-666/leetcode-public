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
tag_jy = "暴力求解 | 单词化的滑动窗口"


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
解法 4: 单词化的滑动窗口 
    """
    def findSubstring_v4(self, s: str, words: List[str]) -> List[int]:
        counter = collections.Counter(words)
        # jy: 字符串 s 的长度
        len_s = len(s) 
        # jy: 总单词数量
        num_word = len(words)
        # jy: 单个单词长度
        len_word = len(words[0]) 
        ls_res = []
        for i in range(len_word):
            s_i = s[i:]
            words_s_i = len(s_i) // len_word
            if words_s_i < num_word:
                break
            ls_s_i_word = [s_i[j * len_word: (j+1) * len_word] for j in range(words_s_i)]
            # jy: 仅用于调试时输出查看
            #print(ls_s_i_word, " === ", words)
            for j in range(words_s_i):
                if j + num_word > words_s_i:
                    break
                candidate_words = ls_s_i_word[j: j + num_word]
                # jy: 仅用于调试时输出查看
                #print("i=%s, j=%s, candidate_words = %s" % (i, j, candidate_words))
                if collections.Counter(candidate_words) == counter:
                    ls_res.append(i + j * len_word)
        return ls_res


    """
解法 5: 单词化的滑动窗口的更精细化写法; 性能极大提升, 但内存占用较多
    """
    def findSubstring_v5(self, s: str, words: List[str]) -> List[int]:
        # jy: 字符串 s 的长度
        len_s = len(s)
        # jy: 单词的数量 
        num_word = len(words)  
        # jy: 单词的长度
        len_word = len(words[0]) 
        ls_res = []
        # jy: 如果字符串 s 的长度小于所有单词拼接起来的长度, 则直接返回
        if len_s < num_word * len_word:
            return ls_res  
        # jy: 枚举每一个切分单词的起点, 共有 len_word 个起点
        for i in range(len_word):
            # jy: 以 i 为起点往后的完整单词数
            num_word_left = (len_s - i) // len_word
            # jy: i 之后的单词数已经不能满足要求, 直接退出
            if num_word_left < num_word:
                break

            # jy: 以下窗口滑动时, diff 总是每一轮都重新构建, 可参考解法 6 优化
            # jy: 单词数能满足要求, 构造固定长度窗口, 并不断向后滑动, 判断窗
            #     口内的单词是否满足要求
            for x in range(num_word_left):
                # jy: 记录滑动窗口中每个单词和 words 中对应单词的个数差值,
                #     diff 为空说明滑动窗口中的单词与 word 一致
                diff = {}
                # jy: 窗口不断滑动之后, 窗口内的单词数不再满足要求, 提前退出
                #     循环
                if num_word_left - x < num_word:
                    break
                # jy: 执行到此处表明窗口内的单词数能满足要求, 则取指定个数的
                #     单词数, 并判断是否满足要求;
                for j in range(num_word):
                    w = s[i + (x + j) * len_word: i + (x + j + 1) * len_word]
                    diff[w] = diff.get(w, 0) + 1
                # jy: 遍历 words, 进行做差
                for word in words:
                    diff[word] = diff.get(word, 0) - 1
                    # jy: 单词数为 0 时说明这个单词在滑动窗口和 words 的数目匹
                    #     配, 直接移除
                    if diff[word] == 0:
                        diff.pop(word)
                if not diff:
                    ls_res.append(i + x * len_word)
        return ls_res

    """
解法 6: 同解法 5, 但优化了每轮起点相同的滑动窗口移动过程中的字符统计: 总是移
除左侧一个单词, 并加入右侧一个单词, 避免了 diff 字典的频繁重操作

leetcode 提交的性能更优越
    """
    def findSubstring_v6(self, s: str, words: List[str]) -> List[int]:
        # jy: 字符串 s 的长度
        len_s = len(s)
        # jy: 单词的数量
        m = len(words)
        # jy: 单词的长度
        n = len(words[0])
        ls_res = []
        # jy: 如果字符串 s 的长度小于所有单词拼接起来的长度, 则直接返回
        if len_s < m * n:
            return ls_res
        # jy: 枚举每一个切分单词的起点, 共有 n 个起点
        for i in range(n):
            # jy: 记录滑动窗口中每个单词和 words 中对应单词的个数差值,
            #     diff 为空说明滑动窗口中的单词与 word 一致
            diff = {}
            # jy: 从起点 i 开始, 将前 m 个单词(滑动窗口中的单词)加入哈希
            #     表, j 表示第几个单词
            for j in range(m):
                # jy: 判断待提取的单词右侧下标是否越界, 如果越界则退出循环
                if i + (j + 1) * n > len_s:
                    break
                w = s[i + j * n : i + (j + 1) * n]
                diff[w] = diff.get(w, 0) + 1
            # jy: 遍历 words, 进行做差
            for word in words:
                diff[word] = diff.get(word, 0) - 1
                # jy: 单词数为 0 时说明这个单词在滑动窗口和 words 的数目匹
                #     配, 直接移除
                if diff[word] == 0:
                    diff.pop(word)
            # jy: 移动这个长度固定为 m*n 的滑动窗口, 左边界 left 为每个单词
            #     的起点, 滑动窗口范围 [left, left + m * n)
            for left in range(i, len_s - m * n + 1, n):
                # jy: 从第二个单词开始, 开始要加入新单词, 移除旧单词
                if left > i:
                    # jy: 右边界 right = left + (m - 1) * n 为要加入滑动窗口
                    #     的单词的起点; 滑动窗口中加入一个单词, 相当于差值 + 1
                    w = s[left + (m - 1) * n : left + m * n]
                    diff[w] = diff.get(w, 0) + 1 

                    if diff[w] == 0:
                        diff.pop(w)
                    # jy: 当前 left 的前一个单词是要移除的单词; 滑动窗口中移
                    #     除一个单词, 相当于差值-1
                    w = s[left - n : left]
                    diff[w] = diff.get(w, 0) - 1

                    if diff[w] == 0:
                        diff.pop(w)
                # 如果 diff 为空, 说明滑动窗口中的单词与 word 一致, left 即为子串起点
                if not diff:
                    ls_res.append(left)
        return ls_res


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


s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
# Output: [8]
res = Solution().findSubstring_v4(s, words)
print(res)


s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
# Output: [8]
res = Solution().findSubstring_v5(s, words)
print(res)


