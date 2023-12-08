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
title_jy = "Palindrome-Partitioning-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string ``s``, partition ``s`` such that every substring of the partition is a
palindrome. Return the minimum cuts needed for a palindrome partitioning of ``s``.


Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1


Constraints:
1 <= s.length <= 2000
s consists of lower-case English letters only.
"""


class Solution:
    """
记 dp[i] 表示 s[0: i+1] 构成回文子串最少需要切割多少次
遍历字符串, 以当前字符或前一个字符和当前字符为中心向两边扩展判断是否是回文
(以 "bab" 和 "baab" 为例进行思考)

JY: 也可以基于 131_Palindrome-Partitioning.py 的解法, 将最终结果列表中的最短列表长度减 1 即可;
    """
    def minCut(self, s: str) -> int:
        n = len(s)
        # jy: 初始化 dp 长度与 s 长度相同, 对应的值为 s 的各个位置的字符下标;
        dp = list(range(n))

        for middle in range(1, n):
            # jy: (以 "bab" 和 "baab" 为例进行思考)
            # jy: 以当前字符为中心向两边扩展判断是否是回文
            self._dp(middle, middle, dp, s)
            # jy: 以当前字符的前一个字符和当前字符为中心向两边扩展判断是否是回文;
            self._dp(middle - 1, middle, dp, s)

        return dp[-1]

    def _dp(self, start, end, dp, s):
        """
        以 s[start: end + 1] 为中心向两边扩展判断是否是回文, 如果是回文, 则对 dp[end]
        进行更新, 更新为 dp[start - 1] + 1
        """
        while start >= 0 and end < len(s) and s[start] == s[end]:
            dp[end] = min(dp[end], 0 if start == 0 else dp[start - 1] + 1)
            start -= 1
            end += 1


s = "aab"
# Output: 1
res = Solution().minCut(s)
print(res)


s = "a"
# Output: 0
res = Solution().minCut(s)
print(res)


s = "ab"
# Output: 1
res = Solution().minCut(s)
print(res)


