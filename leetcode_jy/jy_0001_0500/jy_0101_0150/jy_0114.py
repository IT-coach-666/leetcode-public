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
tag_jy = "递归 | 基于前序遍历"


"""
Given the `root` of a binary tree, flatten the tree into a "linked list":
1) The "linked list" should use the same `TreeNode` class where the right
   child pointer points to the next node in the list and the left child
   pointer is always null.
2) The "linked list" should be in the same order as a pre-order traversal
   of the binary tree.


Example 1:
Input: root = [1, 2, 5, 3, 4, null, 6]
             1
            / \
           2   5
          / \   \
         3   4   6
Output: [1, null, 2, null, 3, null, 4, null, 5, null, 6]
             1
              \
               2
                \
                 3
                  \
                   4
                    \
                     5
                      \
                       6

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]


Constraints:
1) The number of nodes in the tree is in the range [0, 2000].
2) -100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""


from typing import Optional
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import preorderTraversal


class Solution:
    """
解法 1: 基于前序遍历

前序遍历树节点, 然后构造单链表
    """
    def flatten_v1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ls_node = []
        self._preorder(root, ls_node)
        if not ls_node:
            return
        # jy: 将 nodes 列表中的树节点构造成链表 (right 指针充当链表
        #     的 next 指针, 原先的 left 指针指向 None)
        for i in range(len(ls_node) - 1):
            ls_node[i].left = None
            ls_node[i].right = ls_node[i+1]
        ls_node[-1].left = None


    def _preorder(self, root, ls_):
        if not root:
            return
        ls_.append(root)
        self._preorder(root.left, ls_)
        self._preorder(root.right, ls_)


    """
解法 2: 栈 + 循环实现前序遍历, 并对前序遍历过程中的节点基于 right 属性
进行拼接, 并将节点的 left 属性设置为 None
    """
    def flatten_v2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        prev = None
        # jy: 初始时将根节点入栈
        stack = [root]
        while stack:
            node = stack.pop()
            # jy: 如果链表的前一个节点存在, 则将前节点的 right 指针指向当
            #     前出栈的树节点
            if prev:
                prev.right = node

            # jy: 先将树节点的右子节点入栈, 随后将左子节点入栈 (确保左子
            #     节点在后续出栈时比右子节点先出栈)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            # jy: 将当前节点的 left 指针置为 None, 并将 prev 更新为当
            #     前 node 节点
            node.left = None
            prev = node

    """
解法 3: 递归
    """
    def flatten_v3(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        # jy: 如果 root 为叶子节点, 则直接返回
        if not root.left and not root.right:
            return root

        # jy: 递归将左子树拍平, 拍平后即为一个链表 (right 指针即为链表的
        #     next 指针, left 指针值为 None, flatten_left 为链表的头节点)
        flatten_left = self.flatten_v3(root.left)
        # jy: 递归将右子树拍平
        flatten_right = self.flatten_v3(root.right)
        # jy: 如果 flatten_left 存在, 则将当前节点的 right 指针指向该拍平
        #     后的结果,并遍历至 flatten_left 的末尾节点, 将末尾节点的 right 
        #     指针指向 flatten_right
        if flatten_left:
            root.right = flatten_left
            while flatten_left.right:
                flatten_left = flatten_left.right
            flatten_left.right = flatten_right

        # jy: 将根节点的 left 指针指向 None
        root.left = None
        return root




ls_ = [1, 2, 5, 3, 4, None, 6]
root = build_binary_tree(ls_)
Solution().flatten_v1(root)
# jy: [1, null, 2, null, 3, null, 4, null, 5, null, 6]
print(preorderTraversal(root))


ls_ = []
root = build_binary_tree(ls_)
Solution().flatten_v2(root)
# jy: []
print(preorderTraversal(root))


ls_ = [0]
root = build_binary_tree(ls_)
Solution().flatten_v3(root)
# jy: [0]
print(preorderTraversal(root))


