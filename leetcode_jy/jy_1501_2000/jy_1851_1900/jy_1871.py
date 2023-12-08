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
title_jy = "Jump-Game-VII(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:
i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

Example 1:
Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3.
In the second step, move from index 3 to index 5.

Example 2:
Input: s = "01101110", minJump = 2, maxJump = 3
Output: false


Constraints:
2 <= s.length <= 10^5
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length
"""


# Time Limit Exceeded!
class Solution:
    """
解法1(超时)
和 1696. Jump Game VI 的解法1一样, 记 dp[i] 表示能从起始位置跳到 i 处, 则只要能从起始位置跳到 [i - maxJump, i - minJump] 处, 就能从区间 [i - maxJump, i - minJump] 的某处跳到 i 处, 即 dp[i] = any(dp[i - maxJump], dp[i - maxJump + 1], ..., dp[i - minJump], 不过同样会超时;
    """
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if not s:
            return False

        n = len(s)
        dp = [False] * n
        dp[0] = True

        for i in range(minJump, n):
            if s[i] != '0':
                continue

            for j in range(max(i - maxJump, 0), i - minJump + 1):
                if dp[j]:
                    dp[i] = True

                    break

        return dp[-1]


from collections import deque


class Solution:
    """
解法2
同样的, 这里也可以使用一个双端队列来维护窗口, 窗口区间为 [i - maxJump, i - minJump], 当队首的元素位置小于 i - maxJump 时, 表示已在窗口外, 则从对首出队; 如果当前字符为0, 说明可以跳到当前位置, 同时还需要队首的元素位置小于等于 i - queue[0] >= minJump, 即从队首跳到 i 处至少需要 minJump 步;
    """
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if not s:
            return False

        n = len(s)
        dp = [False] * n
        dp[0] = True
        queue = deque([0])

        for i in range(minJump, n):
            if queue and queue[0] < i - maxJump:
                queue.popleft()

            if s[i] == '0' and queue and i - queue[0] >= minJump:
                dp[i] = True
                queue.append(i)

        return dp[-1]


class Solution:
    """
解法3
记 prev_reachable_count 表示可以从数组起始位置跳到区间 [i - maxJump, i - minJump] 的个数, 当窗口移动时, 则需要根据窗口剔除和增加的元素来更新 prev_reachable_count, 如果 prev_reachable_count > 0 且当前元素为 0, 则说明可以从前置窗口跳到当前位置;
    """
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if not s:
            return False

        n = len(s)
        dp = [False] * n
        dp[0] = True
        prev_reachable_count = 0

        for i in range(minJump, n):
            prev_reachable_count += 1 if dp[i - minJump] else 0

            if i > maxJump:
                prev_reachable_count -= 1 if dp[i - maxJump - 1] else 0

            dp[i] = prev_reachable_count > 0 and s[i] == '0'

        return dp[-1]


