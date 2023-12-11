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
title_jy = "Paint-House-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There are a row of n houses, each house can be painted with one of the k colors. The
cost of painting each house with a certain color is different. You have to paint all
the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost
matrix costs. For example, costs[0][0] is the cost of painting house 0 with color 0;
costs[1][2] is the cost of painting house 1 with color 2, and so on...

Return the minimum cost to paint all houses.



Example 1:
Input: costs = [[1, 5, 3], [2, 9, 4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.

Example 2:
Input: costs = [[1, 3], [2, 4]]
Output: 5



Constraints:
costs.length == n
costs[i].length == k
1 <= n <= 100
1 <= k <= 20
1 <= costs[i][j] <= 20


Follow up: Could you solve it in O(nk) runtime?
"""




import sys
from typing import List



class Solution:
    """
解法1: 256_Paint-House.py 的泛化版本, 时间复杂度为 O(n * k^2);
    """
    def minCostII_v1(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        # jy: 初始化 cost_so_far 为将第一个建筑物涂成不同颜色的成本(即 costs[0]), 以下为
        #    什么不直接将 costs[0] 赋值给 cost_so_far? 因为如果直接复制, 两者之间会有联
        #    系, 此时当改变 cost_so_far 的值时, costs 中对应的值也会被更改;
        k = len(costs[0])
        cost_so_far = [x for x in costs[0]]
        # jy: 遍历 costs 中剩下的所有 house;
        for i in range(1, len(costs)):
            current_cost = [0] * k
            # jy: 针对第 i 个 house, 求其被涂成 k 种颜色时, 各个颜色花费金额的最小值;
            for j in range(k):
                # jy: 当前 house 被涂成颜色 j 时, 花费金额的最小值; _min_cost 方法求
                #    当前 house 为颜色 j, 则其原先 house 的颜色不能涂为颜色 j 的成本
                #    最小值, 等同于:
                #    min([cost_so_far[i] for i in range(cost_so_far) if i != j])
                current_cost[j] = self._min_cost(cost_so_far, j) + costs[i][j]

            cost_so_far = current_cost

        return min(cost_so_far)


    def _min_cost(self, cost_so_far, i):
        """
        求当前 house 为颜色 i 的情况下, 其前一个 house 不能为颜色 i, 此时在前一个 house
        为非颜色 i 中找出成本最小值;
        """
        #return min([cost_so_far[j] for j in range(cost_so_far) if j != i])

        min_cost = sys.maxsize

        for j, cost in enumerate(cost_so_far):
            if j != i and min_cost > cost:
                min_cost = cost

        return min_cost


    """
解法2: Follow up 中要求算法的时间复杂度为 O(nk);
相比于维护所有颜色的最少成本, 这里只维护两种最少成本的颜色, 以及最少成本的颜色
对应的下标; 遍历所有的房子, 对每一座房子遍历所有的颜色, 对于当前颜色的最少成本
为当前颜色的成本加上:
1) 如果当前颜色的下标等同于至今最少成本的下标, 由于颜色冲突, 不能选择至今最少成
   本的颜色, 只能选择至今第二少成本的颜色;
2) 如果当前颜色的下标不等同于至今最少成本的下标, 则选择至今最少成本的颜色;

然后根据计算出的当前颜色的成本, 计算出当前房子中所有颜色成本中最少的两个;
    """
    def minCostII_v2(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        # jy: 只维护两种最少成本的颜色(min1 代表最少成本, min2 代表第二少成本), 以
        #    及最少成本颜色对应的下标(即 index1);
        min1 = min2 = 0
        index1 = -1
        k = len(costs[0])

        for i in range(len(costs)):
            current_min1 = sys.maxsize
            current_min2 = sys.maxsize
            current_index1 = -1
            # jy: 遍历第 i 个 house 被涂成 k 种颜色的相应成本;
            for j in range(k):
                # jy: 第一轮外循环时, index1 为 -1, min1 和 min2 均为 0, 此时的 cost 即
                #    为第一个 house 被涂成不同颜色的成本;
                cost = costs[i][j] + (min1 if j != index1 else min2)

                # jy: 以下即获取当前最小值和第二小值, 以及最小值对应的下标;
                if cost < current_min1:
                    current_min2 = current_min1
                    current_min1 = cost
                    current_index1 = j
                elif cost < current_min2:
                    current_min2 = cost

            # jy: 更新 min1 和 min2 以及 index1, 表示截止第 i 个 house 按规则涂颜色所需
            #    要的最少成本和第二少成本, 以及最少成本对应的颜色为 index1;
            min1 = current_min1
            min2 = current_min2
            index1 = current_index1

        return min1



costs = [[1, 5, 3], [2, 9, 4]]
# Output: 5
res = Solution().minCostII_v1(costs)
print(res)


costs = [[1, 3], [2, 4]]
# Output: 5
res = Solution().minCostII_v1(costs)
print(res)


