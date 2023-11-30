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
title_jy = "Reorder-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
You are given the head of a singly linked-list. The list can be represented as:
L0  -->  L1 -->  ... --> Ln - 1  --> Ln
Reorder the list to be on the following form:
L0 --> Ln --> L1 --> Ln - 1 --> L2 --> Ln - 2 --> …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:    https://www.yuque.com/frederick/dtwi9g/bmddl5
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:
The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000
"""


from typing import Optional
from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
1) 使用快慢指针遍历链表找到链表的中间节点(如果链表长度是偶数, 则中间节点为中间两
   个节点的第一个)
2) 从慢指针的下一个节点开始遍历剩下的链表, 将其放入栈中;
3) 从头开始遍历链表，依次从栈中出栈构造新的链表
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        stack = []
        current = slow.next

        while current:
            stack.append(current)
            current = current.next

        current = head
        slow.next = None

        while stack:
            insert_node = stack.pop()
            next_node = current.next
            current.next, current = insert_node, current.next
            insert_node.next = next_node

        return head

    def reorderList_jy_2021_12_26(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        stack = []
        tmp = slow.next
        # jy: slow 的 next 指针必须指向 None, 否则后续链表会带有环, 使得得到的结果链表在
        #     调用 showLnValue 函数查看时, 陷入死循环;
        slow.next = None
        slow = tmp
        while slow:
            stack.append(slow)
            slow = slow.next

        cur_node = head
        while cur_node and stack:
            tmp = cur_node.next
            stack_node = stack.pop()
            cur_node.next = stack_node
            stack_node.next = tmp
            cur_node = tmp

        return head

ls_ = [1, 2, 3, 4]
# Output: [1,4,2,3]
head = getListNodeFromList(ls_)
Solution().reorderList(head)
showLnValue(head)


ls_ = [1, 2, 3, 4, 5]
# Output: [1,5,2,4,3]
head = getListNodeFromList(ls_)
Solution().reorderList(head)
showLnValue(head)


ls_ = [1, 2, 3, 4, 5]
# Output: [1,5,2,4,3]
head = getListNodeFromList(ls_)
Solution().reorderList_jy_2021_12_26(head)
showLnValue(head)


