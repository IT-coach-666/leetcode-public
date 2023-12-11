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
title_jy = "Campus-Bikes(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
On a campus represented on the X-Y plane, there are n workers and m bikes, with n <= m.
You are given an array workers of length n where workers[i] = [xi, yi] is the position of the ith worker. You are also given an array bikes of length m where bikes[j] = [xj, yj] is the position of the jth bike. All the given positions are unique.
Assign a bike to each worker. Among the available bikes and workers, we choose the (workeri, bikej) pair with the shortest Manhattan distance between each other and assign the bike to that worker.
If there are multiple (workeri, bikej) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index. If there are multiple ways to do that, we choose the pair with the smallest bike index. Repeat this process until there are no available workers.
Return an array answer of length n, where answer[i] is the index (0-indexed) of the bike that the ith worker is assigned to.
The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Example 1:    https://www.yuque.com/frederick/dtwi9g/xwga4u

Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]
Explanation: Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].

Example 2:

Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: [0,2,1]
Explanation: Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].


Constraints:
n == workers.length
m == bikes.length
1 <= n <= m <= 1000
workers[i].length == bikes[j].length == 2
0 <= xi, yi < 1000
0 <= xj, yj < 1000
All worker and bike locations are unique.
"""

from typing import List


class Solution:
    """
首先求出工人到自行车的距离, 工人的位置, 自行车的位置的所有组合, 将这些组合排序, 然后遍历排序后的组合, 如果当前工人未分配自行车且当前自行车未被分配则分配当前自行车给当前工人并标记当前自行车已被使用;
    """
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) \
            -> List[int]:
        pairs = []

        for i, (x, y) in enumerate(workers):
            for j, (m, n) in enumerate(bikes):
                pairs.append((abs(x - m) + abs(y - n), i, j))

        result = [-1] * len(workers)
        seen = [False] * len(bikes)

        for _, i, j in sorted(pairs):
            if result[i] == -1 and not seen[j]:
                result[i] = j
                seen[j] = True

        return result


