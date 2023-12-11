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
title_jy = "Check-Completeness-of-a-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given the root of a binary tree, determine if it is a complete binary tree.
In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:

Input: root = [1,2,3,4,5,None,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.


Constraints:
The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000
"""


import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
根据二叉树的性质, 对树的每个节点进行编号, 使用队列对树进行层序遍历, 判断当前节点的编号是否正确;
    """
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        depth = 1
        queue = collections.deque([(root, 1)])

        while queue:
            size = len(queue)

            for i in range(size):
                node, id = queue.popleft()

                if id != pow(2, depth - 1) + i:
                    return False

                if node.left:
                    queue.append((node.left, id * 2))

                if node.right:
                    queue.append((node.right, id * 2 + 1))

            if len(queue) > 0 and size != pow(2, depth - 1):
                return False

            depth += 1

        return True



