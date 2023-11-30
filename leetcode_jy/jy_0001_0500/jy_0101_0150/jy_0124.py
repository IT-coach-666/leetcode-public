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
title_jy = "Binary-Tree-Maximum-Path-Sum(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in
the sequence has an edge connecting them. A node can only appear in the sequence at
most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any path.


Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


Constraints:
The number of nodes in the tree is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000
"""


import sys
from about_TreeNode import *


"""
该题实际是取树中任意两个节点, 计算连接这两个节点的路径上的数字之和, 求所有数字中的最大值;

递归分别判断左右子树可能返回的最大路径和, 由于数字有可能是负数, 所以计算左右子树的路径和时
将其和 0 比较, 从而忽略负数, 左子树和、当前节点值、右子树和三者相加就是整个路径的和, 在搜索
时更新最大值;
"""
class Solution:
    def __init__(self):
        self.max_sum = -sys.maxsize

    def maxPathSum_v1(self, root: TreeNode) -> int:
        if not root:
            return 0
        self._dfs_v1(root)
        return self.max_sum

    def _dfs_v1(self, root):
        if not root:
            return 0
        # jy: 递归获取左子树返回的最大路径和(计算左右子树的路径和时将其和 0 比较, 从而忽略负数);
        left = max(self._dfs_v1(root.left), 0)
        # jy: 递归获取右子树返回的最大路径和;
        right = max(self._dfs_v1(root.right), 0)
        # jy: 左子树和、当前节点值、右子树和三者相加就是整个路径的和, 在搜索时更新最大值;
        current_sum = root.val + left + right
        self.max_sum = max(self.max_sum, current_sum)
        # jy: 注意此处返回的值为 root.val 与左或右子树的最大路径; 此处返回的结果将会是被上一层递
        #     归调用所使用的, 只能包含左或右子节点, 确保与上一层的根节点构成的路径是一连串的, 而
        #     不会产生有三个分支的分叉点(可以画一棵深度为 3 的树进行思考)
        return root.val + max(left, right)

    """
解法2: 在解法 1 的基础上去除类属性的使用(替换时候列表来保存最大值, 使用列表可保证
递归过程的修改也实时生效)
    """
    def maxPathSum_v2(self, root: TreeNode) -> int:
        if not root:
            return 0
        ls_ = [-sys.maxsize]
        self._dfs_v2(root, ls_)
        return ls_[0]

    def _dfs_v2(self, root, ls_):
        if not root:
            return 0

        left = max(self._dfs_v2(root.left, ls_), 0)
        right = max(self._dfs_v2(root.right, ls_), 0)
        current_sum = root.val + left + right
        ls_[0] = max(ls_[0], current_sum)

        return root.val + max(left, right)


ls_ = [1, 2, 3]
# Output: 6
root = build_binary_tree(ls_)
res = Solution().maxPathSum_v1(root)
print(res)


ls_ = [-10, 9, 20, None, None, 15, 7]
# Output: 42
root = build_binary_tree(ls_)
res = Solution().maxPathSum_v2(root)
print(res)


