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
title_jy = "All-Paths-From-Source-to-Target(graph)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all
possible paths from node 0 to node n-1, and return them in any order.

The graph is given as follows: (图: https://www.yuque.com/frederick/dtwi9g/cch44b)
graph[i] is a list of all nodes you can visit from node i (i.e., there is a
directed edge from node i to node graph[i][j]).


Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Example 3:
Input: graph = [[1],[]]
Output: [[0,1]]

Example 4:
Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]

Example 5:
Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]


Constraints:
n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
The input graph is guaranteed to be a DAG.
"""


from typing import List
from collections import deque


class Solution:
    """
解法1: 典型的深度优先搜索遍历;
    """
    def allPathsSourceTarget_v1(self, graph: List[List[int]]) -> List[List[int]]:
        """
        graph 为图, 其数据结构用列表表示, 即 graph 参数为列表类型, 其中 graph 的下标(index)为
        图节点, 而 graph[index] 的值也为列表类型, 列表中的值为当前 index 节点指向的所有下一节
        点;
        """
        if not graph:
            return []
        paths = []
        # jy: 当前的节点值为 0 (0 节点), 对应的路径只有一个节点的路径: [0],
        self._dfs(0, graph, [0], paths)
        return paths

    def _dfs(self, i, graph, path, paths):
        """
        用 i 记录图路径的节点值, 最大值(即长度减 1)为末尾节点; 递归时会遍历 i 节点的
        指向, 并将其加入到路径列表 path 中;
        """
        # jy: 如果 i 已经是末尾节点, 则将当前构造的路径 path 加入路径列表 paths 中;
        if i == len(graph) - 1:
            paths.append(path)
        else:
            # jy: graph[i] 为一个列表, 保存着 i 节点指向的所有下一节点, 而 path 中包含了
            #    某一截止 i 节点为止的路径, 此时遍历 i 节点指向的所有节点(即 graph[i]),
            #    并将其加入到路径 path 中, 加入后递归传递的首个参数也为相应加入的节点,
            #    用于后续获取该配加入到路径最后的节点的所有下一节点指向;
            for j in graph[i]:
                self._dfs(j, graph, path + [j], paths)


    """
解法2: 广度优先搜索版本;
    """
    def allPathsSourceTarget_v2(self, graph: List[List[int]]) -> List[List[int]]:
        """
        graph 为图, 其数据结构用列表表示, 即 graph 参数为列表类型, 其中 graph 的下标(index)为
        图节点, 而 graph[index] 的值也为列表类型, 列表中的值为当前 index 节点指向的所有下一节
        点;
        """
        if not graph:
            return []
        # jy: n 记录末尾节点值;
        n = len(graph) - 1
        paths = []
        # jy: 先将 0 节点以及截止当前 0 节点的路径(即 [0]) 以元组的形式入队;
        queue = deque([(0, [0])])

        while queue:
            # jy: 左侧出队元组元素(实现先入先出; 注意, 此处右侧出队也是可以的, 顺序不重
            #    要), 得到节点 node 以及一条截止该节点为止的路径 path;
            node, path = queue.popleft()
            # jy: 如果 node 是末尾节点, 则将此条截止 node 节点为止的路径 path 加入路径
            #    列表 paths 中;
            if node == n:
                paths.append(path)
            # jy: 如果 node 不是末尾节点, 则遍历 node 节点指向的所有节点, 并将相应节点加入
            #    到 path 中, 同时将元组: (刚加入的节点 i, 加入节点 i 后的 path) 加入到队
            #    列中, 后续出队时会再次遍历节点 i 的下一节点指向, 并将相应的节点加入 path
            #    并继续以相应的节点组成元组继续入队;
            else:
                for i in graph[node]:
                    queue.append((i, path + [i]))

        return paths


graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
res = Solution().allPathsSourceTarget_v1(graph)
print(res)


graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
res = Solution().allPathsSourceTarget_v1(graph)
print(res)


graph = [[1],[]]
# Output: [[0,1]]
res = Solution().allPathsSourceTarget_v2(graph)
print(res)


graph = [[1,2,3],[2],[3],[]]
# Output: [[0,1,2,3],[0,2,3],[0,3]]
res = Solution().allPathsSourceTarget_v2(graph)
print(res)


graph = [[1,3],[2],[3],[]]
# Output: [[0,1,2,3],[0,3]]
res = Solution().allPathsSourceTarget_v2(graph)
print(res)


