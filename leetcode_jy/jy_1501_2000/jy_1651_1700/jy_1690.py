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
title_jy = "Stone-Game-VII(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Alice and Bob take turns playing a game, with Alice starting first.
There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.
Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.
Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the difference in Alice and Bob's score if they both play optimally.

Example 1:
Input: stones = [5,3,1,4,2]
Output: 6
Explanation:
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.

Example 2:
Input: stones = [7,90,5,1,100,10,10,2]
Output: 122


Constraints:
n == stones.length
2 <= n <= 1000
1 <= stones[i] <= 1000
"""


from typing import List


class Solution:
    """
和 877. Stone Game 一样, 只是计算分值的方式不同, 因为分值等于剩下石头的分值和, 所以构造前缀和数组用于计算分值和;
    """
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        prefix_sum = [i for i in stones]

        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]

        for i in range(n):
            dp[i][i] = 0

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                take_left = self._get_sum(prefix_sum, i + 1, j) - dp[i + 1][j]
                take_right = self._get_sum(prefix_sum, i, j - 1) - dp[i][j - 1]
                dp[i][j] = max(take_left, take_right)

        return dp[0][-1]

    def _get_sum(self, prefix_sum, i, j):
        if i == 0:
            return prefix_sum[j]
        else:
            return prefix_sum[j] - prefix_sum[i - 1]


