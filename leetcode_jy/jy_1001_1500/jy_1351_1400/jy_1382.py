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
title_jy = "Balance-a-Binary-Search-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
given a binary search tree, return a balanced binary search tree with the same node values.
A binary search tree is balanced if and only if the depth of the two subtrees of every node
never differ by more than 1. If there is more than one answer, return any of them.


Example 1:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.


Constraints:
The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.
"""


from about_TreeNode import *


class Solution:
    """
首先中序遍历二叉搜索树获得一个有序队列, 题目就变成了 108_Convert-Sorted-Array-to-Binary-Search-Tree.py
    """
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []
        self._inorder(root, values)
        return self._convert_sorted_array_to_bst(values, 0, len(values) - 1)


    def _inorder(self, root, values):
        if not root:
            return
        self._inorder(root.left, values)
        values.append(root.val)
        self._inorder(root.right, values)

    def _convert_sorted_array_to_bst(self, values, low, high):
        if low > high:
            return None

        middle = low + (high - low) // 2
        root = TreeNode(values[middle])
        root.left = self._convert_sorted_array_to_bst(values, low, middle - 1)
        root.right = self._convert_sorted_array_to_bst(values, middle + 1, high)

        return root



ls_ = [1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4]
root = build_binary_tree(ls_)
# print(serialize(root))
# Output: [2,1,3,null,null,null,4]
res = Solution().balanceBST(root)
print(serialize(res))



