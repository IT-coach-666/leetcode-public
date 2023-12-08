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
title_jy = "Isomorphic-Strings(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two strings s and t, determine if they are isomorphic. Two strings s and t are
isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character, but a character
may map to itself.



Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true



Constraints:
1 <= s.length <= 5 * 10^4
t.length == s.lengths and t consist of any valid ascii character.
"""


class Solution:
    """
为每个字符建立 s 到 t 和 t 到 s 的映射的 Map, 如果当前字符都不在映射中, 则将其加入到两
个 Map 中, 否则判断两个映射的对应值是否相同, 不同则返回 false;
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        # jy: 如果长度都不相等, 则肯定非同构(非 isomorphic)
        if len(s) != len(t):
            return False
        # jy: 记录 s 到 t 之间的 map 关系;
        s2t = {}
        # jy: 记录 t 到 s 之间的 map 关系;
        t2s = {}
        # jy: 遍历字符串 s,
        for i, c in enumerate(s):
            if c not in s2t and t[i] not in t2s:
                s2t[c] = t[i]
                t2s[t[i]] = c
            # jy: and 或者 or 都可以, 见 isIsomorphic_jy 中的分析;
            #elif s2t.get(c, '') != t[i] or t2s.get(t[i], '') != c:
            elif s2t.get(c, '') != t[i] and t2s.get(t[i], '') != c:
                return False

        return True


    """
注意: 单边匹配是不对的, 如以下逻辑即为单边匹配逻辑, 针对以下 s 和 t 则不能正确判
      断(预期为 Fasle, 但输出结果为 True):
s: "badc"
t: "baba"
    """
    def isIsomorphic_jy_false(self, s: str, t: str) -> bool:
        s2t = {}
        for char_s, char_t in zip(s, t):
            if char_s not in s2t:
                s2t[char_s] = char_t
            elif s2t[char_s] != char_t:
                return False
        return True


    def isIsomorphic_jy(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        for char_s, char_t in zip(s, t):
            if char_s not in s2t and char_t not in t2s:
                s2t[char_s] = char_t
                t2s[char_t] = char_s
            # jy: 以下 and 或 or 逻辑都可行, 当字符串的大部分都是同构的情况下, 使用 and 更
            #    高效, 因为此时 and 左边的 != 逻辑通常不成立, 就不再需要进一步判断 and 右
            #    边了; 反之, 当字符串的大部分都非同构的情况下, or 逻辑更高效;
            elif s2t.get(char_s, "") != char_t or t2s.get(char_t, "") != char_s:
            #elif s2t.get(char_s, "") != char_t and t2s.get(char_t, "") != char_s:
                return False
        return True


s = "egg"
t = "add"
# Output: true
res = Solution().isIsomorphic(s, t)
print(res)


s = "foo"
t = "bar"
# Output: false
res = Solution().isIsomorphic(s, t)
print(res)


s = "paper"
t = "title"
# Output: true
res = Solution().isIsomorphic(s, t)
print(res)


