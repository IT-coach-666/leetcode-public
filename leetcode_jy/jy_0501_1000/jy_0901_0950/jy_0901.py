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
title_jy = "Online-Stock-Span(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.
For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].
Implement the StockSpanner class:
StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.

Example 1:
Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[None, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100)  # return 1
stockSpanner.next(80)   # return 1
stockSpanner.next(60)   # return 1
stockSpanner.next(70)   # return 2
stockSpanner.next(60)   # return 1
stockSpanner.next(75)   # return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85)   # return 6


Constraints:
1 <= price <= 10^5
At most 10^4 calls will be made to next.
"""


"""
使用一个栈保存股票价格和其对应的 span, 每次调用 next 时持续判断栈顶的价格是否小于当前价格, 如果是则出栈栈顶, 并将栈顶的 span 计入当前价格的 span, 最后将当前价格和其对应 span 入栈;
"""
class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        price_span = 1

        while self.prices and self.prices[-1][0] <= price:
            _, prev_span = self.prices.pop()
            price_span += prev_span

        self.prices.append((price, price_span))

        return price_span


