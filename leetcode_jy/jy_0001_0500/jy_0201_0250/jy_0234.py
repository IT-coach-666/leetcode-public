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
title_jy = "Palindrome-Linked-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a singly linked list, determine if it is a palindrome.


Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true


Follow up: Could you do it in O(n) time and O(1) space?
"""


from about_ListNode import *


class Solution:
    """
解法1: 额外使用一个数组保存所有链表结点的值, 然后从数组尾开始向前遍历至中间位置, 遍历数
组的同时遍历链表, 比较两者的值是否相同, 如果不同则说明不是回文;

JY: 将链表的值加入列表后, 直接双指针判断列表中的值即可;
    """
    def isPalindrome_v1(self, head: ListNode) -> bool:
        stack = []

        # jy: 将链表的节点值不断入栈;
        current = head
        while current:
            stack.append(current.val)
            current = current.next

        # jy: 重新指向链表头节点, 不断遍历链表, 同时从列表末尾倒序遍历(只需遍历一半即可);
        current = head
        for i in range(len(stack)-1, len(stack)//2 - 1, -1):
            if stack[i] != current.val:
                return False
            current = current.next

        return True

    """
解法2: Follow up 中要求 O(1) 的内存空间, 所以不能开辟额外的数组; 根据回文的特性, 可以先
找到链表的中间位置, 然后反转右半部分的链表, 比较该部分的链表和左半部分的链表是否相等即可;
    """
    def isPalindrome_v2(self, head: ListNode) -> bool:
        slow, fast = head, head
        # jy: fast 每次走 2 步, 而 slow 每次走 1 步; 当 fast 或 fast.next 有一个为空,
        #     即表明 slow 正好走到链表的一中间位置(奇数个的正中位置, 偶数个时的下中位置);
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # jy: 如果经过以上循环后 fast 有不为 None, 表明链表的节点数为奇数个(以 1->2->2->1 为
        #     例进行思考), 此时将 slow 指向原先 slow 的下一个, 即奇数个的正中间位置的下一个;
        # jy: 当连接节点为奇数个时, slow 对应正中间节点, 不再跳往下一个节点也是可以的(即把以
        #     下 if 逻辑注释掉也是可以的); 因为该 slow 节点以及其之后的节点会经过反转, 且该 slow
        #     节点的 next 会指向 None, 当是奇数个节点时, 不跳往下一个节点也都是符合后续的逻辑
        #      判断的(可以以 1->2->1 为例进行思考);
        if fast:
            slow = slow.next

        # jy: 将 slow 节点开始至结尾的部分进行反转, 并将反转结果的头节点用 reversed 记录;
        #     最开始的 slow 会指向初始 reversed 值, 即 None(即反转部分的反转后的末尾节点
        #     最终指向 None);
        reversed = None
        while slow:
            # slow.next, reversed, slow = reversed, slow, slow.next
            # jy: 将以上代码拆分如下, 便于理解;
            #     注意, 以上代码不能简单拆分成以下两行, 而是需要引入中间变量 tmp:
            '''
            slow.next, reversed = reversed, slow
            slow = slow.next
            '''
            tmp = slow.next
            slow.next, reversed = reversed, slow
            slow = tmp

        # jy: current 指向头节点, reversed 指向链表后半部分经过反转后的头节点(即原链表的末尾节
        #     点); 此时类似双指针法, 不断循环判断双指针指向的数值是否相等, 不相等则返回 False;
        # jy: 如 1->2->3->2->1 反转后为 1->2->3<-2<-1, 双指针指向头尾, 其中 reversed 循环到中间
        #     截止, 过后为 None【待输出结果, 查看确定】;
        current = head
        while reversed:
            if reversed.val != current.val:
                return False
            current = current.next
            reversed = reversed.next

        return True


ls_ = [1, 2]
# Output: false
head_ = getListNodeFromList(ls_)
res = Solution().isPalindrome_v1(head_)
print(res)


ls_ = [1, 2, 2, 1]
# Output: true
head_ = getListNodeFromList(ls_)
res = Solution().isPalindrome_v1(head_)
print(res)


