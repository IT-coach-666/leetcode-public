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
title_jy = "Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.


For example, given:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""


from typing import List
from about_TreeNode import *


class Solution:
    """
对于前序遍历, 第一个元素是根结点, 由于题目中明确了不会有重复的结点, 所以根据根结点的值
在中序遍历的数组中找到这个值, 记下标为 i, 则 i 之前的元素构成左子树, i 之后的元素构成
右子树, 递归调用求解;
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self._build(preorder, 0, len(preorder)-1,
                           inorder, 0, len(inorder)-1)

    def _build(self,
               preorder: List[int], preorder_left: int, preorder_right: int,
               inorder: List[int], inorder_left: int, inorder_right: int) -> TreeNode:
        """
        依据 preorder[preorder_left, preorder_right] 和 inorder[inorder_left, inorder_right]
        构建树;
        """
        # jy: 递归的退出条件;
        if preorder_left > preorder_right or inorder_left > inorder_right:
            return None

        # jy: 依据前序遍历的首节点, 获取对应的 root 值;
        root_value = preorder[preorder_left]

        # jy: i 为 root_value 在 inorder 中的对应下标; 由于 inorder 在递归过程中的值不会被改变,
        #    故 i 可直接通过 inorder.index(root_value) 获取到;
        i = next(j for j in range(inorder_left, inorder_right+1) if inorder[j] == root_value)
        #i = inorder.index(root_value)

        # jy: 中序遍历中下标 i 的左侧为左子树, 此处获取左子树的元素个数;
        left_tree_length = i - inorder_left
        # jy: 构建根节点;
        root = TreeNode(root_value)
        # jy: 依据 preorder[preorder_left+1, preorder_left + left_tree_length] 和
        #    inorder[inorder_left, i-1] 构建左子树;
        root.left = self._build(
            preorder, preorder_left+1, preorder_left + left_tree_length,
            inorder, inorder_left, i-1)
        # jy: 依据 preorder[preorder_left + left_tree_length + 1, preorder_right] 和
        #    inorder[i+1, inorder_right] 构建右子树;
        root.right = self._build(
            preorder, preorder_left + left_tree_length + 1, preorder_right,
            inorder, i+1, inorder_right)

        return root



preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
res = Solution().buildTree(preorder, inorder)
print(pre_order(res))


