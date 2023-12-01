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
title_jy = "Odd-Even-Linked-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity
and O(nodes) time complexity.



Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL



Constraints:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法1: 分别用 odd 和 even 表示奇偶链表的尾部, 遍历链表, 将结点挂载到相应的链表上, 最后
连接奇偶链表;
    """
    def oddEvenList_v1(self, head: ListNode) -> ListNode:
        is_odd = True
        # jy: 逐个遍历链表时需要用到, 不能直接使用 head 进行遍历, 因为遍历时需要使变量
        #    指向其下一个值, 如果直接用 head, 后续无法找到链表的头部;
        current = head
        # jy: odd 和 even 表示奇偶链表的尾部; head_of_even 表示偶数链表的头, 后续连接
        #    奇偶链表时需要用到;
        odd, head_of_even = ListNode(-1), ListNode(-1)
        even = head_of_even
        # jy: 逐个元素遍历链表;
        while current:
            # jy: 如果当前节点是奇数节点, 将其加入到奇链表后;
            if is_odd:
                odd.next, odd = current, current
            # jy: 如果当前节点是偶数节点, 将其加入到偶链表后;
            else:
                even.next, even = current, current

            is_odd = not is_odd
            current = current.next
        # jy: 奇链表对接偶链表;
        odd.next = head_of_even.next
        even.next = None
        # jy: 返回原链表的头节点;
        return head



    """
解法2: 解法 1 类似, 不同的是在遍历链表时就维护了奇数链表和偶数链表的连接, 无需在遍历完成后进
行两个链表的挂接; 遍历链表时, 如果是奇数结点, 则将其挂载到奇数链表的尾部, 同时指向偶数链表的
首部, 偶数链表的尾部指向当前结点的下一个结点;
    """
    def oddEvenList_v2(self, head: ListNode) -> ListNode:
        if not head:
            return head

        # jy: 与下面的 current 对应(其指向的是第一个偶数链表节点, 故此处为 False, 即非奇数链表节点)
        is_odd = False
        # jy: 初始化奇数链表尾;
        odd_tail = head
        # jy: 初始化偶数链表尾;
        even_tail = head.next
        # jy: 将当前节点设置为第一个偶数链表节点;
        current = head.next

        while current:
            # jy: 以 1->2->3->4->5 为例进行思考:
            #    如果当前节点 current 为奇数节点, 则奇数链表尾节点的下一个节点直接指向当前节点,
            #    同时当前奇数节点的下一个节点为上轮拼接结果的奇数链表尾节点的下一个节点, 并使得当
            #    前 current 节点更新为其下一个节点;
            if is_odd:
                # jy:
                odd_tail.next, current.next, current = current, odd_tail.next, current.next
                odd_tail = odd_tail.next
                even_tail.next, even_tail = current, current
            # jy: 如果当前节点为偶数链表节点, 则跳过直接指向奇数链表节点;
            else:
                current = current.next

            is_odd = not is_odd

        return head



    """
解法3: 上述两种解法都不够简洁, 定义 odd 和 even 作为奇偶链表的尾部, 以 even and even.next 作
为循环判断条件遍历链表, 每次遍历时更新奇偶链表的下一个结点, 以更新 odd 为例, 将 odd.next 指
向 odd.next.next, 并移动 odd 至 odd.next, 最后连接奇偶链表;
    """
    def oddEvenList_v3(self, head: ListNode) -> ListNode:
        if not head:
            return head
        # jy: odd 记录奇链表尾部节点, even 记录偶链表尾部节点;
        odd = head
        even = head.next
        # jy: even_head 记录偶链表头节点, 用于后续奇偶链表的连接;
        even_head = even
        # jy: 如果偶链表节点存在, 则不断遍历操作;
        while even and even.next:
            # jy: 奇链表尾部节点跳过偶节点直接指向下一个奇节点;
            odd.next = odd.next.next
            # jy: 偶链表尾部节点跳过奇节点直接指向下一个偶节点;
            even.next = even.next.next
            # jy: 更新奇偶链表的末尾节点;
            odd = odd.next
            even = even.next
        # jy: 最后奇链表末尾节点与偶链表头节点互连, 实现拼接;
        odd.next = even_head

        return head


ls_ = [1, 2, 3, 4, 5, None]
# Output: 1->3->5->2->4->NULL
head_ = getListNodeFromList(ls_)
res = Solution().oddEvenList_v1(head_)
showLnValue(res)

ls_ = [2, 1, 3, 5, 6, 4, 7, None]
# Output: 2->3->6->7->1->5->4->NULL
head_ = getListNodeFromList(ls_)
res = Solution().oddEvenList_v2(head_)
showLnValue(res)


# Output: 2->3->6->7->1->5->4->NULL
head_ = getListNodeFromList(ls_)
res = Solution().oddEvenList_v3(head_)
showLnValue(res)


