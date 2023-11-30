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
tag_jy = "链表反转技巧 | 相关题型: 0025、0206"



"""
Reverse a linked list from position `m` to `n`. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.


Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法1: 0206 (reverse-linked-list) 的变种, 整个链表反转后将分为三部分: 前置链
表、反转的链表、后置链表; 当链表反转完成后进行拼接即可 

将前置链表的最后一个结点的下一节点作为反转链表的头结点, 同时将反转的链表的尾
结点的下一节点作为后置链表的头结点; 而反转链表的操作同 0206 (reverse-linked-list),
最后返回时需判断前置链表是否存在, 如果存在则返回原链表的头结点, 如果不存在则
返回反转链表的头结点
    """
    def reverseBetween_v1(self, head: ListNode, m: int, n: int) -> ListNode:
        # jy: 原链表的头节点
        old_head = head
        # jy: current 最开始指向头节点
        prev, current = None, head
        # jy: left_tail 记录前置链表的末尾节点, reverse_list_tail 记录反转链
        #     表的末尾节点
        left_tail, reverse_list_tail = None, None
        # jy: 不断循环遍历链表的前 n 个节点, 并从第 m 个节点开始的部分进行反转
        for i in range(1, n+1):
            # jy: 找出前置链表的末尾节点, 到末尾节点时, current 对应待反转链表
            #     的第一个节点
            if i < m:
                left_tail, current = current, current.next
            # jy: 以 1->2->3->4->5, m=2, n=4 为例进行思考
            elif i >= m:
                # jy: 当遍历到第 m 个节点时, 此时的 current 为待反转链表的第一
                #     个节点, 用 reverse_list_tail 指向该节点, 表示反转后的最
                #     后一个节点
                if i == m:
                    reverse_list_tail = current
                # jy: prev 最开始为 None, 第一轮循环时 current 为待反转链表的第
                #     一个节点 (即反转后的链表的最后一个节点); 先暂存当前节点的
                #     下一节点 cur_next, 随后将当前节点的下一节点更新为 prev, 即
                #     反转当前节点的指向, 并更新 prev 为当前节点, current 为
                #     cur_next, 从而进行下一轮节点的反转
                cur_next, current.next = current.next, prev
                prev, current = current, cur_next
        # jy: 经过以上循环后, prev 指向反转链表的第一个节点, current 指向后置链
        #     表的第一个节点; 如果前置链表不为空 (前置链表的末尾节点存在), 则将
        #     其末尾节点的 next 指向反转后的首节点), 并将反转链表的末尾节点指向
        #     后置链表的第一个节点
        if left_tail:
            left_tail.next = prev
        reverse_list_tail.next = current
        # jy: 如果前置链表存在 (前置链表的末尾节点存在), 则返回原先的头节点; 如
        #     果不存在, 则返回反转链表的首节点
        return old_head if left_tail else prev


    """
解法2: 引入 dummy 结点, 消除解法 1 中过多的变量和分支

1) 将 dummy 的下一节点指向 head, 最后只需要返回 dummy.next 即可 (避免额外引入
   old_head 变量)
2) 将解法 1 中的循环拆分为两部分:
   a) 求 left_tail 和 reverse_list_tail
   b) 链表的倒转
    """
    def reverseBetween_v2(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        left_tail = dummy
        # jy: 求前置链表的末尾节点 left_tail (循环移动 m-1 次后, 来到了
        #     第 m-1 个节点)
        for i in range(m-1):
            left_tail = left_tail.next

        # jy: reverse_list_tail 为反转链表的末尾节点 (即待反转链表的第一个节点)
        reverse_list_tail = left_tail.next

        # jy: 将 prev 初始化为 None, current 初始化为待反转链表的首节点 (即第
        #     m 个节点)
        prev, current = None, left_tail.next

        # jy: 对 m 到 n 位置的节点进行反转(第一轮循环时当前节点 current 即为
        #     第 m 个节点): 暂存当前节点的下一节点 cur_next, 并更新当前节点的
        #     下一节点为 prev (即反转当前节点), 随后将 prev 设置为当前节点, 将
        #     current 设置为 cur_next, 开始下一轮反转
        for i in range(m, n+1):
            cur_next, current.next = current.next, prev
            prev, current = current, cur_next

        # jy: 经过以上循环后, prev 为反转链表的首节点, current 为后置链表的首
        #     节点; 将反转链表的末尾节点的下一节点指向后置链表的首节点, 将前
        #     置链表的末尾指向反转链表的首节点, 就完成了整个反转过程
        reverse_list_tail.next = current
        left_tail.next = prev
        return dummy.next


    """
解法 3: 与解法 2 的区别在于反转链表的方法不同; 对于一段链表 abcd 来说, 反转的
操作为 (需操作的次数为 `链表长度 - 1` 次):
1) 将 b 移动到 a 前面, 得到链表 bacd 
2) 将 c 移动到 b 前面, 得到链表 cbad 
3) 将 d 移动到 c 前面, 得到链表 dcba 
记 a 为 reverse_list_tail (即反转链表的末尾节点), 在每一轮的操作中, 由于要
将 reverse_list_tail 的后一个结点移动到反转链表的开头, 所以将 reverse_list_tail
的 next 指针指向 reverse_list_tail.next.next, 之后将后一个结点的 next 指针
指向当前反转链表的头结点(left_tail.next), 作为新的头结点, 最后更新 
left_tail.next 为新的反转链表的头结点
    """
    def reverseBetween_v3(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        # jy: left_tail 最开始指向 head 的前一个节点
        left_tail = dummy
        # jy: 经过 m-1 次循环, left_tail 指向第 m-1 个节点 (即前置链表的末尾节点)
        for i in range(m-1):
            left_tail = left_tail.next
        # jy: 获取反转链表的末尾节点(即待反转链表的首节点)
        reverse_list_tail = left_tail.next

        # jy: 从第 m 个节点开始遍历, 遍历到第 n-1 个节点(共 n-m 个节点), 实现
        #     对 m 到 n 节点的反转; 参考 abcd 的反转对应的操作, 需要的操作次数
        #     为 `待反转链表长度 - 1` 次, 即操作 `n - m` 次
        # jy: 以 leftTail->a->b->c->d 为例进行思考:
        #     第一轮循环: leftTail->b->a->c->d 
        #     第二轮循环: leftTail->c->b->a->d
        #     第三轮循环: leftTail->d->c->b->a
        for i in range(m, n):
            # jy: 第一次循环时, reverse_list_tail 为待反转链表的首节点 (即反转
            #     后的链表的末尾节点); 此处获取其下一节点 (后续会将前置链表的
            #     末尾节点的下一节点设置为该节点)
            cur_next = reverse_list_tail.next
            # jy: 将反转链表的末尾节点的下一节点设置为其下下个节点, 下一轮循环
            #     时该节点将被反转到前面 (经过一次反转操作后, reverse_list_tail
            #     的下一个节点即为其原先的下下个节点)
            reverse_list_tail.next = cur_next.next
            # jy: 将 cur_next (当前节点的下一节点) 的下一节点设置为
            #     left_tail.next (即第 m 个节点), 并将 left_tail.next (前置链
            #     表末尾节点的下一节点) 设置为 cur_next (当前节点的下一节点),
            #     以此实现当前节点与下一节点的反转
            # jy: 该过程不改变 reverse_list_tail, 只改变其指向的下一节点, 使得
            #     后续循环时不断反转 reverse_list_tail 以及其下一节点, 最终实现
            #     链表的反转
            cur_next.next, left_tail.next = left_tail.next, cur_next
        # jy: 以上循环结束后, reverse_list_tail.next 即指向后置链表的首节点, 此
        #     时 m 到 n 节点已实现反转, 并正确拼接, 最后返回原头节点即可
        return dummy.next


m, n = 2, 4

ls1 = [1, 2, 3, 4, 5]
ln1 = getListNodeFromList(ls1)
showLnValue(ln1, "反转前的链表(m=%s, n=%s)" % (m, n))
res_ln = Solution().reverseBetween_v1(ln1, m, n)
showLnValue(res_ln, "res_ln")


ls1 = [1, 2, 3, 4, 5]
ln1 = getListNodeFromList(ls1)
showLnValue(ln1, "反转前的链表(m=%s, n=%s)" % (m, n))
res_ln = Solution().reverseBetween_v2(ln1, m, n)
showLnValue(res_ln, "res_ln")


ls1 = [1, 2, 3, 4, 5]
ln1 = getListNodeFromList(ls1)
showLnValue(ln1, "反转前的链表(m=%s, n=%s)" % (m, n))
res_ln = Solution().reverseBetween_v3(ln1, m, n)
showLnValue(res_ln, "res_ln")



