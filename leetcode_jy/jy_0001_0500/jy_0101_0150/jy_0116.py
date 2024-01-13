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
title_jy = "Populating-Next-Right-Pointers-in-Each-Node(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 循环 | 相似题: 0117"


"""
You are given a perfect binary tree where all leaves are on the same level, and
every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next
right node, the next pointer should be set to NULL. Initially, all next pointers
are set to NULL.



Example 1:
Input: root = [1, 2, 3, 4, 5, 6, 7]
      1
     / \
    2   3
   / \  /\
  4  5 6  7
Output: [1, #, 2, 3, #, 4, 5, 6, 7, #]
Explanation: Given the above perfect binary tree, your function should populate
             each next pointer to point to its next right node, just like:
                     1     --> null
                    / \
                   2   3   --> null
                  / \  /\
                 4  5 6  7 --> null
            The serialized output is in level order as connected by the next
            pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []
 

Constraints:
1) The number of nodes in the tree is in the range [0, 2^12 - 1].
2) -1000 <= Node.val <= 1000
 

Follow-up:
1) You may only use constant extra space.
2) The recursive approach is fine. You may assume implicit stack space does
   not count as extra space for this problem.
"""

from collections import deque
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import inorderTraversal


class Solution:
    """
解法 1: 队列 + 循环/迭代

参考 0102 (Binary-Tree-Level-Order-Traversal) 的解法 1, 但增加一个变量记录当
前层节点的上一个节点, 处理当前层结点时, 依次将同一层的上一个结点的 next 指针
指向当前结点
    """
    def connect_v1(self, root: TreeNode) -> TreeNode:
        queue = deque([root]) if root else deque()
        while queue:
            # jy: 记录当前层节点的上一个节点, 初始化为 None
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()

                # jy: 如果 prev 为 None, 表示此时 node 为当前层的第一个元素;
                #     如果 prev 不为 None, 即 node 的上一个值即为 prev, 此时
                #     将 prev.next 指向当前节点 node, 同时 prev 更新为当前节点
                if not prev:
                    prev = node
                else:
                    prev.next, prev = node, node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


    """
解法 2: 递归

题目要求空间复杂度为常数级, 所以不能使用基于队列的广度优先搜索, 可递归求解:
对于每个结点 root, 它的左子结点的 next 就是右子节点, 而右子结点的 next 就是
root.next 的左子结点
    """
    def connect_v2(self, root: TreeNode) -> TreeNode:
        # jy: 递归的终止条件
        if not root:
            return root

        # jy: 如果当前节点的左子节点存在, 则将其 next 指针指向当前节点的
        #     右子节点
        if root.left:
            root.left.next = root.right

        # jy: root 右节点如果存在, 则将其 next 指向 root.next 的左节点
        if root.right:
            root.right.next = root.next.left if root.next else None
        # jy: 以上完成 root 节点的下一层节点的连接; 随后递归完成其下下层
        self.connect_v2(root.left)
        self.connect_v2(root.right)
        return root


    """
解法 3: 从上往下逐层遍历: 从每一层的最左结点开始, 根据 next 链依次设置当
前结点的左右子节点的 next 指针指向
    """
    def connect_v3(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        # jy: 第一层的最左侧节点即为根节点
        left_most = root
        # jy: 由于是满二叉树, 因此左子节点必定存在
        while left_most.left:
            current = left_most
            # jy: 基于当前层的节点, 将当前层的下一层节点从左到右依次通过 next
            #     指针连接起来
            while current:
                current.left.next = current.right
                # jy: 如果当前层的 next 节点存在, 则将当前层的右子节点的 next
                #     指向当前层的 next 的左子节点
                if current.next:
                    current.right.next = current.next.left
                # jy: 往当前层中递进, 不断连接其下一层
                current = current.next
            # jy: 以上 while 循环完成后, 即完成当前层的下一层的连接; 此时将下
            #     一层的左子节点 (由于是完全二叉树, 对应的左子节点如果不存在,
            #     则表示该层不存在) 赋值后进行下一个 while 循环
            left_most = left_most.left
        return root


ls_ = [1, 2, 3, 4, 5, 6, 7]
root = build_binary_tree(ls_)
print("inorderTraversal: ", inorderTraversal(root))
res = Solution().connect_v1(root)
print("inorderTraversal: ", inorderTraversal(root))
#serialize


ls_ = [1, 2, 3, 4, 5, 6, 7]
root = build_binary_tree(ls_)
print("inorderTraversal: ", inorderTraversal(root))
res = Solution().connect_v2(root)
print("inorderTraversal: ", inorderTraversal(root))


ls_ = [1, 2, 3, 4, 5, 6, 7]
root = build_binary_tree(ls_)
print("inorderTraversal: ", inorderTraversal(root))
res = Solution().connect_v3(root)
print("inorderTraversal: ", inorderTraversal(root))

