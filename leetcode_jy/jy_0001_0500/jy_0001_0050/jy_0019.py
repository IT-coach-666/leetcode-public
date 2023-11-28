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
title_jy = "Remove-Nth-Node-From-End-of-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = "循环迭代 | 快慢指针 | 递归（回溯时计算节点数）"


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
解法1: 循环迭代, 找到 length - n 个节点 (即倒数第 n 个节点的前一个节点), 修改该
该节点的下一个节点的指向即可
    """
    def removeNthFromEnd_v1(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head 

        # jy: 获取链表长度
        cur, length = head, 0 
        while cur:
            length += 1
            cur = cur.next 
        
        # jy: 找到倒数第 n 个节点的前一个节点 (即第 length - n 个节点)
        cur = dummy
        for _ in range(length - n):
            cur = cur.next
        
        # jy: 删除倒数第 n 个节点 (将倒数第 n 个节点的前一个节点的指向改为
        #     倒数第 n 个节点的下一节点)
        cur.next = cur.next.next
        return dummy.next 


    """
解法 2: 快慢指针, 找倒数第 n 个节点的前一个节点
    """
    def removeNthFromEnd_v2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head 
        
        # jy: 快指针先走 n 步
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next 

        # jy: 快慢指针同时走, 直到 fast 指针到达尾部节点, 此时 slow 指针到达
        #     倒数第 n 个节点的前一个节点
        while fast and fast.next:
            slow, fast = slow.next, fast.next 
        
        # jy: 删除倒数第 n 个节点 (将倒数第 n 个节点的前一个节点的指向改为
        #     倒数第 n 个节点的下一节点)
        slow.next = slow.next.next 
        return dummy.next 


    """
递归迭代: 递归迭代; 回溯时, 进行节点计数
    """
    def removeNthFromEnd_v3(self, head: ListNode, n: int) -> ListNode:
        if not head: 
            # jy: 递归至最深层时, self.count 初始化为 0
            self.count = 0
            return head  
        # jy: 递归调用
        head.next = self.removeNthFromEnd_v3(head.next, n)
        # jy: 回溯时进行节点计数 (递归至最深层时 self.count 会初始化为 0)
        self.count += 1
        # jy: 回溯到第 n 个节点时, 即为倒数第 n 个节点
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
res = Solution().removeNthFromEnd_v2(head, n)
# jy: []
showLnValue(res)


ls_ = [1,2]
n = 1
head = getListNodeFromList(ls_)
res = Solution().removeNthFromEnd_v3(head, n)
# jy: [1]
showLnValue(res)



