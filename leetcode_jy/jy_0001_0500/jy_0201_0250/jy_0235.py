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
title_jy = "Lowest-Common-Ancestor-of-a-Binary-Search-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given
nodes in the BST. According to the definition of LCA on Wikipedia:   "The lowest common
ancestor is defined between two nodes p and q as the lowest node in T that has both p
and q as descendants (where we allow a node to be a descendant of itself)."



Given binary search tree: 
root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]

图见: https://www.yuque.com/frederick/dtwi9g/rtgsxy

Example 1:
Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
             according to the LCA definition.



Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""



from about_TreeNode import *
class Solution:
    """
首先计算 p 和 q 两者值的较小值和较大值, 记为 min_value 和 max_value, 根据二叉搜索树的特性:
1) 如果根结点的值在 (min_value, max_value) 区间内, 则这个根结点为 p 和 q 的最近公共祖先
2) 如果根结点的值小于 min_value, 则最近公共祖先在根结点的右子树中
3) 如果根结点的值大于 max_value, 则最近公共祖先在根结点的左子树中
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        min_value = min(p.val, q.val)
        max_value = max(p.val, q.val)

        while current:
            # jy: 如果根节点的值小于 min_value, 表明最近公共祖先在根结点的右子树中;
            if min_value > current.val:
                current = current.right
            # jy: 如果根节点的值大于 max_value, 表明最近公共祖先在根结点的左子树中;
            elif max_value < current.val:
                current = current.left
            # jy: 经过以上 if, 此处表明根节点的值在 (min_value, max_value) 区间内, 即该跟节点
            #    即为 p 和 q 的最近公共祖先;
            else:
                return current



ls_ = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p = 2
q = 8
root = build_binary_tree(ls_)
# Output: 6
res = Solution().lowestCommonAncestor(root, p, q)
print(res.val)


res = Solution().lowestCommonAncestor(root, p, q)
print(res.val)
p = 2
q = 4
# Output: 2


