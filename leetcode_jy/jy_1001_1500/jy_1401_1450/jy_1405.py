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
title_jy = "Longest-Happy-String(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.
Given three integers a, b and c, return any string s, which satisfies following conditions:
s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 2, b = 2, c = 1
Output: "aabbc"

Example 3:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.


Constraints:
0 <= a, b, c <= 100
a + b + c > 0
"""


# Time Limit Exceeded!
class Solution:
    """
解法1(超时)
直接搜索, 不过会超时;
    """
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = {
            0: 'a',
            1: 'b',
            2: 'c'
        }

        return self._dfs([a, b, c], '', chars)

    def _dfs(self, counts, s, chars):
        if counts[0] == 0 and counts[1] == 0 and counts[2] == 0:
            return s

        longest = s

        for i, count in enumerate(counts):
            if count == 0 or s[-2:] == chars[i] * 2:
                continue

            new_counts = [x for x in counts]
            new_counts[i] -= 1
            current = self._dfs(new_counts, s + chars[i], chars)

            if len(current) > len(longest):
                longest = current

        return longest

import heapq


class Solution:
    """
解法2
首先构造一个大顶堆来保存 a, b, c 和其对应的字符, 由于 Python 的堆默认是小顶堆, 所以将数量取反模拟大顶堆, 之所以使用大顶堆是要优先使用数量多的字符, 避免最后剩下的字符都是一样的; 每次从堆中取两个字符的数量, 如果两个字符的数量相等, 那么我们可以交替使用两个字符来构造最后的字符串, 如 abababab...; 如果两个字符的数量不相等, 那么对数量多的字符使用2个字符, 数量少的字符使用一个字符来构造最后的字符串, 如 aabaabaab..., 最后将剩余字符的个数重新添加到堆中;
    """
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        counts = [(-count, char) for count, char in
                  [(a, 'a'), (b, 'b'), (c, 'c')] if count > 0]
        heapq.heapify(counts)

        while len(counts) > 1:
            count1, char1 = heapq.heappop(counts)
            count2, char2 = heapq.heappop(counts)

            if count1 == count2:
                result.extend([char1, char2])
                count1 += 1
                count2 += 1
            else:
                result.extend([char1, char1, char2])
                count1 += 2
                count2 += 1

            if count1 < 0:
                heapq.heappush(counts, (count1, char1))

            if count2 < 0:
                heapq.heappush(counts, (count2, char2))

        if counts:
            count, char = heapq.heappop(counts)
            result.extend([char] * min(2, -count))

        return ''.join(result)


