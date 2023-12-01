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
title_jy = "Binary-Tree-Longest-Consecutive-Sequence(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, return the length of the longest consecutive
sequence path. The path refers to any sequence of nodes from some starting node
to any node in the tree along the parent-child connections. The longest consecutive
path needs to be from parent to child (cannot be the reverse).


Example 1:
Input: root = [1,null,3,2,4,null,null,null,5]
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

Example 2:
Input: root = [2,null,3,2,null,1]
Output: 2
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.


Constraints:
The number of nodes in the tree is in the range [1, 3 * 10^4].
-3 * 10^4 <= Node.val <= 3 * 10^4
"""


from about_TreeNode import *


class Solution:
    """
解法1: 递归求解, 分别计算左右子树的最长连续子序列, 将前一个节点的值和之前的连续
子序列长度分别传入到左右子树的递归调用中
    """
    def longestConsecutive_v1(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self._dfs(root, root.val, 0)

    def _dfs(self, root, prev_value, length_so_far):
        if not root:
            return length_so_far

        length_so_far = length_so_far + 1 if prev_value + 1 == root.val else 1

        left_length = self._dfs(root.left, root.val, length_so_far)
        right_length = self._dfs(root.right, root.val, length_so_far)

        return max(max(left_length, right_length), length_so_far)

    """
解法2: 基于栈的深度优先遍历
    """
    def longestConsecutive_v2(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_length = 0
        stack = [(root, 1)]

        while stack:
            node, length_so_far = stack.pop()
            max_length = max(max_length, length_so_far)

            for child in [node.left, node.right]:
                if not child:
                    continue
                length = length_so_far + 1 if child.val == node.val + 1 else 1
                stack.append((child, length))
        return max_length

    """
解法3: 广度优先搜索版本
    """
    def longestConsecutive_v3(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_length = 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, length_so_far = queue.popleft()
            max_length = max(max_length, length_so_far)
            for child in [node.left, node.right]:
                if not child:
                    continue
                length = length_so_far + 1 if child.val == node.val + 1 else 1
                queue.append((child, length))

        return max_length

    """
JY: 2021-01-01, 递归求解; 自测通过(待 LeetCode 测试);
    """
    def longestConsecutive_jy(self, root):
        if not root:
            return 0
        if not root.right and not root.left:
            return 1
        if root.right and root.right.val == root.val + 1:
            right_num = self.longestConsecutive_jy(root.right) + 1
        else:
            right_num = self.longestConsecutive_jy(root.right)

        if root.left and root.left.val == root.val + 1:
            left_num = self.longestConsecutive_jy(root.left) + 1
        else:
            left_num = self.longestConsecutive_jy(root.left)
        return max(right_num, left_num)

    """
JY: 基于栈实现的版本(队列同理, 入队或入队的顺序不重要); 自测通过(待 LeetCode 测试)
    """
    def longestConsecutive_jy2(self, root):
        stack = [(root, 1)]
        max_num = 1
        while stack:
            node, num = stack.pop()
            if node.left:
                if node.left.val == node.val + 1:
                    max_num = max(max_num, num + 1)
                    stack.append((node.left, num + 1))
                else:
                    stack.append((node.left, num))
            if node.right:
                if node.right.val == node.val + 1:
                    max_num = max(max_num, num + 1)
                    stack.append((node.right, num + 1))
                else:
                    stack.append((node.right, num))
        return max_num


ls_root = [1, None, 3, None, None, 2, 4, None, None, None, None, None, None, None, 5]
# Output: 3
root = build_binary_tree(ls_root)
res = Solution().longestConsecutive_v1(root)
print(res)


ls_root = [2, None, 3, 2, None, 1]
# Output: 2
root = build_binary_tree(ls_root)
res = Solution().longestConsecutive_v2(root)
print(res)


