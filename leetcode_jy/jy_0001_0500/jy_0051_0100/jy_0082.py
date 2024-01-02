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
tag_jy = "去除所有存在重复的节点的技巧 | 相似题: 0083 | IMP"



"""
Given the `head` of a sorted linked list, delete all nodes that have duplicate
numbers, leaving only distinct numbers from the original list. Return the 
linked list sorted as well.


Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3


Constraints:
1) The number of nodes in the list is in the range [0, 300].
2) -100 <= Node.val <= 100
3) The list is guaranteed to be sorted in ascending order.
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法 1: 去除所有存在重复的节点

1) prev 指针指向一个新建的 dummy 结点, 表示当前节点的前一个节点
2) 遍历链表, 先记得当前节点的值, 并判断当前结点的后一个结点的值是否与最初记
   录的值相同:
   a) 如果相同, 则不断将当前节点移动到下一个不相同的节点 (即删除了重复出现的
      节点), 随后进入下一轮循环
   b) 如果不同, 则将该节点记录到 prev.next, 随后更新 prev 和当前节点, 继续下
      轮循环
    """
    def deleteDuplicates_v1(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        # jy: prev 指针指向 dummy, current 指针指向 head
        prev, current = dummy, head
        # jy: 遍历链表
        while current:
            # jy: 记录当前节点的数值, 如果当前节点的下一个节点存在且值等于当
            #     前节点的值, 则不断将当前节点后移, 直到为新值为止 (即已经跳
            #     过出现重复值的节点), 随后进入下一轮循环
            current_value = current.val
            if current.next and current_value == current.next.val:
                while current and current.val == current_value:
                    current = current.next
            # jy: 如果当前节点的下一个节点已经不存在, 或虽然存在, 但下一个节
            #     点的值与当前节点的值不相等, 则将当前节点赋值给 prev.next, 随
            #     后更新 prev 节点和当前节点, 进入下一轮遍历
            else:
                prev.next, prev = current, current
                current = current.next
        # jy: 经过以上 while 循环后, 得到的 current 最终为 None; 如果链表结尾
        #     的 None 为非必须项, 则此处逻辑可去除
        #prev.next = current
        return dummy.next



ls_ = [1, 2, 3, 3, 4, 4, 5]
head_ = getListNodeFromList(ls_)
res = Solution().deleteDuplicates_v1(head_)
# jy: 1->2->5
showLnValue(res)


ls_ = [1, 1, 1, 2, 3]
head_ = getListNodeFromList(ls_)
res = Solution().deleteDuplicates_v1(head_)
# jy: 2->3
showLnValue(res)


ls_ = [1, 2, 3, 3, 4, 4, 5]
head_ = getListNodeFromList(ls_)
res = Solution().deleteDuplicates_v1(head_)
# jy: 1->2->5
showLnValue(res)


ls_ = [1, 1, 1, 2, 3]
head_ = getListNodeFromList(ls_)
res = Solution().deleteDuplicates_v1(head_)
# jy: 2->3
showLnValue(res)


