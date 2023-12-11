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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Best-Time-to-Buy-and-Sell-Stock(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e.,  buy one and sell
one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List
class Solution:
    """
解法1: 股票买卖系列的第一题, 只能交易一次; 等价于求价格列表中差额最大的两个数; 循环价格
列表, 记录至今为止股票价格的最小值, 同时将今天的股票价格减去最小值, 判断是否是至今的最大
利润
    """
    def maxProfit_v1(self, prices: List[int]) -> int:
        min_price = prices[0] if prices else 0
        max_profit = 0
        # jy: 循环价格列表, 记录至今为止股票价格的最小值; 同时将当前股价减最小值, 判断是否
        #    是至今的最大利润;
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit


    """
解法2: 思路同 188_Best-Time-to-Buy-and-Sell-Stock-IV.py, 只是 k 变为 1;
    """
    def maxProfit_v2(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n)]
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] - prices[i])
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1] + prices[i])
        return dp[n-1][1][0]


    """
在解法 1 的基础上获取差值最大的两个下标;
    """
    def maxProfit_jy(self, prices: List[int]) -> int:
        min_price = prices[0] if prices else 0
        max_profit = 0
        # jy: idx_min_price 不能直接用 idx_low 代替, 因为 idx_low 是最终要返回的起始下标,
        #    而 idx_min_price 为当前为止的最小值的下标, 最小值的下标不一定就是最终返回结
        #    果的起始下标;
        idx_min_price, idx_low, idx_high = 0, -1, -1
        # jy: 循环价格列表, 记录至今为止股票价格的最小值; 同时将当前股价减最小值, 判断是否
        #    是至今的最大利润;
        for i in range(1, len(prices)):
            if min_price > prices[i]:
                idx_min_price = i
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                idx_high = i
                idx_low = idx_min_price
        return idx_low, idx_high, max_profit

prices = [7, 1, 5, 3, 6, 4]
# Output: 5
res = Solution().maxProfit_v1(prices)
print(res)



prices = [7, 6, 4, 3, 1]
# Output: 0
res = Solution().maxProfit_v1(prices)
print(res)



prices = [7, 2, 5, 3, 6, 4, 1, 4, 5]
# Output: 5
res = Solution().maxProfit_jy(prices)
print(res)


