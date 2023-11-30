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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Balanced-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary tree, determine if it is height-balanced. For this problem, a
height-balanced binary tree is defined as: a binary tree in which the left and
right subtrees of every node differ in height by no more than 1.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true


Constraints:
The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
"""


from about_TreeNode import *


class Solution:
    """
解法1: 递归遍历每个节点判断左右子树的高度差是否不超过 1
    """
    def isBalanced_v1(self, root: TreeNode) -> bool:
        """
        判断以 root 为根节点的树是否是平衡的二叉树
        """
        # jy: 如果当前节点为空(表明能走到当前空节点, 且之前的节点均是满足平衡要求的), 直接返回 True
        if not root:
            return True
        # jy: 获取左右子树的高度;
        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)
        # jy: 如果左右子树的高度差不大于 1, 且递归判断左子树和右子树也是平衡的
        #     二叉树, 则返回 True;
        return abs(left_height - right_height) <= 1 and self.isBalanced_v1(root.left) and self.isBalanced_v1(root.right)

    def _get_height(self, root):
        """
        获取根节点为 root 的树的高度(递归实现)
        """
        if not root:
            return 0
        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)
        return max(left_height, right_height) + 1

    """
解法2: 解法 1 对每个子树判断高度时存在重复计算, 可以在递归判断树高度的同时就判断是
否平衡, 因为计算树的高度为深度优先搜索, 可同时判断局部二叉树是否平衡, 只要出现不平
衡, 则无需再计算子树的高度
    """
    def isBalanced_v2(self, root: TreeNode) -> bool:
        return self._is_balanced(root)[1]

    def _is_balanced(self, root):
        """
        判断以 root 为根节点的树是否是平衡二叉树, 并返回该树的高度;
        """
        if not root:
            return 0, True

        # jy: 递归判断左子树是否是平衡二叉树(存在一个子树为非平衡二叉树, 则表明整棵
        #     树并非平衡二叉树), 并返回左子树的高度;
        left_height, balanced = self._is_balanced(root.left)
        if not balanced:
            # jy: 当子树为非平衡二叉树时, 此处直接返回 False, 层层递归后该 False 即为
            #     最终的返回结果, 其中左子树高度的返回仅仅是为了确保该递归函数完整, 当
            #     balanced 为 False 时, 返回的 left_height 数值是多少已经不重要, 因为
            #     后续不会再用到了; 此处的 if 判断逻辑即明确 balanced 为 False, 故返回
            #     的 left_height 是多少都无所谓;
            return left_height, balanced
        # jy: 递归判断右子树是否是平衡二叉树, 并返回右子树的高度;
        right_height, balanced = self._is_balanced(root.right)
        if not balanced:
            # jy: 同上, 当子树非平衡时, 直接返回 False, 但为了与该递归方法的返回值格式保
            #     持一致, 故需要多返回一个 right_height (当返回 False 时, 其数值正确与否
            #     已无所谓, 因为后续不会再使用它)
            return right_height, balanced

        # jy: 记录以 root 为根节点的当前树的高度;
        height = max(left_height, right_height) + 1

        # jy: 如果左子树和右子树的高度差大于1, 则直接返回 False (并包含当前树的高度, 方便递归调用);
        if abs(left_height - right_height) > 1:
            # jy: 同上, 所有返回 False 的地方, 其对应返回的 height 数值正确与否都可以, 因为
            #     后续不需要再使用到该数值, 但为了保持与递归方法返回格式一致, 仍需要返回一个值;
            return height, False

        # jy: 返回当前树的高度以及是否是平衡二叉树(递归过程需使用到);
        return height, True


ls_ = [3, 9, 20, None, None, 15, 7]
root = build_binary_tree(ls_)
# Output: true
res = Solution().isBalanced_v1(root)
print(res)


ls_ = [1, 2, 2, 3, 3, None, None, 4, 4]
root = build_binary_tree(ls_)
# Output: false
res = Solution().isBalanced_v1(root)
print(res)


ls_ = []
root = build_binary_tree(ls_)
# Output: true
res = Solution().isBalanced_v1(root)
print(res)


