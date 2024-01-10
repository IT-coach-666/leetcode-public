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
tag_jy = "递归 | 循环/迭代 | 相似题: 0102 | IMP"


"""
Given the `root` of a binary tree, return the bottom-up level order traversal
of its nodes' values. (i.e., from left to right, level by level from leaf to
root).


Example 1:
    3
   / \
  9  20
    /  \
   15   7
Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[15, 7], [9, 20], [3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []


Constraints:
1) The number of nodes in the tree is in the range [0, 2000].
2) -1000 <= Node.val <= 1000
"""


from collections import deque
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import levelorderTraversal


class Solution:
    """
解法 1: 循环/迭代

同 0102 (Binary-Tree-Level-Order-Traversal) 的解法 1, 但最后将结果倒序
    """
    def levelOrderBottom_v1(self, root: TreeNode) -> List[List[int]]:
        ls_level = levelorderTraversal(root)
        return ls_level[::-1]


    """
解法 2: 参考 0102 (Binary-Tree-Level-Order-Traversal) 的解法 2, 但最终
结果插入数组时从数组头插入 (左侧插入), 使得第一层遍历存放在结果列表末尾
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
        # jy: 往指定的层级中加入元素
        queue[-level].append(root.val)

        self._dfs(root.left, level + 1, queue)
        self._dfs(root.right, level + 1, queue)


    """
解法 3: 参考解法 1 和解法 2

使用双向队列存储每一层的遍历结果, 每一层遍历结果从左侧插入
    """
    def levelOrderBottom_v3(self, root: TreeNode) -> List[List[int]]:
        res = deque()
        # jy: 当 root 为 None 时, 不能加入队列中, 否则后续出队为 None,
        #     没有 val 属性, 会报错
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
root = build_binary_tree(ls_)
res = Solution().levelOrderBottom_v1(root)
# jy: [[15, 7], [9, 20], [3]]
print(res)


ls_ = [1]
root = build_binary_tree(ls_)
res = Solution().levelOrderBottom_v2(root)
# jy: [[1]]
print(res)


ls_ = []
root = build_binary_tree(ls_)
res = Solution().levelOrderBottom_v3(root)
# jy: []
print(res)


