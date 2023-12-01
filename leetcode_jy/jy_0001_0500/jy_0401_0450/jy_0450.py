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
title_jy = "Delete-Node-in-a-BST(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST. Basically, the deletion can be
divided into two stages:
Search for a node to remove.
If the node is found, delete the node.


Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
Each node has a unique value.
root is a valid binary search tree.
-10^5 <= key <= 10^5


Follow up: Can you solve it with time complexity O(height of tree)?
"""

from about_TreeNode import *



class Solution:
    """
递归求解
1) 如果当前节点的值小于 key, 则在右子树中删除 key;
2) 如果当前节点的值大于 key, 则在左子树中删除 key;
3) 如果当前节点的值等于 key, 则说明当前的节点需要被删除, 分为三种情况:
   a) 当前节点为叶子结点, 则直接删除当前节点
   b) 当前节点只有一个孩子节点, 则删除当前节点, 将孩子节点提升到当前节点的位置
   c) 当前节点有两个孩子节点, 删除当前节点的同时需要找一个节点替代当前节点, 只
      有当前节点的右子树中最小的节点可以替代, 即交换当前节点和右子树中最小的节
      点, 然后删除交换后的当前节点; 实际操作的时候可以不交换, 直接将当前节点的
      值替换为右子树中最小的节点的值, 然后在右子树中递归调用删除最小的节点即可
    """
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        # jy: 如果当前节点值等于 key, 说明要删除当前节点;
        else:
            # jy: 如果待删除的节点没有左子节点, 则直接返回待删除节点的右子节点即可(为 None 也不影响)
            if not root.left:
                return root.right
            # jy: 如果待删除的节点没有右子节点, 则直接返回待删除节点的左子节点即可(为 None 也不影响)
            elif not root.right:
                return root.left
            # jy: 如果待删除的节点的左右子节点均存在, 则找出右子树中的最小节点, 并将当前待删除的节点
            #    更新为该最小值(即原先节点已删除), 并在该右子树中删除该最小值;
            root.val = self._find_min(root.right)
            root.right = self.deleteNode(root.right, root.val)

        return root


    def _find_min(self, root):
        """找出二叉搜索树中的最小节点"""
        while root.left:
            root = root.left
        return root.val


ls_ = [5, 3, 6, 2, 4, None, 7]
root = build_binary_tree(ls_)
key = 3
# Output: [5, 4, 6, 2, null, null, 7]
res = Solution().deleteNode(root, key)
print("serialize: ", serialize(res))


ls_ = [5, 3, 6, 2, 4, None, 7]
root = build_binary_tree(ls_)
key = 0
# Output: [5,3,6,2,4,null,7]
res = Solution().deleteNode(root, key)
print("serialize: ", serialize(res))


ls_ = []
root = build_binary_tree(ls_)
key = 0
# Output: []
res = Solution().deleteNode(root, key)
print("serialize: ", serialize(res))


