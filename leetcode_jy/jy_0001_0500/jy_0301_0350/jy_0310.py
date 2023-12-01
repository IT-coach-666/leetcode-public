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
title_jy = "Minimum-Height-Trees(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A tree is an undirected graph in which any two vertices are connected by exactly
one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n-1, and an array of n-1 edges where
edges[i] = [ai, bi] indicates that there is an undirected edge between the two
nodes ``ai`` and ``bi`` in the tree, you can choose any node of the tree as the
root. When you select a node ``x`` as the root, the result tree has height h.
Among all possible rooted trees, those with minimum height (i.e. min(h))  are
called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path
between the root and a leaf.


Example 1:    https://www.yuque.com/frederick/dtwi9g/mc5qg5
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with
             label 1 which is the only MHT.

Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

Example 3:
Input: n = 1, edges = []
Output: [0]

Example 4:
Input: n = 2, edges = [[0,1]]
Output: [0,1]


Constraints:
1 <= n <= 2 * 10^4
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
"""


import collections
from typing import List


class Solution:
    """
解法1(超时): 首先根据 edges 使用 Map 保存所有结点的邻居关系, 然后遍历 n, 以每个数字
为根结点, 使用广度优先搜素计算树的高度, 最后返回高度最低的树;
    """
    def findMinHeightTrees_v1(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbours = collections.defaultdict(list)
        # jy: 使用字典保存所有节点之间的相邻关系(双向保存, 如 [1, 0] 时保存为 {0:1, 1:0})
        for edge in edges:
            neighbours[edge[0]].append(edge[1])
            neighbours[edge[1]].append(edge[0])

        min_height = n
        result = []
        # jy: 遍历所有节点(编号为 0 至 n-1), 求将当前节点作为根节点时树的高度(如果高度小于
        #     原先高度, 则更新最小高度, 如果高度相等, 则加入最小高度);
        for i in range(n):
            visited = set()
            height = 0
            queue = collections.deque([i])

            while queue:
                height += 1
                # jy: 获取当前高度时的节点数;
                size = len(queue)
                # jy: 如果高度已经大于原先的最小高度了, 则直接跳出循环, 进行下一轮循环;
                if height > min_height:
                    break
                # jy: 将与当前节点相邻的节点全部加入
                for _ in range(size):
                    # jy: 左侧出队, 确保先进先出(确保当前出队的节点是对应当前高度的节点)
                    node = queue.popleft()
                    visited.add(node)
                    # jy: 将与当前节点相邻的下一节点入队(如果下一节点没有被访问过的话)
                    for neighbour in neighbours[node]:
                        if neighbour not in visited:
                            queue.append(neighbour)
            # jy: 如果当前节点作为树的根节点, 此时计算树的高度等于原先的最小高度记录, 则将当
            #     前根节点加入原先结果中; 如果小于原先记录的最小高度, 则更新最小高度记录;
            if height == min_height:
                result.append(i)
            elif height < min_height:
                result = [i]
                min_height = height

        return result

    """
解法2: 同样根据 edges 使用 Map 保存所有结点的邻居关系, 然后将只有一个邻居的结点加入
到队列中, 广度优先搜索队列, 每次出队一个结点时, 根据 Map 弹出一个该结点的邻居, 同时
在该邻居结点的邻居中删除当前结点, 如果邻居结点的邻居只有 1 个时, 将该邻居加入到队列中;
最后队列中剩下的元素就是满足条件的根结点

JY: LeetCode 上运行表明, 时间复杂度和空间复杂度相对较高
    """
    def findMinHeightTrees_v2(self, n: int, edges: List[List[int]]) -> List[int]:
        # jy-version-1-Begin --------------------------------------------------------------
        #'''
        # jy: 如果 edges 为空, 则此时的 n 肯定为 1 (只有一个节点), 节点编号为 0, 直接
        #     返回 [0] 即可;
        if len(edges) == 0:
            # return [n-1]
            return [0]

        # jy: 使用字典保存所有节点之间的相邻关系(双向保存, 如 [1, 0] 时保存为 {0:1, 1:0})
        neighbours = collections.defaultdict(list)
        for edge in edges:
            neighbours[edge[0]].append(edge[1])
            neighbours[edge[1]].append(edge[0])
        # jy: 将只有一个邻居的结点加入到队列中; 如 edges 为 [[1, 0], [1, 2], [1, 3]] 时, 队
        #     列 queue 为 [3, 2, 0]
        queue = collections.deque()
        # jy: 如果当前节点的邻居只有一个, 表明当前节点是树的 "叶子节点" 将其加入到队列中;
        for node, neighbour in neighbours.items():
            if len(neighbour) == 1:
                queue.append(node)
        # jy: 如果当前队列不为空, 且节点数 n 大于 2, 则继续循环出队(因为不管什么结构, 答案最
        #     多只能有 2 个节点; 也可能是只有 1 个节点)
        while queue and n > 2:
            # jy: 广度优先搜索, 将上一轮的 "叶子节点" 全部出队, 如果相应叶子节点出队后, 与其
            #     相邻的节点
            size = len(queue)
            n -= size
            for _ in range(size):
                # jy: 出队时要左侧出队, 保证先进先出, 确保出队元素是广度优先搜索的当前层的叶子节点;
                node = queue.popleft()
                neighbour = neighbours[node].pop()
                # jy: 由于 node 是 "叶子节点", 获取其相邻节点后, 即可将其在 neighbours 中的记
                #     录删除, 不影响结果(不删除也不影响后续逻辑);
                del neighbours[node]
                # jy: 将叶子节点 node 的相邻节点在 neighbours 中与该叶子节点的关联边记录去除;
                neighbours[neighbour].remove(node)
                # jy: 如果叶子节点 node 的相邻节点在 neighbours 中与该叶子节点的关联边记录去除
                #     后, 对应的相邻节点 neighbour 变成了叶子节点, 则将其如队;
                if len(neighbours[neighbour]) == 1:
                    queue.append(neighbour)
        return list(queue)
        # '''
        # jy-version-1-End ----------------------------------------------------------------
        # jy-version-2-Begin --------------------------------------------------------------
        '''
        # 简单无向图, 套路是建图并遍历; 建图(邻接表), 邻接表为 map, 其值为 list, 它的 size 就是入度数
        if n == 2:
            return [0, 1]
        if n == 1:
            return [0]

        adjs = defaultdict(list)
        # 图的邻接表表示法, 基本是模板
        for x in edges:
            adjs[x[0]].append(x[1])
            adjs[x[1]].append(x[0])
        # BFS 队列: 初始队列放入初始元素, size=1 的为叶子, 入队
        queue = deque()
        for key, value in adjs.items():
            if len(value) == 1:
                queue.append(key)

        # BFS 两个大循环
        while queue:
            size = len(queue)
            n = n - size

            for _ in range(size):
                v = queue.popleft()
                # v 的邻接仅一个, 弹出即删除
                v_adj = adjs[v].pop()
                # 在 v 的邻接元素的邻接列表里删除 v
                adjs[v_adj].remove(v)
                if len(adjs[v_adj]) == 1:
                    queue.append(v_adj)
            if n == 1:
                return [queue.popleft()]
            if n == 2:
                return [queue.popleft(), queue.popleft()]
        '''
        # jy-version-2-End ----------------------------------------------------------------


n = 4
edges = [[1, 0], [1, 2], [1, 3]]
# Output: [1]
res = Solution().findMinHeightTrees_v1(n, edges)
print(res)


n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
# Output: [3,4]
res = Solution().findMinHeightTrees_v1(n, edges)
print(res)


n = 1
edges = []
# Output: [0]
res = Solution().findMinHeightTrees_v1(n, edges)
print(res)


n = 2
edges = [[0, 1]]
# Output: [0,1]
res = Solution().findMinHeightTrees_v1(n, edges)
print(res)



