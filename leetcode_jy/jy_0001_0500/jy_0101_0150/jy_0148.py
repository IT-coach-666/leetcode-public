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
title_jy = "Sort-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the head of a linked list, return the list after sorting it in ascending order.


Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []


Constraints:
The number of nodes in the list is in the range [0, 5 * 10^4].
-10^5 <= Node.val <= 10^5


Follow up:
Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""


from typing import Optional
from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法1: 使用归并排序, 先使用快慢指针找到链表的中间节点, 然后以中间节点为界拆分
链表, 分别递归调用排序两个链表, 最后合并链表
    """
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        middle = self._find_middle(head)

        head2 = middle.next
        middle.next = None

        list1 = self.sortList(head)
        list2 = self.sortList(head2)

        return self._merge(list1, list2)

    def _find_middle(self, head):
        slow, fast = head, head
        while slow and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, a, b):
        dummy = ListNode(0)
        current = dummy

        while a and b:
            if a.val <= b.val:
                current.next = a
                a = a.next
            else:
                current.next = b
                b = b.next
            current = current.next
        current.next = a or b

        return dummy.next

    """
JY: 2021-12-26
    """
    def sortList_jy(self, head):
        # jy: 先快慢指针找出中间节点
        if not head or not head.next:
            return head
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # jy: 此处必须要将链表从 slow 处断开(slow 之前的为前一半, 包括 slow 在内的之后为后一半)
        if prev:
            prev.next = None
        head_1 = self.sortList_jy(head)
        head_2 = self.sortList_jy(slow)
        return self.sort_two_sortedListNode(head_1, head_2)

    def sort_two_sortedListNode(self, head_1, head_2):
        """
        该方法即为归并中的 merge
        """
        dummy = ListNode(0)
        prev = dummy
        while head_1 and head_2:
            if head_1.val >= head_2.val:
                tmp = head_2.next
                prev.next, prev = head_2, head_2
                # jy: 以下代码可有可无
                # head_2.next = None
                head_2 = tmp
            else:
                tmp = head_1.next
                prev.next, prev = head_1, head_1
                # jy: 以下代码可有可无
                # head_1.next = None
                head_1 = tmp
        if head_1 or head_2:
            prev.next = head_1 or head_2

        return dummy.next


ls_ = [4, 2, 1, 3]
# Output: [1,2,3,4]
head_ = getListNodeFromList(ls_)
res = Solution().sortList(head_)
showLnValue(res)


ls_ = [-1, 5, 3, 4, 0]
# Output: [-1,0,3,4,5]
head_ = getListNodeFromList(ls_)
res = Solution().sortList(head_)
showLnValue(res)


ls_ = []
# Output: []
head_ = getListNodeFromList(ls_)
res = Solution().sortList(head_)
showLnValue(res)


ls_ = [-1, 5, 3, 4, 0]
# Output: [-1,0,3,4,5]
head_ = getListNodeFromList(ls_)
res = Solution().sortList_jy(head_)
showLnValue(res)


