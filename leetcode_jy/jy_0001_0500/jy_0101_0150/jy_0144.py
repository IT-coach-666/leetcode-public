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
title_jy = "Binary-Tree-Preorder-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.


Example 1:    https://www.yuque.com/frederick/dtwi9g/fe2brb
Input: root = [1, null, 2, 3]
Output: [1, 2, 3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1, 2]
Output: [1, 2]

Example 5:
Input: root = [1, null, 2]
Output: [1, 2]


Constraints:
• The number of nodes in the tree is in the range [0, 100].
• -100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""


from typing import List
from about_TreeNode import *


class Solution:
    """
解法1: 递归;
    """
    def preorderTraversal_v1(self, root: TreeNode) -> List[int]:
        values = []
        self._preorder_traversal(root, values)
        return values

    def _preorder_traversal(self, root: TreeNode, values: List[int]) -> None:
        # jy: 递归终止条件: 如果 root 为 None, 终止递归;
        if not root:
            return
        values.append(root.val)
        self._preorder_traversal(root.left, values)
        self._preorder_traversal(root.right, values)


    """
解法2: 循环, 首先将根节点压入栈, 只要栈不为空, 则执行出栈, 将出栈节点的值放入最终结果中, 如
果当前节点的右节点存在, 则将右节点压入栈, 如果左节点存在, 则将左节点压入栈;
    """
    def preorderTraversal_v2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        values = []
        # jy: 先将根节点入栈;
        stack = [root]
        while stack:
            # jy: 出栈一个元素, 并将出栈的元素加入 values 结果中;
            current = stack.pop()
            values.append(current.val)
            # jy: 先入栈当前节点的右子节点(如果右子节点存在)
            if current.right:
                stack.append(current.right)
            # jy: 后入栈当前节点的左子节点(如果左子节点存在)
            if current.left:
                stack.append(current.left)
            # jy: 经过以上, 下一轮 while 循环将会先出栈左子节点(且会先遍历完左子树, 再遍历右子树);
        return values


ls_ = [1, None, 2, None, None, 3]
root = build_binary_tree(ls_)
res = Solution().preorderTraversal_v1(root)
print(res)
# Output: [1, 2, 3]

ls_ = []
root = build_binary_tree(ls_)
res = Solution().preorderTraversal_v2(root)
print(res)
# Output: []

ls_ = [1]
root = build_binary_tree(ls_)
res = Solution().preorderTraversal_v2(root)
print(res)
# Output: [1]

ls_ = [1, 2]
root = build_binary_tree(ls_)
res = Solution().preorderTraversal_v2(root)
print(res)
# Output: [1, 2]

ls_ = [1, None, 2]
root = build_binary_tree(ls_)
res = Solution().preorderTraversal_v2(root)
print(res)
# Output: [1, 2]


