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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Convert-Sorted-Array-to-Binary-Search-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array where elements are sorted in ascending order, convert it to a
height-balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.


Example:
Given the sorted array: [-10, -3, 0, 5, 9],
One possible answer is: [0, -3, 9, -10, null, 5], which represents the
following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
"""


from typing import List
from about_TreeNode import *


class Solution:
    """
首先将根结点定为数组的中间元素, 这样左子树就是左半部分, 右子树就是右半部分, 两边的高
度差不超过 1, 然后对左右半边进行递归调用;
    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # jy: 依据 nums[0, len(nums)-1] 构建树;
        return self._build_tree(nums, 0, len(nums)-1)

    def _build_tree(self, nums: List[int], low: int, high: int) -> TreeNode:
        # jy: 设定递归终止条件;
        if low > high:
            return None
        # jy: 找出数组中的中间元素, 将其作为根节点;
        middle = (low + high) // 2
        root = TreeNode(nums[middle])
        # jy: 用数组中间元素的左边元素构建左子树;
        root.left = self._build_tree(nums, low, middle-1)
        # jy: 用数组中间元素的右边元素构建右子树;
        root.right = self._build_tree(nums, middle+1, high)
        return root


ls_ = [-10, -3, 0, 5, 9]
res = Solution().sortedArrayToBST(ls_)
#print(pre_order(res, ls_=[]))
print("in_order: ", in_order(res, ls_=[]))

expected = [0, -3, 9, -10, None, 5]
ex_tree = build_binary_tree(expected)
#print(pre_order(ex_tree, ls_=[]))
print("in order(Expected):", in_order(ex_tree, ls_=[]))


