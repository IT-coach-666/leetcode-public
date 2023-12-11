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
title_jy = "Stone-Game-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.
Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.

Example 2:
Input: piles = [1,2,3,4,5,100]
Output: 104


Constraints:
1 <= piles.length <= 100
1 <= piles[i] <= 10^4
"""


from typing import List


class Solution:
    """
使用动态规划求解, 记 dp[i][m] 表示当前玩家在 M 等于 m 的情况下, 从 piles[i:] 可获得的最大石头数, 同时构造一个 piles 从后往前的前缀和数组, 对每个位置 i, 尝试拿取1到 2m 个位置的石头, 假设拿的位置为 j (1 <= j <= 2 * m), 则当前玩家先拿取的石头个数为 prefix_sum[i] - prefix_sum[i + j], 则另一个玩家在剩下的石头中拿取的最大石头个数为 dp[i + j, max(m, j)], 那么当前玩家在 piles[i + j:] 中可拿取的最大石头数为 prefix_sum[i + j] - dp[i + j, max(m, j)], 则当前玩家在 piles[i] 中一共可拿取的最大石头数为 (prefix_sum[i] - prefix_sum[i + j]) + (prefix_sum[i + j] - dp[i + j, max(m, j)])
    """
    def stoneGameII(self, piles: List[int]) -> int:
        prefix_sum = [n for n in piles]
        memo = [[0] * len(piles) for _ in range(len(piles))]

        for i in range(len(piles) - 2, -1, -1):
            prefix_sum[i] += prefix_sum[i + 1]

        return self._dfs(prefix_sum, 1, 0, memo)

    def _dfs(self, prefix_sum, m, i, memo):
        if i + 2 * m >= len(prefix_sum):
            return prefix_sum[i]

        if memo[i][m] > 0:
            return memo[i][m]

        result = 0

        for j in range(1, 2 * m + 1):
            take = prefix_sum[i] - prefix_sum[i + j]
            result = max(result, take + prefix_sum[i + j] -
                         self._dfs(prefix_sum, max(j, m), i + j, memo))

        memo[i][m] = result

        return result


