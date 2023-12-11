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
title_jy = "Campus-Bikes-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
On a campus represented as a 2D grid, there are n workers and m bikes, with n <= m. Each worker and bike is a 2D coordinate on this grid.
We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.
Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.
The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Example 1:

Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: 6
Explanation:
We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.

Example 2:

Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: 4
Explanation:
We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2, bike 2 to worker 2 or worker 1. Both assignments lead to sum of the Manhattan distances as 4.

Example 3:
Input: workers = [[0,0],[1,0],[2,0],[3,0],[4,0]], bikes = [[0,999],[1,999],[2,999],[3,999],[4,999]]
Output: 4995


Constraints:
n == workers.length
m == bikes.length
1 <= n <= m <= 10
workers[i].length == 2
bikes[i].length == 2
0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
All the workers and the bikes locations are unique.
"""


import collections
import sys
from typing import List


class Solution:
    """
直接搜索, 不过需要借助缓存加速查找, 这里使用 bit mask 来作为缓存的 key, 自行车的数量总共不超过10辆, 所以可以使用10位二进制来表示已经被使用的自行车;
    """
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) \
            -> int:
        memo = collections.defaultdict(int)

        return self._dfs(workers, bikes, 0, 0, memo)

    def _dfs(self, workers, bikes, worker_index, seen_bikes, memo):
        if worker_index == len(workers):
            return 0

        if seen_bikes in memo:
            return memo[seen_bikes]

        min_distance_sum = sys.maxsize

        for i in range(len(bikes)):
            if (seen_bikes >> i) & 1 == 1:
                continue

            distance = self._get_distance(workers[worker_index], bikes[i])
            current_distance_sum = distance + self._dfs(
                workers, bikes, worker_index + 1, seen_bikes | (1 << i), memo)
            min_distance_sum = min(min_distance_sum, current_distance_sum)

        memo[seen_bikes] = min_distance_sum

        return min_distance_sum

    def _get_distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])



