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
title_jy = "Boundary-of-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
The boundary of a binary tree is the concatenation of the root, the left boundary,
the leaves ordered from left-to-right, and the reverse order of the right boundary.
The left boundary is the set of nodes defined by the following:
1) The root node's left child is in the left boundary. If the root does not have a
   left child, then the left boundary is empty.
2) If a node in the left boundary and has a left child, then the left child is in
   the left boundary.
3) If a node is in the left boundary, has no left child, but has a right child, then
   the right child is in the left boundary.
4) The leftmost leaf is not in the left boundary.

The right boundary is similar to the left boundary, except it is the right side of
the root's right subtree. Again, the leaf is not part of the right boundary, and the
right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not
a leaf.

Given the root of a binary tree, return the values of its boundary.


Example 1:    https://www.yuque.com/frederick/dtwi9g/rcwkc2
Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
Explanation: The left boundary is empty because the root does not have a left child.
             The right boundary follows the path starting from the root's right child
             2 -> 4, 4 is a leaf, so the right boundary is [2]. The leaves from left to
             right are [3,4]. Concatenating everything results in:
             [1] + [] + [3,4] + [2] = [1,3,4,2].


Example 2:
Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
Output: [1,2,4,7,8,9,10,6,3]
Explanation: The left boundary follows the path starting from the root's left child 2 -> 4,
             4 is a leaf, so the left boundary is [2]. The right boundary follows the path
             starting from the root's right child 3 -> 6 -> 10, 10 is a leaf, so the right
             boundary is [3,6], and in reverse order is [6,3]. The leaves from left to right
             are [4,7,8,9,10]. Concatenating everything results in:
             [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-1000 <= Node.val <= 1000
"""


from typing import Optional, List
from about_TreeNode import *


class Solution:
    """
分别依次求得左边界，叶子结点，右边界
    """
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left_boundary = self._get_left_boundary(root.left)
        leaves = self._get_leaves(root)
        right_boundary = self._get_right_boundary(root.right)

        return [root.val] + left_boundary + leaves + right_boundary

    def _is_leaf(self, node):
        return not node.left and not node.right

    def _get_left_boundary(self, node):
        if not node:
            return []

        order = []

        while not self._is_leaf(node):
            order.append(node.val)

            node = node.left or node.right

        return order

    def _get_right_boundary(self, node):
        if not node:
            return []

        order = []

        while not self._is_leaf(node):
            order.append(node.val)

            node = node.right or node.left

        return order[::-1]

    def _get_leaves(self, root):
        if self._is_leaf(root):
            return []

        stack = [root]
        order = []

        while stack:
            node = stack.pop()

            if self._is_leaf(node):
                order.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)

        return order


ls_ = [1, None, 2, 3, 4]
# Output: [1,3,4,2]
root = build_binary_tree(ls_)
res = Solution().boundaryOfBinaryTree(root)
print(res)


root = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10]
# Output: [1,2,4,7,8,9,10,6,3]
root = build_binary_tree(ls_)
res = Solution().boundaryOfBinaryTree(root)
print(res)

# 求树的边界节点值（按逆时针顺序）


