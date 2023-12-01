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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Closest-Binary-Search-Tree-Value-II(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are
closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target.


Example 1:
Input: root = [4, 2, 5, 1, 3], target = 3.714286, k = 2
Output: [4, 3]

Example 2:
Input: root = [1], target = 0.000000, k = 1
Output: [1]


Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 10^4.
0 <= Node.val <= 10^9
-10^9 <= target <= 10^9


Follow up: Assume that the BST is balanced. Could you solve it in less than O(n) runtime (where n = total nodes)?
"""


import collections
from typing import List
from about_TreeNode import *


class Solution:
    """
解法1: 使用中序遍历将二叉搜索树转为有序数组, 题目就变成了 658_Find-K-Closest-Elements.py;
    """
    def closestKValues_v1(self, root: TreeNode, target: float, k: int) -> List[int]:
        sorted_values = []
        # jy: 二叉搜索树中序遍历, 得到的一个升序排序的数组;
        self._inorder_traversal_v1(root, sorted_values)

        return self._find_closest_elements(sorted_values, k, target)


    def _inorder_traversal_v1(self, root: TreeNode, values: List[int]) -> None:
        if not root:
            return
        self._inorder_traversal_v1(root.left, values)
        values.append(root.val)
        self._inorder_traversal_v1(root.right, values)


    def _find_closest_elements(self, arr: List[int], k: int, x: float) -> List[int]:
        """658_Find-K-Closest-Elements.py 中的解法 2"""
        low, high = 0, len(arr) - k

        while low < high:
            middle = low + (high - low) // 2

            if x - arr[middle] > arr[middle + k] - x:
                low = middle + 1
            else:
                high = middle

        return arr[low:low + k]


    """
解法2: 和解法 1 类似, 首先使用一个双端队列保存中序遍历的结果, 然后一直检查双端队列的首尾, 将距
离 taret 远的元素移除, 一直到双端队列的长度等于 k;
    """
    def closestKValues_v2(self, root: TreeNode, target: float, k: int) -> List[int]:
        deque = collections.deque([])
        self._inorder_traversal_v2(root, deque)

        while len(deque) > k:
            if abs(deque[0] - target) > abs(deque[-1] - target):
                deque.popleft()
            else:
                deque.pop()

        return list(deque)


    def _inorder_traversal_v2(self, root: TreeNode, deque) -> None:
        if not root:
            return
        self._inorder_traversal_v2(root.left, deque)
        deque.append(root.val)
        self._inorder_traversal_v2(root.right, deque)



ls_ = [4, 2, 5, 1, 3]
target = 3.714286
k = 2
# Output: [4, 3]
root = build_binary_tree(ls_)
res = Solution().closestKValues_v1(root, target, k)
print(res)



ls_ = [1]
target = 0.000000
k = 1
# Output: [1]
root = build_binary_tree(ls_)
res = Solution().closestKValues_v2(root, target, k)
print(res)


