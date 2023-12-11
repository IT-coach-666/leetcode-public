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
title_jy = "Univalued-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A binary tree is uni-valued if every node in the tree has the same value.
Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Example 1:

Input: root = [1,1,1,1,1,None,1]
Output: true

Example 2:

Input: root = [2,2,2,5,2]
Output: false


Constraints:
The number of nodes in the tree is in the range [1, 100].
0 <= Node.val < 100
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
解法1
广度优先搜索;
    """
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        value = root.val
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node.val != value:
                return False

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return True


import collections
from typing import Optional


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
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self._dfs(root, root.val)

    def _dfs(self, root, value):
        if not root:
            return True

        if root.val != value:
            return False

        return self._dfs(root.left, value) and self._dfs(root.right, value)


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
解法3
基于栈的深度优先搜索;
    """
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [root]
        value = root.val

        while stack:
            node = stack.pop()

            if node.val != value:
                return False

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return True




