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
title_jy = "Plus-One-Linked-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.


Example 1:
Input: head = [1, 2, 3]
Output: [1, 2, 4]

Example 2:
Input: head = [0]
Output: [1]


Constraints:
The number of nodes in the linked list is in the range [1, 100].
0 <= Node.val <= 9
The number represented by the linked list does not contain leading zeros except for the zero itself. 
"""

from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法1: 将链表先转成数组, 然后同 066_Plus-One.py 加 1 后再将数组转成链表;
    """
    def plusOne_v1(self, head: ListNode) -> ListNode:
        digits = []
        current = head
        # jy: 将链表转换为数组 digits
        while current:
            digits.append(current.val)
            current = current.next
        # jy: 对数组所代表的数值进行加 1 操作;
        digits = self._plus_one(digits)
        # jy: 构建完新数组后, 依据数组构建链表;
        dummy = ListNode(-1)
        prev = dummy
        for n in digits:
            current = ListNode(n)
            prev.next, prev = current, current

        return dummy.next


    def _plus_one(self, digits):
        """ 066_Plus-One.py: 对数组所代表的数值进行加 1 操作"""
        if not digits:
            return []

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits



    """
解法2: 遍历链表定位到最后一个不为 9 的节点, 将该节点值加 1:
1) 如果该节点后没有其他节点, 则此时的链表就是加 1 后的链表
2) 如果该节点后还有其他节点, 说明剩余节点的值都是 9, 将这些节点的值都置为 0;
    """
    def plusOne_v2(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        # jy: last_not_9 记录最后一个不为 0 的节点, 初始化为 dummy 节点(值为 0);
        last_not_9 = dummy
        dummy.next = head
        current = head
        # jy: 定位到最后一个不为 9 的节点;
        while current:
            if current.val != 9:
                last_not_9 = current

            current = current.next
        # jy: 无论如何, 最后一个不为 9 的节点肯定是需要加 1 的, 且加 1 后不会进位;
        last_not_9.val += 1

        # jy: 将 current 定位到 last_not_9 的下一个节点, 如果该节点存在, 则该节点及其之后的节点
        #    均需要被置为 0;
        current = last_not_9.next
        while current:
            current.val = 0
            current = current.next
        # jy: 如果 dummy 对应的节点值为 1(表明链表中没找到最后一个值为非 9 的节点, 即原链表中的
        #    值均为 9)
        return dummy if dummy.val == 1 else head


ls_ = [1, 2, 3]
# Output: [1, 2, 4]
head_ = getListNodeFromList(ls_)
res = Solution().plusOne_v1(head_)
print(res.val, res.next.val, res.next.next.val)

ls_ = [0]
# Output: [1]
head_ = getListNodeFromList(ls_)
res = Solution().plusOne_v1(head_)
print(res.val)


