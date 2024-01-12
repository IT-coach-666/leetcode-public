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
tag_jy = "循环 | 递归 | 相似题: 0116"


"""
Given a binary tree:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no
next right node, the next pointer should be set to NULL. Initially, all next
pointers are set to NULL.


Follow up:
1) You may only use constant extra space.
2) Recursive approach is fine, you may assume implicit stack space does not
   count as extra space for this problem.


Input: root = [1, 2, 3, 4, 5, null, 7]
	              1
		     / \
		    2   3
		   / \   \
		  4  5    7
Output: [1, #, 2, 3, #, 4, 5, 7, #]
Explanation: Given the above binary tree, your function should populate each
             next pointer to point to its next right node, just like:
		      1     --> null
		     / \
		    2   3   --> null
		   / \   \
		  4  5    7 --> null
             The serialized output is in level order as connected by the next
             pointers, with '#' signifying the end of each level.


Constraints:
1) The number of nodes in the given tree is less than 6000.
2) -100 <= node.val <= 100
"""


from collections import deque
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import inorderTraversal


class Solution:
    """
解法 1: 同 0116 (Populating-Next-Right-Pointers-in-Each-Node) 的解法 1
    """
    def connect_v1(self, root: TreeNode) -> TreeNode:
        queue = deque([root]) if root else deque()
        while queue:
            prev = None
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
解法 2: 递归

同理 0116 (Populating-Next-Right-Pointers-in-Each-Node) 的解法 2, 需要注意两点:
1) 为左右子结点赋值 next 时, 需找出 root.next 的下一层的第一个节点
2) 递归调用时要先处理右子结点, 再处理左子结点, 否则处理下层结点时有可能上层结
   点的 next 链还没有构建完成 (因为确保右侧的 next 链先构建好, 后续遍历左侧时
   寻找 next 节点才能连续)
    """
    def connect_v2(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        # jy: 找出 root.next 的下一层的第一个节点
        next_node = self._find_next(root.next)
        # jy: 如果 root 的左子节点存在, 将其 next 指向 root 的右子节点 (如果
        #     不存在则指向 root.next 的下一层的第一个节点)
        if root.left:
            root.left.next = root.right or next_node
        # jy: 如果 root 的右子节点存在, 则将其 next 指向 next_node
        if root.right:
            root.right.next = next_node
        # jy: 注意: 递归时要先处理右子节点, 再处理左子结点【trick】
        self.connect_v2(root.right)
        self.connect_v2(root.left)
        return root

    def _find_next(self, root: TreeNode) -> TreeNode:
        """
        找出 root 的下一层的第一个节点
        """
        while root:
            if root.left or root.right:
                return root.left or root.right
            root = root.next
        return None


    """
解法 3: 创建一个 dummy 节点作为当前层的哑节点, 基于上一层的结点将当前层的
节点进行连接 (初始时, 上一层即根节点, 当前层即第二层, 即根节点的下一层; 当
上一层节点存在 next 指针时, 会从左到右遍历完上一层的所有节点)
    """
    def connect_v3(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        head = root
        # jy: dummy 节点作为每一层的首节点使用; 
        dummy = TreeNode(-1)

        # jy: current 表示当前层的当前节点, 初始化为哑节点
        current = dummy
        # jy: 不断循环遍历当前层节点
        #     1) 如果存在左子节点, 则拼接到 current.next, 并更新 current 值
        #        为该子节点
        #     2) 如果存在右子节点, 则拼接到 current.next, 并更新 current 值
        #        为该子节点
        while root:
            if root.left:
                current.next = root.left
                current = current.next
            if root.right:
                current.next = root.right
                current = current.next
            # jy: 更新当前层的节点, 使其向 next 前进一个; 如果节点不存在, 表
            #     明当前层已经完成; 此时将 root 置为 dummy.next (即原样恢复当
            #     前层的首节点), 将 dummy.next 置为 None (原样恢复 dummy 节
            #     点), 并恢复 current 值为 dummy (即下一层的首节点)
            root = root.next
            if not root:
                root = dummy.next
                dummy.next = None
                current = dummy

        return head



ls_ = [1, 2, 3, 4, 5, None, 7]
root = build_binary_tree(ls_)
print("inorderTraversal: ", inorderTraversal(root))
res = Solution().connect_v1(root)
print("inorderTraversal: ", inorderTraversal(root))



ls_ = [1, 2, 3, 4, 5, None, 7]
root = build_binary_tree(ls_)
print("inorderTraversal: ", inorderTraversal(root))
res = Solution().connect_v2(root)
print("inorderTraversal: ", inorderTraversal(root))



ls_ = [1, 2, 3, 4, 5, None, 7]
root = build_binary_tree(ls_)
print("inorderTraversal: ", inorderTraversal(root))
res = Solution().connect_v3(root)
print("inorderTraversal: ", inorderTraversal(root))

