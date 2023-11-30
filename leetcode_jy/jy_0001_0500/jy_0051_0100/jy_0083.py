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
title_jy = "Remove-Duplicates-from-Sorted-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法1: 直接遍历链表, 判断当前结点的值是否与下一个结点相同, 如果不同, 则移动到下一个结点, 如
果相同则将当前结点的 next 指针指向下下个结点, 由于头结点不会改变, 所以最后返回头结点即可;
    """
    def deleteDuplicates_v1(self, head: ListNode) -> ListNode:
        current = head
        # jy: 如果当前节点和下一个节点均存在
        while current and current.next:
            # jy: 判断当前值的下一个节点值是否与当前值相同, 如果相同则将当前值的下一个节点指向
            #    当前值的下下个节点, 随后继续判断当前值的下一个节点值与当前值是否相等, 直到不
            #    等为止, 将当前值切换为当前值的下一个并继续遍历判断;
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head



    """
解法2: 递归版本;
    """
    def deleteDuplicates_v2(self, head: ListNode) -> ListNode:
        # jy: 如果当前值或当前值的下一个值不存在, 则返回当前值;
        if not head or not head.next:
            return head
        # jy: 对 head 的下一节点进行去重;
        head.next = self.deleteDuplicates_v2(head.next)
        # jy: 如果 head 的下一节点的去重结果(即以 head.next 为第一个元素的链表) 中的
        #    head.next 对应的值与当前节点 head 值不同, 则返回当前节点 head, 否则返回
        #    当前节点的下一节点;
        return head if head.val != head.next.val else head.next


a =  [1, 1, 2]
head = getListNodeFromList(a)
res = Solution().deleteDuplicates_v1(head)
# jy: 1->2
showLnValue(res)

a = [1, 1, 2, 3, 3]
head = getListNodeFromList(a)
res = Solution().deleteDuplicates_v2(head)
# jy: 1->2->3
showLnValue(res)



