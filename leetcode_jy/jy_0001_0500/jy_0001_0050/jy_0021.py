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
title_jy = "Merge-Two-Sorted-Lists(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归（IMP, 思路新颖）"


"""
You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
图片参考: https://www.yuque.com/it-coach/leet-code/qcwgvkpfxr4ud00z

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both `list1` and `list2` are sorted in non-decreasing order.
"""

from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法 1: 递归, 时间复杂度: O(m+n)
判断 l1 和 l2 头结点哪个更小, 然后较小结点的 next 指针指向其余结点的合并结果
    """
    def mergeTwoLists_v1(self, l1: ListNode, l2: ListNode) -> ListNode:
        # jy: 如果传入的两个链表中有一个为空, 则返回另一个非空链表
        #     (递归的终止条件)
        if not l1: 
            return l2
        if not l2: 
            return l1
        # jy: 递归调用, 如果 l1 的当前节点更小, 则递归设置其下一节点后返回当
        #     前节点; 如果 l2 的当前节点更小, 则递归设置其下一节点后返回当前
        #     节点
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists_v1(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_v1(l1, l2.next)
            return l2

    """
解法 2: 逐个节点遍历判断, 并创建新节点进行拼接
    """
    def mergeTwoLists_v2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # jy: 创建哑节点作为结果链表的开头
        dummy = ListNode(0)
        # jy: 游标标识结果链表的结尾
        prev = dummy
        # jy: l1 和 l2 都未遍历结束
        while l1 and l2:
            # jy: 如果 l1 的数值比较小, 则把 l1 头部节点拼接到结果链表的结
            #     尾, 并将 l1 移至下一节点; 如果 l2 的数值比较小, 同理
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            # jy: 移动结果链表的结尾指针
            prev = prev.next
        # jy: 将 l1 或 l2 尚未使用完的部分拼接到结果链表的最后
        prev.next = l1 if l1 else l2
        # jy: 返回哑节点的下一个位置 (即结果链表的头节点)
        return dummy.next


ls1 = [1,2,4]
ls2 = [1,3,4]
list1 = getListNodeFromList(ls1)
list2 = getListNodeFromList(ls2)
res = Solution().mergeTwoLists_v1(list1, list2)
# jy: [1,1,2,3,4,4]
showLnValue(res)



ls1 = []
ls2 = []
list1 = getListNodeFromList(ls1)
list2 = getListNodeFromList(ls2)
res = Solution().mergeTwoLists_v1(list1, list2)
# jy: []
showLnValue(res)


ls1 = []
ls2 = [0]
list1 = getListNodeFromList(ls1)
list2 = getListNodeFromList(ls2)
res = Solution().mergeTwoLists_v2(list1, list2)
# jy: [0]
showLnValue(res)


