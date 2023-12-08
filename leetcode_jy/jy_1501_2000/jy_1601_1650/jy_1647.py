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
title_jy = "Minimum-Deletions-to-Make-Character-Frequencies-Unique(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A string s is called good if there are no two different characters in s that have the same frequency.
Given a string s, return the minimum number of characters you need to delete to make s good.
The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:
Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).


Constraints:
1 <= s.length <= 10^5
s contains only lowercase English letters.
"""


import collections


class Solution:
    """
使用 Map 保存每个字符出现的次数, 同时使用一个 Set 用于保存所有唯一的频次, 遍历 Map, 如果当前字符出现的次数在 Set 中, 则不断将其减1, 然后将更新后的当前字符频次放入到 Set 中;
    """
    def minDeletions(self, s: str) -> int:
        counter = collections.Counter(s)
        count = 0
        visited = set()

        for key in counter.keys():
            while counter[key] > 0 and counter[key] in visited:
                counter[key] -= 1
                count += 1

            visited.add(counter[key])

        return count



