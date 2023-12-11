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
title_jy = "Best-Time-to-Buy-and-Sell-Stock-IV(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note: You may not engage in multiple transactions at the same time (ie, you must sell the
stock before you buy again).


Example 1:
Input: [2, 4, 1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: [3, 2, 6, 5, 0, 3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

from typing import List

class Solution:
    """
题解: 使用动态规划求解, 定义:
dp[i][j][0] 表示第 i 天时已经交易了 j 次, 并且未持有股票的目前利润;
dp[i][j][1] 表示第 i 天时已经交易了 j 次, 并且持有 1 只股票的目前利润;

则下一天时有:
dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])
dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])

注意: 当 k 很大时, 此题会超时, 可以进行优化: 判断 k 是否比价格列表的一半长度大, 如果是则
表示每天都可以交易, 则问题退化为 122_Best-Time-to-Buy-and-Sell-Stock-II.py
    """
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        # jy: 如果 k 大于列表长度的一半, 则表示每天都可以交易, 等同于 122_Best-Time-to-Buy-and-Sell-Stock-II.py;
        if k >= len(prices) // 2:
            return self._max_profit_greedy(prices)

        profits = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(len(prices))]

        for i in range(k+1):
            profits[0][i][0] = 0
            profits[0][i][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(k+1):
                profits[i][j][0] = max(profits[i-1][j][0], profits[i-1][j-1][1] + prices[i]) if j >= 1 else profits[i-1][j][0]
                profits[i][j][1] = max(profits[i-1][j][1], profits[i-1][j][0] - prices[i])

        return max([x[0] for x in profits[-1]])


    def _max_profit_greedy(self, prices: List[int]) -> int:
        """
        122_Best-Time-to-Buy-and-Sell-Stock-II.py 中的解法;
        """
        profit = 0
        i = 0
        while i < len(prices) - 1:
            diff = prices[i+1] - prices[i]
            if diff > 0:
                profit += diff
            i += 1

        return profit


prices = [2, 4, 1]
k = 2
# Output: 2
res = Solution().maxProfit(k, prices)
print(res)

prices = [3, 2, 6, 5, 0, 3]
k = 2
# Output: 7
res = Solution().maxProfit(k, prices)
print(res)



