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
title_jy = "Stone-Game(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.
Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.
Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

Example 1:
Input: piles = [5,3,4,5]
Output: true
Explanation:
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

Example 2:
Input: piles = [3,7,2,3]
Output: true


Constraints:
2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles[i]) is odd.
"""


from typing import List


class Solution:
    """
解法1
先手必赢, 因为石头堆的个数是偶数, 所以最终两人能拿的石头堆个数是相同的, 又由于石头总数是奇数, 最后两人手里的石头数量也不可能相等, 先手可以做到永远只拿第偶数个石头堆或第奇数个石头堆, 判断两种情况下哪种方案拿的石头多即可(各取一半石头堆的组合有很多, 只拿偶数堆或奇数堆最简单又能分出胜负)
    """
    def stoneGame(self, piles: List[int]) -> bool:
        return True

from typing import List


class Solution:
    """
解法2
使用动态规划求解, 记 dp[i][j] 表示从 piles[i:j + 1] 先手拿石头最多能比对方多多少石头(注意这里不限定拿石头的是 Alice 还是 Bog), 则 Alice 要么从 piles[i] 先拿石头, 要么从 piles[j] 先拿石头, 以先从 piles[i] 拿石头为例, 则 dp[i][j] = piles[i] + Alice 从 piles[i + 1:j + 1] 拿石头的最大个数 - Bob 从 piles[i + 1:j + 1] 拿石头的最大个数 = piles[i] - (Bob 从 piles[i + 1:j + 1] 拿石头的最大个数 - Alice 从 piles[i + 1:j + 1] 拿石头的最大个数), 而 Bob 从 piles[i + 1:j + 1] 拿石头的最大个数 - Alice 从 piles[i + 1:j + 1] 拿石头的最大个数 就等于 dp[i + 1][j], 因为 dp 不关心是谁拿的石头, Alice 从 piles[j] 先拿石头同理, 所以 dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
    """
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(piles[i] - dp[i + 1][j],
                               piles[j] - dp[i][j - 1])

        return dp[0][-1] > 0


