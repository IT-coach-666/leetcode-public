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
title_jy = "Path-Sum(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree and an integer ``targetSum``, return true if the
tree has a root-to-leaf path such that adding up all the values along the path
equals targetSum. A leaf is a node with no children.


Example 1:   https://www.yuque.com/frederick/dtwi9g/zy0vte
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:
Input: root = [1,2], targetSum = 0
Output: false


Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


from about_TreeNode import *
from collections import deque


class Solution:
    """
解法1: 递归判断左右子树是否有满足条件的路径
    """
    def hasPathSum_v1(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        return self._has_path_sum(root, targetSum)

    def _has_path_sum(self, root, target):
        # jy: 如果当前节点的左右子树均为 None(即表明已经到了叶子节点), 则返回当前节
        #     点值与 target 是否相等;
        if root.left is None and root.right is None:
            return root.val == target
        # jy: 否则, 表明当前节点的左右子树至少有一个存在, 递归判断左右子树中是否存
        #     在值为 target - root.val 的根节点到叶子节点的全路径;
        else:
            path_in_left = root.left and self._has_path_sum(root.left, target - root.val)
            path_in_right = root.right and self._has_path_sum(root.right, target - root.val)
            return path_in_left or path_in_right

    """
解法2: 使用栈的深度优先搜素
    """
    def hasPathSum_v2(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        # jy: 使用一个栈记录当前节点, 以及根节点到当前节点的路径中的数值总和; 初始化为
        #     含一个元组 (根节点, 根节点值) 的列表;
        stack = [(root, root.val)]
        while stack:
            # jy: 出栈元组, 判断根节点到当前节点的路径之和是否等于目标值, 且当前节点是否为
            #     叶子节点(左右子树均不存在), 如果均是, 则返回 True;
            node, sum_so_far = stack.pop()
            if not node.left and not node.right and sum_so_far == targetSum:
                return True
            # jy: 如果有左子节点, 则左子节点入栈, 并更新到左子节点为止的路径和;
            if node.left:
                stack.append((node.left, sum_so_far + node.left.val))
            # jy: 如果有右子节点, 则右子节点入栈, 并更新到右子节点为止的路径和;
            if node.right:
                stack.append((node.right, sum_so_far + node.right.val))

    """
解法3: 使用队列的广度优先搜索; 原理同深度优先搜索(先进先出和后进先出均可, 顺序不重要);
    """
    def hasPathSum_v3(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        queue = deque([(root, root.val)])

        while queue:
            node, sum_so_far = queue.popleft()
            if not node.left and not node.right and sum_so_far == targetSum:
                return True
            if node.left:
                queue.append((node.left, sum_so_far + node.left.val))
            if node.right:
                queue.append((node.right, sum_so_far + node.right.val))


ls_ = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
root = build_binary_tree(ls_)
targetSum = 22
# Output: true
res = Solution().hasPathSum_v1(root, targetSum)
print(res)


ls_ = [1, 2, 3]
targetSum = 5
root = build_binary_tree(ls_)
# Output: false
res = Solution().hasPathSum_v1(root, targetSum)
print(res)


ls_ = [1, 2]
root = build_binary_tree(ls_)
targetSum = 0
# Output: false
res = Solution().hasPathSum_v1(root, targetSum)
print(res)


