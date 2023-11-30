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
title_jy = "Reverse-Linked-List-II(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.


Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法1: 206_reverse-linked-list.py 的变种, 整个链表反转后将分为三部分, 反转链表的前置链
表, 反转的链表, 反转链表的后置链表; 当链表反转完成后, 进行拼接: 将前置链表的最后一个结
点的 next 指针指向反转链表的头结点, 同时将反转链表的尾结点的 next 指针指向后置链表的头
结点; 而反转链表的操作同 206_reverse-linked-list.py, 最后返回的时候需要判断前置链表是否
存在, 如果存在则返回原链表的头结点, 如果不存在则返回反转链表的头结点;
    """
    def reverseBetween_v1(self, head: ListNode, m: int, n: int) -> ListNode:
        # jy: 原链表的头节点;
        old_head = head
        # jy: current 最开始指向头节点;
        prev, current = None, head
        # jy: tail_of_left 记录前置链表的末尾, tail_of_reverse_list 记录反转链表的末尾;
        tail_of_left, tail_of_reverse_list = None, None
        # jy: 不断循环遍历链表的前 n 个节点, 对第 m 个节点开始的链表进行反转;
        for i in range(1, n+1):
            # jy: 找出前置链表的末尾; 此时的 current 对应待反转链表的第一个节点;
            if i < m:
                tail_of_left, current = current, current.next
            # jy: 以下以 [1, 2, 3, 4, 5], m=2, n=4 为例进行思考
            # jy: 当遍历到第 m 个节点时, 此时的 current 为待反转链表的第一个节点, 此时将
            #    tail_of_reverse_list 指向该节点(即待反转链表的第一个节点为反转后的最后一节点);
            elif i >= m:
                if i == m:
                    tail_of_reverse_list = current
                # jy: prev 最开始为 None, 当第一次循环时, current 为待反转链表的第一个节点, 即反
                #    转后的链表的最后一个节点; 将当前节点的 next 值置为 prev(最开始为 None, 随后
                #    总是等于上一个节点), 即总是将当前节点的下一个节点指向上一个节点, 使得链表不
                #    断反转; 
                next, current.next = current.next, prev
                # jy: 将 prev 置为 current, current 置为其下一个节点(必须通过引入中间变量 next 来指
                #    定, 因为原先的 current.next 已经在上一步做了重新赋值), 不断的循环反转下去;
                prev, current = current, next
        # jy: 经过以上循环后, prev 指向反转链表的第一个节点, current 指向后置链表的第一个节点;
        # jy: 如果前置链表不为空(前置链表的末尾节点存在), 则将其末尾节点的 next 指向反转后的首
        #    节点), 并将反转链表的末尾节点执行后置链表的第一个节点;
        if tail_of_left:
            tail_of_left.next = prev
        tail_of_reverse_list.next = current
        # jy: 如果前置链表存在(前置链表的末尾节点存在), 则返回原先的头节点; 如果不存在, 则返回
        #    反转链表的首节点;
        return old_head if tail_of_left else prev


    """
解法2: 解法 1 使用了过多的变量和分支; 消除过多变量的第一步是引入 dummy 结点, 将其 next 指针指
向 head, 这样最后返回头结点时只需要返回 dummy.next 即可, 无需引入 old_head 变量; 第二步是将解
法 1 中的循环拆分为两部分, 第一部分是求 tail_of_left 和 tail_of_reverse_list, 第二部分才是链
表的倒转, 链表的倒转同解法 1;
    """
    def reverseBetween_v2(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        tail_of_left = dummy
        # jy: 求 tail_of_left, 即前置链表的末尾;
        for i in range(m-1):
            tail_of_left = tail_of_left.next
        # jy: 求 tail_of_reverse_list, 即反转链表的末尾, 即待反转链表的第一个节点;
        tail_of_reverse_list = tail_of_left.next
        # jy: 将 prev 初始化为 None, current 初始化为待反转链表的首节点;
        prev, current = None, tail_of_left.next

        # jy: 对 m 到 n 位置的节点进行反转: 将当前节点的 next 指向前一节点, 随后将前一节点指向
        #    当前节点, 完成对当前节点的反转, 并更新当前节点为当前节点的下一个, 随后不断循环遍
        #    历节点, 进行反转;
        for i in range(m, n+1):
            next, current.next = current.next, prev
            prev, current = current, next

        # jy: 经过以上循环后, prev 指向反转链表的首节点, current 指向后置链表的首节点; 以下将
        #    反转链表的末尾节点的下一节点指向后置链表的首节点, 将前置链表的末尾指向反转链表的
        #    首节点;
        tail_of_reverse_list.next = current
        tail_of_left.next = prev
        return dummy.next



    """
解法3: 与解法 2 的区别在于反转链表的方法不同; 对于一段链表 abcd 来说, 反转的操作
为(需操作的次数为(链表长度-1)次):
1. 将 b 移动到 a 前面, 得到链表 bacd 
2. 将 c 移动到 b 前面, 得到链表 cbad 
3. 将 d 移动到 c 前面, 得到链表 dcba 
我们记 a 为 tail_of_reverse_list(即反转链表的末尾节点), 在每一轮的操作中, 由于要
将 tail_of_reverse_list 的后一个结点移动到反转链表的开头, 所以将 tail_of_reverse_list 
的 next 指针指向 tail_of_reverse_list.next.next, 也就是 tail_of_reverse_list 的后一个
结点的后一个结点, 之后将后一个结点的 next 指针指向当前反转链表的头结点(tail_of_left.next), 
作为新的头结点, 最后更新 tail_of_left.next 为新的反转链表的头结点;
    """
    def reverseBetween_v3(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        # jy: tail_of_left 最开始指向 head 的前一个节点;
        tail_of_left = dummy
        # jy: 经过 m-1 次循环, tail_of_left 指向第 m-1 个节点, 即前置链表的末尾节点;
        for i in range(m-1):
            tail_of_left = tail_of_left.next
        # jy: 获取反转链表的末尾节点(即待反转链表的首节点)
        tail_of_reverse_list = tail_of_left.next

        # jy: 从第 m 个节点开始遍历, 遍历到第 n-1 个节点(共 n-m 个节点), 实现对 m 到 n 节点
        #    的反转; 参考 abcd 的反转对应的操作, 需要的操作次数为 (待反转链表长度-1) 次, 即
        #    操作 n-m 次;
        for i in range(m, n):
            # jy: 第一次循环时, tail_of_reverse_list 为待反转链表的首节点(即反转链表的末尾节
            #    点); 此处获取其下一节点; 随后将该节点拼接到前置链表的末尾节点的下一个;
            next = tail_of_reverse_list.next
            # jy: 将反转链表的末尾节点的下一个节点设置为其下下个节点, 因为下一个即将被反转到
            #    前面(经过一次反转操作后, tail_of_reverse_list 的下一个节点即为其原先的下下
            #    个节点)
            tail_of_reverse_list.next = next.next
            # jy: 将原 tail_of_reverse_list 的下一个拼接到前置链表的末尾节点的 next, 并将拼接
            #    过去的节点的 next 指向原 tail_of_left 的 next 节点; 即在原 tail_of_left 与
            #    原 tail_of_left.next 中间插入一个节点;
            next.next, tail_of_left.next = tail_of_left.next, next
        # jy: 以上循环结束后, tail_of_reverse_list.next 即指向后置链表的首节点, 此时 m 到 n 节
        #    点已实现反转, 并正确拼接, 最后返回原头节点即可;
        return dummy.next



ls1 = [1, 2, 3, 4, 5]
ln1 = getListNodeFromList(ls1)
showLnValue(ln1, "ListNode1")

m, n = 2, 4
res_ln = Solution().reverseBetween_v1(ln1, m, n)
showLnValue(res_ln, "res_ln")


ls1 = [1, 2, 3, 4, 5]
ln1 = getListNodeFromList(ls1)
res_ln = Solution().reverseBetween_v2(ln1, m, n)
showLnValue(res_ln, "res_ln")


ls1 = [1, 2, 3, 4, 5]
ln1 = getListNodeFromList(ls1)
res_ln = Solution().reverseBetween_v3(ln1, m, n)
showLnValue(res_ln, "res_ln")



