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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Find-All-The-Lonely-Nodes(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.
Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.

Example 1:

Input: root = [1,2,3,None,4]
Output: [4]
Explanation: Light blue node is the only lonely node.
Node 1 is the root and is not lonely.
Nodes 2 and 3 have the same parent and are not lonely.

Example 2:

Input: root = [7,1,4,6,None,5,3,None,None,None,None,None,2]
Output: [6,2]
Explanation: Light blue nodes are lonely nodes.
Please remember that order doesn't matter, [2,6] is also an acceptable answer.

Example 3:

Input: root = [11,99,88,77,None,None,66,55,None,None,44,33,None,None,22]
Output: [77,55,33,66,44,22]
Explanation: Nodes 99 and 88 share the same parent. Node 11 is the root.
All other nodes are lonely.

Example 4:
Input: root = [197]
Output: []

Example 5:
Input: root = [31,None,78,None,28]
Output: [78,28]


Constraints:
The number of nodes in the tree is in the range [1, 1000].
Each node's value is between [1, 10^6].
"""

import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
解法1
广度优先搜索;
    """
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        nodes = []
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if (node.left and not node.right) \
                    or (node.right and not node.left):
                nodes.append(node.left.val if node.left else node.right.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return nodes

import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
解法2
深度优先搜索;
    """
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []

        self._dfs(root, nodes)

        return nodes

    def _dfs(self, node, nodes):
        if not node:
            return

        if (node.left and not node.right) \
                or (node.right and not node.left):
            nodes.append(node.left.val if node.left else node.right.val)

        if node.left:
            self._dfs(node.left, nodes)

        if node.right:
            self._dfs(node.right, nodes)

        return nodes



