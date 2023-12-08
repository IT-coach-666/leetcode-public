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
title_jy = "Replace-the-Substring-for-Balanced-String(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.
A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.
Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.
Return 0 if the string is already balanced.

Example 1:
Input: s = "QWER"
Output: 0
Explanation: s is already balanced.

Example 2:
Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

Example 3:
Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER".

Example 4:
Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".


Constraints:
1 <= s.length <= 10^5
s.length is a multiple of 4
s contains only 'Q', 'W', 'E' and 'R'.
"""


import collections


class Solution:
    """
使用滑动窗口求解, 首先计算出所有字符的出现次数, 遍历字符串, 每次遍历时将对应字符出现的次数减1, 同时维护一个滑动窗口, 和一般的滑动窗口不同, 常见的滑动窗口是当窗口内的元素达到某个条件后进行窗口调整, 这里则是当窗口外的元素达到某个条件后进行窗口调整, 即当窗口外的每个字符个数都小于等于时, 说明窗口内的字符可能需要调整, 需要调整的次数就是窗口的长度即 end - start + 1, 为什么等于窗口的长度? 因为字符串只由 Q, W, E, R 四个字符组成, 字符串的长度始终是4的倍数, 所以字符串必然是可以被修改为平衡的, 当窗口外的所有字符的个数都小于时, 假设每个字符的个数距离为, 窗口长度为 k, 窗口内字符个数加上窗口外字符个数等于所有字符个数, 有;
    """
    def balancedString(self, s: str) -> int:
        counter = collections.Counter(s)
        n = len(s)
        count = n
        start = 0

        for end, c in enumerate(s):
            counter[c] -= 1

            while start < n and all(n # 4 >= counter[c] for c in 'QWER'):
                count = min(count, end - start + 1)
                counter[s[start]] += 1
                start += 1

        return count


