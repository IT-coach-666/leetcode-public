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
title_jy = "Count-Good-Nodes-in-Binary-Tree(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:    https://www.yuque.com/frederick/dtwi9g/uczyna

Input: root = [3,1,4,3,None,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,None,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.


Constraints:
The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
解法1
使用深度优先搜索, 分别遍历左右子树, 遍历时记录至今遇到的最大节点值, 如果当前节点的值大于该值, 则找到了一个满足条件的节点;
    """
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self._dfs(root, root.val)

    def _dfs(self, root, max_so_far):
        count = 1 if root.val >= max_so_far else 0

        if root.left:
            count += self._dfs(root.left, max(root.val, max_so_far))

        if root.right:
            count += self._dfs(root.right, max(root.val, max_so_far))

        return count

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
解法2
广度优先搜索版本;
    """
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        queue = deque([(root, root.val)])

        while queue:
            node, max_so_far = queue.popleft()

            if node.val >= max_so_far:
                count += 1

            if node.left:
                queue.append((node.left, max(node.val, max_so_far)))

            if node.right:
                queue.append((node.right, max(node.val, max_so_far)))

        return count


