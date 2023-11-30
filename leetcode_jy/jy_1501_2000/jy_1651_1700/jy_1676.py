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
title_jy = "Lowest-Common-Ancestor-of-a-Binary-Tree-IV(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given the root of a binary tree and an array of TreeNode objects nodes, return the 
lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in
the tree, and all values of the tree's nodes are unique.

Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes
p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant 
(where we allow a node to be a descendant of itself) for every validi". A descendant of
a node x is a node y that is on the path from node x to some leaf node.



Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
Output: 2
Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
Output: 1
Explanation: The lowest common ancestor of a single node is the node itself.

Example 3:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
Output: 5
Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.

Example 4:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [0,1,2,3,4,5,6,7,8]
Output: 3
Explanation: The lowest common ancestor of all the nodes is the root node.



Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
All nodes[i] will exist in the tree.
All nodes[i] are distinct.
"""


from about_TreeNode import *


class Solution:
    """
解法1(超时): 在 236_Lowest-Common-Ancestor-of-a-Binary-Tree.py 已经求解过两个节点的
场景, 对于 n 个节点, 使用分治法将 n 个节点分为两半, 依次求解各一半的节点的最近公共
祖先, 然后求解这两个局部公共祖先的最近公共祖先;
    """
    def lowestCommonAncestor_v1(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # jy: 采用分治算法, 求出 nodes 列表中第一个节点(下标为 0)到最后一个节点(下标为 len(nodes)-1)
        #    的最小公共祖先;
        return self._divide_and_conquer(root, nodes, 0, len(nodes) - 1)


    def _divide_and_conquer(self, root, nodes, start, end):
        # jy: 如果 start 大于 end, 返回 None, 终止递归;
        if start > end:
            return None
        # jy: start 等于 end 时, 表示求当前单个节点的最小公共祖先, 为其本身, 直接返回;
        elif start == end:
            return nodes[start]
        else:
            middle = start + (end - start) // 2
            # jy: 找出 nodes 列表中下标为 start 到 middle 的节点的最小公共祖先;
            p = self._divide_and_conquer(root, nodes, start, middle)
            # jy: 找出 nodes 列表中下标为 middle+1 到 end 的节点的最小公共祖先;
            q = self._divide_and_conquer(root, nodes, middle + 1, end)
            # jy: 找出 p 和 q 节点的最小公共祖先;
            return self._lowest_common_ancestor_v1(root, p, q)


    def _lowest_common_ancestor_v1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        找出两个节点的最小公共祖先, 同 236_Lowest-Common-Ancestor-of-a-Binary-Tree.py
        """
        # jy: 如果根节点为空, 或者 p 或 q 当中有一个等于根节点, 则直接返回根节点;
        if not root or p.val == root.val or q.val == root.val:
            return root

        # jy: 分别从根节点的左子树和右子树中找 p 和 q 节点的最小公共祖先:
        #    1) 如果 p 和 q 节点均在左子树中, 则求得的 left 为其最小公共祖先, 而 right 则为 None;
        #    2) 如果 p 和 q 节点均在右子树中, 则求得的 right 为其最小公共祖先, 而 left 则为 None;
        #    3) 如果 p 和 q 分布在左右子树(各占一个), 则 left 和 right 即为 p 和 q 节点本身, 此时
        #       的最小公共祖先为根节点 root;
        left = self._lowest_common_ancestor_v1(root.left, p, q)
        right = self._lowest_common_ancestor_v1(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right


    """
解法2: 和 236_Lowest-Common-Ancestor-of-a-Binary-Tree.py 一样, 事先将 nodes 转成 Set, 
原来判断 root 等于 p 或 q 改为 root 在 Set 中; 
    """
    def lowestCommonAncestor_v2(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        return self._lowest_common_ancestor(root, set([i.val for i in nodes]))
        # return self._lowest_common_ancestor(root, set(nodes))


    def _lowest_common_ancestor(self, root, nodes) -> TreeNode:
        # jy: 如果当前根节点在 nodes 列表中, 则直接返回当前根节点;
        # if not root or root in nodes:
        # if not root or root.val in [i.val for i in nodes]:
        if not root or root.val in nodes:
            return root
        # jy: 分别从根节点的左子树和右子树中找 nodes 中的所有节点的最小公共祖先:
        #    1) 如果 nodes 中的节点均在左子树中, 则求得的 left 为其最小公共祖先, 而 right 则为 None;
        #    2) 如果 nodes 中的节点均在右子树中, 则求得的 right 为其最小公共祖先, 而 left 则为 None;
        #    3) 如果 nodes 中的节点分布在左右子树(均含有), 则 left 和 right 即为 nodes 中部分节点的
        #       最小公共祖先, 此时所有 nodes 节点的最小公共祖先为根节点 root;
        left = self._lowest_common_ancestor(root.left, nodes)
        right = self._lowest_common_ancestor(root.right, nodes)

        if left and right:
            return root
        else:
            return left or right



ls_ = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build_binary_tree(ls_)
nodes = [TreeNode(i) for i in [4, 7]]
# Output: 2
res = Solution().lowestCommonAncestor_v1(root, nodes)
print(res.val)


ls_ = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build_binary_tree(ls_)
nodes = [TreeNode(i) for i in [1]]
# Output: 1
res = Solution().lowestCommonAncestor_v1(root, nodes)
print(res.val)


ls_ = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build_binary_tree(ls_)
nodes = [TreeNode(i) for i in [7, 6, 2, 4]]
# Output: 5
res = Solution().lowestCommonAncestor_v2(root, nodes)
print(res.val)


ls_ = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build_binary_tree(ls_)
nodes = [TreeNode(i) for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]]
# Output: 3
res = Solution().lowestCommonAncestor_v2(root, nodes)
print(res.val)



