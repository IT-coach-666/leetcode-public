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
title_jy = "Two-Sum-IV_Input-is-a-BST(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the
BST such that their sum is equal to the given  target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
Output: True


Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7
Target = 28
Output: False
"""


from typing import Set
from about_TreeNode import *



class Solution:
    """
和 001_Two-Sum.py 如出一辙: 遍历二叉搜索树, 对于树中的每一个元素 n, 判断 k-n 是否也在树中; 由于不需
要知道配对元素的位置, 所以可以使用 Set 而不是 Map 来记录已经遍历过的元素;
    """
    def findTarget(self, root: TreeNode, k: int) -> bool:
        return self._find(root, k, set())


    def _find(self, root: TreeNode, k: int, visited: Set[int]) -> bool:
        # jy: 如果 root 为空, 直接返回 False
        if not root:
            return False
        # jy: 如果目标值减去当前节点值的结果在已有集合中存在, 直接返回 True
        if k - root.val in visited:
            return True

        # jy: 如果目标值减去当前节点值的结果不在已有集合中, 则将当前节点值加入集合, 并递归
        #    遍历剩余树节点, 看是否存在满足要求的节点;
        visited.add(root.val)

        return self._find(root.left, k, visited) or self._find(root.right, k, visited)

ls_ = [5, 3, 6, 2, 4, None, 7]
root = build_binary_tree(ls_)
res = Solution().findTarget(root, 9)
print(res)


res = Solution().findTarget(root, 28)


