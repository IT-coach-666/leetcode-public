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
title_jy = "Smallest-Subtree-with-all-the-Deepest-Nodes(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, the depth of each node is the shortest distance to the root.
Return the smallest subtree such that it contains all the deepest nodes in the original tree.
A node is called the deepest if it has the largest depth possible among any node in the entire tree.
The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

Example 1:    https://www.yuque.com/frederick/dtwi9g/ecchv1

Input: root = [3,5,1,6,2,0,8,None,None,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.

Example 2:
Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.

Example 3:
Input: root = [0,1,3,None,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.


Constraints:
The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.
Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
解法1
首先求出最深的叶子节点到根节点的路径, 然后求所有路径的最深公共祖先;
    """
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        stack = [(root, 1, [])]
        max_depth = 0
        candidates = []

        while stack:
            node, depth, paths = stack.pop()

            if not node.left and not node.right:
                if depth > max_depth:
                    max_depth = depth
                    candidates = [paths + [node]]
                elif depth == max_depth:
                    candidates.append(paths + [node])

            if node.left:
                stack.append((node.left, depth + 1, paths + [node]))

            if node.right:
                stack.append((node.right, depth + 1, paths + [node]))

        if len(candidates) == 1:
            return candidates[0][-1]

        for i in range(len(candidates[0])):
            for j in range(1, len(candidates)):
                if candidates[j][i] != candidates[j - 1][i]:
                    return candidates[0][i - 1]



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth


class Solution:
    """
解法2
递归判断左右子树中的最深叶子节点, 如果两者的深度相同, 那么当前节点就是所求的公共节点; 如果左节点深度大于右节点, 则返回左节点的结果, 否则返回右结点的结果;
    """
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self._dfs(root).node

    def _dfs(self, root):
        if not root:
            return Node(None, 0)

        left = self._dfs(root.left)
        right = self._dfs(root.right)

        if left.depth == right.depth:
            return Node(root, left.depth + 1)
        elif left.depth > right.depth:
            return Node(left.node, left.depth + 1)
        else:
            return Node(right.node, right.depth + 1)



