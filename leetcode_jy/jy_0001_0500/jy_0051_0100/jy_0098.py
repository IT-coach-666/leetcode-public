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
tag_jy = "递归 | 中序遍历 (循环/迭代 + 栈)"



"""
Given the `root` of a binary tree, determine if it is a valid binary search
tree (BST). A valid BST is defined as follows:
1) The left subtree of a node contains only nodes with keys less than the
   node's key.
2) The right subtree of a node contains only nodes with keys greater than
   the node's key.
3) Both the left and right subtrees must also be binary search trees.


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


Constraints:
1) The number of nodes in the tree is in the range [1, 10^4].
2) -2^31 <= Node.val <= 2^31 - 1
"""


import sys
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import inorderTraversal


class Solution:
    """
解法 0: 错误递归示例

仅考虑到根节点比左子节点大, 比右子节点小; 无法确保根节点比所有的左子节点
大, 或比所有的右子节点小

Input: [5, 4, 6, None, None, 3, 7]
    5
   / \
  4   6
     / \
    3   7
    """
    def isValidBST_v0(self, root: TreeNode) -> bool:
        if not root:
            return True

        if root.left:
            if root.val <= root.left.val:
                return False
        if root.right:
            if root.val >= root.right.val:
                return False

        is_left_valid = self.isValidBST_v1(root.left)
        is_right_valid = self.isValidBST_v1(root.right)
        return is_left_valid and is_right_valid


    """
解法 1: 递归

递归时传入当前子树结点值的最大值和最小值:
1) 左子树最大值限定为根结点的值, 最小值初始化为极小值
2) 右子树最小值为根结点的值, 最大值初始化为极大值

递归时将最大, 最小值更新为当前结点的值
    """
    def isValidBST_v1(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self._is_valid(root.left, -sys.maxsize, root.val) and \
               self._is_valid(root.right, root.val, sys.maxsize)

    def _is_valid(self, root: TreeNode, low: int, high: int) -> bool:
        """
        限定以 root 为根节点的树中节点的最小值与最大值
        """
        if not root:
            return True
        # jy: 如果根节点的值不在有效数值范围内, 则返回 False
        if root.val <= low or root.val >= high:
            return False

        # jy: 左子树的最大值不能超过当前根节点值; 右子树的最小值不能
        #     小于当前根节点的值
        return self._is_valid(root.left, low, root.val) and \
               self._is_valid(root.right, root.val, high)


    """
解法 2: 中序遍历后判断遍历结果是否单调升序 (后一个数是否都比前一个数大)
    """
    def isValidBST_v2(self, root: TreeNode) -> bool:
        # jy: 中序遍历二叉树
        ls_num = inorderTraversal(root)
        # jy: 判断遍历的结果中是否总是前一个数小于后一个数的值
        for i in range(1, len(ls_num)):
            if ls_num[i] <= ls_num[i-1]:
                return False
        return True


    """
解法 3: 非递归模式的中序遍历 (栈) 中补充代码逻辑

每次出栈一个元素时, 如果当前元素的值小于或等于前一个值, 则返回 false
    """
    def isValidBST_v3(self, root: TreeNode) -> bool:
        stack = []
        current = root
        # jy: 记录中序遍历过程中的前一值, 初始化为一个很小的值
        prev_value = -sys.maxsize
        while current or stack:
            # jy: 将当前节点入栈, 随后不断循环将其左节点入栈
            while current:
                stack.append(current)
                current = current.left

            # jy: 出栈一个节点, 如果小于等于前一节点值, 则返回 False
            current = stack.pop()
            if current.val <= prev_value:
                return False
            # jy: 将 prev_value 更新为最新出栈的节点值
            prev_value = current.val
            # jy: 将当前节点指向当前出栈节点的右子节点, 随后进行下一轮循环
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





