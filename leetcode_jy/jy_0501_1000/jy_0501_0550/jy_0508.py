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
title_jy = "Most-Frequent-Subtree-Sum(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given the root of a binary tree, return the most frequent subtree sum. If there
is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by
the subtree rooted at that node (including the node itself).


Example 1:    https://www.yuque.com/frederick/dtwi9g/bio7g7
Input: root = [5,2,-3]
Output: [2,-3,4]

Example 2:
Input: root = [5,2,-5]
Output: [2]


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
"""


import collections
from typing import List
from about_TreeNode import *


class Solution:
    """
使用 Map 保存各个子树的和，然后遍历求解出现最频繁的子树和
    """
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        sums = collections.defaultdict(int)
        frequent_sums = []

        self._dfs(root, sums)

        max_frequency = max(sums.values())

        for sum, frequency in sums.items():
            if max_frequency == frequency:
                frequent_sums.append(sum)

        return frequent_sums

    def _dfs(self, root, sums):
        if not root:
            return 0
        # jy: 计算以当前 root 为根节点的数的所有节点值的总和, 并将总和出现的次数记录到 sums 字
        #     典中(所有子树的总节点和也都会被递归计算后记录到 sums 字典中);
        current_sum = root.val + self._dfs(root.left, sums) + self._dfs(root.right, sums)
        sums[current_sum] += 1

        return current_sum


ls_ = [5, 2, -3]
# Output: [2,-3,4]
root = build_binary_tree(ls_)
res = Solution().findFrequentTreeSum(root)
print(res)


ls_ = [5, 2, -5]
# Output: [2]
root = build_binary_tree(ls_)
res = Solution().findFrequentTreeSum(root)
print(res)


