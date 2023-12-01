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
title_jy = "Delete-Node-in-a-Linked-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Write a function to delete a node in a singly-linked list. You will not be given
access to the head of the list, instead you will be given access to the node to
be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.



Example 1:
图见: https://www.yuque.com/frederick/dtwi9g/qusnwy
Input: head = [4, 5, 1, 9], node = 5
Output: [4, 1, 9]
Explanation: You are given the second node with value 5, the linked list should
             become 4 -> 1 -> 9 after calling your function.

Example 2:
Input: head = [4, 5, 1, 9], node = 1
Output: [4, 5, 9]
Explanation: You are given the third node with value 1, the linked list should
             become 4 -> 5 -> 9 after calling your function.

Example 3:
Input: head = [1, 2, 3, 4], node = 3
Output: [1, 2, 4]

Example 4:
Input: head = [0, 1], node = 0
Output: [1]

Example 5:
Input: head = [-3, 5, -99], node = -3
Output: [5, -99]



Constraints:
The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node to be deleted is in the list and is not a tail node
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
不按常规套路走的题; 删除当前节点采用将当前节点的值修改为后一个节点的值的方式(因为题目
中描述当前节点不是尾节点, 所以 node.next 不为空), 同时将当前节点的 next 指针指向下一
个节点的 next 指针;
    """
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


ls_ = [4, 5, 1, 9]
node = 5
head = getListNodeFromList(ls_)
res = Solution().deleteNode(head.next)
showLnValue(head)
# Output: [4, 1, 9]


ls_ = [4, 5, 1, 9]
node = 1
# Output: [4, 5, 9]
head = getListNodeFromList(ls_)
res = Solution().deleteNode(head.next.next)
showLnValue(head)


ls_ = [1, 2, 3, 4]
node = 3
# Output: [1, 2, 4]
head = getListNodeFromList(ls_)
res = Solution().deleteNode(head.next.next)
showLnValue(head)

ls_ = [0, 1]
node = 0
# Output: [1]
head = getListNodeFromList(ls_)
res = Solution().deleteNode(head)
showLnValue(head)

ls_ = [-3, 5, -99]
node = -3
# Output: [5, -99]
head = getListNodeFromList(ls_)
res = Solution().deleteNode(head)
showLnValue(head)


