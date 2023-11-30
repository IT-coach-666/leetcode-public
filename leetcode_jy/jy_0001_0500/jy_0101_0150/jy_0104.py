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
tag_jy = ""


"""
Given a binary tree, find its maximum depth. The maximum depth is the number
of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.


Example:
Given binary tree [3, 9, 20, null, null, 15, 7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


from collections import deque
from about_TreeNode import *


class Solution:
    """
解法1: 分别递归求解左右子树的高度, 返回两者的最大值加 1 即可
    """
    def maxDepth_v1(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth_v1(root.left)
        right = self.maxDepth_v1(root.right)
        return max(left, right) + 1


    """
解法2: 广度优先搜索; 使用一个队列存储每一层的结点, 每次出队一层的结点, 同时树的深度加 1;
    """
    def maxDepth_v2(self, root: TreeNode) -> int:
        queue = deque([root]) if root else deque()
        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            # jy: 一次 for 循环出队一层的节点, 并将下一层的节点入队;
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

res = Solution().maxDepth_v2(root)
print(res)


