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
title_jy = "Intersection-of-Two-Linked-Lists(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists: begin to intersect at node c1.

图见: https://www.yuque.com/frederick/dtwi9g/vgpbfh



Example 1:   https://www.yuque.com/frederick/dtwi9g/vgpbfh
Input: intersectVal = 8, listA = [4, 1, 8, 4, 5], listB = [5, 0, 1, 8, 4, 5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the
                   two lists intersect). From the head of A, it reads as [4, 1, 8, 4, 5]. From
                   the head of B, it reads as [5, 0, 1, 8, 4, 5]. There are 2 nodes before the
                   intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:   https://www.yuque.com/frederick/dtwi9g/vgpbfh
Input: intersectVal = 2, listA = [0, 9, 1, 2, 4], listB = [3, 2, 4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists
                   intersect). From the head of A, it reads as [0, 9, 1, 2, 4]. From the head of B,
                   it reads as [3, 2, 4]. There are 3 nodes before the intersected node in A; There
                   are 1 node before the intersected node in B.


Example 3:   https://www.yuque.com/frederick/dtwi9g/vgpbfh
Input: intersectVal = 0, listA = [2, 6, 4], listB = [1, 5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2, 6, 4]. From the head of B, it reads as [1, 5].
                   Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB
                   can be arbitrary values.
Explanation: The two lists do not intersect, so return null.



Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法1: 找某个结点是否存在的问题可以使用 Map 或者 Set, 首先遍历 headA, 将所有的结点放入一个 Set 中, 然后遍
历 headB, 如果 headB 中的结点在 Set 中, 则表示找到了两个链表的相交的结点;
    """
    def getIntersectionNode_v1(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = set()
        current1, current2 = headA, headB

        while current1:
            nodes.add(current1)
            current1 = current1.next
        # print(nodes)
        while current2:
            if current2 in nodes:
                return current2
            current2 = current2.next

        return None

    """
解法2: 题目中最后写明了算法时间复杂度需要常量级, 所以不能使用 Set 保存结点; 这里巧妙的使用了两个指针分别
指向两个链表遍历, 如果其中一个链表遍历完成, 则将该指针指向另一个链表的开头再次遍历, 如果两个链表有交点, 则
最后两个指针会相等 (当是以 None 值相等条件下退出 while 循环时, 返回的 current1 也为 None, 符合题意);

证明如下: 如果两个链表存在交点, 当两个链表长度相等时, 两个指针同时遍历最后必然会相遇, 如果链表长度不相等, 分
别记为 L1 和 L2, 并假设 L1 < L2, 则第一个指针走完 L1 路程后, 第二个指针还剩下 L2 - L1 的路程; 此时第一个指
针开始从第二个链表遍历, 接着第二个指针走完 L2 - L1 路程后, 开始从第一个链表遍历, 此时第一个指针距离走完第二
个链表还有 L2 - (L2 - L1) = L1, 正好是第二个指针走完第一个链表的距离, 所以当两个指针继续走 L1 的路程后, 正好
各自走完了链表, 因此如果两个链表存在交点, 两个指针必然在中途相遇;
    """
    def getIntersectionNode_v2(self, headA: ListNode, headB: ListNode) -> ListNode:
        current1, current2 = headA, headB

        while current1 != current2:
            current1 = current1.next if current1 else headB
            current2 = current2.next if current2 else headA
        print(current1, " ====== ", current2)

        return current1

    """
解法3: 还可以先求出两个链表各自的长度, 如果两个链表长度不相等, 则长的链表指针先开始移动, 直到两个链表剩余的
路程长度相等, 接着两个链表同时开始遍历判断结点是否相等即可 (因为链表交点之后的部分肯定是等长的);
    """
    def getIntersectionNode_v3(self, headA: ListNode, headB: ListNode) -> ListNode:
        length_a = self._get_list_length(headA)
        length_b = self._get_list_length(headB)
        current1, current2 = headA, headB

        if length_a > length_b:
            for _ in range(length_a - length_b):
                current1 = current1.next
        else:
            for _ in range(length_b - length_a):
                current2 = current2.next

        while current1 and current2 and current1 != current2:
            current1 = current1.next
            current2 = current2.next

        return current1

    def _get_list_length(self, head: ListNode) -> int:
        length = 0

        while head:
            length += 1
            head = head.next

        return length

    def getIntersectionNode_v4(self, headA, headB):
        # 使用两个栈(后进先出),用来存放两个链表中的所偶遇节点
        stack1 = []
        stack2 = []

        # 加到栈中去
        while headA:
            stack1.append(headA)
            headA = headA.next
        while headB:
            stack2.append(headB)
            headB = headB.next
        # 存放第一个公共节点的
        node = None
        # 当两个栈不为空, 且最后1个节点相同, 则弹出继续往前找
        while stack1 and stack2 and stack1[-1] is stack2[-1]:
            # 用变量node记录下这个相同节点
            node = stack1.pop()
            stack2.pop()

        return node




"""
jy: 以下的输出结果均为 None, 不符合预期, 原因是链表中的 Node 不能判断是否相等 (可以依据 val 值判断是否相等? )
"""
listA = [4, 1, 8, 4, 5]
listB = [5, 0, 1, 8, 4, 5]
# jy: 以下参数值不需要使用到;
# skipA = 2
# skipB = 3
# intersectVal = 8
# Output: Reference of the node with value = 8
head_A = getListNodeFromList(listA)
head_B = getListNodeFromList(listB)
print(head_A.next.next == head_B.next.next.next)
res = Solution().getIntersectionNode_v1(headA=head_A, headB=head_B)
print(res)
# showLnValue(head_A)
# showLnValue(res)

listA = [0, 9, 1, 2, 4]
listB = [3, 2, 4]
# jy: 以下参数值不需要使用到;
# skipA = 3
# skipB = 1
# intersectVal = 2
# Output: Reference of the node with value = 2
head_A = getListNodeFromList(listA)
head_B = getListNodeFromList(listB)
res = Solution().getIntersectionNode_v2(headA=head_A, headB=head_B)
print(res)

listA = [2, 6, 4]
listB = [1, 5]
# jy: 以下参数值不需要使用到;
# skipA = 3
# skipB = 2
# intersectVal = 0
# Output: null
head_A = getListNodeFromList(listA)
head_B = getListNodeFromList(listB)
res = Solution().getIntersectionNode_v3(headA=head_A, headB=head_B)
print(res)
res = Solution().getIntersectionNode_v2(headA=head_A, headB=head_B)
print(res)

listA = [0, 9, 1, 2, 4]
listB = [3, 2, 4]
# jy: 以下参数值不需要使用到;
# skipA = 3
# skipB = 1
# intersectVal = 2
# Output: Reference of the node with value = 2
head_A = getListNodeFromList(listA)
head_B = getListNodeFromList(listB)
res = Solution().getIntersectionNode_v4(headA=head_A, headB=head_B)
print(res)



