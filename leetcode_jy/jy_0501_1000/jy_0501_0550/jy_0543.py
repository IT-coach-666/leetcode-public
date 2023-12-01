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
title_jy = "Diameter-of-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root. The length of a
path between two nodes is represented by the number of edges between them.


Example 1:    https://www.yuque.com/frederick/dtwi9g/uhgk7w
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100
"""


from about_TreeNode import *


class Solution:
    """
解法1: 递归求解; 最长路径存在两种情况:
1) 经过根节点: 从左子树到右子树, 则最长路径等于左子树的高度加上右子树的高度
2) 不经过根节点:
   在左子树中
   在右子树中
    """
    def diameterOfBinaryTree_v1(self, root: TreeNode) -> int:
        if not root:
            return 0
        # jy: 求经过根节点时的最长路径(左子树高度 + 右子树高度), 以及不经过根节点
        #     路径(经过左子树根节点, 或经过右子树根节点)的最长路径, 三者取最大值;
        diameter = self._get_depth(root.left) + self._get_depth(root.right)
        left_diameter = self.diameterOfBinaryTree_v1(root.left)
        right_diameter = self.diameterOfBinaryTree_v1(root.right)
        return max(diameter, left_diameter, right_diameter)

    def _get_depth(self, root):
        """
        求以 root 为根节点的树的最大高度
        """
        if not root:
            return 0
        return 1 + max(self._get_depth(root.left), self._get_depth(root.right))

    """
解法2: 解法 1 存在大量的重复计算，可以将两个递归进行合并

JY: 相比于解法 1, 时间复杂度大大提高;
    """
    def diameterOfBinaryTree_v2(self, root: TreeNode) -> int:
        # jy: 由于递归过程必须返回两个结果, 因此需要额外定义一个方法来实现;
        return self._dfs(root)[0]

    def _dfs(self, root):
        """
        返回以 root 为根节点的树的最大深度和最长直径(diameter)
        """
        if not root:
            return 0, 0
        # jy: 求左子树的最大深度(高度)以及最长直径
        left_diameter, left_depth = self._dfs(root.left)
        # jy: 求右子树的最大深度(高度)以及最长直径
        right_diameter, right_depth = self._dfs(root.right)
        # jy: 当前树(以当前 root 为根节点的树)的最长直径为左子树的最长直径, 或右子树的最长
        #     直径, 或经过当前根节点的最长直径三者中的最大值;
        diameter = max(left_diameter, right_diameter, left_depth + right_depth)
        # jy: 计算以 root 为根节点的树的最大深度(高度), 递归过程需要使用到;
        depth = 1 + max(left_depth, right_depth)

        return diameter, depth


ls_root = [1, 2, 3, 4, 5]
# Output: 3
root = build_binary_tree(ls_root)
res = Solution().diameterOfBinaryTree_v1(root)
print(res)


ls_root = [1, 2]
# Output: 1
root = build_binary_tree(ls_root)
res = Solution().diameterOfBinaryTree_v1(root)
print(res)


