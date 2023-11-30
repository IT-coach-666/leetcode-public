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
title_jy = "Remove-Duplicates-from-Sorted-List-II(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving 
only distinct numbers from the original list.


Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
首先建立一个 dummy 结点和一个 prev 指针指向 dummy, 然后遍历链表, 判断当前结点和
后一个结点的值是否相同, 如果不同, 则将 prev 的 next 指针指向当前结点, 并将 prev 赋
值为当前结点; 如果相同, 则一直遍历链表直到遇到和当前结点的值不同的结点, 最后返
回 dummy.next;
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        # jy: prev 指针指向 dummy, current 指针指向 head;
        prev, current = dummy, head
        # jy: 遍历链表;
        while current:
            current_value = current.val
            # jy: 如果 current 有下一个元素, 且值与 current 相同, 则不断遍历, 直到
            #    找到与当前值不同的元素为止(即更新后的 current), 此时即忽略掉了有
            #    重复的元素; 随后在该值的基础上进一步以上的 while 循环;
            if current.next and current_value == current.next.val:
                while current and current.val == current_value:
                    current = current.next
            # jy: 如果 current 与 current.next 的值不同时, 即表明 current 在有序链
            #    表中没有出现重复, 此时将 prev 和 prev.next 指针指向该值; 随后将
            #    current 前进一步, 继续循环判断;
            else:
                prev.next, prev = current, current
                current = current.next
        # jy: 经过以上 while 循环后, 得到的 current 最终为 None; 如果链表结尾的 None 为
        #    非必须项, 则此处逻辑可去除;
        #prev.next = current
        return dummy.next

    """
找出待删除的元素, 随后遍历链表删除; 不如解法 1 ;
    """
    def deleteDuplicates_jy(self, head: ListNode) -> ListNode:
        current = head
        val_to_delete = []
        while current:
            if current.next and current.next.val == current.val:
                val_to_delete.append(current.val)
                while current and current.val == val_to_delete[-1]:
                    current = current.next
            else:
                current = current.next

        tmp = ListNode(None)
        dummy = tmp
        while head:
            if head.val not in val_to_delete:
                tmp.next = head
                tmp = tmp.next
            head = head.next
        tmp.next = head
            
        return dummy.next



ls_ = [1, 2, 3, 3, 4, 4, 5]
head_ = getListNodeFromList(ls_)
res = Solution().deleteDuplicates(head_)
# jy: 1->2->5
showLnValue(res)


ls_ = [1, 1, 1, 2, 3]
head_ = getListNodeFromList(ls_)
res = Solution().deleteDuplicates(head_)
# jy: 2->3
showLnValue(res)


print("=================【jy】===============")
ls_ = [1, 2, 3, 3, 4, 4, 5]
head_ = getListNodeFromList(ls_)
res = Solution().deleteDuplicates_jy(head_)
# jy: 1->2->5
showLnValue(res)


ls_ = [1, 1, 1, 2, 3]
head_ = getListNodeFromList(ls_)
res = Solution().deleteDuplicates_jy(head_)
# jy: 2->3
showLnValue(res)




