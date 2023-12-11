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
title_jy = "All-Nodes-Distance-K-in-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.

Example 1:    https://www.yuque.com/frederick/dtwi9g/nahyw2

Input: root = [3,5,1,6,2,0,8,None,None,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: []


Constraints:
The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
"""


import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
解法1
首先使用 Map 保存每个节点的父节点, 然后将目标节点加入队列, 每次出队时, 将当前节点的左节点, 右节点, 父节点加入队列, 并将距离增加1;
    """
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []
        parents, queue, visited = {}, collections.deque([(target, 0)]), set()

        self._get_parents(root, None, parents)

        while queue:
            node, distance = queue.popleft()

            if node in visited:
                continue

            visited.add(node)

            if distance == k:
                result.append(node.val)

            if node.left:
                queue.append((node.left, distance + 1))

            if node.right:
                queue.append((node.right, distance + 1))

            if node in parents and parents[node]:
                queue.append((parents[node], distance + 1))

        return result

    def _get_parents(self, root, parent, parents):
        parents[root] = parent

        if root.left:
            self._get_parents(root.left, root, parents)

        if root.right:
            self._get_parents(root.right, root, parents)


from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
解法2
基于栈的深度优先搜索;
    """
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []
        parents, stack, visited = {}, [(target, 0)], set()

        self._get_parents(root, None, parents)

        while stack:
            node, distance = stack.pop()

            if node in visited:
                continue

            visited.add(node)

            if distance == k:
                result.append(node.val)

            if node.left:
                stack.append((node.left, distance + 1))

            if node.right:
                stack.append((node.right, distance + 1))

            if node in parents and parents[node]:
                stack.append((parents[node], distance + 1))

        return result

    def _get_parents(self, root, parent, parents):
        parents[root] = parent

        if root.left:
            self._get_parents(root.left, root, parents)

        if root.right:
            self._get_parents(root.right, root, parents)


