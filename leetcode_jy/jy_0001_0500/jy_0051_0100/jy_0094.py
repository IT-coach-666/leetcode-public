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
title_jy = "Binary-Tree-Inorder-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given the `root` of a binary tree, return the inorder traversal of its
nodes' values.

Example 1:
Input: [1, null, 2, 3]
   1
    \
     2
    /
   3
Output: [1, 3, 2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]



Constraints:
1) The number of nodes in the tree is in the range [0, 100].
2) -100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""


from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import inorderTraversal, inorderTraversal_v2

class Solution:
    """
解法 1: 递归
    """
    def inorderTraversal_v1(self, root: TreeNode) -> List[int]:
        # jy: 参考 leetcode_jy.utils_jy.about_TreeNode 中的 inorderTraversal 函数
        return inorderTraversal(root)   


    """
解法 2: 维护一个栈, 只要当前结点有左子结点, 就将当前结点压入栈, 并将左子结点赋值给当
前结点, 直到遇到没有左子结点后, 则出栈一个结点, 然后对该结点的右子结点重复上述操作;
    """
    def inorderTraversal_v2(self, root: TreeNode) -> List[int]:
        return inorderTraversal_v2(root)


ls_ = [1, None, 2, None, None, 3]
root = build_binary_tree(ls_)

res = Solution().inorderTraversal_v1(root)
print(res)


res = Solution().inorderTraversal_v2(root)
print(res)



