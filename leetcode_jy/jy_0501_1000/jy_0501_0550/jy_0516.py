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
title_jy = "Longest-Palindromic-Subsequence(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string ``s``, find the longest palindromic subsequence's length in ``s``.
A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining elements.


Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".


Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
"""


from typing import List
from functools import lru_cache
from collections import defaultdict
import bisect


class Solution:
    """
动态规划: 记 dp[i][j] 表示 s[i] 到 s[j] 的最长回文子串的长度, 则:
1) 当 s[i] == s[j] 时, 这两个字符本身已构成回文, 只需要进一步看 s[i+1] 到 s[j-1] 这个子串的
   回文长度(即使 s[i+1] 到 s[j-1] 之间没有能构成回文的子串, 即 dp[i+1][j-1] 为 0, 可以当做
   将其全部删除, 删除后 s[i] 与 s[j] 也是长度为 2 的回文), 即:
   dp[i][j] = dp[i+1][j-1] + 2
2) 当 s[i] != s[j] 时, 说明 s[i] 和 s[j] 必然不会同时成为回文的组成部分, 所以要分情况看当
    s[i] 或 s[j] 成为回文计算的一部分时的字符串长度, 即:
    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

因为计算 dp[i][j] 依赖 dp[i+1][j-1] 和 dp[i+1][j] 以及 dp[i][j-1], 所以构造 dp 需要从 s 的
尾部向头部遍历(i 从后向前遍历, j 从前向后遍历);
    """
    def longestPalindromeSubseq_v1(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        # jy: dp 先均初始化为 0 (dp[i][i] 应全都初始化为 1, 在 for 循环中会进行该初始化过程; 也可以在
        #     此处补充并在 for 循环中去除);
        dp = [[0] * n for _ in range(n)]
        # jy: i 从最后一个位置坐标 n-1 开始向前遍历至第一个位置坐标 0;
        for i in range(n-1, -1, -1):
            # jy: 初始化当前位置字符对应的最长回文长度为 1 (单个字符可以看成是长度为 1 的回文);
            dp[i][i] = 1
            # jy: j 从位置坐标 i 的下一个位置 i+1 (因为 dp[i][i] 已知为 1) 遍历至字符串末尾;
            for j in range(i+1, n):
                # jy: 当 s[i] == s[j] 时, 这两个字符本身已构成回文, 只需要进一步看 s[i+1] 到 s[j-1] 这
                #     个子串的回文长度(即使 s[i+1] 到 s[j-1] 之间没有能构成回文的子串, 即 dp[i+1][j-1]
                #     为 0, 可以当做将其全部删除, 删除后 s[i] 与 s[j] 也是长度为 2 的回文), 即:
                #     dp[i][j] = dp[i+1][j-1] + 2
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                # jy: 当 s[i] != s[j] 时, 说明 s[i] 和 s[j] 必然不会同时成为回文的组成部分, 所以要分情
                #     况看当 s[i] 或 s[j] 成为回文计算的一部分时的字符串长度, 即:
                #     dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # jy: 最后即返回第一个字符(下标为 0)到最后一个字符(下标为 n-1)的最长回文的长度;
        return dp[0][n-1]

    """
解法 2: 递归 + lru_cache; 执行效率和内存占比都极佳(去除 lru_cache 会超时);
参考: https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/python-ji-yi-hua-di-gui-99-by-qubenhao-c3iv/

如果某字母组成最大的回文子串, 则最大回文子串的两端一定是某字符的最左边和最右边的坐标; 如 "bbbabc",
"b" 如果是最终答案的回文串的两端, 一定是第一个 "b" 和最后一个 "b", 因为其他任意 "b" 的组合都比它更
小(剩余字符串总是被最贪心的取法覆盖); 而以这两个 "b" 为两端, 剩下的字符串中能取出多大的回文子序列，
就构成了这两个 "b" 的答案, 也就是递归的思想;
    """
    def longestPalindromeSubseq_v2(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        n = len(s)
        # jy: 统计字符串中的每个字母的所在位置下标(最终保存每个字符的下标列表均为有序列表)
        char_idx = defaultdict(list)
        for i, c in enumerate(s):
            char_idx[c].append(i)

        # jy: 注意, lru_cache 装饰器不能去除, 否则会超时;
        @lru_cache(None)
        def dfs(low, high):
            if low >= high:
                return low == high
            max_len = 0
            # jy: 遍历字符串 s 中的各个字符(不需重复遍历相同的字符), 找出字符串中;
            for char in set(s):
                # jy: 在 s 的位置下标 low 之后(包含 low)的下标中找出第一个 char 的所在下标;
                #     (如果 low 下标对应的字符就是 char, 则得到的 left 就是 low; 否则 left
                #     会大于 low);
                left = bisect.bisect_left(char_idx[char], low)
                # jy: 在 s 的位置下标 high 之后(包含 high)的下标中找出第一个 char 的所在下标;
                right = bisect.bisect_left(char_idx[char], high)
                if right == len(char_idx[char]) or char_idx[char][right] > high:
                    right -= 1
                max_len = max(max_len,
                              dfs(char_idx[char][left] + 1, char_idx[char][right] - 1) + 2
                              ) if right > left else max(max_len, 1)
            return max_len

        return dfs(0, n - 1)


s = "bbbab"
# Output: 4
res = Solution().longestPalindromeSubseq_v1(s)
print(res)


s = "cbbd"
# Output: 2
res = Solution().longestPalindromeSubseq_v2(s)
print(res)


