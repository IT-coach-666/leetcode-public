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
title_jy = "Best-Time-to-Buy-and-Sell-Stock-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (i.e., you must sell the stock
before you buy again).

Example 1:
Input: [3, 3, 5, 0, 0, 3, 1, 4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: [1, 2, 3, 4, 5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7, 6, 4, 3, 1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List
class Solution:
    """
思路同 188_Best-Time-to-Buy-and-Sell-Stock-IV.py, 只是 k 变为 2
    """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        length = len(prices)
        profits = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(length)]
        profits[0][0][0], profits[0][0][1] = 0, -prices[0]
        profits[0][1][0], profits[0][1][1] = 0, -prices[0]
        profits[0][2][0], profits[0][2][1] = 0, -prices[0]
        for i in range(1, length):
            profits[i][0][0] = profits[i-1][0][0]
            profits[i][0][1] = max(profits[i-1][0][1], profits[i-1][0][0] - prices[i])
            profits[i][1][0] = max(profits[i-1][1][0], profits[i-1][0][1] + prices[i])
            profits[i][1][1] = max(profits[i-1][1][1], profits[i-1][1][0] - prices[i])
            profits[i][2][0] = max(profits[i-1][2][0], profits[i-1][1][1] + prices[i])
        return max(profits[-1][0][0], profits[-1][1][0], profits[-1][2][0])


prices = [3, 3, 5, 0, 0, 3, 1, 4]
# Output: 6
res = Solution().maxProfit(prices)
print(res)

prices = [1, 2, 3, 4, 5]
# Output: 4
res = Solution().maxProfit(prices)
print(res)

prices = [7, 6, 4, 3, 1]
# Output: 0
res = Solution().maxProfit(prices)
print(res)


