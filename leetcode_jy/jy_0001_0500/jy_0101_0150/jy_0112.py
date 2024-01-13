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
tag_jy = "递归 | 栈/队列 + 循环 | 相似题: 0013"


"""
Given the `root` of a binary tree and an integer `targetSum`, return true if
the tree has a root-to-leaf path such that adding up all the values along 
the path equals `targetSum`. A leaf is a node with no children.


Example 1: 
Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22
             5
            / \
           4   8
          /   / \ 
        11   13  4
       /  \       \
      7    2       1
Output: true
Explanation: 5 -> 4 -> 11 -> 2

Example 2:
Input: root = [1, 2, 3], targetSum = 5
             1
            / \
           2   3
Output: false

Example 3:
Input: root = [1,2], targetSum = 0
Output: false


Constraints:
1) The number of nodes in the tree is in the range [0, 5000].
2) -1000 <= Node.val <= 1000
3) -1000 <= targetSum <= 1000
"""


from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from collections import deque


class Solution:
    """
解法 1: 递归

递归判断左右子树是否有满足条件的路径
    """
    def hasPathSum_v1(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        return self._has_path_sum(root, targetSum)

    def _has_path_sum(self, root, target):
        # jy: 如果当前节点的左右子树均为 None (即已经到了叶子节点), 则返
        #     回当前节点值与 target 是否相等
        if root.left is None and root.right is None:
            return root.val == target
        # jy: 否则, 如果存在左子树, 则递归判断左子树; 如果存在右子树, 则递
        #     归判断右子树 (去除根节点的值后, 子树中待寻找的路径数值即为
        #     target - root.val), 只要其中一个子树满足条件, 即可返回 True
        else:
            path_in_left = root.left and self._has_path_sum(root.left, target - root.val)
            path_in_right = root.right and self._has_path_sum(root.right, target - root.val)
            return path_in_left or path_in_right


    """
解法 2: 栈 + 循环/迭代
    """
    def hasPathSum_v2(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        # jy: 使用一个栈记录当前节点, 以及根节点到当前节点的路径中的
        #     数值总和; 初始化为含一个元组 (根节点, 根节点值) 的列表
        stack = [(root, root.val)]
        while stack:
            # jy: 出栈元组, 判断当前节点是否为叶子节点,  且累计的数值
            #     总和是否等于目标值, 如果均满足要求, 则返回 True
            node, sum_so_far = stack.pop()
            if not node.left and not node.right and sum_so_far == targetSum:
                return True
            # jy: 如果有左子节点, 则左子节点入栈, 并更新到左子节点为
            #     止的路径和
            if node.left:
                stack.append((node.left, sum_so_far + node.left.val))
            # jy: 如果有右子节点, 则右子节点入栈, 并更新到右子节点为
            #     止的路径和
            if node.right:
                stack.append((node.right, sum_so_far + node.right.val))

        return False


    """
解法 3: 队列 + 循环/迭代
    """
    def hasPathSum_v3(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        queue = deque([(root, root.val)])

        while queue:
            # jy: 先进先出和后进先出均可, 顺序不重要
            node, sum_so_far = queue.popleft()
            #node, sum_so_far = queue.pop()
            if not node.left and not node.right and sum_so_far == targetSum:
                return True
            if node.left:
                queue.append((node.left, sum_so_far + node.left.val))
            if node.right:
                queue.append((node.right, sum_so_far + node.right.val))
        return False


ls_ = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
root = build_binary_tree(ls_)
targetSum = 22
res = Solution().hasPathSum_v1(root, targetSum)
# jy: true
print(res)


ls_ = [1, 2, 3]
targetSum = 5
root = build_binary_tree(ls_)
res = Solution().hasPathSum_v2(root, targetSum)
# jy: false
print(res)


ls_ = [1, 2]
root = build_binary_tree(ls_)
targetSum = 0
res = Solution().hasPathSum_v3(root, targetSum)
# jy: false
print(res)

