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
title_jy = "Flip-Equivalent-Binary-Trees(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivelent or false otherwise.

Example 1:     https://www.yuque.com/frederick/dtwi9g/qar8bm

Input: root1 = [1,2,3,4,5,6,None,None,None,7,8], root2 = [1,3,2,None,6,4,5,None,None,None,None,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Example 2:
Input: root1 = [], root2 = []
Output: true

Example 3:
Input: root1 = [], root2 = [1]
Output: false

Example 4:
Input: root1 = [0,None,1], root2 = []
Output: false

Example 5:
Input: root1 = [0,None,1], root2 = [0,1]
Output: true


Constraints:
The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
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
递归判断左右子树;
    """
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) \
            -> bool:
        if not root1 and not root2:
            return True

        if not self._equal(root1, root2):
            return False

        if self._equal(root1.left, root2.left) \
                and self._equal(root1.right, root2.right):
            return self.flipEquiv(root1.left, root2.left) \
                   and self.flipEquiv(root1.right, root2.right)
        elif self._equal(root1.left, root2.right) \
                and self._equal(root1.right, root2.left):
            return self.flipEquiv(root1.left, root2.right) \
                   and self.flipEquiv(root1.right, root2.left)
        else:
            return False

    def _equal(self, root1, root2):
        if root1 and root2:
            return root1.val == root2.val
        else:
            return not root1 and not root2


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    """
解法2
分别使用两个栈遍历树的节点, 根据两个树的节点的值来判断第二个栈的节点入栈顺序;
    """
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) \
            -> bool:
        if not root1 and not root2:
            return True

        stack1 = [root1]
        stack2 = [root2]

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if not self._equal(node1, node2):
                return False

            left1 = node1.left
            right1 = node1.right
            left2 = node2.left
            right2 = node2.right

            if left1:
                stack1.append(left1)

            if right1:
                stack1.append(right1)

            if self._equal(left1, left2) and self._equal(right1, right2):
                if left2:
                    stack2.append(left2)

                if right2:
                    stack2.append(right2)
            elif self._equal(left1, right2) and self._equal(right1, left2):
                if right2:
                    stack2.append(right2)

                if left2:
                    stack2.append(left2)
            else:
                return False

        return not stack1 and not stack2

    def _equal(self, root1, root2):
        if root1 and root2:
            return root1.val == root2.val
        else:
            return not root1 and not root2


