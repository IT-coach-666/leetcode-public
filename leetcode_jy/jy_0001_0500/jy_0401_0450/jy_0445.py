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
title_jy = "Add-Two-Numbers-II(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7


Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
"""

from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
这道题和 002_Add-Two-Numbers.py 相反, 数字在链表中是正序存储, 最高位在链表头, 所以
不能直接遍历两个链表相加;

一种方法是先将两个链表反转, 这样就将这道题变成了 002_Add-Two-Numbers.py; 由于链表是
反转后进行加和, 故在计算反转链表当前位置加和后, 将加和结果不断从后往前放置;

在循环链表前, 新建一个 prev 结点指向空, 循环链表时, 将新结点的 next 指针指向 prev ,
然后将 prev 更新为新结点(即 prev 总是指向当前链表的头节点);
    """
    def addTwoNumbers_v1(self, l1: ListNode, l2: ListNode) -> ListNode:
        # jy: 对链表进行反转;
        current1, current2 = self._reverse_list(l1), self._reverse_list(l2)
        prev = None
        carry = 0

        while current1 or current2:
            sum = carry
            # jy: 当 current1 和 current2 都存在时, 则加上对应位置的值后均递进一位;
            if current1:
                sum += current1.val
                current1 = current1.next
            if current2:
                sum += current2.val
                current2 = current2.next

            carry = sum // 10
            new = ListNode(sum % 10)
            # jy: 将当前节点的 next 指向 prev 节点, 随后 prev 指向当前节点(总是保证在新链
            #    表的最左端);
            new.next, prev = prev, new

        if carry != 0:
            new = ListNode(carry)
            new.next, prev = prev, new

        return prev

    def _reverse_list(self, head: ListNode) -> ListNode:
        """反转链表"""
        # jy: 初始化 prev 为 None, current 为头结点;
        prev, current = None, head
        # jy: 不断将遍历得到的节点置于 prev 前, 同时 prev 总是移动至最前面的节点(第一个节点)
        while current:
            # jy: version-1 =======================================
            '''
            next, current.next = current.next, prev
            prev, current = current, next
            '''
            # jy: version-2 =======================================
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev


    """
解法 1 改变了输入的列表, 而题目中最后要求不允许改变原来的链表;
一种巧妙的解法是使用栈, 首先遍历链表, 将结点的值放入栈中, 遍历完成后栈顶就是链表所
表示数字的最低位, 然后两个栈依次执行出栈相加操作, 此时解问题又回到了 002_Add-Two-Numbers.py;
    """
    def addTwoNumbers_v2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # jy: 将链表节点入栈(栈顶即为最小位对应的值);
        stack1, stack2 = self._convert_list_to_stack(l1), self._convert_list_to_stack(l2)
        prev = None
        carry = 0

        while stack1 or stack2:
            sum = carry
            if stack1:
                sum += stack1.pop()
            if stack2:
                sum += stack2.pop()

            carry = sum // 10
            new = ListNode(sum % 10)
            new.next, prev = prev, new

        if carry != 0:
            new = ListNode(carry)
            new.next, prev = prev, new

        return prev

    def _convert_list_to_stack(self, head: ListNode) -> List[int]:
        """将链表节点入栈"""
        stack, current = [], head
        while current:
            stack.append(current.val)
            current = current.next
        return stack

    """
解法3: 首先算出两个链表所代表的数的和, 然后将这个和的每一位转换为最终链表的结点;
    """
    def addTwoNumbers_v3(self, l1: ListNode, l2: ListNode) -> ListNode:
        # jy: 将链表代表的数值进行真正的加和;
        sum = self._get_list_sum(l1) + self._get_list_sum(l2)

        # jy: version-1-Begin ==========================================================
        '''
        # jy: 将数值转为字符串形式;
        numbers = list(str(sum))
        # jy: 逐个遍历数值字符串, 将其转为整数形式后构造链表节点不断往后连接构成链表;
        dummy = ListNode(-1)
        prev = dummy
        for n in numbers:
            new = ListNode(int(n))
            prev.next, prev = new, new
        '''
        # jy: version-1-End =============================================================
        # jy: version-2-Begin ==========================================================

        # jy: 规避特殊情况(ls1=[0] 且 ls2=[0] 时)-方式-1
        # if sum == 0:
        #     return ListNode(0)

        prev = None
        while sum != 0:
            new = ListNode(sum % 10)
            new.next, prev = prev, new
            sum = sum // 10

        # jy: 规避特殊情况(ls1=[0] 且 ls2=[0] 时)-方式-2
        if prev is None:
            return ListNode(0)

        return prev
        # jy: version-2-End =============================================================

        return dummy.next


    def _get_list_sum(self, head: ListNode) -> int:
        """将链表代表的数值转换为真正的整数形式"""
        sum, current = 0, head
        while current:
            sum = sum * 10 + current.val
            current = current.next
        return sum


ls1 = [7, 2, 4, 3]
ls2 = [5, 6, 4]
# (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
head_1 = getListNodeFromList(ls1)
head_2 = getListNodeFromList(ls2)
res = Solution().addTwoNumbers_v1(head_1, head_2)
showLnValue(res)


ls1 = [7, 2, 4, 3]
ls2 = [5, 6, 4]
# (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
head_1 = getListNodeFromList(ls1)
head_2 = getListNodeFromList(ls2)
res = Solution().addTwoNumbers_v2(head_1, head_2)
showLnValue(res)


ls1 = [7, 2, 4, 3]
ls2 = [5, 6, 4]
# (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
head_1 = getListNodeFromList(ls1)
head_2 = getListNodeFromList(ls2)
res = Solution().addTwoNumbers_v3(head_1, head_2)
showLnValue(res)


