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
title_jy = "Merge-Two-Binary-Trees(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given two binary trees ``root1`` and ``root2``. Imagine that when you put one of
them to cover the other, some nodes of the two trees are overlapped while the others are
not. You need to merge the two trees into a new binary tree. The merge rule is that if
two nodes overlap, then sum node values up as the new value of the merged node. Otherwise,
the NOT null node will be used as the node of the new tree. Return the merged tree.

Note: The merging process must start from the root nodes of both trees.


Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:
Input: root1 = [1], root2 = [1,2]
Output: [2,2]


Constraints:
The number of nodes in both trees is in the range [0, 2000].
-10^4 <= Node.val <= 10^4
"""


from typing import Optional
from about_TreeNode import *


class Solution:
    """
对左右子树分别递归合并
    """
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)

            return root1


ls_root1 = [1, 3, 2, 5]
ls_root2 = [2, 1, 3, None, 4, None, 7]
# Output: [3,4,5,5,4,null,7]
root1 = build_binary_tree(ls_root1)
root2 = build_binary_tree(ls_root2)
res = Solution().mergeTrees(root1, root2)
serialize(res)


ls_root1 = [1]
ls_root2 = [1, 2]
# Output: [2,2]
root1 = build_binary_tree(ls_root1)
root2 = build_binary_tree(ls_root2)
res = Solution().mergeTrees(root1, root2)
serialize(res)

# 合并两棵树（重叠的节点数值相加）


