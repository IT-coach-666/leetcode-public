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
title_jy = "Shortest-Distance-to-Target-Color(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an array colors, in which there are three colors: 1, 2 and 3.
You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

Example 1:
Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation:
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).

Example 2:
Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.


Constraints:
1 <= colors.length <= 5*10^4
1 <= colors[i] <= 3
1 <= queries.length <= 5*10^4
queries[i].length == 2
0 <= queries[i][0] < colors.length
1 <= queries[i][1] <= 3
"""


import bisect
import collections
from typing import List


class Solution:
    """
类似 244. Shortest Word Distance II 先保存每种颜色所在的位置, 搜索时使用二分查找定位应该插入到数组中的位置, 计算最小距离;
    """
    def shortestDistanceColor(self, colors: List[int],
                              queries: List[List[int]]) -> List[int]:
        positions = collections.defaultdict(list)
        result = []

        for i, color in enumerate(colors):
            positions[color].append(i)

        for i, color in queries:
            result.append(self._shortest(positions, i, color))

        return result

    def _shortest(self, positions, i, color):
        position = positions.get(color, [])

        if not position:
            return -1

        j = bisect.bisect_left(position, i)

        if j == 0:
            return abs(i - position[0])
        elif j == len(position):
            return abs(i - position[-1])
        else:
            return min(abs(i - position[j - 1]), abs(i - position[j]))




