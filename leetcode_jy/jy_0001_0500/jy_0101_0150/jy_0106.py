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
title_jy = "Construct-Binary-Tree-from-Inorder-and-Postorder-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two integer arrays ``inorder`` and ``postorder`` where inorder is the inorder
traversal of a binary tree and postorder is the postorder traversal of the same tree,
construct and return the binary tree.


Example 1:    https://www.yuque.com/frederick/dtwi9g/nriba4
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]


Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder/postorder is guaranteed to be the inorder/postorder traversal of the tree.
"""


from typing import List
from about_TreeNode import *


class Solution:
    """
参考 105_Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal.py
基于中序和后续遍历的特性: 后序遍历的最后一个元素是树的根节点, 在中序遍历中寻找该根节点
值的下标位置 idx_root_val, 则中序遍历的该下标位置左侧、右侧分别为左子树、右子树的中序遍
历结果, 根据左子树、右子树的元素个数, 即可在后续遍历中获取对应的左子树、右子树的后续遍
历结果, 使得可以递归依据左子树的中序遍历结果和后续遍历结果构造二叉树(右子树同理)
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self._build_tree(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def _build_tree(self, inorder, inorder_start, inorder_end,
                          postorder, postorder_start, postorder_end):
        """
        inorder: 中序遍历结果(由该结果中的下标范围为 [inorder_start, inorder_end] 的数值构造当前树)
        postorder: 后序遍历结果(由该结果中的下标范围为 [postorder_start, postorder_end] 的数值构造当前树)
        """
        # jy: 如果起始下标大于终止下标, 则直接返回 None;
        if inorder_start > inorder_end or postorder_start > postorder_end:
            return None

        # jy: 后续遍历的最后一个节点即为当前树的根节点;
        root_value = postorder[postorder_end]
        root = TreeNode(root_value)

        # jy: 找出中序遍历中该根节点的下标;
        inorder_root_index = -1
        for i in range(inorder_start, inorder_end + 1):
            if inorder[i] == root_value:
                inorder_root_index = i
                break

        # jy: 计算当前根节点的左子树的节点数;
        left_tree_size = inorder_root_index - inorder_start
        # jy: 递归构造左子树
        #     1) inorder[inorder_start: inorder_root_index] 为左子树的中序遍历结果;
        #     2) postorder[postorder_start: postorder_start + left_tree_size] 为左子树的后续遍历结果;
        root.left = self._build_tree(inorder, inorder_start, inorder_root_index - 1,
                                     postorder, postorder_start, postorder_start + left_tree_size - 1)
        # jy: 递归构造右子树;
        #     1) inorder[inorder_root_index + 1: inorder_end + 1] 为右子树的中序遍历结果;
        #     2) postorder[postorder_start + left_tree_size: postorder_end] 为右子树的后续遍历结果;
        root.right = self._build_tree(inorder, inorder_root_index + 1, inorder_end,
                                      postorder, postorder_start + left_tree_size, postorder_end - 1)
        return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
# Output: [3,9,20,null,null,15,7]
res = Solution().buildTree(inorder, postorder)
print(serialize(res))


inorder = [-1]
postorder = [-1]
# Output: [-1]
res = Solution().buildTree(inorder, postorder)
print(serialize(res))


