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
title_jy = "Linked-List-in-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary tree root and a linked list with head as the first node.
Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
In this context downward path means a path that starts at some node and goes downwards.

Example 1:

Input: head = [4,2,8], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.

Example 2:

Input: head = [1,4,2,6], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
Output: true

Example 3:
Input: head = [1,4,2,6,8], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.


Constraints:
The number of nodes in the tree will be in the range [1, 2500].
The number of nodes in the list will be in the range [1, 100].
1 <= Node.val <= 100 for each node in the linked list and binary tree.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
解法1
直接递归搜索, 搜索时需要标记当前链表的节点是否是头结点, 因为如果不是头结点说明后续的搜索必须是一条连续的路径;
    """
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) \
            -> bool:
        return self._dfs(head, root, True)

    def _dfs(self, head, root, is_head):
        if not head:
            return True

        if not root:
            return False

        if root.val == head.val:
            if is_head:
                return self._dfs(head.next, root.left, False) \
                       or self._dfs(head.next, root.right, False) \
                       or self._dfs(head, root.left, True) \
                       or self._dfs(head, root.right, True)
            else:
                return self._dfs(head.next, root.left, False) \
                       or self._dfs(head.next, root.right, False)
        else:
            if is_head:
                return self._dfs(head, root.left, True) \
                       or self._dfs(head, root.right, True)
            else:
                return False

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
解法2
解法2和解法1类似, 只是 _dfs 搜索的是以当前树节点起始是否存在路径和链表匹配;
    """
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) \
            -> bool:
        if not root:
            return not head

        if self._dfs(head, root):
            return True

        return self.isSubPath(head, root.left) \
            or self.isSubPath(head, root.right)

    def _dfs(self, head, root):
        if not head:
            return True

        if not root:
            return False

        if head.val != root.val:
            return False

        return self._dfs(head.next, root.left) \
            or self._dfs(head.next, root.right)


