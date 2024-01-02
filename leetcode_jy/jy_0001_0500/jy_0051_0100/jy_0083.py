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
tag_jy = "节点去重技巧 | 相似题: 0082"



"""
Given the `head` of a sorted linked list, delete all duplicates such that 
each element appears only once. Return the linked list sorted as well.


Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3


Constraints:
1) The number of nodes in the list is in the range [0, 300].
2) -100 <= Node.val <= 100
3) The list is guaranteed to be sorted in ascending order.
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法 1: 参照 0082 的解法进行适当修改
    """
    def deleteDuplicates_v1(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        prev = dummy
        current = head
        while current:
             while current.next and current.next.val == current.val:
                 current = current.next
             prev.next = current
             prev = current
             current = current.next

        return dummy.next


    """
解法 2: 无需引入 dummy 节点

直接遍历链表, 判断当前结点与下一结点的值是否相同:
1) 如果不同, 则移动到下一个结点
2) 如果相同, 则将当前结点的 next 指针指向下下个结点 (即删除掉已知的相同节点)

由于头结点不会改变, 所以最后返回头结点即可
    """
    def deleteDuplicates_v2(self, head: ListNode) -> ListNode:
        current = head
        # jy: 确保当前节点和下一节点均存在的情况下操作
        while current and current.next:
            # jy: 如果当前节点与下一个节点的值相同, 则将当前节点的下一节点指向
            #     当前节点的下下个节点 (即删除已知的重复节点), 随后会不断删除发
            #     现的重复节点, 直到与当前节点不同的节点为止, 才将当前节点切换
            #     到该节点, 随后继续循环判断
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


    """
解法 3: 递归版本
    """
    def deleteDuplicates_v3(self, head: ListNode) -> ListNode:
        # jy: 如果当前值或当前值的下一个值不存在, 则返回当前值, 终止递归
        if not head or not head.next:
            return head
        # jy: 对以 head.next 为头节点的链表进行去重处理
        head.next = self.deleteDuplicates_v3(head.next)
        # jy: 如果以 head.next 为头节点的链表去重后的头节点 (即 head.next) 与
        #     当前头节点 head 的值相同, 则从这两个节点中去重, 即返回 head.next
        #     即可
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


a = [1, 1, 2, 3, 3]
head = getListNodeFromList(a)
res = Solution().deleteDuplicates_v3(head)
# jy: 1->2->3
showLnValue(res)


