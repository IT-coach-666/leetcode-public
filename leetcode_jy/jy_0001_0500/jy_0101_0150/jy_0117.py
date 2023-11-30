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
title_jy = "Populating-Next-Right-Pointers-in-Each-Node-II(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary tree:
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


Input: root = [1, 2, 3, 4, 5, null, 7]
      1
     / \
    2   3
   / \   \
  4  5    7
Output: [1, #, 2, 3, #, 4, 5, 7, #]
Explanation: Given the above binary tree, your function should populate each next
pointer to point to its next right node, just like:
      1     --> null
     / \
    2   3   --> null
   / \   \
  4  5    7 --> null

The serialized output is in level order as connected by the next pointers, with '#'
signifying the end of each level.


Constraints:
• The number of nodes in the given tree is less than 6000.
• -100 <= node.val <= 100
"""


from collections import deque
from about_TreeNode import *


class Solution:
    """
解法1: 116_Populating-Next-Right-Pointers-in-Each-Node.py 的解法 1 本身就适用普通的二叉树;
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
解法2: 同理 116_Populating-Next-Right-Pointers-in-Each-Node.py 解法 2(递归), 需要注意两点:
1. 为左右子结点赋值 next 时, 需遍历父结点的 next 链, 直到找到第一个结点为止
2. 递归调用时要先处理右子结点, 再处理左子结点, 否则处理下层结点时有可能上层结点的 next 链还没有构建完成
    """
    def connect_v2(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        # jy: 找出 root.next 的下一层的第一个节点
        next_node = self._find_next(root.next)
        # jy: 如果 root 的左子节点存在, 将其 next 指向 root 的右子节点(如果不存在则指
        #    向 root.next 的下一层的第一个节点)
        if root.left:
            root.left.next = root.right or next_node
        # jy: 如果 root 的右子节点存在, 则将其 next 指向 root 的右子节点(如果不存在则指
        #    向 root.next 的下一层的第一个节点)
        if root.right:
            root.right.next = next_node
        # jy: 递归时要先处理右子节点, 再处理左子结点;【trick】
        self.connect_v2(root.right)
        self.connect_v2(root.left)
        return root

    def _find_next(self, root: TreeNode) -> TreeNode:
        """找出 root 的下一层的第一个节点"""
        while root:
            if root.left or root.right:
                return root.left or root.right
            root = root.next
        # jy: 此处即返回 None;
        return root


    """
解法3: 为下一层的结点创建一个 dummy 头, 上一层的结点随着 next 移动时, 构建下一层的结点链
表, 当某一层的结点走完后, 以 dummy.next 结点开始新的一层遍历;
    """
    def connect_v3(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        head = root
        dummy = TreeNode(-1)
        current = dummy
        # jy: 不断循环遍历当前层节点, 先将其左节点(如果存在)拼接到 current 节点, 并更新 current 值,
        #    再将其右子节点(如果存在)拼接到 current, 并更新 current 值; 即将当前层的下一层进行拼接;
        while root:
            if root.left:
                current.next = root.left
                current = current.next
            if root.right:
                current.next = root.right
                current = current.next
            # jy: 更新当前层的节点, 递进一个; 如果节点不存在, 表明当前层已经完成; 此时将 root 置为
            #    dummy.next, 即下一层的首节点; 并将 dummy.next 置为 None, 并恢复 current 值为 dummy,
            #    进行下一轮循环;
            root = root.next
            if not root:
                root = dummy.next
                dummy.next = None
                current = dummy

        return head



ls_ = [1, 2, 3, 4, 5, None, 7]
root = build_binary_tree(ls_)
print("in_order: ", in_order(root, ls_ = []))
res = Solution().connect_v1(root)
print("in_order: ", in_order(root, ls_ = []))




ls_ = [1, 2, 3, 4, 5, None, 7]
root = build_binary_tree(ls_)
print("in_order: ", in_order(root, ls_ = []))
res = Solution().connect_v2(root)
print("in_order: ", in_order(root, ls_ = []))




ls_ = [1, 2, 3, 4, 5, None, 7]
root = build_binary_tree(ls_)
print("in_order: ", in_order(root, ls_ = []))
res = Solution().connect_v3(root)
print("in_order: ", in_order(root, ls_ = []))


