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
title_jy = "Construct-Binary-Search-Tree-from-Preorder-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Return the root node of a binary search tree that matches the given ``preorder`` traversal.

Recall that a binary search tree is a binary tree where for every node:
node.left.val < node.val
node.right.val > node.val

Also recall that a preorder traversal displays the value of the node first, then traverses 
node.left, then traverses node.right.


Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
"""


import sys
from typing import List
from about_TreeNode import *


class Solution:
    """
解法1: 和 105_Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal.py 类似, 数组的
第一个元素为根结点的值, 根据根结点的值在数组中找到第一个大于根结点的值, 记下标为 i, 则 i
之前的元素构成左子树,  i 之后的元素构成右子树, 递归调用求解; 
    """
    def bstFromPreorder_v1(self, preorder: List[int]) -> TreeNode:
        return self._build(preorder, 0, len(preorder) - 1)

    def _build(self, preorder: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None

        root_value = preorder[start]
        # jy: right_tree_start 为一个数值, 即第一个 preorder[i] > root_value 的下标位置;
        right_tree_start = next((i for i in range(start, end + 1) if preorder[i] > root_value), end + 1)
        # print(right_tree_start)

        root = TreeNode(root_value)
        # jy: 构建左子树;
        root.left = self._build(preorder, start + 1, right_tree_start - 1)
        # jy: 构建右子树;
        root.right = self._build(preorder, right_tree_start, end)

        return root

    """
解法2: 还可以用栈和循环求解, 数组的首个元素为根结点, 将根结点压入栈, 然后遍历第一个元
素后的值, 每次循环取数组的当前元素作为新的子结点, 然后去栈中找这个新结点的父结点, 只要
栈顶的元素的值小于当前结点, 则执行出栈;
    """
    def bstFromPreorder_v2(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        # jy: 利用前序遍历的第一个元素构造根节点, 并将根节点入栈;
        n = len(preorder)
        root = TreeNode(preorder[0])
        stack = [root]
        # jy: 从前序遍历的第二个元素开始循环遍历;
        for i in range(1, n):
            # jy: 栈顶元素为根节点, 遍历得到的当前节为子节点;
            node, child = stack[-1], TreeNode(preorder[i])
            # jy: 如果栈不为空, 且栈顶的值小于当前子节点的值, 则出栈, 直到栈为空或者栈顶元素
            #    值大于或等于子节点值;
            while stack and stack[-1].val < child.val:
                node = stack.pop()
            # jy: 如果子节点小于当前父节点值, 则将子节点作为左子节点, 否则作为右子节点;
            if node.val > child.val:
                node.left = child
            else:
                node.right = child
            # jy: 将子节点入栈;
            stack.append(child)

        return root


preorder = [8, 5, 1, 7, 10, 12]
# Output: [8,5,10,1,7,null,12]
res = Solution().bstFromPreorder_v1(preorder)
# print(res)
print(serialize(res))

res = Solution().bstFromPreorder_v2(preorder)
# print(res)
print(serialize(res))



