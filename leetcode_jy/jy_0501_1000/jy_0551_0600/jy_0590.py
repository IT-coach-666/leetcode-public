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
title_jy = "N-ary-Tree-Postorder-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal. Each group
of children is separated by the null value (See examples)

Example 1: (图: https://www.yuque.com/frederick/dtwi9g/hqa2dl)
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
Constraints:The number of nodes in the tree is in the range [0, 10^4].0 <= Node.val <= 10^4The height of the n-ary tree is less than or equal to 1000.
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


from typing import List
from collections import deque
from about_TreeNode import *


class Solution:
    """
解法1: 递归求解: 如果当前节点有子节点, 则优先遍历子节点, 子节点遍历完成再遍历根节点;
    """
    def postorder_v1(self, root: 'Node') -> List[int]:
        values = []
        # jy: 后序遍历二叉树, 并将遍历结果存放在 values 列表中;
        self._postorder(root, values)

        return values


    def _postorder(self, root, values):
        """
        后序遍历二叉树, 并将遍历结果存放在 values 列表中
        """
        # jy: 如果当前节点为空, 直接返回(递归终止条件)
        if not root:
            return
        # jy: 如果当前节点有子节点, 则先遍历子节点;
        if root.children:
            for child in root.children:
                self._postorder(child, values)
        # jy: 子节点遍历完后再遍历根节点
        values.append(root.val)


    """
解法2: 和 145_Binary-Tree-Postorder-Traversal.py 的解法 2 一样;
    """
    def postorder_v2(self, root: 'Node') -> List[int]:
        if not root:
            return []
        # jy: 双向队列, 用于存放后续遍历的结果;
        values = deque([])
        # jy: 将根节点入栈;
        stack = [root]
        # jy: 如果栈不为空, 则不断遍历出栈;
        while stack:
            # jy: 右侧出栈;
            node = stack.pop()
            # jy: 每次将出栈的元素均加入到队列的左侧, 使得先入栈的元素, 最后被 "挤" 到队
            #    列的右侧;
            values.appendleft(node.val)
            # jy: 如果当前节点有子节点, 则将子节点从左往右入栈;  后续出栈时会右侧节点先出,
            #    并不断将其加入到队列左侧, 使得子节点原先的从左到右顺序在队列中依然是从左
            #    到右排列;
            if node.children:
                for child in node.children:
                    stack.append(child)

        return list(values)

ls_N_ary = [1, [3, [5, 6], 2, 4]]
root = build_N_ary_tree(ls_N_ary)
res = Solution().postorder_v1(root)
# Output: [5,6,3,2,4,1]
print(res)


ls_N_ary = [1, [2, 3, [6, 7, [11, [14]]], 4, [8, [12]], 5, [9, [13], 10]]]
root = build_N_ary_tree(ls_N_ary)
res = Solution().postorder_v2(root)
# Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
print(res)


