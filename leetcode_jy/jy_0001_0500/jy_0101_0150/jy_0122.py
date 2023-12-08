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
title_jy = "Best-Time-to-Buy-and-Sell-Stock-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions
as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell
the stock before you buy again).


Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

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
由于交易数不受限制, 所以可以使用贪心算法: 遍历每一天的股价, 只要后一天的股价大
于今天, 则在今天买入, 后一天卖出, 汇总每次交易的收益;
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        while i < len(prices) - 1:
            diff = prices[i+1] - prices[i]
            if diff > 0:
                profit += diff
            i += 1
        return profit


prices = [7, 1, 5, 3, 6, 4]
# Output: 7
res = Solution().maxProfit(prices)
print(res)

prices = [7, 1, 5, 3, 4, 6]
# Output: 7
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


