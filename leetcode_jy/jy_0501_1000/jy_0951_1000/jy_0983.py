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
title_jy = "Minimum-Cost-For-Tickets(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You have planned some train traveling one year in advance. The days of the year in
which you will travel are given as an integer array ``days``. Each day is an integer
from 1 to 365.    Train tickets are sold in three different ways:
1) a 1-day pass is sold for costs[0] dollars,
2) a 7-day pass is sold for costs[1] dollars, and
3) a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.  For example, if we get a 7-day
pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.


Example 1:
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
             On day 1, you bought a 1-day pass for costs[0] = 2, which covered day 1.
             On day 3, you bought a 7-day pass for costs[1] = 7, which covered days 3, 4, ..., 9.
             On day 20, you bought a 1-day pass for costs[0] = 2, which covered day 20.
             In total, you spent $11 and covered all the days of your travel.

Example 2:
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
             On day 1, you bought a 30-day pass for costs[2] = 15 which covered days 1, 2, ..., 30.
             On day 31, you bought a 1-day pass for costs[0] = 2 which covered day 31.
             In total, you spent $17 and covered all the days of your travel.
 

Constraints:
1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""


from functools import lru_cache


class Solution:
    """
解法1: 递归式实现动态规划(从后向前推算); 该方法的时间复杂度和空间复杂度均较差;
    """
    def mincostTickets_v1(self, days: List[int], costs: List[int]) -> int:
        # jy: 尽管 days 中的数值不重复, 但将其转换为集合形式对后续的: i in dayset 逻辑
        #     判断的执行效率会大大提升;
        dayset = set(days)
        durations = [1, 7, 30]

        # jy: 定义 dp[i] 为第 i 天开始到一年结束需要花的最少钱(目标即求 dp[1]);
        @lru_cache(None)
        def dp(i):
            """
            求第 i 天开始到一年结束, 需要花的钱(目标即求 dp(1));
            """
            # jy: 如果 i 大于 365, 则返回, 终止递归;
            if i > 365:
                return 0
            # jy: 如果 i 在 dayset 中, 则计算第 (i+1), (i+7), (i+15) 天到一年结束需要花的钱,
            #     再分别加上买 1, 7, 15 天通行证所需要的费用, 求三者中的最小值;
            elif i in dayset:
                return min(dp(i + d) + cost for d, cost in zip(durations, costs))
            # jy: 如果 i 不在 dayset 中(即第 i 天不是出行日期, 通行证没必要在该天买), 则 dp(i) = dp(i+1)
            else:
                return dp(i + 1)
        # jy: 最终返回 dp(1), 即从第 1 天开始到一年结束需要花的最少钱;
        return dp(1)

    """
解法2: 动态规划(从前往后), 性能大大提升;
    """
    def mincostTickets_v2(self, days: List[int], costs: List[int]) -> int:
        # jy: dp[i] 代表截止第 i 天需要花费的最少钱(最大天数即 days 中的最后一个
        #     数值对应的所在天数);
        dp = [0 for _ in range(days[-1] + 1)]
        # jy: days_idx 用于记录 days 数组中当前待处理的天数的下标;
        days_idx = 0
        for i in range(1, len(dp)):
            # jy: 若 i 不是当前待处理天数, 则其花费费用和前一天相同;
            if i != days[days_idx]:
                dp[i] = dp[i-1]
            # jy: 若 i 为当前待处理天数, 为了确保当前天数可同行, 有三种方式买同行证:
            #     1) 选择当前第 i 天的前 1 天花费 costs[0] 买 1 天的通行证(即当前第 i 天)
            #     2) 选择当前第 i 天的前 7 天花费 costs[1] 买 7 天的通行证(即可包含当前的第 i 天)
            #     3) 选择当前第 i 天的前 30 天花费 costs[2] 买 30 天的通行证(即可包含当前的第 i 天)
            #     选择以上三种方式中成本花费最小值:
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
                # jy: 经过以上, 表明 days 中的下标为 days_idx 的对应天数已经处理完, days_idx 加 1 后
                #     继续后续的处理(由代码逻辑可知, i 的最大值为 days 数组中的最后一个天数, 当 days_idx
                #     为 days 数组的最后一个下标位置时, 只有当 i 等于 days 的最后一个天数时, 此处的
                #     days_idx 会进一步加 1 越界, 但此时的 i 已经是最后一轮循环了, 故 days_idx 不会
                #     再进行 days[days_idx] 操作, 故不会存在 days_idx 越界问题);
                days_idx += 1
        # jy: 返回截止最后一天需要花费的最少钱;
        return dp[-1]


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
# Output: 11
res = Solution().mincostTickets(days, costs)
print(res)


days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
costs = [2, 7, 15]
# Output: 17
res = Solution().mincostTickets(days, costs)
print(res)


