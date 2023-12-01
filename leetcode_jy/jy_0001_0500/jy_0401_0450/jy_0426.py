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
title_jy = "Convert-Binary-Search-Tree-to-Sorted-Doubly-Linked-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and
successor pointers in a doubly-linked list. For a circular doubly linked list, the
predecessor of the first element is the last element, and the successor of the last
element is the first element.

We want to do the transformation in place. After the transformation, the left pointer
of the tree node should point to its predecessor, and the right pointer should point
to its successor. You should return the pointer to the smallest element of the linked list.


Example 1:   https://www.yuque.com/frederick/dtwi9g/pz1d4o
Input: root = [4, 2, 5, 1, 3]
Output: [1, 2, 3, 4, 5]
Explanation: The figure below shows the transformed BST. The solid line indicates the
             successor relationship, while the dashed line means the predecessor relationship.

Example 2:
Input: root = [2, 1, 3]
Output: [1, 2, 3]

Example 3:
Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty Linked List.

Example 4:
Input: root = [1]
Output: [1]


Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
All the values of the tree are unique.
"""


from about_TreeNode import *


class Solution:
    """
在 094_Binary-Tree-Inorder-Traversal.py 的基础上, 出栈的同时即构造链表的节点;
当所有节点处理完成后, 将尾节点和头节点进行关联;
    """
    def treeToDoublyList(self, root: 'TreeNode') -> 'TreeNode':
        # jy: 初始化 dummy 节点, 作为双向链表(此处为一个树节点, right 代表 next, left 代
        #    表 prev)的头节点的 prev 节点;
        dummy = TreeNode(-1)
        # jy: 双向链表为空时, prev 指向 dummy 节点;
        prev = dummy
        stack = []
        # jy: 当前节点初始化为根节点;
        current = root
        # jy: 如果当前节点或栈不为空, 则不断循环;
        while current or stack:
            # jy: 将当前节点的所有左子节点不断入栈, 经过该循环后, 栈顶元素是二叉搜索
            #    树中最左侧元素(最小值)
            while current:
                stack.append(current)
                current = current.left
            # jy: 经过以上循环后, 栈顶元素为最小值, 将该最小值出栈, 并用该值重新构建一个树节
            #    点, 并将该节点加入到 prev 的下右侧节点(即构造双向链表, right 代表 next, left
            #    代表 prev;)
            current = stack.pop()
            node = TreeNode(current.val)
            # jy: 将前一个节点(即 prev)的 right (对应链表的 next 属性)指向当前节点, 将当前节点
            #    的 left (对应链表的 prev 属性)指向前一个节点, 即完成树节点加入双向链表;
            node.left, prev.right = prev, node
            prev = node
            # jy: 将当前节点指向当前节点的右子节点(如果右子节点存在的话); 如果右子节点不存在, 则
            #    current 为 None, 下轮循环中会继续从栈中出当前栈中最小的树节点元素, 继续构造双向
            #    链表;
            current = current.right
        # jy: 经过以上 while 循环后, 如果 prev 不是 dummy 节点, 表明双向链表中不止一个节点, 且此
        #    时的 prev 为链表的最后一个节点了, 此时将该节点与第一个节点(即 dummy.right)双向连接
        #    起来;
        if prev is not dummy:
            prev.right = dummy.right
            dummy.right.left = prev
        # jy: 最终返回 dummy.right, 即头节点;
        return dummy.right


ls_ = [4, 2, 5, 1, 3]
# Output: [1, 2, 3, 4, 5]
root = build_binary_tree(ls_)
res = Solution().treeToDoublyList(root)
print(res.val)
#print("pre_order: ", pre_order(res))


ls_ = [2, 1, 3]
# Output: [1, 2, 3]
root = build_binary_tree(ls_)
res = Solution().treeToDoublyList(root)
print(res.val)


ls_ = []
# Output: []
root = build_binary_tree(ls_)
res = Solution().treeToDoublyList(root)
print(res)


ls_ = [1]
# Output: [1]
root = build_binary_tree(ls_)
res = Solution().treeToDoublyList(root)
print(res.val)


