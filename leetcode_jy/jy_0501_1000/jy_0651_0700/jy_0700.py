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
title_jy = "Search-in-a-Binary-Search-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given the root of a binary search tree (BST) and an integer ``val``. Find the node in
the BST that the node's value equals ``val`` and return the subtree rooted with that node. If
such a node does not exist, return null.


Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []


Constraints:
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10^7
root is a binary search tree.
1 <= val <= 10^7
"""


from about_TreeNode import *


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        current = root

        while current:
            if current.val == val:
                return current
            elif current.val > val:
                current = current.left
            else:
                current = current.right

        return None


ls_ = [4, 2, 7, 1, 3]
val = 2
# Output: [2,1,3]
root = build_binary_tree(ls_)
res = Solution().searchBST(root, val)
print("pre_order: ", pre_order(res))


ls_ = [4, 2, 7, 1, 3]
val = 5
# Output: []
root = build_binary_tree(ls_)
res = Solution().searchBST(root, val)
print("pre_order: ", pre_order(res))


