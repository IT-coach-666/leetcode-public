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
title_jy = "Count-Binary-Substrings(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.


Constraints:
1 <= s.length <= 10^5
s[i] is either '0' or '1'.
"""


class Solution:
    """
    记 prev_count 表示上一个连续的字符, current_count 表示当前连续的字符, 则符合条件的组合个数为 min(prev_count, current_count), 如 1110000, prev_count 等于3, current_count 等于4, 满足条件的组合为 min(3, 4) = 3, 即 111000, 1100, 10
    """
    def countBinarySubstrings(self, s: str) -> int:
        prev_count = 0
        current_count = 1
        count = 0

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                count += min(prev_count, current_count)
                prev_count, current_count = current_count, 1
            else:
                current_count += 1

        count += min(prev_count, current_count)

        return count


