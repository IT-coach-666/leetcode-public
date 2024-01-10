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
tag_jy = "递归 | 相似题: 0106 | IMP2"


"""
Given two integer arrays `preorder` and `inorder` where `preorder` is the
preorder traversal of a binary tree and `inorder` is the inorder traversal
of the same tree, construct and return the binary tree.


Example 1:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
Return the following binary tree: [3, 9, 20, null, null, 15, 7]
    3
   / \
  9  20
    /  \
   15   7

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:
1) 1 <= preorder.length <= 3000
2) inorder.length == preorder.length
3) -3000 <= preorder[i], inorder[i] <= 3000
4) `preorder` and `inorder` consist of unique values.
5) Each value of `inorder` also appears in `preorder`.
6) `preorder` is guaranteed to be the preorder traversal of the tree.
7) `inorder` is guaranteed to be the inorder traversal of the tree.
"""


from typing import List
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import serialize


class Solution:
    """
解法 1: 递归

前序遍历的第一个元素是根结点, 由于题目中明确不会有重复的结点, 所以在中序
遍历的数组中找到根节点的值, 假设下标为 i, 则 i 之前的元素构成左子树, i 之
后的元素构成右子树, 递归调用求解
    """
    def buildTree_v1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self._build(preorder, 0, len(preorder)-1,
                           inorder, 0, len(inorder)-1)

    def _build(self,
               preorder: List[int], p_left: int, p_right: int,
               inorder: List[int], i_left: int, i_right: int) -> TreeNode:
        """
        依据以下前序遍历和中序遍历的下标范围 (两端的边界下标均包含在内) 构
        建二叉树:
        preorder 中的下标范围 [p_left, p_right]
        inorder 中的下标范围  [i_left, i_right]
        """
        # jy: 递归的退出条件
        if p_left > p_right or i_left > i_right:
            return None

        # jy: 前序遍历的首节点为根节点
        root_value = preorder[p_left]

        # jy: i 为 root_value 在 inorder 中的对应下标
        i = next(j for j in range(i_left, i_right+1) if inorder[j] == root_value)
        # jy: inorder 在递归过程中的值不会被改变, 因此 i 也可直接通过以下方式获取
        #i = inorder.index(root_value)

        # jy: 中序遍历中下标 i 的左侧为左子树, 基于 i 可获取左子树的元素个数
        left_tree_length = i - i_left
        # jy: 构建根节点
        root = TreeNode(root_value)
        # jy: 依据以下下标范围 (两端边界的下标均包含在内) 构建左子树:
        #     preorder 的下标范围 [p_left + 1, p_left + left_tree_length]
        #     inorder  的下标范围 [i_left, i - 1]
        root.left = self._build(
            preorder, p_left + 1, p_left + left_tree_length,
            inorder, i_left, i-1)
        # jy: 依据以下下标范围 (两端边界的下标均包含在内) 构建右子树:
        #     preorder 的下标范围 [p_left + left_tree_length + 1, p_right]
        #     inorder 的下标范围  [i + 1, i_right]
        root.right = self._build(
            preorder, p_left + left_tree_length + 1, p_right,
            inorder, i+1, i_right)

        return root


    """
解法 2: 递归的另一种写法
    """
    def buildTree_v2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # jy: 递归终止条件
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])  
        idx = inorder.index(preorder[0])
        # jy: 递归对 root 的左右子树求解
        root.left = self.buildTree_v2(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree_v2(preorder[1 + idx:], inorder[idx + 1:])
        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
res = Solution().buildTree_v1(preorder, inorder)
# jy: [3, 9, 20, None, None, 15, 7]
print(serialize(res))


preorder = [-1]
inorder = [-1]
res = Solution().buildTree_v1(preorder, inorder)
# jy: [-1]
print(serialize(res))


