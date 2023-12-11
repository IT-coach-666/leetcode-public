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
title_jy = "Minimum-Cost-Tree-From-Leaf-Values(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array arr of positive integers, consider all binary trees such that:
Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.
A node is a leaf if and only if it has zero children.

Example 1:   https://www.yuque.com/frederick/dtwi9g/xbrf0c

Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.

Example 2:

Input: arr = [4,11]
Output: 44


Constraints:
2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it is less than 2^31).
"""

import sys
from typing import List


class Solution:
    """
记 dp[i][j] 表示 arr[i:j + 1] 组成的二叉树中所有非叶子结点的和的最小值; 对于 [i, j] 和 k (i <= k < j), 计算以 k 为根节点的子树下所有非叶子结点的和的最小值;
    """
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        return self._dfs(dp, arr, 0, n - 1)

    def _dfs(self, dp, arr, left, right):
        if dp[left][right] != 0:
            return dp[left][right]

        if left == right:
            return 0

        smallest = sys.maxsize

        for i in range(left, right):
            left_max = max(arr[left: i + 1])
            right_max = max(arr[i + 1: right + 1])
            left_sum = self._dfs(dp, arr, left, i)
            right_sum = self._dfs(dp, arr, i + 1, right)
            current_sum = left_max * right_max + left_sum + right_sum
            smallest = min(smallest, current_sum)

        dp[left][right] = smallest

        return smallest


