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
title_jy = "Lowest-Common-Ancestor-of-a-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the
tree. According to the definition of LCA on Wikipedia:   "The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and q as
descendants (where we allow a node to be a descendant of itself)."



Given the following binary tree:  root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]

图见: https://www.yuque.com/frederick/dtwi9g/ln9hrl

Example 1:
Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.


Example 2:
Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.



Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""


from about_TreeNode import *

class Solution:
    """
235_Lowest-Common-Ancestor-of-a-Binary-Search-Tree.py 的加强版, 核心思想在于从根结点的
左右子树中分别找 p 或 q:
1) 如果 p 或 q 一个在左子树, 一个在右子树, 则表示根结点为最近公共祖先;
2) 如果左子树没有 p 也没有 q, 则继续在右子树找 p 和 q;
3) 如果右子树没有 p 也没有 q, 则继续在左子树找 p 和 q;
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # jy: 如果 root 已经为 None, 则直接返回 None, 表示没找到 p 或 q;
        #    如果 p 或 q 的值为 root, 则直接返回 root, 表示已经找到 p 或 q;
        if not root or p.val == root.val or q.val == root.val:
            return root
        # jy: 从左子树中查找 p 或 q(由于 p 或 q 都是唯一的, 在左子树找到了则不可能在右子树找到);
        left = self.lowestCommonAncestor(root.left, p, q)
        # jy: 从右子树中查找 p 或 q;
        right = self.lowestCommonAncestor(root.right, p, q)

        # jy: 如果 left 和 right 都不为 None, 表明 p 和 q 在 root 的左右两侧, 直接返回 root;
        if left and right:
            return root
        # jy: 如果 left 和 right 有一个为 None, 表明 p 和 q 同时在其某一侧, 返回该侧找到的 p
        #    或 q 节点即可;
        else:
            return left or right


ls_ = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
ls_p = [5]
ls_q = [1]
# Output: 3
root = build_binary_tree(ls_)
p = build_binary_tree(ls_p)
q = build_binary_tree(ls_q)
res = Solution().lowestCommonAncestor(root, p, q)
print(res.val)

ls_ = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
ls_p = [5]
ls_q = [4]
# Output: 5
root = build_binary_tree(ls_)
p = build_binary_tree(ls_p)
q = build_binary_tree(ls_q)
res = Solution().lowestCommonAncestor(root, p, q)
print(res.val)


