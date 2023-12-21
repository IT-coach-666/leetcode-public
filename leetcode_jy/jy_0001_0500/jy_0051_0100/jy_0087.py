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
title_jy = "Scramble-String(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
We can scramble a string `s` to get a string `t` using the following algorithm:
1) If the length of the string is 1, stop.
2) If the length of the string is > 1, do the following:
   a) Split the string into two non-empty substrings at a random index, i.e.,
      if the string is `s`, divide it to `x` and `y` where `s = x + y`.
   b) Randomly decide to swap the two substrings or to keep them in the same
      order. i.e., after this step, `s` may become `s = x + y` or `s = y + x`.
   c) Apply step 1 recursively on each of the two substrings `x` and `y`.

Given two strings `s1` and `s2` of the same length, return `true` if `s2` is
a scrambled string of `s1`, otherwise, return `false`.

 
Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
# divide at random index:
  "great" --> "gr/eat"
# random decision is not to swap the two substrings and keep them in order:
  "gr/eat" --> "gr/eat" 
# apply the same algorithm recursively on both substrings. divide at random
# index each of them:
  "gr/eat" --> "g/r / e/at"
# random decision was to swap the first substring and to keep the second
# substring in the same order:
  "g/r / e/at" --> "r/g / e/at"
# again apply the algorithm recursively, divide "at" to "a/t":
  "r/g / e/at" --> "r/g / e/ a/t"
# random decision is to keep both substrings in the same order:
  "r/g / e/ a/t" --> "r/g / e/ a/t"

The algorithm stops now, and the result string is "rgeat" which is `s2`.
As one possible scenario led `s1` to be scrambled to `s2`, we return `true`.


Example 2:
Input: s1 = "abcde", s2 = "caebd"
Output: false


Example 3:
Input: s1 = "a", s2 = "a"
Output: true
 

Constraints:
1) s1.length == s2.length
2) 1 <= s1.length <= 30
3) `s1` and `s2` consist of lowercase English letters.
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/scramble-string/solutions/51990/miao-dong-de-qu-jian-xing-dpsi-lu-by-sha-yu-la-jia/
    """
    def isScramble_v1(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            if self.isScramble_v1(s1[:i], s2[:i]) and self.isScramble_v1(s1[i:], s2[i:]) or \
                    (self.isScramble_v1(s1[:i], s2[-i:]) and self.isScramble_v1(s1[i:], s2[:-i])):
                return True
        return False


s1 = "great"
s2 = "rgeat"
res = Solution().isScramble_v1(s1, s2)
# jy: true
print(res)


s1 = "abcde"
s2 = "caebd"
res = Solution().isScramble_v1(s1, s2)
# jy: false
print(res)


s1 = "a"
s2 = "a"
res = Solution().isScramble_v1(s1, s2)
# jy: true
print(res)


