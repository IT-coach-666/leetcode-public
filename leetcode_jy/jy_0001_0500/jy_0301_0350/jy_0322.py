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
title_jy = "Coin-Change(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given ``coins`` of different denominations and a total amount of money
``amount``. Write a function to compute the fewest number of coins that you need
to make up that amount. If that amount of money cannot be made up by any combination
of the coins, return -1.


Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1


Note: You may assume that you have an infinite number of each kind of coin.
"""


import sys
from typing import List


class Solution:
    """
动态规划: 定义 dp[i] 表示兑换成总数额为 i 时需要的最少硬币个数, 目标即求 dp[amount];
则有(即找出 dp[i - coin] 中的最小值, 前提是至少要有一个 dp[i - coin] 存在, 不存在则 dp[i] 还是原
来的 dp[i], 不做更新):
dp[i] = min([ dp[i - coin] for coin in coins if i >= coin]) + 1
即兑换成总数额 i 时需要的最少硬币数等价于兑换成总数额为 i - coin (需确保该数额是一个有效数额, 即
确保 i - coin >= 0) 时需要的最少硬币数加 1 (其中 coin 表示所有的硬币面额中的一种), 因为如果能使用
最少的硬币数兑换成总数额为 i - coin, 则使用该最少硬币数兑换成 i - coin 后, 再加上 1 个面额为 coin
的硬币, 就能确保总数为 i 了, 且此时使用的硬币数最少;
    """
    def coinChange_v1(self, coins: List[int], amount: int) -> int:
        # jy: 定义 dp[i] 表示兑换钱数为 i 时需要的最少硬币个数, 目标即求 dp[amount]; dp 初始化
        #     为长度为 amount + 1 的数组, 除了 dp[0] 初始值均为最大值(dp[0] 为 0, 表示兑换钱数
        #     为 0 时需要的最少硬币数是 0);
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0

        # jy: i 从 1 到 amount (从小到大) 循环遍历, 每一轮外层 for 循环, 都求出相应的 dp[i] 结果;
        #     注意, i 必须是从小到大遍历, 因为计算 dp[i] 时依赖于 dp[i - coin], 其中 i - coin 肯定
        #     比 i 小, 只有 i 从小到大遍历, 逐个求出 dp[i], 才能确保计算 dp[amount] 时依赖的
        #     dp[amount - coin] 已经求解出;
        for i in range(1, amount + 1):
            # jy-version-1-Begin -------------------------------------------------------------
            # jy: 如果兑换成总数额 i - coin 使需要的硬币最少, 则在该最少硬币数的基础上加上面额为 coin
            #     的硬币, 即为总数额 i, 此时使用的硬币数最少; 因此需要找出不同面额 coin 对应的 dp[i - coin]
            #     中的最小值(前提是至少要有一个 dp[i - coin] 存在, 不存在则 dp[i] 还是原来的 dp[i], 不
            #     做更新; 求 dp[i - coin] 也要确保 i - coin 有效, 即 i - coin >= 0), 在该最小值的基础
            #     上加 1 即可;
            ls_count = [dp[i - coin] for coin in coins if i >= coin]
            if ls_count:
                dp[i] = min(ls_count) + 1
            # jy-version-1-End ---------------------------------------------------------------

            # jy-version-2-Begin -------------------------------------------------------------
            '''
            # jy: 该方式每轮 for 循环基本都要调用 min 获取最小值, 影响执行效率
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
            '''
            # jy-version-2-End ---------------------------------------------------------------

        # jy: 如果兑换成 amount 数额的硬币数(即 dp[amount])小于 amount 值, 表明兑换成该数额
        #    硬币组合存在, 直接返回, 否则返回 -1;
        return dp[amount] if dp[amount] <= amount else -1

    """
解法2: 完全背包问题: 填满容量为 amount 的背包最少需要多少硬币
思路同解法 1, 只是求解过程中外层循环是循环遍历 coins 中的硬币面额, 内层循环遍历不同的总数
额 j 并求解其对应的 dp[j] 值; 该方式的好处在于, 遍历总数额 j 时可以从 coin 到 amount 遍历,
确保每个 j - coin 都是有效的, 减少了不必要的 if 判断;

由于每次都要进行 min 获取最小值, 性能比解法 1 差;
    """
    def coinChange_v2(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1


coins = [1, 2, 5]
amount = 11
# Output: 3
res = Solution().coinChange_v1(coins, amount)
print(res)


coins = [2]
amount = 3
# Output: -1
res = Solution().coinChange_v2(coins, amount)
print(res)


