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
title_jy = "Inorder-Successor-in-BST-II(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a node in a binary search tree, return the in-order successor of that node in the BST.
If that node has no in-order successor, return null. The successor of a node is the node with
the smallest key greater than node.val. You will have direct access to the node but not to
the root of the tree. Each node will have a reference to its parent node. Below is the
definition for Node:
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}


Example 1: (图: https://www.yuque.com/frederick/dtwi9g/pc33l1)
Input: tree = [2, 1, 3], node = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.

Example 2:
Input: tree = [5,3,6,2,4,null,null,1], node = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.

Example 3:
Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 15
Output: 17

Example 4:
Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 13
Output: 15

Example 5:
Input: tree = [0], node = 0
Output: null


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
All Nodes will have unique values.


Follow up: Could you solve it without looking up any of the node's values?
"""


from about_TreeNode import *

class Solution:
    """
Follow up 中要求不允许比较节点的值, 根据二叉搜索树的性质:
1) 如果 node 存在右节点, 则它在中序遍历中的后继节点为它的右子树中的最小值, 等价于求右子树中最深的左叶子节点;
2) 如果不存在右节点, 则它的中序遍历中的后继节点只可能存在于它的父辈节点中, 一直遍历当前节点的父节点, 当父节
  点的左子树为当前节点时, 说明此时父节点比当前节点大, 也就是第一个比 node 大的节点;

    """
    def inorderSuccessor(self, node: 'TreeNode') -> 'TreeNode':
        # jy: 如果有右子树, 则找出右子树中最深的左叶子节点(即不断遍历右子树的左子节点, 直到对应的左
        #    子节点不再有左子节点为止; 如果一开始的节点就没有左子节点, 则直接返回该节点值);
        if node.right:
            current = node.right

            while current.left:
                current = current.left

            return current
        # jy: 如果不存在右子树, 则其中序遍历的后继节点只可能存在于父辈节点中, 一直遍历当前节点的父节点, 当父
        #    节点的左子树为当前节点时, 说明此时的父节点比当前节点大, 也就是第一个比 node 大的节点;
        current = node
        while current.parent:
            if current.parent.left is current:
                return current.parent

            current = current.parent

        return None


tree = [2, 1, 3]
# node = 1
# Output: 2
root = build_binary_tree(tree)
node = root.left
res_node = Solution().inorderSuccessor(node)
print(res_node.val)


tree = [5, 3, 6, 2, 4, None, None, 1]
# node = 6
# Output: null
root = build_binary_tree(tree)
node = root.right
res_node = Solution().inorderSuccessor(node)
print(res_node)




tree = [15, 6, 18, 3, 7, 17, 20, 2, 4, None, 13, None, None, None, None, None, None, None, None, 9]
# node = 15
# Output: 17
root = build_binary_tree(tree)
node = root
res_node = Solution().inorderSuccessor(node)
print(res_node.val)



tree = [15, 6, 18, 3, 7, 17, 20, 2, 4, None, 13, None, None, None, None, None, None, None, None, 9]
# node = 13
# Output: 15
root = build_binary_tree(tree)
node = root.left.right.right
res_node = Solution().inorderSuccessor(node)
print(res_node.val)



tree = [0]
# node = 0
# Output: null
root = build_binary_tree(tree)
node = root
res_node = Solution().inorderSuccessor(node)
print(res_node)


