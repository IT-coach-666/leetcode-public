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
title_jy = "Binary-Tree-Inorder-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1, null, 2, 3]
   1
    \
     2
    /
   3
Output: [1, 3, 2]


Follow up: Recursive solution is trivial, could you do it iteratively?
"""


from typing import List
from about_TreeNode import *


class Solution:
    """
解法1: 递归求解;
    """
    def inorderTraversal_v1(self, root: TreeNode) -> List[int]:
        values = []
        self.traversal(root, values)
        return values
    
    # jy: 中序遍历;
    def traversal(self, root: TreeNode, values: List[int]) -> None:
        if not root:
            return
        self.traversal(root.left, values)
        values.append(root.val)
        self.traversal(root.right, values)


    """
解法2: 维护一个栈, 只要当前结点有左子结点, 就将当前结点压入栈, 并将左子结点赋值给当
前结点, 直到遇到没有左子结点后, 则出栈一个结点, 然后对该结点的右子结点重复上述操作;
    """
    def inorderTraversal_v2(self, root: TreeNode) -> List[int]:
        values = []
        stack = []
        current = root
        # jy: 当前节点和栈均空的情况下退出循环;
        while current or stack:
            # jy: 将当前节点入栈后, 当前节点指向当前节点的左节点, 并不断循环入栈, 直到
            #    当前节点为空;
            while current:
                stack.append(current)
                current = current.left
            # jy: 经过以上内部 while 循环后, 局部左子节点即遍历完成, 此时出栈, 并将该值
            #    添加到列表中;
            current = stack.pop()
            values.append(current.val)
            # jy: 随后指向该节点的右节点(可能为空), 并进入下一轮循环; 当右节点为空但此时
            #    栈中有值时, 继续出栈, 然后继续遍历右节点; 不断循环直到栈空即遍历完成;
            current = current.right
        return values



ls_ = [1, None, 2, None, None, 3]
root = build_binary_tree(ls_)

res = Solution().inorderTraversal_v1(root)
print(res)


res = Solution().inorderTraversal_v2(root)
print(res)



