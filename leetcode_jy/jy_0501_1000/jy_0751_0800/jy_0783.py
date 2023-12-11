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
title_jy = "Minimum-Distance-Between-BST-Nodes(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


# 找出二叉搜索树中节点值之差的最小值
"""
Given the root of a Binary Search Tree (BST), return the minimum difference
between the values of any two different nodes in the tree.


Example 1:    https://www.yuque.com/frederick/dtwi9g/sv7w1g
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,None,None,12,49]
Output: 1


Constraints:
The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 10^5
Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""


import sys
from typing import Optional
from about_TreeNode import *


class Solution:
    """
解法1: 对每一个节点, 找到左子树中的最大值和右子树中的最小值, 和当前节点的比较差值
    """
    def minDiffInBST_v1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_diff = sys.maxsize
        stack = [root]

        while stack:
            node = stack.pop()

            if node.left:
                min_diff = min(min_diff, node.val - self._find_max(node.left))
                stack.append(node.left)

            if node.right:
                min_diff = min(min_diff, self._find_min(node.right) - node.val)
                stack.append(node.right)

        return min_diff

    def _find_max(self, root):
        max_value = root.val
        while root:
            max_value = max(max_value, root.val)
            root = root.right
        return max_value

    def _find_min(self, root):
        min_value = root.val
        while root:
            min_value = min(min_value, root.val)
            root = root.left
        return min_value


    """
解法2: 首先中序遍历求得二叉搜索树的有序排列, 然后遍历有序判断求相邻两个数字的最小差值
    """
    def minDiffInBST_v2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_diff = sys.maxsize
        # jy: 中序遍历二叉搜索树, 将遍历结果保存至 values 列表;
        values = []
        self._inorder(root, values)

        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i-1])

        return min_diff

    def _inorder(self, root, values):
        if not root:
            return
        self._inorder(root.left, values)
        values.append(root.val)
        self._inorder(root.right, values)


    """
解法3: 中序遍历二叉树(非递归方式), 并在遍历过程中不断更新最小差值;
    """
    def minDiffInBST_v3(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0



ls_ = [4,2,6,1,3]
root =
# Output: 1
res = Solution().minDiffInBST_v1(root)


ls_ = [1,0,48,None,None,12,49]
root =
# Output: 1
res = Solution().minDiffInBST_v2(root)


