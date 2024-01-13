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
title_jy = "Binary-Tree-Level-Order-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 循环/迭代"


"""
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).


Example 1:
Given binary tree [3, 9, 20, null, null, 15, 7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[ [3],
  [9,20],
  [15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
 

Constraints:
1) The number of nodes in the tree is in the range [0, 2000].
2) -1000 <= Node.val <= 1000
"""


from collections import deque
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import levelorderTraversal, levelorderTraversal_v2


class Solution:
    """
解法 1: 循环 + 队列 (先进先出)
    """
    def levelOrder_v1(self, root: TreeNode) -> List[List[int]]:
        ls_level = levelorderTraversal(root)
        return ls_level


    """
解法 2: 递归
    """
    def levelOrder_v2(self, root: TreeNode) -> List[List[int]]:
        ls_level = levelorderTraversal_v2(root)
        return ls_level



ls_ = [3, 9, 20, None, None, 15, 7]
root = build_binary_tree(ls_)

res = Solution().levelOrder_v1(root)
print(res)

res = Solution().levelOrder_v2(root)
print(res)




