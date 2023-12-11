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
title_jy = "Last-Stone-Weight-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.
Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

Example 2:
Input: stones = [31,26,33,21,40]
Output: 5

Example 3:
Input: stones = [1,2]
Output: 1


Constraints:
1 <= stones.length <= 30
1 <= stones[i] <= 100
"""

from typing import List


class Solution:
    """
该问题可看做将石头分为两堆, 求两堆石头权重和的差值的最小值, 记 dp[i][j] 表示将 stones[:i] 放入容量为 j 的背包时, 背包所存放的实际容量; 最后返回 total - dp[n][total # 2] * 2 等价于 石头堆1 - 石头堆2 = (total - 石头堆2) - 石头堆2 = total - 石头堆2 * 2;
    """
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n = len(stones)
        dp = [[0] * (total # 2 + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, total # 2 + 1):
                if j >= stones[i - 1]:
                    current = dp[i - 1][j - stones[i - 1]] + stones[i - 1]
                    dp[i][j] = max(dp[i - 1][j], current)
                else:
                    dp[i][j] = dp[i - 1][j]

        return total - dp[n][total # 2] * 2


