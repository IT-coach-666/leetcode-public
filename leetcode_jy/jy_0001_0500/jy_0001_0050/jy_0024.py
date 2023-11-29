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
type_jy = ""
# jy: 记录该题的英文简称以及所属类别
title_jy = "swap-nodes-in-pairs(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法1: 由于链表反转会改变原有链表的头结点, 我们使用一个 dummy 节点来指向原链表的头结
点(即 dummy.next = head), 最后返回 dummy.next 即为新链表的头结点; 首先定义两个变量, 
prev 指向 dummy(即当前节点的前一节点), current 指向 dummy.next(即当前节点),当 current 
和 current.next 都不为空时, 反转 current 和 current.next:

1)将 current 的 next 指针指向 current.next 的 next 指针
current.next = current.next.next

2)将原 current 的下一个结点的 next 指针指向 current:
current.next.next = current

3)将 prev.next 指向【原 current】的下一个结点(此处的作用是保证链表片段间能连接起来):
prev.next = current.next

然后, 将 prev 新赋值为 current, 将 current 新赋值为 current.next
并将【现 current】指向【原 current】的下下个节点(next.next)
    """
    def swapPairs_v1(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        # jy: 定义两个变量, prev 指向 dummy(即 head 的前一节点), current 指向 dummy.next(即 head);
        prev, current = dummy, dummy.next
        # jy: 如果当前节点及其下一节点均存在(以 1->2->3->4 为例进行思考);
        while current and current.next:
            #part-v1: 必须引入中间变量(如果是数值, 可通过算术运算特性避免中间变量)
            """
            next = current.next
            current.next, next.next, prev.next = next.next, current, next
            """
            #part-v2: 必须引入中间变量(如果是数值, 可通过算术运算特性避免中间变量)
            c_next = current.next
            current.next = c_next.next
            c_next.next = current
            prev.next = c_next         # jy: 此处的作用是保证链表片段间能连接起来;

            #print(c_next.val)
            # jy: 更新 prev 为原先的 current, 因为原先的 current 与其下一个调换后, 就成
            #    为下下个的 prev; 更新 current 为原先 current 的下下个, 即 current.next; 经
            #    过更新后的 current.next 即已经指向了【原 current】的下下个节点(next.next)
            prev, current = current, current.next
        return dummy.next


    """
解法2: 同样还可以用递归求解
    """
    def swapPairs_v2(self, head: ListNode) -> ListNode:
        # jy: 以 1->2->3->4 为例进行思考
        if not head or not head.next:
            return head
        # jy: 获取原头节点的下一个节点;
        h_next = head.next
        # jy: 调换后, 头节点的下一个节点为原头节点的下下个节点开始进行调换的结果;
        head.next = self.swapPairs_v2(h_next.next)
        # jy: 调换后, 原头节点的下一个节点的下一个节点为原头节点;
        h_next.next = head
        # jy: 调换后的头节点为原头节点的下一个节点;
        return h_next


ls1 = [1, 2, 3, 4, 5]
ln1 = getListNodeFromList(ls1)
print("ln1 ============: ")
showLnValue(ln1)

res_ln = Solution().swapPairs_v1(ln1)
print("res_ln ============: ")
showLnValue(res_ln)


ls1 = [1, 2, 3, 4]
ln1 = getListNodeFromList(ls1)
print("ln1 ============: ")
showLnValue(ln1)

res_ln = Solution().swapPairs_v2(ln1)
print("res_ln ============: ")
showLnValue(res_ln)


