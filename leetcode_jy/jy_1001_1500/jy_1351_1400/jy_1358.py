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
title_jy = "Number-of-Substrings-Containing-All-Three-Characters(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".

Example 3:
Input: s = "abc"
Output: 1


Constraints:
3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""


import collections


class Solution:
    """
解法1
a, b, c 每个数字都要出现一遍, 等价于需要出现3个不同的数字, 题目就转变成了 992. Subarrays with K Different Integers, 只是这里 k 为固定值3;
    """
    def numberOfSubstrings(self, s: str) -> int:
        return self._at_most_k(s, 3) - self._at_most_k(s, 2)

    def _at_most_k(self, nums, k):
        counter = collections.defaultdict(int)
        count = 0
        start = 0

        for end, n in enumerate(nums):
            counter[n] += 1

            while len(counter) > k:
                counter[nums[start]] -= 1

                if counter[nums[start]] == 0:
                    counter.pop(nums[start])

                start += 1

            count += end - start + 1

        return count


import collections


class Solution:
    """
解法2
和求解至多 k 个不同类似, 只是计算 count 的增量不是 end - start + 1, 而是 start, 对于子数组, 当跳出 while len(counter) == 3 的循环时, 构成的窗口满足包含3个不同的字符, 因为整个字符串只由3个不同的字符组成, 所以对于下述的子数组:
1.
2.
3.
4. ...
5.
共有 start - 1 - 0 + 1= start 个;
    """
    def numberOfSubstrings(self, s: str) -> int:
        start, count = 0, 0
        counter = collections.defaultdict(int)

        for end, c in enumerate(s):
            counter[c] += 1

            while len(counter) == 3:
                counter[s[start]] -= 1

                if counter[s[start]] == 0:
                    counter.pop(s[start])

                start += 1

            count += start

        return count


