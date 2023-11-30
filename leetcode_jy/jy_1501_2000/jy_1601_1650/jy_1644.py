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
title_jy = "Lowest-Common-Ancestor-of-a-Binary-Tree-II(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given 
nodes, p and q. If either node p or q does not exist in the tree, return null.  All 
values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two 
nodes p and q in a binary tree T is the lowest node that has both p and q as descendants
(where we allow a node to be a descendant of itself)". A descendant of a node x is a 
node y that is on the path from node x to some leaf node.



Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.

Example 3:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.



Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q



Follow up: Can you find the LCA traversing the tree, without checking nodes existence?
"""


from about_TreeNode import *


class Solution:

    def __init__(self):
        # jy: 记录 p 和 q 节点值出现的总次数;
        self.node_found_count = 0

    """
在 236_Lowest-Common-Ancestor-of-a-Binary-Tree.py 的基础上删除了 p 和 q 一定存在的前
提; 因此需要使用一个变量标记找到 p 和 q 的次数, 如果次数等于 2 说明 p 和 q 均存在(因
为节点值不会重复, 均唯一, 故出现次数为 2 表明均存在), 否则最后返回空; 
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = self._lowest_common_ancestor(root, p, q)
        return node if self.node_found_count == 2 else None


    def _lowest_common_ancestor(self, root, p, q):
        if not root:
            return root
        # jy: 从左子树中找 p 和 q 节点的最小公共祖先;
        left = self._lowest_common_ancestor(root.left, p, q)
        right = self._lowest_common_ancestor(root.right, p, q)

        # jy: 如果当前节点值正好是 p 或 q 对应的节点值, 则出现次数加 1, 并返回当前节点值(另
        #    外一个节点值会在当前节点值的左右子树中查找, 如果找到则出现次数会加 1, 且表明当
        #    前节点值即为最小公共祖先);
        if root.val == p.val or root.val == q.val:
            self.node_found_count += 1
            return root

        # jy: 如果当前节点的值不等于 p 和 q 节点对应的值, 但左右子树中均能找到与 p 或 q 节点
        #    相等的值, 表明当前节点 root 为他们的最小公共祖先(因为 p 和 q 节点肯定是分布在
        #    左右子树中, 否则返回的 left 和 right 中肯定有一个是空结果)
        if left and right:
            return root
        else:
            return left or right



ls_ = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build_binary_tree(ls_)
p = root.left      # 5
q = root.right     # 1
# Output: 3
res = Solution().lowestCommonAncestor(root, p, q)
print(res.val)



ls_ = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build_binary_tree(ls_)
p = root.left              # 5
q = root.left.right.right  # 4
# Output: 5
res = Solution().lowestCommonAncestor(root, p, q)
print(res.val)



ls_ = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build_binary_tree(ls_)
p = root.left       # 5
q = TreeNode(10)    # 10
# Output: null
res = Solution().lowestCommonAncestor(root, p, q)
print(res)



