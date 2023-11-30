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
title_jy = "reverse-linked-list(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = "循环 | 递归 | 整个链表反转 | 相关题型: 0025、0206"



"""
Reverse a singly linked list.


Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL


Follow up: A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""

from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法 1: 循环

1) 声明两个变量 prev (表示链表的上一个结点) 和 current (表示当前结点), 如果
   当前结点不为空, 则暂存当前结点的下一结点 tmp_next
2) 将当前结点的 next 指针指向上一个结点 prev
3) 将 prev 赋值为 current, 将 current 赋值为 tmp_next
4) 最后返回 prev 结点, 即为反转后的链表的头结点
    """
    def reverseList_v1(self, head: ListNode) -> ListNode:
        """
        以 1->2->3->4->5->None 为例进行思考
        """
        # jy: 初始化 prev 为 None, current 为头节点 head
        prev, current = None, head
        while current:
            # jy: 将原 current.next 暂存起来 (后续作为下一轮循环的 current), 并
            #     并将新的 current.next 指定为 prev
            tmp_next, current.next = current.next, prev
            # jy: 完成 current 的反转后, 更新下一轮循环的 prev 和 current
            prev, current = current, tmp_next
            # jy: 以上两行代码逻辑等价于如下:
            '''
            tmp_next = current.next
            current.next = prev
            prev = current
            current = tmp_next
            '''
        # jy: 每轮循环的结果如下(忽略未反转的节点):
        #    1->None current=2, prev=1
        #    2->1->None, current=3, prev=2
        #    3->2->1->None, current=4, prev=3
        #    4->3->2->1->None, current=5, prev=4
        #    5->4->3->2->1->None, current=None, prev=5
        return prev


    """
解法 2: 递归 (本质和循环一样)

递归的终止条件是 current 为空, 此时 prev 即为反转后链表的头结点; 当 current 不
为空时, 将 current 的 next 指针指向 prev, 同时对 current 的下一个结点做递归调用
    """
    def reverseList_v2(self, head: ListNode) -> ListNode:
        # jy: 递归反转链表 (传入前一个节点和当前节点)
        return self._reverse(None, head)

    def _reverse(self, prev, current):
        # jy: 当 current 为空时表明反转完成, 此时前一个节点即为反转后的头节点,
        #     直接返回, 终止递归
        if not current:
            return prev
        # jy: 将当前节点的下一节点暂存起来, 用于作为下一轮递归时的 current, 并
        #     更新当前节点的下一节点更新为 prev; 下一轮递归时的 prev 即为当前
        #     节点 current
        tmp_next, current.next = current.next, prev
        return self._reverse(current, tmp_next)



ls1 = [1, 2, 3, 4, 5, None]
ln1 = getListNodeFromList(ls1)
showLnValue(ln1, "ListNode1")
res_ln = Solution().reverseList_v1(ln1)
showLnValue(res_ln, "res_ln")


ls1 = [1, 2, 3, 4, 5, None]
ln1 = getListNodeFromList(ls1)
res_ln = Solution().reverseList_v2(ln1)
showLnValue(res_ln, "res_ln")


