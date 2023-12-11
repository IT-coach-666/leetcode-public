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
title_jy = "Diameter-of-N-Ary-Tree(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.
The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.
(Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)

Example 1:    https://www.yuque.com/frederick/dtwi9g/ixpx4r

Input: root = [1,None,3,2,4,None,5,6]
Output: 3
Explanation: Diameter is shown in red color.

Example 2:

Input: root = [1,None,2,None,3,4,None,5,None,6]
Output: 4

Example 3:

Input: root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
Output: 7


Constraints:
The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [1, 10^4].
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def __init__(self):
        self.max_length = 0
    """
在 543. Diameter of Binary Tree 的基础上扩展为一般的树, 对于某个节点来说, 经过当前节点的最长路径为当前节点最深的两个孩子节点的高度之和;
    """
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self._dfs(root)

        return self.max_length

    def _dfs(self, root):
        if not root:
            return 0

        max1, max2 = 0, 0

        for child in root.children:
            height = self._dfs(child)

            if height > max1:
                max1, max2 = height, max1
            elif height > max2:
                max2 = height

        self.max_length = max(self.max_length, max1 + max2)

        return max1 + 1


