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
title_jy = "Remove-Linked-List-Elements(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Remove all elements from a linked list of integers that have value val.


Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法1: 创建一个 dummy 节点指向 head, 初始化 prev 节点指向 dummy, current 节点指向 head, 遍
历链表, 如果当前节点的值不等于 val, 则移动 prev 至当前节点, 否则将 prev 的 next 指针指向当
前节点的下一个节点;
    """
    def removeElements_v1(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, next=head)
        prev, current = dummy, head

        while current:
            if current.val != val:
                prev = current
            # jy: 如果当前节点的值为待移除的目标值, 则将 prev 的下一个节点指向当前节点的下一个
            #    节点(本来 prev 的下一节点是指向当前节点的);
            else:
                prev.next = current.next
            current = current.next
        return dummy.next


    """
解法2: 解法 1 的递归版本
    """
    def removeElements_v2(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next


ls_ = [1, 2, 6, 3, 4, 5, 6]
val = 6
# Output: 1->2->3->4->5
ln1 = getListNodeFromList(ls_)
res = Solution().removeElements_v1(ln1, val)
showLnValue(res)


