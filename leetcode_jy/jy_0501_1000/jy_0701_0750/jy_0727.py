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
title_jy = "Minimum-Window-Subsequence(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given strings ``s1`` and ``s2``, return the minimum contiguous substring part
of ``s1``, so that ``s2`` is a subsequence of the part. If there is no such
window in ``s1`` that covers all characters in ``s2``, return the empty string
"". If there are multiple such minimum-length windows, return the one with the
left-most starting index.


Example 1:
Input: s1 = "abcdebdde", s2 = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of s2 in the window must occur in order.

Example 2:
Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
Output: ""


Constraints:
1 <= s1.length <= 2 * 10^4
1 <= s2.length <= 100
s1 and s2 consist of lowercase English letters.
"""


import sys


class Solution:
    """
解法1: 动态规划: 记 dp[i][j] 表示从 s1 字符串开头到下标位置 i (即 s1[0: i+1]) 中, 包含
s2 字符串开头到下标位置 j (即 s2[0: j+1]) 对应的子序列的最远下标位置(如果不能包含 s2[1: j+1]
子序列, 则值为 -1; 注意, 不能为 0, 因为 0 表示字符串的初始下标, 有可能初始下标是一个包
含了子序列的有效下标);

如: s1 = 'abcde', s2 = 'bd', 则 dp[3][1] = 1

最后逐个遍历 s1 中各个位置下标, 找出满足条件的下标位置(假如 s1 的下标位置 i 满足条件, 则
dp[i][n-1] 为一个非 -1 的有效数值, 该数值表示截止 s1 的当前下标位置 i, 包含 s2 的子序列的
s1 中的最远下标位置), 依据下标位置求得有效的窗口大小: i - dp[i][n-1] + 1; 后续如果仍有有
效下标位置, 则会有新的窗口, 如果新窗口更小, 则对最小窗口进行更新, 最终即求得最小窗口;

参考: https://www.cnblogs.com/haoweizh/p/10238670.html
    """
    def minWindow_v1(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        # jy: dp[i][j] 表示从 s1 字符串开头到下标位置 i (即 s1[0: i+1]) 中, 包含 s2 字符串开头
        #     到下标位置 j (即 s2[0: j+1]) 对应的子序列的最远下标位置(如果不能包含 s2[1: j+1]
        #     子序列, 则值为初始值 -1; 注意, 不能为 0, 因为 0 表示字符串的初始下标, 有可能初始
        #     下标是一个包含了子序列的有效下标);
        dp = [[-1] * n for _ in range(m)]
        # jy: 遍历 s1 字符串的下标位置, 如果字符 s[i] 与 s2[0] 相等, 则 dp[i][0] 更新为 i, 表示
        #     从 s1 开头到下标位置 i 的子串中, 包含 s2[0] 子序列的 s1 中的最远下标位置为 i;
        for i in range(m):
            if s1[i] == s2[0]:
                dp[i][0] = i
        # jy: 遍历 s2 字符串的下标位置 j, 求 dp[i][j] 的值; (j 从下标位置 1 开始, 因为下标位置 0 的
        #     dp[i][0] 已经在上一轮 for 循环中全部计算得到)
        for j in range(1, n):
            # jy: start 记录截止 s1 字符串的下标位置 i 为止, 包含 s2[: j+1] 子序列的最远位置下标;
            start = -1
            # jy: 遍历 s1 字符串的下标位置 i (从 0 开始遍历)
            for i in range(m):
                if s1[i] == s2[j]:
                    dp[i][j] = start
                start = max(start, dp[i][j-1])

        # jy: 依据 dp 结果的最后一列获取满足要求的最小窗口;
        min_length, start = sys.maxsize, -1
        # jy: 遍历 s1 字符串的字符下标, 找出使得 dp[i][n-1] 不为 -1 的下标 i, 此时的
        #     dp[i][n-1] 的值为截止 s1 当前下标位置 i 之前的子串中, 包含了整个 s2 子
        #     序列的最远起始下标位置;
        for i in range(m):
            if dp[i][n-1] == -1:
                continue

            current_length = i - dp[i][n-1] + 1

            if current_length < min_length:
                min_length = current_length
                start = dp[i][n-1]

        return s1[start:start + min_length] if start != -1 else ''

    """
JY: 滑动窗口;  待 leetcode 验证;

验证不通过:
"jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
"k"
    """
    def minWindow_v2(self, s1, s2):
        # jy: i 指向 s1 的下标位置, 初始化为 0 下标;
        i = 0
        min_window = (None, None)
        while i < len(s1):
            # jy: j 指向 s2 的下标位置, 初始化为 0 下标;
            j = 0

            end = None
            while j < len(s2) and i < len(s1) and s1[i] != s2[j]:
                i += 1
            j += 1
            start = i
            while j < len(s2) and i < len(s1):
                if s1[i] == s2[j]:
                    j += 1
                i += 1

            if j == len(s2):
                end = i-1
            if start and end:
                if None in min_window:
                    min_window = (start, end)
                elif end - start < min_window[1] - min_window[0]:
                    min_window = (start, end)

            i = start + 1
        return "" if None in min_window else s1[min_window[0]: min_window[1] + 1]


s1 = "abcdebdde"
s2 = "bde"
#Output: "bcde"
res = Solution().minWindow_v1(s1, s2)
print(res)
res = Solution().minWindow_v2(s1, s2)
print(res)

s1 = "abedc"
s2 = "bde"
#Output: ""
res = Solution().minWindow_v1(s1, s2)
print(res)
res = Solution().minWindow_v2(s1, s2)
print(res)


s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
s2 = "u"
#Output: ""
res = Solution().minWindow_v1(s1, s2)
print(res)
res = Solution().minWindow_v2(s1, s2)
print(res)


