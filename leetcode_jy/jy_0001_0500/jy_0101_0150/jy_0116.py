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
tag_jy = ""


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


Follow up:
• You may only use constant extra space.
• Recursive approach is fine, you may assume implicit stack space does not
  count as extra space for this problem.


Example 1:
Input: root = [1, 2, 3, 4, 5, 6, 7]
      1
     / \
    2   3
   / \  /\
  4  5 6  7
Output: [1, #, 2, 3, #, 4, 5, 6, 7, #]
Explanation: Given the above perfect binary tree, your function should populate each next
pointer to point to its next right node, just like:
      1     --> null
     / \
    2   3   --> null
   / \  /\
  4  5 6  7 --> null

The serialized output is in level order as connected by the next pointers, with '#'
signifying the end of each level.


Constraints:
• The number of nodes in the given tree is less than 4096.
• -1000 <= node.val <= 1000
"""

from collections import deque
from about_TreeNode import *


class Solution:
    """
解法1: 同 102_Binary-Tree-Level-Order-Traversal.py 的解法2, 处理当前层结点
时, 依次将上一个结点的 next 指针指向当前结点;
    """
    def connect_v1(self, root: TreeNode) -> TreeNode:
        queue = deque([root]) if root else deque()
        while queue:
            prev = None
            # jy: 每循环一次就会从 queue 中出队(左侧出队)当前层的所有节点, 并将下一层的节点
            #    添加到队尾(先添加左子节点, 后添加右子节点), 使得每一次 for 循环从左侧出队
            #    时即为树结构当前层从左到右的结果;
            for _ in range(len(queue)):
                node = queue.popleft()
                # jy: 如果 prev 为 None, 表示此时 node 为当前层的第一个元素; 将 prev 设置为
                #    首元素;
                if not prev:
                    prev = node
                # jy: 如果 prev 不为 None, 即 node 的上一个值即为 prev, 此时将 prev.next 指向
                #    node 即可; 同时 prev 指向该值;
                else:
                    prev.next, prev = node, node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


    """
解法2: 题目中要求算法的空间复杂度为常数级, 所以不能使用基于队列的广度优先搜索, 可以使用递归求解; 对于
每个结点 root, 它的左子结点的 next 就是右子节点, 而右子结点的 next 就是 root.next 的左子结点;
    """
    def connect_v2(self, root: TreeNode) -> TreeNode:
        # jy: 递归的终止条件;
        if not root:
            return root
        # jy: root 左节点如果存在, 则将其 next 指向 root 的右节点;
        if root.left:
            root.left.next = root.right
        # jy: root 右节点如果存在, 则将其 next 指向 root.next 的 左节点;
        if root.right:
            root.right.next = root.next.left if root.next else None
        # jy: 经过以上, 即完成 root 节点的下一层节点的连接; 随后递归完成其下下层的连接;
        self.connect_v2(root.left)
        self.connect_v2(root.right)
        return root



    """
解法3: 从上往下逐层遍历, 从每一层的最左结点开始, 根据 next 链依次设置当前结点的左右子节点的 next 指针指向;
    """
    def connect_v3(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        # jy: 第一层的最左侧节点即为根节点;
        left_most = root
        while left_most.left:
            current = left_most
            # jy: 将当前层的左子节点(即下一层)的 next 指向当前层的右子节点;
            while current:
                current.left.next = current.right
                # jy: 如果当前层的 next 节点存在, 则将当前层的右子节点的 next 指向当前层的 next 的左子节点;
                if current.next:
                    current.right.next = current.next.left
                # jy: 往当前层中递进, 不断连接其下一层;
                current = current.next
            # jy: 以上 while 循环完成后, 即完成当前层的下一层的连接; 此时, 将下一层的左子节点(由于是完全二叉
            #    树, 对应的左子节点如果不存在, 则表示该层不存在)赋值后进行下一个 while 循环;
            left_most = left_most.left
        return root


ls_ = [1, 2, 3, 4, 5, 6, 7]
root = build_binary_tree(ls_)
print("in_order: ", in_order(root, ls_ = []))
#print("pre_order: ", pre_order(root, ls_ = []))
res = Solution().connect_v1(root)
print("in_order: ", in_order(root, ls_ = []))



ls_ = [1, 2, 3, 4, 5, 6, 7]
root = build_binary_tree(ls_)
print("in_order: ", in_order(root, ls_ = []))
#print("pre_order: ", pre_order(root, ls_ = []))
res = Solution().connect_v2(root)
print("in_order: ", in_order(root, ls_ = []))


ls_ = [1, 2, 3, 4, 5, 6, 7]
root = build_binary_tree(ls_)
print("in_order: ", in_order(root, ls_ = []))
#print("pre_order: ", pre_order(root, ls_ = []))
res = Solution().connect_v3(root)
print("in_order: ", in_order(root, ls_ = []))


