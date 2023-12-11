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
title_jy = "Stone-Game-IV(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.
Also, if a player cannot make a move, he/she loses the game.
Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.

Example 1:
Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.

Example 2:
Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).

Example 3:
Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).

Example 4:
Input: n = 7
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 -> 0).
If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 -> 0).

Example 5:
Input: n = 17
Output: false
Explanation: Alice can't win the game if Bob plays optimally.


Constraints:
1 <= n <= 10^5
"""


class Solution:
    """
使用动态规划求解, 记 dp[i] 表示在 i 个石头的情况下, 先手是否获胜; 对每个 i, 遍历不超过 i 的完全平方数, 假设为 p, 如果存在 dp[i - p] 为 False, 说明当前玩家先拿走 p 个石头, 那么另一个玩家就一定会输, 等同于当前玩家会赢, 即 dp[i] 为 True;
    """
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            k = 1

            while k * k <= i:
                if not dp[i - k * k]:
                    dp[i] = True

                    break

                k += 1

        return dp[-1]


