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
title_jy = "Coin-Change-2(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an integer array ``coins`` representing coins of different denominations
and an integer ``amount`` representing a total amount of money. Return the number of
combinations that make up that amount. If that amount of money cannot be made up by any
combination of the ``coins``, return 0.

You may assume that you have an infinite number of each kind of coin. The answer is
guaranteed to fit into a signed 32-bit integer.


Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1
 

Constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""


from typing import List


class Solution:
    """
解法1: 动态规划(完全背包之组合问题: 填满容量为 amount 的背包, 有几种组合)
coins 的每个元素可以选取多次, 且不考虑选取元素的顺序(即计算硬币选取的组合数);

定义 dp[j] 表示金额之和等于 j 的硬币组合数, 目标即求 dp[amount]
dp[0]=1, 因为只有当不选取任何硬币时金额之和才为 0, 因此金额为 0 的有 1 种组合;
对于面额为 coin 的硬币:
1) 当 coin 大于 amount 时, coin 不能构成组成 amount 数额的组合;
2) 当 coin 小于或等于 amount 时, 如果存在金额为 i − coin 的硬币组合(即 dp[i-coin] 不为 0),
   则在每一个该组合中增加一个面额为 coin 的硬币即可得到金额为 i 的硬币组合数(即 dp[i]);
因此可以遍历 coins 中的每一种面额(假设为 coin)的硬币, 更新金额为 coin 至 amount 的所有组
合数: 即, 假设 coin <= i <= amoint, 更新每一个 dp[i] 为 dp[i] + dp[i - coin] (在原有组合数
的基础上加上当前新的组合数 dp[i - coin]); 所有硬币面额遍历完成后, 最终的 dp[amount] 即为所
求答案;

由于外层 for 循环是遍历 coins 中的所有面额 coin, 内层 for 循环是计算 coin 到 amount 中的各
个不同的金额的组合数; 如果当前面额 coin 能成为某金额 i 的组合数 (即 dp[i - coin] 不为 0),
则表明当前 coin 可以组合为金额 i, 新增的组合数有 dp[i - coin] 个, 故 dp[i] 需要在原来的基
础上加上当前新增的组合数 dp[i - coin] ; 由于 coins 中的面额均唯一, 故遍历计算时不会将相同
组合的不同排列情况重复计算在内;
    """
    def change_v1(self, amount: int, coins: List[int]) -> int:
        # jy: 定义 dp[j] 表示金额之和等于 j 的硬币组合数, 目标即求 dp[amount]
        dp = [0] * (amount + 1)
        # jy: 金额为 0 的组合有 1 种, 即不选取任何硬币;
        #     也只有当这么初始化之后, 后续遍历 coin 到 amount 的金额时(假设金额为 i),
        #     dp[i] += dp[i - coin], 当 i 等于 coin 时, 能确保 dp[coin] 在原有基础上加
        #     上 dp[0], 即加上 1, 表示当前面额 coin 也是组成金额为 coin 的硬币组合中的
        #     一种;
        dp[0] = 1
        # jy: 遍历 coins 中的所有硬币面额 coin, 每一次都计算金额为 coin 至 amount 的组
        #     合数 (面额都是唯一的, 不会重复)
        for coin in coins:
            # jy: 表示 coin 到 amount 之间的金额 j 的所有组合数(即 dp[j]) 中, 如果当前
            #     硬币面额 coin 能够成为合成金额为 j 的组合(即 dp[j - coin] 不为 0), 则
            #     表示金额为 j 的组合数需要加上 dp[j - coin] (因为所有金额为 j - coin 的
            #     组合均能加上当前面额 coin 使得金额为 j);
            # jy: 注意, j 必须是升序遍历, 即 j 由小到大, 越来越大; 因为硬币面额 coin 是可以
            #     重复使用的, 而 dp[j] 的计算依赖于 dp[j - coin], 且不管是上一轮外层 for 循
            #     环的 coin 得到的 dp[j - coin] 还是当前轮说当前由于 j - coin 比 j 小, 故
            #     小的需要先计算出来, 故 j 需要由小到大遍历, 否则不对; 这是与 494_Target-Sum.py
            #     中解法 4 的主要区别;
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[amount]

    def change_v2(self, amount: int, coins: List[int]) -> int:
        # jy: 定义 dp[i][j] 表示考虑前 i 个硬币, 凑成总和为 j 的所有方案(组合)数; 即目标求 dp[len(coins)][amount]
        dp = [[0] * (amount + 1)] * (len(coins) + 1)
        dp[0][0] = 1
        # jy-version-1-Begin-------------------------------------------------------
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if j >= coins[i]:
                    dp[i + 1][j] = dp[i][j] + dp[i + 1][j - coins[i]]
                else:
                    dp[i + 1][j] = dp[i][j]
        # jy-version-1-End---------------------------------------------------------
        # jy-version-2-Begin-------------------------------------------------------
        """
        # jy: 参考一下 java 代码, 但 java 能通过, 以下不能通过
        # https://leetcode-cn.com/problems/coin-change-2/solution/gong-shui-san-xie-xiang-jie-wan-quan-bei-6hxv/
        for i in range(len(coins)):
            coin = coins[i]
            for j in range(amount + 1):
                dp[i + 1][j] = dp[i][j]
                k = 1
                while k * coin <= j:
                    dp[i + 1][j] += dp[i][j - k * coin]
                    k += 1
        """
        # jy-version-2-End---------------------------------------------------------
        return dp[len(coins)][amount]


amount = 5
coins = [1, 2, 5]
# Output: 4
res = Solution().change_v1(amount, coins)
print(res)


amount = 3
coins = [2]
# Output: 0
res = Solution().change_v1(amount, coins)
print(res)


amount = 10
coins = [10]
# Output: 1
res = Solution().change_v2(amount, coins)
print(res)


