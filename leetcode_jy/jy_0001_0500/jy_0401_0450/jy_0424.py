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
title_jy = "Longest-Repeating-Character-Replacement(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given a string ``s`` and an integer ``k``. You can choose any character of the
string and change it to any other uppercase English character. You can perform this
operation at most ``k`` times. Return the length of the longest substring containing the
same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
"""


import collections


class Solution:
    """
解法1: 使用滑动窗口求解, 记录窗口中每个字符出现的次数, 当窗口的长度减去窗口中出现
次数最多的字符大于 k 时, 说明需要大于 k 次的操作才能将窗口中的字符都变为相同的字
符, 所以从窗口起始位置剔除一个字符
    """
    def characterReplacement_v1(self, s: str, k: int) -> int:
        start = 0
        max_length = 0
        counter = collections.defaultdict(int)

        for end, c in enumerate(s):
            counter[c] += 1

            if end - start + 1 - max(counter.values()) > k:
                counter[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length

    """
解法2: 对解法1的一个优化, 解法1每次都会判断 counter 中出现次数最多的字符, 可以优化
为维护至今遇到的出现次数最多的字符; 出现次数最多的字符并不一定在当前窗口中, 但不影
响最终结果, 因为最终结果要的是最长的窗口长度, 当出现次数最多的字符不在当前窗口中时,
说明在之前的窗口中, 也说明当前窗口没有一个字符的出现次数能超过之前的最大出现次数,
即当前窗口不可能是最优解
    """
    def characterReplacement_v2(self, s: str, k: int) -> int:
        start = 0
        max_count = 0
        max_length = 0
        counter = collections.defaultdict(int)

        for end, c in enumerate(s):
            counter[c] += 1
            max_count = max(max_count, counter[c])

            if end - start + 1 - max_count > k:
                counter[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length


s = "ABAB"
k = 2
# Output: 4
res = Solution().characterReplacement_v1(s, k)
print(res)


s = "AABABBA"
k = 1
# Output: 4
res = Solution().characterReplacement_v2(s, k)
print(res)


