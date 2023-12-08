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
title_jy = "Paint-House(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There is a row of n houses, where each house can be painted one of three colors:
red, blue, or green.  The cost of painting each house with a certain color is
different. You have to paint all the houses such that no two adjacent houses have
the same color.


The cost of painting each house with a certain color is represented by an n x 3 
cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red;
costs[1][2] is the cost of painting house 1 with color green, and so on...


Return the minimum cost to paint all houses.



Example 1:
Input: costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.

Example 2:
Input: costs = [[7, 6, 2]]
Output: 2


Constraints:
costs.length == n
costs[i].length == 3
1 <= n <= 100
1 <= costs[i][j] <= 20
"""




from typing import List


class Solution:
    """
记 cost_so_far 为至今为止刷房子的成本, 包含三个元素, 分别表示当前房子刷成红色, 蓝色, 绿
色的至今的成本, 初始化为刷第一个房子的成本; 从第二个房子开始遍历, 根据 cost_so_far 更新
将当前房子刷成红色, 蓝色, 绿色需要的成本, 例如将当前房子刷成红色, 那么它至今的成本为上
一个房子刷成绿色或蓝色的成本的较小值加上将当前房子刷成红色的成本, 最后返回 cost_so_far 
中的最小值;

jy: costs[i] 中的 3 个值表示把第 i 个房子刷成不同颜色的成本;
    """
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        # jy: [red, blue, green]
        cost_so_far = [costs[0][0], costs[0][1], costs[0][2]]

        for i in range(1, len(costs)):
            # jy: 将当前房子刷成 red, 则得基于上一个房子刷成 blue 或 green 中的最小值;
            red_cost = min(cost_so_far[1], cost_so_far[2]) + costs[i][0]
            # jy: 将当前房子刷成 blue, 则得基于上一个房子刷出 red 或 green 中的最小值;
            blue_cost = min(cost_so_far[0], cost_so_far[2]) + costs[i][1]
            # jy: 将当前房子刷成 green, 则得基于上一个房子刷成 red 或 blue 中的最小值;
            green_cost = min(cost_so_far[0], cost_so_far[1]) + costs[i][2]
            cost_so_far = [red_cost, green_cost, blue_cost]

        return min(cost_so_far)


costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
# Output: 10
res = Solution().minCost(costs)
print(res)

costs = [[7, 6, 2]]
# Output: 2
res = Solution().minCost(costs)
print(res)


