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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "reverse-nodes-in-k-group(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = "链表反转技巧 | 相关题型: 0092、0206"



"""
Given a linked list, reverse the nodes of a linked list `k` at a time and
return its modified list. `k` is a positive integer and is less than or equal
to the length of the linked list. If the number of nodes is not a multiple
of `k` then left-out nodes in the end should remain as it is. (即如果剩余节
点不足 k 个, 则保留原样, 不再进行反转)


Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5


Note:    
1) Only constant extra memory is allowed.
2) You may not alter the values in the list's nodes, only nodes itself may
   be changed.
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue

class Solution:
    """
解法 1: 0024 (swap-nodes-in-pairs) 的升级, 由原来的两个结点一组反转链表变
为 k 个结点一组反转链表

思路: 将链表根据 k 分成几组 (因此需先遍历一次链表求出链表的总长度), 每组内各
自进行链表反转; 每组内的链表反转同 0092 (reverse-linked-list-II) 中的解法 3
    """
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        以 head 为 1->2->3->4->5, k 为 4 进行思考, 反转结果: 4->3->2->1->5
        """
        # jy: 依据链表长度对链表进行按 k 分组
        groups = getLen(head) // k
        # jy: 初始化一个哑节点, 并使该节点的下一节点为链表头节点, 最终返回
        #     该哑节点的下一节点即可
        dummy = ListNode(-1)
        dummy.next = head
        # jy: 初始化上一组的末尾和当前组的末尾节点; 最开始, 上一组的末尾为
        #     dummy, 当前组的末尾定为 head (经过反转后 head 即为末尾节点)
        prev_group_tail, cur_group_tail = dummy, dummy.next
        # jy: 循环遍历每一组, 对每一组进行反转
        for _ in range(groups):
            # jy: 将当前组的第 2 个元素以及之后的元素进行反转 (共有 k-1 个
            #     元素, 因此循环 k-1 次); 以 head 为 1->2->3->4->5, k 为 4
            #     进行思考(以下每轮循环中, prev_group_tail 和 cur_group_tail
            #     均不会改变):
            #     第一轮循环后的结果: dummy->2->1->3->4->5 
            #     第二轮循环后的结果: dummy->3->2->1->4->5
            #     第三轮循环后的结果: dummy->4->3->2->1->5
            for xx in range(k-1):
                # jy: 获取当前节点 (最开始为头节点) 的下一节点
                cur_next = cur_group_tail.next
                # jy: 将当前组的下一个节点, 
                cur_group_tail.next = cur_next.next
                cur_next.next, prev_group_tail.next = prev_group_tail.next, cur_next
            # jy: 一组反转完成后即可视为上一组, 此时更新 prev_group_tail 和
            #     cur_group_tail, 随后进行下一轮反转
            prev_group_tail, cur_group_tail = cur_group_tail, cur_group_tail.next
        return dummy.next



ls1 = [1, 2, 3, 4, 5]
ln1 = getListNodeFromList(ls1)
# jy: ListNode1: 1->2->3->4->5
showLnValue(ln1, "ListNode1")

k = 2
res_ln = Solution().reverseKGroup(ln1, k)
# jy: res_ln (k=2): 2->1->4->3->5
showLnValue(res_ln, "res_ln (k=2)")


ls1 = [1, 2, 3, 4, 5]
ln1 = getListNodeFromList(ls1)
k = 3
res_ln = Solution().reverseKGroup(ln1, k)
# jy: res_ln (k=3): 3->2->1->4->5
showLnValue(res_ln, "res_ln (k=3)")


ls1 = [1, 2, 3, 4, 5]
ln1 = getListNodeFromList(ls1)
k = 4
res_ln = Solution().reverseKGroup(ln1, k)
# jy: res_ln (k=4): 4->3->2->1->5
showLnValue(res_ln, "res_ln (k=4)")

