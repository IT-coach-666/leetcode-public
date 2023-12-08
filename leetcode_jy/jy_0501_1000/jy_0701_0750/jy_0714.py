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
title_jy = "Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Your are given an array of integers prices, for which the i-th element is the price of
a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction
fee for each transaction.  You may not buy more than 1 share of a stock at a time (ie.
you must sell the stock share before you  buy again.)

Return the maximum profit you can make.



Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.



Note:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""


from typing import List

class Solution:
    """
同其他股票买卖的问题一样, 使用动态规划求解, 定义:
1) dp[i][0] 表示第 i 天时未持有股票的目前利润
2) dp[i][1] 表示第 i 天时持有股票的目前利润
注意卖出股票时需要扣除交易费;
    """
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        length = len(prices)
        profits = [[0 for _ in range(2)] for _ in range(length)]
        # jy: 第 0 天时未持有股票的目前利润为 0;
        profits[0][0] = 0
        # jy: 第 0 天时持有股票的目前利润为第一只股票的价格的相反数(因为持有股票需要买入该股票)
        profits[0][1] = -prices[0]
        # jy: 以上处理完股票价格列表的第一个元素, 剩下的则从第二个元素开始逐个遍历;
        for i in range(1, length):
            # jy: 第 i 天未持有股票的目前利润等价于:
            #    a) 第 i-1 天未持有股票的目前利润
            #    b) 第 i-1 天持有股票的目前利润(持有股票的成本已经在利润中扣减), 加上当前第 i 天
            #       将持有的股票卖出的卖出价格, 再减掉交易费用;
            profits[i][0] = max(profits[i-1][0], profits[i-1][1] + prices[i] - fee)
            # jy: 第 i 天持有股票的目前利润等价于:
            #    a) 第 i-1 天持有股票的目前利润
            #    b) 第 i-1 天未持有股票的目前利润, 加上当前的第 i 天持有股票(在已有利润的基础上减
            #       掉当前持有股票时买入该股票时的价格)
            profits[i][1] = max(profits[i-1][1], profits[i-1][0] - prices[i])

        return profits[-1][0]


prices = [1, 3, 2, 8, 4, 9]
fee = 2
# Output: 8
res = Solution().maxProfit(prices, fee)
print(res)

