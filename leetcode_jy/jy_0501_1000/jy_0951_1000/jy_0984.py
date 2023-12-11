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
title_jy = "String-Without-AAA-or-BBB(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two integers a and b, return any string s such that:
s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.

Example 1:
Input: a = 1, b = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.

Example 2:
Input: a = 4, b = 1
Output: "aabaa"


Constraints:
0 <= a, b <= 100
It is guaranteed such an s exists for the given a and b.
"""


import heapq


class Solution:
    """
同 1405. Longest Happy String;
    """
    def strWithout3a3b(self, a: int, b: int) -> str:
        heap = [(-a, 'a'), (-b, 'b')]
        heapq.heapify(heap)
        result = []

        while len(heap) > 1:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)

            if count1 == count2:
                result.extend([char1, char2])
                count1 += 1
                count2 += 1
            else:
                result.extend([char1, char1, char2])
                count1 += 2
                count2 += 1

            if count1 < 0:
                heapq.heappush(heap, (count1, char1))

            if count2 < 0:
                heapq.heappush(heap, (count2, char2))

        if heap:
            count, char = heapq.heappop(heap)
            result.extend([char] * -count)

        return ''.join(result)


