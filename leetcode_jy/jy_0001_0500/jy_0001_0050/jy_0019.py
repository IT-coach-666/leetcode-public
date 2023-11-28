# M19. Remove Nth Node From End of List
# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
from typing import List, Dict
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Remove-Nth-Node-From-End-of-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the `head` of a linked list, remove the `n-th` node from the end of the
list and return its head.

 

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
图形参考: https://www.yuque.com/it-coach/leet-code/fmdkpgptegrz8ge6

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:
The number of nodes in the list is `sz`.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""

from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法1: 循环迭代 -- 找到 length -n 个节点
    """
    def removeNthFromEnd_v1(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head 

        #step1: 获取链表长度
        cur, length = head, 0 
        while cur:
            length += 1
            cur = cur.next 
        
        #step2: 找到倒数第N个节点的前面一个节点
        cur = dummy
        for _ in range(length - n):
            cur = cur.next
        
        #step3: 删除节点，并重新连接
        cur.next = cur.next.next
        return dummy.next 


    """
解法 2: 快慢指针 -- 找倒数第N个节点的前一个节点
    """
    def removeNthFromEnd_v2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head 
        
        #step1: 快指针先走n步
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next 

        #step2: 快慢指针同时走，直到fast指针到达尾部节点，此时slow到达倒数第N个节点的前一个节点
        while fast and fast.next:
            slow, fast = slow.next, fast.next 
        
        #step3: 删除节点，并重新连接
        slow.next = slow.next.next 
        return dummy.next 


    """
递归迭代: 递归迭代 -- 回溯时，进行节点计数
    """
    def removeNthFromEnd_v3(self, head: ListNode, n: int) -> ListNode:
        if not head: 
            self.count = 0
            return head  
        head.next = self.removeNthFromEnd(head.next, n) # 递归调用
        self.count += 1 # 回溯时进行节点计数
        return head.next if self.count == n else head 


ls_ = [1, 2, 3, 4, 5]
n = 2
head = getListNodeFromList(ls_)
res = Solution().removeNthFromEnd_v1(head, n)
# jy: [1,2,3,5]
showLnValue(res)


ls_ = [1]
n = 1
head = getListNodeFromList(ls_)
res = Solution().removeNthFromEnd_v1(head, n)
# jy: []
showLnValue(res)


ls_ = [1,2]
n = 1
head = getListNodeFromList(ls_)
res = Solution().removeNthFromEnd_v1(head, n)
# jy: [1]
showLnValue(res)



