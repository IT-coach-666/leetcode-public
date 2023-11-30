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
title_jy = "Validate-Binary-Search-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
• The left subtree of a node contains only nodes with keys less than the node's key.
• The right subtree of a node contains only nodes with keys greater than the node's key.
• Both the left and right subtrees must also be binary search trees.


Example 1:
Input: [2, 1, 3]
    2
   / \
  1   3
Output: true


Example 2:
Input: [5, 1, 4, null, null, 3, 6]
    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""



import sys
from about_TreeNode import *


class Solution:
    """
解法1: 可以使用递归求解, 分别递归左子树和右子树, 递归时传入当前子树结点值的最大值和最小值, 对于
左子树来说最大值为根结点的值, 最小值初始化为整型的最小值; 对于右子树来说, 最小值为根结点的值, 最
大值初始化为整型的最大值, 递归时将最大, 最小值更新为当前结点的值;
    """
    def isValidBST_v1(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self._is_valid(root.left, -sys.maxsize, root.val) and \
               self._is_valid(root.right, root.val, sys.maxsize)

    def _is_valid(self, root: TreeNode, low: int, high: int) -> bool:
        if not root:
            return True
        # jy: 如果根节点的值小于最小值或大于最大值, 则返回 False;
        if root.val <= low or root.val >= high:
            return False

        return self._is_valid(root.left, low, root.val) and \
               self._is_valid(root.right, root.val, high)


    """
解法2: 第二种解法是先通过中序遍历树, 将所有的结点的值放入数组中, 如果是合法的二叉搜索
树, 则最后数组是有序排列, 最后遍历数组判断数组的后一个数是否都比前一个数大;
    """
    def isValidBST_v2(self, root: TreeNode) -> bool:
        numbers = []
        # jy: 中序遍历二叉树(递归方式);
        self._inorder_traversal(root, numbers)
        # jy: 判断遍历的结果中是否总是前一个数小于后一个数的值, 如果存在前一个数大于或等
        #    于后一个数, 则返回 False;
        for i in range(1, len(numbers)):
            if numbers[i] <= numbers[i-1]:
                return False
        return True

    def _inorder_traversal(self, root: TreeNode, numbers):
        """二叉树中序遍历"""
        if not root:
            return
        self._inorder_traversal(root.left, numbers)
        numbers.append(root.val)
        self._inorder_traversal(root.right, numbers)


    """
解法3: 借助 094_Binary-Tree-Inorder-Traversal.py 非递归模式的中序遍历(栈), 每次出栈一个元素时
判断当前元素的值是否小于等于前一个值, 是则返回 false;
    """
    def isValidBST_v3(self, root: TreeNode) -> bool:
        stack = []
        current = root
        # jy: prev_value 记录中序遍历过程中的前一值, 初始化为一个很小的值;
        prev_value = -sys.maxsize
        while current or stack:
            # jy: 将当前节点入栈, 随后不断循环将其左节点入栈;
            while current:
                stack.append(current)
                current = current.left
            # jy: 出栈一个节点, 后续遍历该节点右子节点(该过程出栈时即为中序遍历过程);
            #    此时比较出栈时的节点值, 如果小于等于前一节点值, 则返回 False;
            current = stack.pop()
            if current.val <= prev_value:
                return False
            # jy: 将 prev_value 设为最新出栈的节点值;
            prev_value = current.val
            current = current.right
        return True


ls_ = [2, 1, 3]
root = build_binary_tree(ls_)
res = Solution().isValidBST_v1(root)
print(res)


ls_ = [5, 1, 4, None, None, 3, 6]
root = build_binary_tree(ls_)
res = Solution().isValidBST_v2(root)
print(res)


res = Solution().isValidBST_v3(root)
print(res)





