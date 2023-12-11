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
title_jy = "Count-Unique-Characters-of-All-Substrings-of-a-Given-String(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Let's define a function countUniqueChars(s) that returns the number of unique characters on s.
For example if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.
Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

Example 1:
Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:
Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.

Example 3:
Input: s = "LEETCODE"
Output: 92


Constraints:
1 <= s.length <= 105
s consists of uppercase English letters only.
"""


import collections


# Time Limit Exceeded!
class Solution:
    """
解法1(超时): 记 dp[i][j] 表示 s[i: j+1] 中唯一字符的个数, 同时 dp[i][j] 维护
s[i: j+1] 中唯一的字符及重复的字符;
    """
    def uniqueLetterString_v1(self, s: str) -> int:
        n = len(s)
        dp = [[[0, set(), set()] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = [1, set(s[i]), set()]

            for j in range(i+1, n):
                prev_unique_count = dp[i][j-1][0]
                prev_unique_letters = dp[i][j-1][1]
                prev_duplicate_letters = dp[i][j-1][2]

                if s[j] in prev_unique_letters:
                    dp[i][j] = [prev_unique_count - 1,
                                prev_unique_letters - {s[j]},
                                prev_duplicate_letters | {s[j]}]
                elif s[j] in prev_duplicate_letters:
                    dp[i][j] = [prev_unique_count,
                                prev_unique_letters,
                                prev_duplicate_letters]
                else:
                    dp[i][j] = [prev_unique_count + 1,
                                prev_unique_letters | {s[j]},
                                prev_duplicate_letters]

        count = 0

        for i in range(n):
            for j in range(n):
                count += dp[i][j][0]

        return count


    """
解法2: 题目要求的是每个子串中唯一字符的个数, 换个角度想, 这个等价于字符串中每
个字符在所有子串中只出现一次的子串数量和; 首先使用一个 Map 记录每个字符在 s 中
的位置, 然后遍历每个字符的出现位置, 例如对于位置 a, b, c 来说, 仅包含 b 位置的
子串范围是 [a + 1, c - 1], 其中包含 b 的子串个数为 len([a+1, b]) * len([b, c-1])
    """
    def uniqueLetterString_v2(self, s: str) -> int:
        n = len(s)
        positions = collections.defaultdict(list)

        for i, c in enumerate(s):
            positions[c].append(i)

        count = 0

        for position in positions.values():
            for i in range(len(position)):
                prev = position[i-1] if i > 0 else -1
                next = position[i+1] if i < len(position) - 1 else n
                count += (position[i] - prev) * (next - position[i])

        return count


s = "ABC"
# Output: 10
res = Solution().uniqueLetterString_v1(s)
print(res)


s = "ABA"
# Output: 8
res = Solution().uniqueLetterString_v1(s)
print(res)


s = "LEETCODE"
# Output: 92
res = Solution().uniqueLetterString_v2(s)
print(res)



