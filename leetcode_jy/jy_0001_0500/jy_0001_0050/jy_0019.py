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
        
        # jy: 快慢指针初始化为哑节点
        slow, fast = dummy, dummy
        # jy: 快指针先走 n 步, 到达第 n 个节点
        for _ in range(n):
            fast = fast.next 

        # jy: 快慢指针同时走, 直到 fast 指针到达尾部节点, 此时 slow 指针到
        #     达倒数第 n 个节点的前一个节点
        while fast and fast.next:
            slow, fast = slow.next, fast.next 
        
        # jy: 删除倒数第 n 个节点 (将倒数第 n 个节点的前一个节点的指向改为
        #     倒数第 n 个节点的下一节点)
        slow.next = slow.next.next 
        return dummy.next 


    """
解法3: 双指针法, 同解法 2 , 但不引入哑节点

需有一个变量记录原链表的长度, 好判断最终返回的是头节点还是头节点的下一节点
    """
    def removeNthFromEnd_v3(self, head: ListNode, n: int) -> ListNode:
        # jy: 快慢指针初始化为头节点 (即第 1 个节点), step 记录 fast 指针当前
        #     处于第几个节点
        slow, fast = head, head
        step = 1
        while fast.next:
            step += 1
            # jy: step 为 2 时, fast 指针已经移动到第 2 个节点
            fast = fast.next
            # jy: 当 step 为 n+2 时, fast 已经在第 n+2 个节点; 此时 slow 开始
            #     移动, slow 指针指向第 2 个节点, 即 slow 指针比 fast 指针少
            #     移动 n 个节点, 当 fast 指针移动到末尾时(即倒数第 1 个节点),
            #     show 指针为倒数第 n+1 个节点
            if step > n + 1:
                slow = slow.next

        # jy: step 也即统计链表中的节点数, 如果 n == step, 表明倒数第 n 个节
        #     点即为头节点, 即表明删除的是头节点, 直接返回头节点的下一节点即可
        if step == n:
            return head.next

        # jy: 此时的 slow 指针位于倒数第 n+1 个节点, 删除第 n 个节点即跳过该节点
        slow.next = slow.next.next
        return head


    """
递归迭代: 递归迭代; 回溯时, 进行节点计数
    """
    def removeNthFromEnd_v4(self, head: ListNode, n: int) -> ListNode:
        if not head: 
            # jy: 递归至最深层时, self.count 初始化为 0
            self.count = 0
            return head  
        # jy: 递归调用
        head.next = self.removeNthFromEnd_v4(head.next, n)
        # jy: 回溯时进行节点计数 (递归至最深层时 self.count 会初始化为 0)
        self.count += 1
        # jy: 回溯到第 n 个节点时, 即为倒数第 n 个节点
        return head.next if self.count == n else head 


    """
解法 5: 基于字典和链表长度信息进行处理, 额外增加空间复杂度

遍历链表, 将链表中的第 i 个结点按 key 为 i, value 为节点的形式放入字典中,
字典初始值为 {0: dummy 节点}, 其中 dummy 节点的 next 指针指向头结点; 链表
遍历完成后, 字典中的总节点数为原链表节点数加 1, 需要删除的节点的 key 为
`len(mapping) - n`, 删除该结点的操作等价于将序号为 `size(mapping) - n - 1`
的结点的 next 指针指向序号为 `size(mapping) - n + 1` 的结点

注意: 如果 `size(Map) - n + 1` 节点不存在, 则将其值设置为 None

最终返回 dummy.next 即可
    """
    def removeNthFromEnd_v5(self, head: ListNode, n: int) -> ListNode:
        current = head
        dummy = ListNode(-1)
        dummy.next = head
        i, mapping = 0, {0: dummy}
        while current:
            i += 1
            mapping[i] = current
            current = current.next
        index_to_delete = len(mapping) - n
        mapping[index_to_delete - 1].next = mapping.get(index_to_delete + 1, None)
        return dummy.next

    """
解法 6: 同解法 5, 但不需要使用 dummy 节点
    """
    def removeNthFromEnd_v6(self, head: ListNode, n: int) -> ListNode:
        current = head
        # jy: 第 1 个节点对应的 key 为 0, 第 len_ 个节点(即倒数第 1 个节点) 对
        #     应的 key 为 len_ - 1; 倒数第 n 个节点对应的 key 为 len_ - n
        i, mapping = 0, {}
        while current:
            mapping[i] = current
            current = current.next
            i += 1
        # jy: 即倒数第 n 个节点在字典中的下标
        index_to_delete = len(mapping) - n
        # jy: 如果待删除的节点在字典中的下标为 0, 表明要删除头节点, 直接返回头
        #     节点的下一节点即可
        if index_to_delete == 0:
            return head.next
        # jy: 如果不是头节点, 则将待删除的节点的前一节点的下一节点指向待删除的
        #     节点的下一节点
        mapping[index_to_delete - 1].next = mapping.get(index_to_delete + 1, None)
        return head




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



ls_ = [1,2]
n = 1
head = getListNodeFromList(ls_)
res = Solution().removeNthFromEnd_v4(head, n)
# jy: [1]
showLnValue(res)


