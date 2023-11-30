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
title_jy = "Flatten-Binary-Tree-to-Linked-List(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, flatten the tree into a "linked list":
1) The "linked list" should use the same TreeNode class where the right child pointer
   points to the next node in the list and the left child pointer is always null.
2) The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:  https://www.yuque.com/frederick/dtwi9g/by0hd2
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]


Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""


from typing import Optional
from about_TreeNode import *


class Solution:
    """
解法1: 首先前序遍历树, 然后构造单链表
    """
    def flatten_v1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        self._preorder(root, nodes)
        if not nodes:
            return
        # jy: 将 nodes 列表中的树节点构造成链表(right 指针充当链表的 next 指针, 原
        #     先的 left 指针指向 None)
        '''
        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].left = None
            nodes[i-1].right = nodes[i]
            nodes[i-1].left = None
        '''
        # jy-version-2-Begin------------------------------
        '''
        # jy: 替换为如下逻辑时, 要确保 nodes 不为空(增加最开始边界条件的判断), 否则就会
        #     出现 index 越界问题
        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].left = None
            nodes[i-1].right = nodes[i]
        nodes[0].left = None
        '''
        # jy-version-2-End--------------------------------
        # jy-version-3-Begin------------------------------
        # jy: 替换为如下逻辑时, 要确保 nodes 不为空(增加最开始边界条件的判断), 否则就会
        #     出现 index 越界问题
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
        nodes[-1].left = None
        # jy-version-3-End--------------------------------

    def _preorder(self, root, nodes):
        if not root:
            return
        nodes.append(root)
        self._preorder(root.left, nodes)
        self._preorder(root.right, nodes)

    """
解法2: 基于二叉树的前序遍历(【栈 + 循环】实现)
    """
    def flatten_v2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        prev = None
        # jy: 初始时将根节点入栈, 只有栈不为空, 则不断出栈; 随后将出栈的节点
        #     的右子节点入栈, 然后再子左节点入栈(栈 + 循环实现二叉树的前序遍历);
        stack = [root]
        while stack:
            node = stack.pop()
            # jy: 如果链表的前一个节点存在, 则将前节点的 right 指针指向当前出栈的树节点;
            if prev:
                prev.right = node
            # jy: 先将树节点的右子节点入栈, 随后将左子节点入栈;
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            # jy: 将当前节点的 left 指针置为 None, 并将 prev 更新为当前 node 节点;
            node.left = None
            prev = node

    """
解法3: 递归求解, 当左子树存在时, 需要遍历找到左子树的最后一个节点, 将其指向右子树

JY: 暂未理解
    """
    def flatten_v3(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self._dfs_v3(root)

    def _dfs_v3(self, root):
        if not root:
            return None
        # jy: 如果 root 为叶子节点, 则直接返回;
        if not root.left and not root.right:
            return root
        # jy: 递归获取当前树的左子树;
        left = self._dfs_v3(root.left)
        # jy: 递归获取当前树的右子树;
        right = self._dfs_v3(root.right)
        # jy: 如果左子树存在, 则将当前节点的 right 指针指向该左子树; 并找到该左子树的最后
        #     一个节点(最后一个右子节点), 将该右子节点指向当前节点的右子树;
        if left:
            root.right = left
            while left.right:
                left = left.right
            left.right = right
        # jy: 随后将当前节点的 left 指针指向 None;
        root.left = None
        return root


ls_ = [1, 2, 5, 3, 4, None, 6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
root = build_binary_tree(ls_)
Solution().flatten_v1(root)
print(pre_order(root))

ls_ = []
# Output: []
root = build_binary_tree(ls_)
Solution().flatten_v1(root)
print(pre_order(root))

ls_ = [0]
# Output: [0]
root = build_binary_tree(ls_)
Solution().flatten_v1(root)
print(pre_order(root))


