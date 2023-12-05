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
title_jy = "Paint-House-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There is a row of ``m`` houses in a small city, each house must be painted with one of
the ``n`` colors (labeled from 1 to n), some houses that have been painted last summer
should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same
color. For example:
houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].

Given an array ``houses``, an m x n matrix ``cost`` and an integer ``target`` where:
  1) houses[i]: is the color of the house i, and 0 if the house is not painted yet.
  2) cost[i][j]: is the cost of paint the house i with the color j+1.
Return the minimum cost of painting all the remaining houses in such a way that there
are exactly ``target`` neighborhoods. If it is not possible, return -1.



Example 1:
Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
             This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
             Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

Example 2:
Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
             This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
             Cost of paint the first and last house (10 + 1) = 11.

Example 3:
Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
Output: 5

Example 4:
Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.



Constraints:
m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4
"""


import functools
import sys
from typing import List


class Solution:
    """
记 i 表示当前的房子(0 <= i < m), neighbor_count 表示当前房子的邻居的数量(0 <= neighbor_cout < target),
prev_color 表示前一个房子的颜色(1 <= prev_color <=n), 给当前房子上色的成本为:
1) 如果当前房子已经上色了, 则直接返回下一个房子的上色成本
2) 如果当前房子未上色, 则遍历所有的颜色, 计算出最小的成本
    """
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @functools.lru_cache(None)
        def dfs(i, neighbor_count, prev_color):
            """
            计算从第 i 个房子进行上色(在此之前共有 neighbor_count 个邻居, 且上一个房子的颜色为 prev_color),
            递归上色到最后一个且邻居数正好为 target 个时, 上色成本最小是多少;
            """
            # jy: 如果 i 等于 m 且邻居数为 target, 表明最后一个房子(m-1) 已经上色完成, 且邻居数已等于目标
            #    值, 则直接返回 0, 终止递归;
            if i == m and neighbor_count == target:
                return 0
            # jy: 如果 i 大于等于 m, 或者邻居数大于 target, 则返回极大值, 终止递归(返回的极大值会被获取
            #    到, 但由于数值大, 会被舍弃忽略);
            if i >= m or neighbor_count > target:
                return sys.maxsize

            # jy: 先初始化最小成本为极大值(后续多个颜色不断判断时, 会将该最小成本进行更新);
            current_min_cost = sys.maxsize
            # jy: 如果当前房子已经上色, 则直接返回从下一个房子开始上色的最小上色成本;
            if houses[i]:
                # jy: 邻居数由当前的邻居数加上 True 或 False(如果当前房子的颜色与前一个房子颜色相同,
                #    则为 False), 并把当前房子的颜色作为下一个房子的 prev_color;
                current_min_cost = dfs(i+1, neighbor_count + (houses[i] != prev_color), houses[i])
            else:
                # jy: 遍历所有的颜色(1 到 n), 逐个尝试将当前房子上为该颜色(并对当前房子之后的房子按该
                #    方式递归上色, 获取最小上色成本), 获取其中的最小上色成本;
                for color in range(1, n+1):
                    # jy: 先递归获取当前房子之后的房子上色的最小成本, 再结合当前的上色成本算出最小的上
                    #    色成本; 当前房子被上色为 color 后, 邻居数做相应的更新, 且将当前颜色 color 传
                    #    入作为下一轮的 prev_color;
                    next_house_cost = dfs(i+1, neighbor_count + (color != prev_color), color)
                    # jy: current_min_cost 初始值为极大值, 如果当前上色后的成本更小, 则会更新, 如果也为
                    #    极大值, 则会保留原先的极大值;
                    current_min_cost = min(current_min_cost, cost[i][color - 1] + next_house_cost)
            return current_min_cost

        # jy: 计算从第 0 个 house 开始到最后一个进行上色(会递归进行上色), 最终上完后总共有 target 个
        #    邻居, 需要的上色成本最小是多少;
        min_cost = dfs(0, 0, None)

        return min_cost if min_cost != sys.maxsize else -1


houses = [0,0,0,0,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m = len(cost)      # 5
n = len(cost[0])   # 2
target = 3
# Output: 9
res = Solution().minCost(houses, cost, m, n, target)
print(res)


houses = [0,2,1,2,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m = len(cost)      # 5
n = len(cost[0])   # 2
target = 3
# Output: 11
res = Solution().minCost(houses, cost, m, n, target)
print(res)


houses = [0,0,0,0,0]
cost = [[1,10],[10,1],[1,10],[10,1],[1,10]]
m = len(cost)      # 5
n = len(cost[0])   # 2
target = 5
# Output: 5
res = Solution().minCost(houses, cost, m, n, target)
print(res)


houses = [3,1,2,3]
cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
m = len(cost)      # 4
n = len(cost[0])   # 3
target = 3
# Output: -1
res = Solution().minCost(houses, cost, m, n, target)
print(res)

