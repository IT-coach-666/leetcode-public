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
tag_jy = ""


"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf
paths where each path's sum equals targetSum. A leaf is a node with no children.


Example 1:   https://www.yuque.com/frederick/dtwi9g/tmpe60
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


from collections import deque
from typing import List
from about_TreeNode import *


class Solution:
    """
在 112_Path-Sum.py 的基础上稍作修改, 不同的是要找到所有可能的路径, 所以左右子树都要遍历
    """
    def pathSum_v1(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # jy: 用于存放所有路径组合;
        paths = []
        self._path_sum(root, targetSum, [], paths)
        return paths

    def _path_sum(self, root, target, path_so_far, paths):
        """
        target 为 targetSum 与 path_so_far 中的元素值总和相差的数值(target 初始值为 targetSum, 对
        应的 path_so_far 为空列表 []); paths 是一个用于递归过程中存放目录路径结果的列表;
        """
        # jy: 如果当前节点值为 None, 则返回终止(递归终止条件);
        if not root:
            return
        # jy: 如果当前节点为叶子节点(左右子树均不存在), 则判断当前节点值与 target 是否相等, 相等则
        #     将当前节点值加入 path_so_far, 此时的 path_so_far 即为目标路径, 将其加入到 paths 中;
        elif root.left is None and root.right is None:
            if root.val == target:
                paths.append(path_so_far + [root.val])
        # jy: 如果左右子树至少存在一个, 则继续将当前节点值加入 path_so_far, 并递归在左右子树中继续
        #     寻找值为 target - root.val 的路径(前提是在对应的子树存在的情况下);
        else:
            if root.left:
                self._path_sum(root.left, target - root.val, path_so_far + [root.val], paths)
            if root.right:
                self._path_sum(root.right, target - root.val, path_so_far + [root.val], paths)

    """
使用栈的深度优先搜素
    """
    def pathSum_v2(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # jy: paths 用于存放目标路径结果;
        paths = []
        if not root:
            return []
        # jy: 栈中的元素为元组: (当前节点, 根节点到当前节点的路径之和, 根节点到当前节点的路径列表)
        stack = [(root, root.val, [root.val])]
        # jy: 如果栈不为空, 则不断出栈, 随后出栈元素, 并判断该元素是否是叶子节点, 如果是则判断到该
        #     节点为止的路径和是否等于目标值, 如果是则加入结果列表; 如果非叶子节点, 则继续将子节点
        #     入栈;
        while stack:
            node, sum_so_far, path_so_far = stack.pop()

            if not node.left and not node.right and sum_so_far == targetSum:
                paths.append(path_so_far)
                # jy: 补充以下 continue 语句提升效率
                continue

            if node.left:
                stack.append((node.left, sum_so_far + node.left.val, path_so_far + [node.left.val]))
            if node.right:
                stack.append((node.right, sum_so_far + node.right.val, path_so_far + [node.right.val]))
        return paths

    """
解法3: 使用队列的广度优先搜索(同理解法 2 中的栈, 只是队列是先进先出, 顺序不影响)
    """
    def pathSum_v3(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []
        if not root:
            return []

        queue = deque([(root, root.val, [root.val])])
        while queue:
            node, sum_so_far, path_so_far = queue.popleft()
            if not node.left and not node.right and sum_so_far == targetSum:
                paths.append(path_so_far)

            if node.left:
                queue.append((node.left, sum_so_far + node.left.val, path_so_far + [node.left.val]))
            if node.right:
                queue.append((node.right, sum_so_far + node.right.val, path_so_far + [node.right.val]))

        return paths


ls_ = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
root = build_binary_tree(ls_)
targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
res = Solution().pathSum_v1(root, targetSum)
print(res)


ls_ = [1, 2, 3]
targetSum = 5
root = build_binary_tree(ls_)
# Output: []
res = Solution().pathSum_v1(root, targetSum)
print(res)


ls_ = [1, 2]
root = build_binary_tree(ls_)
targetSum = 0
# Output: []
res = Solution().pathSum_v1(root, targetSum)
print(res)


