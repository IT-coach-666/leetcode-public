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
title_jy = "Tree-Diameter(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.
The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

Example 1:    https://www.yuque.com/frederick/dtwi9g/mpd92c

Input: edges = [[0,1],[0,2]]
Output: 2
Explanation:
A longest path of the tree is the path 1 - 0 - 2.

Example 2:

Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation:
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.


Constraints:
0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.
"""


import collections
from typing import List


class Solution:
    def __init__(self):
        self.max_length = 0
    """
和 1522. Diameter of N-Ary Tree 一样, 对于某个节点来说, 经过当前节点的最长路径为当前节点最深的两个孩子节点的高度之和, 不过这道题并没有给出树的结构, 所以要事先初始化一个 Map 保存每个节点及其可访问的其他节点;
    """
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        self._dfs(graph, 0, -1)

        return self.max_length

    def _dfs(self, graph, node, parent):
        max1, max2 = 0, 0

        for child in graph[node]:
            if child == parent:
                continue

            depth = self._dfs(graph, child, node)

            if depth > max1:
                max1, max2 = depth, max1
            elif depth > max2:
                max2 = depth

        self.max_length = max(self.max_length, max1 + max2)

        return max1 + 1


