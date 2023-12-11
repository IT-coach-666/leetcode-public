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
title_jy = "Subtree-of-Another-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the roots of two binary trees ``root`` and ``subRoot``, return true if there is
a subtree of ``root`` with the same structure and node values of ``subRoot`` and false
otherwise. A subtree of a binary tree ``tree`` is a tree that consists of a node in
``tree`` and all of this node's descendants. The tree ``tree`` could also be considered
as a subtree of itself.


Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false


Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4
"""


from about_TreeNode import *


class Solution:
    """
遍历二叉树，当 root.val == subRoot.val 时，递归判断 root 的左右子树是否和 subRoot 的左右子树相同
    """
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return self._dfs(root, subRoot, False)

    def _dfs(self, root, sub_root, need_continuous):
        if not root:
            return not sub_root

        if not sub_root:
            return False

        if root.val == sub_root.val \
                and self._dfs(root.left, sub_root.left, True) \
                and self._dfs(root.right, sub_root.right, True):
            return True

        if need_continuous:
            return False
        else:
            return self._dfs(root.left, sub_root, False) or self._dfs(root.right, sub_root, False)


ls_root = [3, 4, 5, 1, 2]
ls_subRoot = [4, 1, 2]
#Output: true
root = build_binary_tree(ls_root)
subRoot = build_binary_tree(ls_subRoot)
res = Solution().isSubtree(root, subRoot)
print(res)


ls_root = [3, 4, 5, 1, 2, None, None, None, None, 0]
ls_subRoot = [4,1,2]
# Output: false
root = build_binary_tree(ls_root)
subRoot = build_binary_tree(ls_subRoot)
res = Solution().isSubtree(root, subRoot)
print(res)

# 判断树是否是另一棵树的子树


