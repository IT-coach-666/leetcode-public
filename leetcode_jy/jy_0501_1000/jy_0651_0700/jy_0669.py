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
title_jy = "Trim-a-Binary-Search-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree
so that all its elements lies in [L, R] (R >= L). You might need to change the root of the
tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

L = 1
R = 2

Output:
     1
      \
       2


Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

L = 1
R = 3

Output:
      3
     /
   2
  /
 1
"""




from about_TreeNode import *

class Solution:
    """
递归求解, 如果当前节点的值大于 R, 则返回递归调用左子树, 如果当前结点的值小于 L, 则返回递归调用右子
树, 否则对左右子树分别调用 trimBST, 作为当前结点的新的左右子树;
    """
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        # jy: 如果当前节点值大于 R, 则返回递归调用左子树的结果;
        if root.val > R:
            return self.trimBST(root.left, L, R)
        # jy: 如果当前节点值小于 L, 则返回递归调用右子树的结果;
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        # jy: 如果当前节点值在 L 和 R 之间(包含 L 和 R), 则当前节点的左子节点为递归调用左子树的结果,
        #    同理右子节点为递归调用右子树的结果;
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)

        return root


ls_ = [1, 0, 2]
L = 1
R = 2
root = build_binary_tree(ls_)
res = Solution().trimBST(root, L, R)
print("pre_order: ", pre_order(res))


ls_ = [3, 0, 4, None, 2, None, None, None, None, 1]
L = 1
R = 3
root = build_binary_tree(ls_)
print("pre_order: root ", pre_order(root))
print("in_order: root ", in_order(root))
print("post_order: root ", post_order(root))
res = Solution().trimBST(root, L, R)
print("pre_order: ", pre_order(res))


