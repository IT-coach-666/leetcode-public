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
title_jy = "Longest-Substring-with-At-Most-Two-Distinct-Characters(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string s, return the length of the longest substring that contains at most
two distinct characters.


Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.


Constraints:
1 <= s.length <= 10^4
s consists of English letters.
"""


import collections


class Solution:
    """
同 340_Longest-Substring-with-At-Most-K-Distinct-Characters.py, 将 k 设置为 2
    """
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        k = 2
        counter = collections.defaultdict(int)
        start = 0
        max_length = 0
        for end in range(len(s)):
            counter[s[end]] += 1
            if len(counter) > k:
                while start < len(s) and len(counter) > k:
                    counter[s[start]] -= 1
                    if counter[s[start]] == 0:
                        counter.pop(s[start])
                    start += 1
            max_length = max(max_length, end - start + 1)

        return max_length


s = "eceba"
# Output: 3
res = Solution().lengthOfLongestSubstringTwoDistinct(s)
print(res)

s = "ccaabbb"
# Output: 5
res = Solution().lengthOfLongestSubstringTwoDistinct(s)
print(res)


