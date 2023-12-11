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
title_jy = "Cousins-in-Binary-Tree(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example 1:    https://www.yuque.com/frederick/dtwi9g/giv2fq

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,None,4,None,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,None,4], x = 2, y = 3
Output: false


Constraints:
The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
解法1
深度优先搜索树, 记录上一个遇到 x 或 y 时的父节点和深度, 再次遇到 x 或 y 时比较两者的父节点和深度;
    """

    def isCousins_v1(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        stack = [(root, 0, None)]
        prev_parent = None
        prev_depth = -1

        while stack:
            node, depth, parent = stack.pop()

            if node.val == x or node.val == y:
                if prev_parent:
                    return prev_parent != parent and depth == prev_depth
                else:
                    prev_parent = parent
                    prev_depth = depth

            if node.left:
                stack.append((node.left, depth + 1, node))

            if node.right:
                stack.append((node.right, depth + 1, node))

        return False

import collections
from typing import Optional



    """
解法2: 广度优先搜索
    """
    def isCousins_v2(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = collections.deque([(root, 0, None)])
        prev_parent = None
        prev_depth = -1

        while queue:
            node, depth, parent = queue.popleft()

            if node.val == x or node.val == y:
                if prev_parent:
                    return prev_parent != parent and depth == prev_depth
                else:
                    prev_parent = parent
                    prev_depth = depth

            if node.left:
                queue.append((node.left, depth + 1, node))

            if node.right:
                queue.append((node.right, depth + 1, node))

        return False



