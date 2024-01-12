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
tag_jy = "循环/迭代 + 层次遍历"


"""
Given a binary tree, find its minimum depth. The minimum depth is the number
of nodes along the shortest path from the root node down to the nearest leaf
node.

Note: A leaf is a node with no children.


Example:
Given binary tree [3, 9, 20, null, null, 15, 7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.


Example 2:
Input: root = [2, null, 3, null, 4, null, 5, null, 6]
Output: 5
 

Constraints:
1) The number of nodes in the tree is in the range [0, 10^5].
2) -1000 <= Node.val <= 1000
"""


from collections import deque
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree


class Solution:
    """
解法 1: 循环/迭代 (广度优先搜索)

基于层次遍历, 如果层次遍历过程中出现某一节点的左右子节点均空, 则
当前层数即为最小深度
    """
    def minDepth_v1(self, root: TreeNode) -> int:
        queue = deque([root]) if root else deque()
        # jy: 统计当前的层数
        depth = 0
        while queue:
            # jy: 每次 for 循环都会遍历一层, 遍历时 depth 加 1, 表示当前层数
            depth += 1
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                # jy: 如果碰到当前节点没有左右子节点, 即返当前的层数值, 为
                #     最小层数
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


    """
解法 2: 递归

以以下树为例进行思考:
    3
   / \
  9  20
       \
        7
    """
    def minDepth_v2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l_depth = self.minDepth_v2(root.left)
        r_depth = self.minDepth_v2(root.right)

        # jy: 如果根节点没有左子节点, 则根节点对应的树的深度为以右子
        #     节点为根节点的树的深度加 1
        if not root.left:
            return r_depth + 1
        # jy: 如果根节点没有右子节点, 则根节点对应的树的深度为以左子
        #     节点为根节点的树的深度加 1
        if not root.right:
            return l_depth + 1
        # jy: 如果根节点左右子节点均存在, 则最小深度为左子树的深度与
        #     右子树的深度的较小值加 1
        else:
            return min(l_depth, r_depth) + 1



ls_ = [3, 9, 20, None, None, 15, 7]
root = build_binary_tree(ls_)
res = Solution().minDepth_v1(root)
# jy: 2
print(res)


ls_ = [2, None, 3, None, 4, None, 5, None, 6]
root = build_binary_tree(ls_)
res = Solution().minDepth_v1(root)
# jy: 5
print(res)

