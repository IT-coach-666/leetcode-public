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
title_jy = "Find-All-Anagrams-in-a-String(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two strings ``s`` and ``p``, return an array of all the start indices of p's
anagrams in ``s``. You may return the answer in any order.


Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc".
             The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation: The substring with start index = 0 is "ab", which is an anagram of "ab".
             The substring with start index = 1 is "ba", which is an anagram of "ab".
             The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
"""


from typing import List
import collections


class Solution:
    """
解法1(超出内存限制): 事先求出 p 的所有 anagram, 保存到 Set, 然后遍历 s 维护一个长度
为 len(p) 的窗口, 判断窗口中的字符串是否在 Set 中, 不过会超出内存限制
    """
    def findAnagrams_v1(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        anagrams = set()

        self._get_anagrams(p, len(p), '', anagrams)

        start, n = 0, len(s)
        chars_so_far = ''
        positions = []

        for c in s:
            chars_so_far += c

            if len(chars_so_far) < len(p):
                continue
            elif len(chars_so_far) > len(p):
                chars_so_far = chars_so_far[1:]
                start += 1

            if chars_so_far in anagrams:
                positions.append(start)

        return positions

    def _get_anagrams(self, s, n, anagram, anagrams):
        if len(anagram) == n:
            anagrams.add(anagram)

            return

        for i, c in enumerate(s):
            self._get_anagrams(s[0:i] + s[i+1:], n, anagram + c, anagrams)

    """
解法2: 解法 1 花了大量时间和空间在构建 p 的 anagram 上, 实际上并不需要构建出 p 的所
有 anagram, 因为 anagram 的一个特性就是每个字符的出现次数和 p 相同, 所以可以先求出 p
的所有字符出现的次数, 将其保存在 Map 中, 然后同样维护一个窗口, 以及窗口中各字符出现
的次数, 如果窗口大小超过 p 的长度, 则剔除窗口 start 位置处的字符, 并将 start 向右移
动一位, 同时将窗口的 current_counter 对应字符个数减1, 如果 current_counter 等于
counter, 则当前窗口中的字符串是 p 的 anagram
    """
    def findAnagrams_v2(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        start = 0
        positions = []
        counter = collections.Counter(p)
        current_counter = collections.defaultdict(int)

        for end, c in enumerate(s):
            current_counter[c] += 1
            current_length = end - start + 1

            if current_length < len(p):
                continue
            elif current_length > len(p):
                current_counter[s[start]] -= 1

                if current_counter[s[start]] == 0:
                    current_counter.pop(s[start])

                start += 1

            if current_counter == counter:
                positions.append(start)

        return positions


s = "cbaebabacd"
p = "abc"
# Output: [0,6]
res = Solution().findAnagrams_v1(s, p)
print(res)


s = "abab"
p = "ab"
# Output: [0,1,2]
res = Solution().findAnagrams_v1(s, p)
print(res)


