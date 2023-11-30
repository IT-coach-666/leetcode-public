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
title_jy = "Binary-Tree-Postorder-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.


Example 1:
Input: root = [1, null, 2, 3]
Output: [3, 2, 1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1, 2]
Output: [2, 1]

Example 5:
Input: root = [1, null, 2]
Output: [2, 1]


Constraints:
• The number of the nodes in the tree is in the range [0, 100].
• -100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import List
import collections
from about_TreeNode import *

class Solution:
    """
解法1: 递归;
    """
    def postorderTraversal_v1(self, root: TreeNode) -> List[int]:
        values = []
        self._postorder_traversal(root, values)
        return values

    def _postorder_traversal(self, root: TreeNode, values: List[int]) -> None:
        if not root:
            return
        self._postorder_traversal(root.left, values)
        self._postorder_traversal(root.right, values)
        values.append(root.val)

    """
解法2: 与 144_Binary-Tree-Preorder-Traversal.py 的解法 2 类似, 不过这里需要使用双向队列来
保存最终值; 同样是先将根节点入栈, 只要栈不为空, 则执行出栈, 不同的是将出栈的节点值放入双端
队列的头部, 然后如果左节点存在, 则将左节点入栈, 如果右节点存在, 则将右节点入栈;

jy: 此处的双向队列 values 也可以使用 [], 然后插入元素时一直在列表左侧插入: values.insert(0, val)
但列表的这种插入方式时间复杂度较高;
    """
    def postorderTraversal_v2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # jy: 构建双向队列;
        values = collections.deque([])
        # jy: 先将根节点入栈;
        stack = [root]
        while stack:
            # jy: 出栈一个元素, 并加入到队列的左侧;
            node = stack.pop()
            values.appendleft(node.val)
            # jy: 先将出栈元素的左子节点入栈, 再将右子节点入栈(如果子节点存在的话);
            #    下一轮 while 循环时, 由于右子节点先入栈, 故右子节点会先出栈, 出栈
            #    后会被加入到队列的左侧, 即越后入栈的元素, 将在队列的越左侧(越前面);
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return list(values)


ls_ = [1, None, 2, None, None, 3]
root = build_binary_tree(ls_)
res = Solution().postorderTraversal_v1(root)
print(res)
# Output: [3, 2, 1]

ls_ = []
root = build_binary_tree(ls_)
res = Solution().postorderTraversal_v2(root)
print(res)
# Output: []

ls_ = [1]
root = build_binary_tree(ls_)
res = Solution().postorderTraversal_v2(root)
print(res)
# Output: [1]

ls_ = [1, 2]
root = build_binary_tree(ls_)
res = Solution().postorderTraversal_v2(root)
print(res)
# Output: [2, 1]

ls_ = [1, None, 2]
root = build_binary_tree(ls_)
res = Solution().postorderTraversal_v2(root)
print(res)


