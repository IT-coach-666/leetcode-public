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
title_jy = "Partition-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a linked list and a value x, partition it such that all nodes less 
than x come before nodes greater than or equal to x. You should preserve 
the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法1: 直观的方法是额外创建两个链表, 一个存放值小于 x 的结点, 一个存放值大于等于 x 的结
点, 然后遍历链表根据值的大小判断当前的结点应该放到哪个链表中, 最后将两个新链表连接起来即可;
    """
    def partition_v1(self, head: ListNode, x: int) -> ListNode:
        # jy: 额外创建两个链表, l1 用于存放小于 x 的值, l2 用于存放大于等于 x 的值;
        #     l1 和 l2 分别记录着两个链表的头节点之前的节点;
        l1 = ListNode(-1)
        l2 = ListNode(-1)
        # jy: less 和 greater 分别记录 l1 链表和 l2 链表的尾节点;
        less, greater = l1, l2
        current = head
        # jy: 遍历链表
        while current:
            # jy: 如果链表值小于 x, 则连接到 less.next, 并将 less 指向该值(less 始终指向尾节点);
            if current.val < x:
                less.next, less = current, current
            # jy: 如果链表值大于等于 x, 则连接到 greater.next, 并将 greater 指向该值(greater 始终指向尾节点);
            else:
                greater.next, greater = current, current
            # jy: 将 current 指向下一个节点, 继续遍历;
            current = current.next
        # jy: 将 greater.next 设为 None, less.next 设置为 l2.next, 使得 l1, l2 链表连接起来;
        greater.next = None
        less.next = l2.next
        return l1.next

    """
解法2: 思想和解法 1 类似, 只是没有用到额外的辅助链表; 首先找出第一个值大于等于 x 的结点, 然后开
始遍历剩余的结点, 如果结点的值小于 x, 则将此结点移动到分割结点的前面, 否则继续遍历下一个结点;
    """
    def partition_v2(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        # jy: 找出第一个值大于等于 x 的节点(即以下 while 循环后的 prev.next 值), prev 表示
        #     其前一个节点;
        while prev.next and prev.next.val < x:
            prev = prev.next
        # jy: 将 current 指向 prev 节点(第一个大于等于 x 的节点的前一个节点), 并不断往后遍历;
        current = prev
        while current and current.next:
            # jy: 如果碰到小于 x 的节点(用 next 表示), 则将其链接到 prev.next, 并将 current.next
            #     指向 current.next.next; 相当于从后半部分删除小于 x 的节点并将其链接到前半部分中,
            #     并保证前半部分与后半部分总是连接起来(next.next = prev.next)
            if current.next.val < x:
                next = current.next
                current.next = next.next
                next.next, prev.next = prev.next, next
                prev = prev.next
            # jy: 如果 current.next 值大于等于 x, 则继续遍历;
            else:
                current = current.next
        return dummy.next


a = [1, 4, 3, 2, 5, 2]
x = 3
head = getListNodeFromList(a)
res = Solution().partition_v1(head, x)
# jy: 1->2->2->4->3->5
showLnValue(res)


head = getListNodeFromList(a)
res = Solution().partition_v2(head, x)
# jy: 1->2->2->4->3->5
showLnValue(res)


a = [2, 4, 3, 1, 5, 2]
x = 3
head = getListNodeFromList(a)
res = Solution().partition_v1(head, x)
showLnValue(res)




