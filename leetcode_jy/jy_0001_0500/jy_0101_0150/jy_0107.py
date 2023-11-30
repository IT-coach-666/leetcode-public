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
title_jy = "Binary-Tree-Level-Order-Traversal-II(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, return the bottom-up level order traversal of its
nodes' values. (i.e., from left to right, level by level from leaf to root).


Example 1:   https://www.yuque.com/frederick/dtwi9g/agadog
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""


from collections import deque
from typing import List
from about_TreeNode import *


class Solution:
    """
解法1: 同 102_Binary-Tree-Level-Order-Traversal.py 的解法 3, 只是最后将结果倒序
    """
    def levelOrderBottom_v1(self, root: TreeNode) -> List[List[int]]:
        queue = deque([root]) if root else deque()
        levels = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return list(reversed(levels))

    """
解法2: 同 102_Binary-Tree-Level-Order-Traversal.py 的解法2, 不同的是往最终结果插入
数组时从数组头插入, 因为层序遍历从下往上
    """
    def levelOrderBottom_v2(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        self._dfs(root, 1, queue)
        return list(queue)

    def _dfs(self, root: TreeNode, level: int, queue: List[List[int]]) -> None:
        if not root:
            return
        # jy: 如果当前的层级序号大于队列中的长度, 则往队列左侧加入空列表, 使队列长度等于
        #     当前层级的序号值, 确保后续能在该层级中插入元素;
        #     注意加入时是左侧加入, 后续存放层级中的元素时也是层级越大越往左, 最右边的层
        #     级是最小的;
        if level > len(queue):
            queue.appendleft([])
        # jy: 往指定的层级中加入元素,
        queue[-level].append(root.val)

        self._dfs(root.left, level + 1, queue)
        self._dfs(root.right, level + 1, queue)

    """
JY: 同解法1, 但使用了双向队列存储最终结果, 减少一次倒序排序;
    """
    def levelOrderBottom_jy(self, root: TreeNode) -> List[List[int]]:
        res = deque()
        # jy: 当 root 为 None 时, 不能加入队列中, 否则后续出队为 None, 没有 val 属性, 会报错;
        deque_ = deque([root]) if root else deque()
        while deque_:
            current_level = []
            len_ = len(deque_)
            for i in range(len_):
                node_ = deque_.popleft()
                current_level.append(node_.val)
                if node_.left:
                    deque_.append(node_.left)
                if node_.right:
                    deque_.append(node_.right)
            res.appendleft(current_level)
        return list(res)


ls_ = [3, 9, 20, None, None, 15, 7]
# Output: [[15,7],[9,20],[3]]
root = build_binary_tree(ls_)
res = Solution().levelOrderBottom_v1(root)
print(res)

ls_ = [1]
# Output: [[1]]
root = build_binary_tree(ls_)
res = Solution().levelOrderBottom_v2(root)
print(res)

ls_ = []
# Output: []
root = build_binary_tree(ls_)
res = Solution().levelOrderBottom_jy(root)
print(res)


