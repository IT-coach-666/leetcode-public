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
title_jy = "Lowest-Common-Ancestor-of-a-Binary-Tree-III(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two 
nodes p and q in a tree T is the lowest node that has both p and q as descendants 
(where we allow a node to be a descendant of itself)."


Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q exist in the tree.
"""

from about_TreeNode import TreeNode as Node
from about_TreeNode import build_binary_tree


class Solution:
    """
解法1: p 和 q 分别顺着父节点往上找, 并使用一个 Set 保存途中遇到的节点, 如果当前节点已经
在 Set 中, 说明该节点就是最近公共祖先(需要特殊处理的是当 p 和 q 最开始在同一层级上时, 两
者向上前进的速度一致, Set 中始终不会存在当前节点, 而 p 和 q 最终满足 p.parent == q.parent,
此时 p.parent 就是最近公共祖先;
    """
    def lowestCommonAncestor_v1(self, p: 'Node', q: 'Node') -> 'Node':
        parents = set()

        while p or q:
            # jy: 当 p 和 q 在同一层级, 当 p 和 q 不断向上遍历 parent 时, 如果有公共祖先, 则
            #    会相聚, 此时的 p 和 q 相等, 当 p 和 q 相等时, 两者均未被加入到 parents 中,
            #    不能通过判断 parents 中是否存在来判断其是否是公共祖先, 故要在此处补充如下:
            # if p and q and p.parent is q.parent:
            #     return p.parent
            if p and p is q:
            # if p and q and p is q:
                return p

            if p and p in parents:
                return p

            if q and q in parents:
                return q

            if p:
                parents.add(p)
                p = p.parent

            if q:
                parents.add(q)
                q = q.parent


    """
解法2: 这道题本质上和 160_Intersection-of-Two-Linked-Lists.py 一样, 两个节点
分别从 p 和 q 向上走, 当其中一个节点走到头时, 从另一个节点的起始处继续开始; 
    """
    def lowestCommonAncestor_v2(self, p: 'Node', q: 'Node') -> 'Node':
        # jy: 用 a 和 b 记录待更新的 2 个节点, p 和 q 保持不变;
        a, b = p, q

        while a is not b:
            # jy: 两个节点分别各自往上走, 当其中一个节点走到头时, 从另一个节点的起始
            #    处继续开始, 最终两节点会相遇, 相遇的节点即为最小公共祖先;
            a = q if a.parent is None else a.parent
            b = p if b.parent is None else b.parent

        return a


ls_ = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build_binary_tree(ls_)
p = root.left    # 5
q = root.right   # 1
# Output: 3
res = Solution().lowestCommonAncestor_v1(p, q)
print(res.val)


ls_ = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build_binary_tree(ls_)
p = root.left              # 5
q = root.left.right.right  # 4
# Output: 5
res = Solution().lowestCommonAncestor_v2(p, q)
print(res.val)


ls_ = [1, 2]
root = build_binary_tree(ls_)
p = root       # 1
q = root.left  # 2
# Output: 1
res = Solution().lowestCommonAncestor_v1(p, q)
print(res.val)



