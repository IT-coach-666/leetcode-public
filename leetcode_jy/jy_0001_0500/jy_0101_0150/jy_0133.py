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
title_jy = "Clone-Graph(graph)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a reference of a node in a connected undirected graph. Return a deep copy (clone)
of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its
neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}



Test case format:
For simplicity sake, each node's value is the same as the node's index (1-indexed). For example,
the first node with val = 1, the second node with val = 2, and so on. The graph is represented in
the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list
describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given
node as a reference to the cloned graph.



Example 1:    https://www.yuque.com/frederick/dtwi9g/pfqgrs
Input: adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
Output: [[2, 4], [1, 3], [2, 4], [1, 3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only
one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Example 4:
Input: adjList = [[2], [1]]
Output: [[2], [1]]


Constraints:
• 1 <= Node.val <= 100
• Node.val is unique for each node.
• Number of Nodes will not exceed 100.
• There is no repeated edges and no self-loops in the graph.
• The Graph is connected and all nodes can be visited starting from the given node.
"""


from collections import deque
from about_GraphNode import *
from typing import Dict


class Solution:
    """
解法1: 使用广度优先搜索求解, 将原图的结点和新图的结点的映射存储在 Map 中, 每次出
队一个结点, 遍历该结点的邻居结点;
    """
    def cloneGraph_v1(self, node: Node) -> Node:
        if not node:
            return node
        queue = deque([node])
        visited = {
            node: Node(node.val)
        }
        while queue:
            old_node = queue.popleft()
            for neighbor in old_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[old_node].neighbors.append(visited[neighbor])
        return visited[node]

    """
解法2: 还可以使用深度优先搜索;
    """
    def cloneGraph_v2(self, node: Node) -> Node:
        visited = {}
        return self._clone(node, visited)

    def _clone(self, node: Node, visited: Dict[Node, Node]) -> Node:
        if not node:
            return node
        if node not in visited:
            visited[node] = Node(node.val)
        else:
            return visited[node]
        for neighbor in node.neighbors:
            visited[node].neighbors.append(self._clone(neighbor, visited))
        return visited[node]


adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
# Output: [[2, 4], [1, 3], [2, 4], [1, 3]]
node = build_graph(adjList)
res = Solution().cloneGraph_v2(node)
showNode(res, ls_adj=[])
print(len(res.neighbors))


adjList = [[]]
# Output: [[]]

adjList = []
# Output: []

adjList = [[2], [1]]
# Output: [[2], [1]]


