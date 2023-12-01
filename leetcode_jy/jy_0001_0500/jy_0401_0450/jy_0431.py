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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Encode-N-ary-Tree-to-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree
to get the original N-ary tree.

An N-ary tree is a rooted tree in which each node has no more than N children. Similarly,
a binary tree is a rooted tree in which each node has no more than 2 children.

There is no restriction on how your encode/decode algorithm should work. You just need to
ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded
to the original N-nary tree structure.

Nary-Tree input serialization is represented in their level order traversal, each group of
children is separated by the null value (See following example).

For example, you may encode the following 3-ary tree to a binary tree in this way:
Input: root = [1,null,3,2,4,null,5,6]

https://www.yuque.com/frederick/dtwi9g/kbzcw4

Note that the above is just an example which might or might not work. You do not necessarily
need to follow this format, so please be creative and come up with different approaches yourself.



Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
Do not use class member/global/static variables to store states.
Your encode and decode algorithms should be stateless.
"""


from about_TreeNode import *



class Codec:
    """
编码: 将 N 叉树的第一个孩子节点作为左子树的根节点, 将后续其他孩子节点(第一个孩子节点的兄弟节点)
递归作为左子树根节点的右节点
    """
    def encode(self, root: 'Node') -> TreeNode:
        """
        Encodes an n-ary tree to a binary tree.
        """
        if not root:
            return None
        # jy: 使用 N 叉树的根节点值构造一个二叉树节点
        binary_tree = TreeNode(root.val)
        # jy: 如果 N 叉树没有子节点, 直接返回构造的二叉树节点;
        if not root.children:
            return binary_tree
        # jy: 将 N 叉树的第一个孩子节点递归作为左子树的根节点
        binary_tree.left = self.encode(root.children[0])
        # jy: 定位到左子树的根节点, 并将其它孩子节点递归作为左子树根节点的右子节点
        node = binary_tree.left
        for child in root.children[1:]:
            node.right = self.encode(child)
            node = node.right

        return binary_tree

    """
解码: 将二叉树的左子树的根节点作为当前 N 叉树根节点的孩子节点的第一个节点, 并将
左子树的根节点的右子节点作为当前 N 叉树根节点的其它孩子节点;
    """
    def decode(self, data: TreeNode) -> 'Node':
        """Decodes your binary tree to an n-ary tree."""
        if not data:
            return None
        # jy: 依据二叉树的根节点值, 构造 N 叉树的根节点
        n_ary_tree = Node(data.val, [])
        # jy: 将二叉树的左子树的根节点作为当前 N 叉树根节点的孩子节点的第一个节点, 并将左子树根节点的
        #    右子节点作为后续的兄弟节点
        node = data.left
        while node:
            n_ary_tree.children.append(self.decode(node))
            node = node.right

        return n_ary_tree


ls_N_ary = [1, [3, [5, 6], 2, 4]]
root_N = build_N_ary_tree(ls_N_ary)
print(show_N_ary_tree(root_N))

root_2 = Codec().encode(root_N)
"""
    1
   /
  3
 / \
5   2
 \   \
  6   4
即以上二叉树节点中, 凡是右子节点以及其父节点均是 N 叉树中的同一层的节点
"""
print("in_order: ", in_order(root_2))
print("pre_order: ", pre_order(root_2))
print("post_order: ", post_order(root_2))

dec_root_N = Codec().decode(root_2)
print(show_N_ary_tree(dec_root_N))


