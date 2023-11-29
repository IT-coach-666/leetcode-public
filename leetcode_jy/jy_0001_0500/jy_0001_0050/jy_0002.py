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
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Add-Two-Numbers(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = "链表 | 数值计算与进位"


"""
You are given two non-empty linked lists representing two
non-negative integers. 

The digits are stored in reverse order and each of their
nodes contain a single digit. Add the two numbers and
return it as a linked list.

You may assume the two numbers do not contain any leading
zero, except the number 0 itself.


Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
数值链表倒序存储, 最低位在链表头, 所以可以遍历两个链表, 将两个链表
同等位置结点上的值相加并与 10 做模运算, 得到的值即为新链表同等位置
结点的值 (如果相加后值大于等于 10, 则产生进位, 该进位需加到后两个
结点的和上)

循环两个链表之前创建一个 dummy 结点作为新链表的头, 和一个 prev 结
点用于记录当前节点的前一个节点, prev 初始指向 dummy

循环链表时, 将 prev 的 next 指针指向新建的结点, 随后更新 prev 为
prev.next, 当两个链表都循环完时, 有可能存在进位还没有处理的情况,
所以需要单独为进位生成一个链表结点, 最后返回 dummy.next
    """
    def addTwoNumbers(self, 
                      l1: ListNode, 
                      l2: ListNode) -> ListNode:
        current1, current2 = l1, l2
        # jy: 创建链表的头节点, 最终返回该头节点的下一个节点即
        #     为链接的第一个有效节点
        dummy = ListNode(-1)
        # jy: 记录当前节点的前一个节点(会随着计算过程不断变化)
        prev = dummy
        # jy: 记录是否产生进位
        carry = 0    

        # jy: 只要当前节点不为空, 就不断遍历
        while current1 or current2:
            # jy: sum 的初始值为进位值
            sum = carry
            # jy: 同时遍历两个链表相同位置的值(仅遍历非空节点部
            #     分), 并进行相加
            if current1:
                sum += current1.val
                current1 = current1.next
            if current2:
                sum += current2.val
                current2 = current2.next
            # jy: 取进位
            carry = sum // 10
            # jy: 取个位, 并创建节点, 随后将前一节点指向当前节点
            prev.next = ListNode(sum % 10)
            prev = prev.next

        # jy: 遍历所有节点后, 如果最终进位不为 0, 则基于进位再创
        #     建一个节点
        if carry != 0:
            prev.next = ListNode(carry)
        # jy: 返回链表头节点的下一个节点, 即为第一个有效节点
        return dummy.next


    """
不引入其它链表进行求解: 判断哪个链表长, 在长链表的基础上进行节点值
的修改, 最后返回
    """
    def addTwoNumbers_jy(self, 
                         l1: ListNode, 
                         l2: ListNode) -> ListNode:
        # jy: 初始进位为 0
        carry = 0
        # jy: 用 l1 记录更长的链表
        if getLen(l1) < getLen(l2):
            l1, l2 = l2, l1
        # jy: dummy 指向长链表表头
        dummy = l1
        
        # jy: 两链表的同等位置均有值时的相应操作 
        while l1 and l2:
            # jy: 结合进位和两链表同位置节点进行加和
            sum_ = l1.val + l2.val + carry
            # jy: 取余数即为相加后当前节点的值
            l1.val = sum_ % 10
            # jy: 取进位
            carry = sum_ // 10
            # jy: 两个链表的节点均向后移
            l1 = l1.next
            l2 = l2.next

        # jy: 长链表的剩下位置节点的操作优化点: 当此处 carry 已
        #     经为 0 (没有进位), 则不需要再有后续的操作, 可直接
        #     返回 dummy
        while l1 and carry:
            sum_ = l1.val + carry
            l1.val = sum_ % 10
            carry = sum_ // 10
            l1 = l1.next

        if carry:
            tail_node = getTailNode(dummy)
            tail_node.next = ListNode(carry)

        return dummy
        
            

ls1 = [2, 4, 3]
ls2 = [5, 6, 4]
# jy: 构造链表数据结构, 供测试使用
ln1 = getListNodeFromList(ls1)
ln2 = getListNodeFromList(ls2)
showLnValue(ln1, "ListNode1")
showLnValue(ln2, "ListNode2")
res = Solution().addTwoNumbers(ln1, ln2)
showLnValue(res, "ListNode1 + ListNode2")

res = Solution().addTwoNumbers_jy(ln1, ln2)
showLnValue(res, "ListNode1 + ListNode2")


print("=" * 50)

ls1 = [2, 4, 3]
ls2 = [5, 6, 8]
ln1 = getListNodeFromList(ls1)
ln2 = getListNodeFromList(ls2)
showLnValue(ln1, "ListNode1")
showLnValue(ln2, "ListNode2")
res = Solution().addTwoNumbers_jy(ln1, ln2)
showLnValue(res, "ListNode1 + ListNode2")


print("=" * 50)

ls1 = [2, 4, 3, 6]
ls2 = [5, 6, 8]
ln1 = getListNodeFromList(ls1)
ln2 = getListNodeFromList(ls2)
showLnValue(ln1, "ListNode1")
showLnValue(ln2, "ListNode2")
res = Solution().addTwoNumbers_jy(ln1, ln2)
showLnValue(res, "ListNode1 + ListNode2")

print("=" * 50)

ls1 = [2, 4, 3]
ls2 = [5, 6, 8, 6]
ln1 = getListNodeFromList(ls1)
ln2 = getListNodeFromList(ls2)
showLnValue(ln1, "ListNode1")
showLnValue(ln2, "ListNode2")
res = Solution().addTwoNumbers_jy(ln1, ln2)
showLnValue(res, "ListNode1 + ListNode2")


print("=" * 50)

ls1 = [2, 4, 3]
ls2 = [5, 6, 8, 9, 4]
ln1 = getListNodeFromList(ls1)
ln2 = getListNodeFromList(ls2)
showLnValue(ln1, "ListNode1")
showLnValue(ln2, "ListNode2")
res = Solution().addTwoNumbers_jy(ln1, ln2)
showLnValue(res, "ListNode1 + ListNode2")

