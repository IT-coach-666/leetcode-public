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
title_jy = "Maximum-Depth-of-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 循环/迭代"


"""
Given the `root` of a binary tree, return its maximum depth. A binary tree's
maximum depth is the number of nodes along the longest path from the root 
node down to the farthest leaf node.


Example 1:
Given binary tree [3, 9, 20, null, null, 15, 7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


Example 2:
Input: root = [1, null, 2]
Output: 2
 

Constraints:
1) The number of nodes in the tree is in the range [0, 10^4].
2) -100 <= Node.val <= 100
"""


from collections import deque
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree


class Solution:
    """
解法 1: 递归

递归求解左右子树的高度, 返回两者的最大值加 1
    """
    def maxDepth_v1(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth_v1(root.left)
        right = self.maxDepth_v1(root.right)
        return max(left, right) + 1


    """
解法 2: 基于树的层级遍历

树的总层数即为树的最大高度
    """
    def maxDepth_v2(self, root: TreeNode) -> int:
        queue = deque([root]) if root else deque()
        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


ls_ = [3, 9, 20, None, None, 15, 7]
root = build_binary_tree(ls_)
res = Solution().maxDepth_v1(root)
print(res)


ls_ = [1, None, 2]
root = build_binary_tree(ls_)
res = Solution().maxDepth_v2(root)
print(res)

