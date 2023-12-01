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
title_jy = "N-ary-Tree-Preorder-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
N-ary-Tree input serialization is represented in their level order traversal. Each
group of children is separated by the null value (See examples)


Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]


Constraints:
The number of nodes in the tree is in the range [0, 10^4].
0 <= Node.val <= 10^4
The height of the n-ary tree is less than or equal to 1000.


Follow up:  Recursive solution is trivial, could you do it iteratively?
"""


from typing import List
from about_TreeNode import *



class Solution:
    """
解法1递归求解;
    """
    def preorder_v1(self, root: 'Node') -> List[int]:
        values = []
        self._preorder(root, values)
        return values

    def _preorder(self, root, values):
        if not root:
            return
        # jy: 前序遍历, 先遍历根节点, 再从左侧开始递归遍历子节点(如果子节点存在的话)
        values.append(root.val)
        if root.children:
            for child in root.children:
                self._preorder(child, values)

    """
解法2: 和 144_Binary-Tree-Preorder-Traversal.py 的解法 2 一样;
    """
    def preorder_v2(self, root: 'Node') -> List[int]:
        if not root:
            return []
        # jy: 先将根节点入栈
        stack = [root]
        values = []
        # jy: 如果栈不为空, 则出栈遍历一节点, 并将该节点的子节点从右往左逐个入栈(因
        #    为前序遍历时, 左子节点优先右子节点遍历; 入栈时右子节点得优先入栈(栈的
        #    先进后出/后进先出特点))
        while stack:
            node = stack.pop()
            values.append(node.val)

            if node.children:
                for i in range(len(node.children) - 1, -1, -1):
                    stack.append(node.children[i])

        return values


ls_N_ary = [1, [3, [5, 6], 2, 4]]
root = build_N_ary_tree(ls_N_ary)
# print(show_N_ary_tree(root))
# Output: [1,3,5,6,2,4]
res = Solution().preorder_v1(root)
print(res)


ls_N_ary = [1, [2, 3, [6, 7, [11, [14]]], 4, [8, [12]], 5, [9, [13], 10]]]
root = build_N_ary_tree(ls_N_ary)
# print(show_N_ary_tree(root))
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
res = Solution().preorder_v2(root)
print(res)


