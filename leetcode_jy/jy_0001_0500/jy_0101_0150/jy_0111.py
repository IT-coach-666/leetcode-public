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
title_jy = "Minimum-Depth-of-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.


Example:
Given binary tree [3, 9, 20, null, null, 15, 7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


from collections import deque
from about_TreeNode import *


class Solution:
    """
广度优先搜索; 使用一个队列存储每一层的结点, 出队时判断该结点是
否是叶子结点, 如果是则该结点所在层为树的最小深度;
    """
    def minDepth(self, root: TreeNode) -> int:
        # jy: 根节点作为第一层入队;
        queue = deque([root]) if root else deque()
        depth = 0
        while queue:
            # jy: 每次 for 循环都会遍历一层, 遍历时 depth 加 1, 表示当前层数;
            depth += 1
            size = len(queue)
            # jy: 每次 for 循环遍历出一层, 并将当前层的下一层节点入队; for 循环的
            #    过程中 size 值不变, 一轮 for 循环后, queue 中的元素个数即下一层
            #    元素的个数;
            for _ in range(size):
                node = queue.popleft()
                # jy: 如果碰到当前节点没有左右子节点, 即返当前的层数值, 为最小层数;
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


ls_ = [3, 9, 20, None, None, 15, 7]
root = build_binary_tree(ls_)
res = Solution().minDepth(root)
print(res)


