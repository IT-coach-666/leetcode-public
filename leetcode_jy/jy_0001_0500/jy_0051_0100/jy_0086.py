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
tag_jy = "链表移动拼接技巧 | IMP"



"""
Given the `head` of a linked list and a value `x`, partition it such that all
nodes less than `x` come before nodes greater than or equal to `x`. 

You should preserve the original relative order of the nodes in each of the 
two partitions.


Example 1:
Input: head = [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]

Example 2:
Input: head = [2, 1], x = 2
Output: [1, 2]
 

Constraints:
1) The number of nodes in the list is in the range [0, 200].
2) -100 <= Node.val <= 100
3) -200 <= x <= 200
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法 1: 基于辅助链表

题意: 将小于指定值的节点放到指定值的左边, 大于指定值的节点放到指定值
的右边, 且左右两边的节点保持原有的相对位置不变

额外创建两个链表, 一个存放值小于 x 的结点, 一个存放值大于等于 x 的结
点, 然后遍历链表根据值的大小判断当前的结点应放到哪个链表中, 最后将两
个新链表连接起来即可
    """
    def partition_v1(self, head: ListNode, x: int) -> ListNode:
        # jy: l1 用于存放小于 x 的值, l2 用于存放大于等于 x 的值,
        #     此处表示两个链表的头节点之前的节点
        dummy_l1 = ListNode(-1)
        dummy_l2 = ListNode(-1)
        # jy: tail_l1 和 tail_l2 分别记录 l1 链表和 l2 链表的尾节点
        tail_l1, tail_l2 = dummy_l1, dummy_l2
        current = head
        # jy: 遍历链表
        while current:
            # jy: 如果链表值小于 x, 则连接到 tail_l1.next, 并将 tail_l1
            #     指向该值 (tail_l1 始终指向尾节点)
            if current.val < x:
                tail_l1.next, tail_l1 = current, current
            # jy: 如果链表值大于等于 x, 则连接到 tail_l2.next, 并将 
            #     tail_l2 指向该值 (tail_l2 始终指向尾节点)
            else:
                tail_l2.next, tail_l2 = current, current
            # jy: 将 current 指向下一个节点, 继续遍历
            current = current.next
        # jy: 将 tail_l2.next 设为 None, tail_l1.next 设置为 l2.next,
        #     使得 l1, l2 链表连接起来
        tail_l2.next = None
        tail_l1.next = dummy_l2.next
        return dummy_l1.next


    """
解法 2: 优化解法 1, 无需使用辅助链表

首先找出第一个大于等于 x 的结点的前一个节点 prev, 然后开始遍历剩余的结点,
如果结点值小于 x, 则将此结点移动到分割结点的前面, 否则继续遍历下一个结点
    """
    def partition_v2(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        # jy: 找出第一个大于等于 x 的节点 (即以下 while 循环后的 prev.next
        #     值), prev 表示其前一个节点
        while prev.next and prev.next.val < x:
            prev = prev.next
        # jy: 从 prev 节点 (第一个大于等于 x 的节点的前一个节点) 不断往后遍历
        current = prev
        while current and current.next:
            # jy: 如果碰到下一个小于 x 的节点
            if current.next.val < x:
                # jy: 用 next_ 记录下一个小于 x 的节点 
                next_ = current.next
                # jy: 先将当前节点的指向跳过原下一个节点, 直接指向下下个节点
                current.next = next_.next
                # jy: 将 next_ 节点的下一个节点先修改为 prev 的下一个节点, 随
                #     后将 prev 的下一个节点设置为 next_ (即将 next_ 成功插入
                #     到 prev 的后面, 并使得左右依旧相连)
                next_.next, prev.next = prev.next, next_
                # jy: prev 更新为 prev.next, 随后进入下一轮循环
                prev = prev.next
            # jy: 如果 current.next 值大于等于 x, 则继续遍历
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


ls_ = [2, 1]
x = 2
head = getListNodeFromList(ls_)
res = Solution().partition_v1(head, x)
# jy: [1, 2]
showLnValue(res)


