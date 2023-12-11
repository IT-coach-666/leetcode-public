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
title_jy = "Binary-Tree-Longest-Consecutive-Sequence-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, return the length of the longest consecutive
path in the tree. This path can be either increasing or decreasing. For example,
[1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not
valid. On the other hand, the path can be in the child-Parent-child order, where
not necessarily be parent-child order.


Example 1:    https://www.yuque.com/frederick/dtwi9g/uvuuv7
Input: root = [1,2,3]
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].

Example 2:
Input: root = [2,1,3]
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].


Constraints:
The number of nodes in the tree is in the range [1, 3 * 10^4].
-3 * 10^4 <= Node.val <= 3 * 10^4
"""


from about_TreeNode import *


class Solution:
    """
在 298_Binary-Tree-Longest-Consecutive-Sequence.py 的基础上, 对某个节点, 对左右子树分别求:
1) 以 "父-子" 节点为顺序的递增的最长子序列
2) 以 "父-子" 节点为顺序的递减的最长子序列
3) 以 "子-父-子" 节点为顺序的递增、递减的最长子序列


前两个不考虑 "子-父" 节点顺序是因为 "子-父" 顺序等价于 "父-子" 节点顺序下取反递增/递减, 第
三个子序列的长度等于前两个子序列的长度相加减 1, 减 1 是因为根节点被两个子序列都使用了, 然后
根据根节点和左右子树的值的关系更新这三个子序列的长度
    """
    def longestConsecutive(self, root: TreeNode) -> int:
        return max(self._dfs(root))

    def _dfs(self, root):
        if not root:
            return 0, 0, 0

        max_increasing_length = 1
        max_decreasing_length = 1

        left_increasing_length, left_decreasing_length, left_full_length = self._dfs(root.left)
        right_increasing_length, right_decreasing_length, right_full_length = self._dfs(root.right)

        if root.left:
            if root.left.val - root.val == 1:
                max_increasing_length = left_increasing_length + 1

            if root.left.val - root.val == -1:
                max_decreasing_length = left_decreasing_length + 1

        if root.right:
            if root.right.val - root.val == 1:
                max_increasing_length = max(max_increasing_length, right_increasing_length + 1)

            if root.right.val - root.val == -1:
                max_decreasing_length = max(max_decreasing_length, right_decreasing_length + 1)

        return max_increasing_length, max_decreasing_length, max(
            max_increasing_length + max_decreasing_length - 1,
            left_full_length, right_full_length)


ls_ = [1,2,3]
# Output: 2
root = build_binary_tree(ls_)
res = Solution().longestConsecutive(ls_)
print(res)


ls_ = [2,1,3]
# Output: 3
root = build_binary_tree(ls_)
res = Solution().longestConsecutive(ls_)
print(res)


# 求树的最长连续（升序或降序）路径


