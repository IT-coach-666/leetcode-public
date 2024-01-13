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
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Path-Sum-II(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 栈/队列 + 循环 | 相似题: 0012"


"""
Given the `root` of a binary tree and an integer `targetSum`, return all
root-to-leaf paths where each path's sum equals `targetSum`. A leaf is a
node with no children.


Example 1:
Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], targetSum = 22
             5
            / \
           4   8
          /   / \
        11   13  4
       /  \     / \
      7    2   5   1
Output: [[5, 4, 11, 2], [5, 8, 4, 5]]

Example 2:
Input: root = [1, 2, 3], targetSum = 5
             1
            / \
           2   3
Output: []

Example 3:
Input: root = [1, 2], targetSum = 0
Output: []


Constraints:
1) The number of nodes in the tree is in the range [0, 5000].
2) -1000 <= Node.val <= 1000
3) -1000 <= targetSum <= 1000
"""


from collections import deque
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree


class Solution:
    """
解法 1: 递归 

在 0112 的解法 1 的基础上改写
    """
    def pathSum_v1(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # jy: 用于存放所有路径组合
        ls_path = []
        self._path_sum(root, targetSum, [], ls_path)
        return ls_path

    def _path_sum(self, root, target, path_so_far, ls_path):
        """
        从以 root 为根节点的树中找一条值为 target 的路径, 将路径节点存放
        至 path_so_far 列表中, 并将满足要求的路径添加到 ls_path 结果列表

        target: targetSum 与 path_so_far 中的元素值总和相差的数值 (target
                初始值为 targetSum, 对应的 path_so_far 为空列表 [])
        ls_path: 用于递归过程中存放目录路径结果的列表
        """
        # jy: 如果当前节点值为 None, 则返回, 终止递归; 注意: 由于树的节点
        #     值和目标值均有可能为负数, 因此不能基于 target 提前终止递归
        if not root:
            return

        # jy: 如果当前节点为叶子节点 (左右子树均不存在), 则判断当前节点值
        #     与 target 是否相等, 相等则表明找到一条符合要求的路径, 将当前
        #     节点值加入 path_so_far, 此时的 path_so_far 即为目标路径, 将
        #     其加入到 ls_path 中
        elif root.left is None and root.right is None:
            if root.val == target:
                ls_path.append(path_so_far + [root.val])
        # jy: 如果存在左/右子树, 则继续递归遍历查找至叶子节点, 并同时更
        #     新离目标值的差值 (路径更新为从子节点开始后, 差值即更新为
        #     target - root.val) 
        else:
            if root.left:
                self._path_sum(root.left, target - root.val,
                               path_so_far + [root.val], ls_path)
            if root.right:
                self._path_sum(root.right, target - root.val,
                               path_so_far + [root.val], ls_path)

    """
解法 2: 栈 + 循环/迭代

在 0112 的解法 2 的基础上改写
    """
    def pathSum_v2(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # jy: 存放目标路径结果
        ls_path = []
        if not root:
            return []
        # jy: 栈中的元素为元组: (当前节点, 根节点到当前节点的路径之和, 根
        #     节点到当前节点的路径列表)
        stack = [(root, root.val, [root.val])]
        # jy: 如果栈不为空, 则不断出栈元素, 如果该节点为叶子节点, 则判断到
        #     该节点为止的路径和是否等于目标值, 如果是则加入结果列表; 如果
        #     非叶子节点, 则继续将子节点入栈
        while stack:
            node, sum_so_far, path_so_far = stack.pop()

            if not node.left and not node.right:
                if sum_so_far == targetSum:
                    ls_path.append(path_so_far)

            if node.left:
                stack.append((node.left, sum_so_far + node.left.val, path_so_far + [node.left.val]))
            if node.right:
                stack.append((node.right, sum_so_far + node.right.val, path_so_far + [node.right.val]))
        return ls_path


    """
解法 3: 队列 + 循环/迭代

在 0112 的解法 3 的基础上改写
    """
    def pathSum_v3(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ls_path = []
        if not root:
            return []

        queue = deque([(root, root.val, [root.val])])
        while queue:
            node, sum_so_far, path_so_far = queue.popleft()
            if not node.left and not node.right and sum_so_far == targetSum:
                ls_path.append(path_so_far)

            if node.left:
                queue.append((node.left, sum_so_far + node.left.val, path_so_far + [node.left.val]))
            if node.right:
                queue.append((node.right, sum_so_far + node.right.val, path_so_far + [node.right.val]))

        return ls_path


ls_ = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
root = build_binary_tree(ls_)
targetSum = 22
res = Solution().pathSum_v1(root, targetSum)
# jy: [[5, 4, 11, 2], [5, 8, 4, 5]]
print(res)


ls_ = [1, 2, 3]
targetSum = 5
root = build_binary_tree(ls_)
res = Solution().pathSum_v2(root, targetSum)
# jy: []
print(res)


ls_ = [1, 2]
root = build_binary_tree(ls_)
targetSum = 0
res = Solution().pathSum_v3(root, targetSum)
# jy: []
print(res)


