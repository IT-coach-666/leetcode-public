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
title_jy = "Best-Time-to-Buy-and-Sell-Stock-with-Cooldown(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Say you have an array for which the i_th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you
like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
1) You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
2) After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)


Example:
Input: [1, 2, 3, 0, 2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""




from typing import List

class Solution:
    """
使用动态规划求解
定义三维数组 dp (题解中的 profits 数组):
第一维对应的值为对应天数;
第二维的值是 0 或 1, 0 表示非冷冻期, 1 表示冷冻期;
第三维的值是 0 或 1, 0 表示目前利润(且未持有股票), 1 表示目前利润(且持有一只股票):
则有:
dp[i][0][0] 表示第 i 天处于非冷冻期的已有利润(未持有股票)
dp[i][0][1] 表示第 i 天处于非冷冻期的已有利润(持有一只股票)
dp[i][1][0] 表示第 i 天处于冷冻期的已有利润(未持有股票)

不可能有 dp[i][1][1], 因为发生冷冻期时必然是之前刚卖掉股票, 不可能还持有股票;
    """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        length = len(prices)
        # jy: 此处初始化 profits 数组, 将其数值设置全为 0;
        profits = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(length)]
        # jy: profits[0][0][0] 表示第 0 天非冷冻期, 未持有股票的目前利润, 值为 0;
        #    profits[0][0][1] 表示第 0 天非冷冻期, 持有一只股票的目前利润, 值初始化为 -prices[0]
        profits[0][0][0], profits[0][0][1] = 0, -prices[0]
        # jy: profits[0][1][0] 表示第 0 天时处于冷冻期, 未持有股票的目前利润, 值为 0;
        #    profits[0][1][1] 的情况不存在, 初始化该值为 0 (可将此部分去除, 后续不会使用到);
        # profits[0][1][0], profits[0][1][1] = 0, 0
        profits[0][1][0] = 0

        for i in range(1, length):
            # jy: 第 i 天处于非冷冻期的已有利润(未持有股票) ==等价于== 前一天处于非冷冻期或冷冻
            #    期的已有利润(未持有股票)的最大值;
            profits[i][0][0] = max(profits[i-1][0][0], profits[i-1][1][0])
            # jy: 第 i 天处于非冷冻期的已有利润(持有一只股票) ==等价于== 前一天处于非冷冻期的已
            #    有利润(持有一只股票) ==或== 前一天处于非冷冻期的已有利润(未持有股票)并购买当前的
            #    股票 这两者中的最大值;
            profits[i][0][1] = max(profits[i-1][0][1], profits[i-1][0][0] - prices[i])
            # jy: 第 i 天处于冷冻期的已有利润(未持有股票) ==等价于== 前一天处于非冷冻期的已有利
            #    润(持有一只股票), 并以当前价格将该股票卖出得到的总利润;
            profits[i][1][0] = profits[i-1][0][1] + prices[i]

        # jy: 利润最大时, 肯定是手头上不持有股票的(因为持有股票需要额外花钱), 故第三维是 0;
        return max(profits[-1][0][0], profits[-1][1][0])


prices = [1, 2, 3, 0, 2]
# Output: 3
res = Solution().maxProfit(prices)
print(res)


