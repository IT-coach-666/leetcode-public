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
title_jy = "Closest-Binary-Search-Tree-Value(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary search tree and a target value, return the value in the
BST that is closest to the target.


Example 1:
Input: root = [4, 2, 5, 1, 3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
0 <= Node.val <= 10^9
-10^9 <= target <= 10^9
"""


import sys
from about_TreeNode import *


class Solution:
    """
遍历二叉搜索树, 判断当前节点是否更接近 target, 然后比较当前节点的值和 target, 如果当前节点的
值比 target 大, 则走左子树(根据二叉搜索树的性质, 右子树的值必然比当前节点值大, 故右子树的值
与 target 的差值必然比当前节点与 target 的差值大), 否则走右子树;
    """
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = sys.maxsize

        if not root:
            return closest

        node = root

        while node:
            # jy: 如果 if 判断成立, 表明当前节点的值(node.val) 与 target 更接近;
            if abs(closest - target) > abs(node.val - target):
                closest = node.val
            # jy: 如果当前节点的值大于 target, 则走左子树;
            node = node.left if target < node.val else node.right

        return closest

ls_ = [4, 2, 5, 1, 3]
root = build_binary_tree(ls_)
target = 3.714286
# Output: 4
res = Solution().closestValue(root, target)
print(res)

ls_ = [1]
root = build_binary_tree(ls_)
target = 4.428571
# Output: 1
res = Solution().closestValue(root, target)
print(res)


