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
title_jy = "Insertion-Sort-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the head of a singly linked list, sort the list using insertion sort, and return
the sorted list's head. The steps of the insertion sort algorithm:
1) Insertion sort iterates, consuming one input element each repetition and growing
   a sorted output list.
2) At each iteration, insertion sort removes one element from the input data, finds the
   location it belongs within the sorted list and inserts it there.
3) It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially
sorted list (black) initially contains only the first element in the list. One element
(red) is removed from the input data and inserted in-place into the sorted list with
each iteration.


Example 1:   https://www.yuque.com/frederick/dtwi9g/zpkv1m
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]


Constraints:
The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000
"""

from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
因为链表的头节点有可能改变, 所以建立一个 dummy 节点来辅助处理, 首先处理头结点的下一
个节点, 借助 dummy 节点遍历当前节点应该插入的位置, 将节点插入后继续处理后续节点
    """
    def insertionSortList_v1(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        tail = head.next
        sorted_list_tail = head

        while tail:
            rest = tail.next
            prev = dummy

            while prev.next is not tail and prev.next.val <= tail.val:
                prev = prev.next

            if prev.next is tail:
                sorted_list_tail = tail
                tail = rest
                continue

            prev.next, tail.next = tail, prev.next
            sorted_list_tail.next = rest
            tail = rest

        return dummy.next

    """
JY: LeetCode 上性能比解法 1 好
    """
    def insertionSortList_jy_2021_12_26(self, head):
        new_head = head
        new_tail = head
        cur_node = head.next
        # jy: 注意, tail 的 next 指针必须保持指向 None, 防止如果 head 就是最大指针节点
        #     时, 没事先指向 None, 后续的 new_tail 也一直不会被更新, 导致出现链表环, 使
        #     得以下 while cur_node 中陷入死循环(且该指向 None 的过程必须在 cur_node 赋
        #     值之后, 否则会使得 cur_node 开始就是 None);
        new_tail.next = None
        while cur_node:
            if cur_node.val > new_tail.val:
                tmp = cur_node.next
                new_tail.next, new_tail = cur_node, cur_node
                cur_node.next = None
                cur_node = tmp
            elif cur_node.val < new_head.val:
                tmp = cur_node.next
                cur_node.next = new_head
                new_head = cur_node
                cur_node = tmp
            else:
                tmp_head = new_head
                while tmp_head.next and tmp_head.next.val < cur_node.val:
                    tmp_head = tmp_head.next
                old_next = tmp_head.next
                tmp = cur_node.next
                tmp_head.next = cur_node
                cur_node.next = old_next
                cur_node = tmp
        return new_head


ls_ = [4, 2, 1, 3]
# Output: [1,2,3,4]
head_ = getListNodeFromList(ls_)
res = Solution().insertionSortList_v1(head_)
showLnValue(res)


ls_ = [-1, 5, 3, 4, 0]
# Output: [-1,0,3,4,5]
head_ = getListNodeFromList(ls_)
res = Solution().insertionSortList_v1(head_)
showLnValue(res)


ls_ = [-1, 5, 3, 4, 0]
# ls_ = [4, 2, 1, 3]
head_ = getListNodeFromList(ls_)
res = Solution().insertionSortList_jy_2021_12_26(head_)
showLnValue(res)


