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
title_jy = "Flatten-a-Multilevel-Doubly-Linked-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given a doubly linked list which in addition to the next and previous pointers, it
could have a child pointer, which may or may not point to a separate doubly linked list.
These child lists may have one or more children of their own, and so on, to produce a
multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list.

Example 1:   https://www.yuque.com/frederick/dtwi9g/lqq6yw
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is as follows:
             After flattening the multilevel linked list it becomes:

Example 2:
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation: The input multilevel linked list is as follows:
  1---2---NULL
  |
  3---NULL

Example 3:
Input: head = []
Output: []

How multilevel linked list is represented in test case:
We use the multilevel linked list from Example 1 above:
1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

To serialize all levels together we will add nulls in each level to signify no node
connects to the upper node of the previous level. The serialization becomes:
[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]

Merging the serialization of each level and removing trailing nulls we obtain:
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]


Constraints:
The number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5
"""

from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue
from leetcode_jy.utils_jy.about_ListNode import showDoublyLinkedListValue

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child



class Solution:
    """
解法1: 递归求解
1) 如果当前节点不存在 child, 则直接递归打平 next 节点即可;
2) 如果存在, 则先递归打平 head.child 节点, 然后将 head 的 next 指针指向 child 的头节
  点, 将 child 链表的尾节点指向 head 的 next 节点, 并更新相应的 prev 指针, 最后将当前的 child 指针置为空;
    """
    def flatten_v1(self, head: 'Node') -> 'Node':
        if not head:
            return None

        if head.child:
            # jy: 打平 head.child 节点
            child_head = self.flatten_v1(head.child)
            # jy: 获取打平后的末尾节点;
            child_tail = child_head
            while child_tail and child_tail.next:
                child_tail = child_tail.next
            # jy: 打平 head.next
            next = self.flatten_v1(head.next)
            # jy: 将 head 与打平后的 child 头节点拼接, 并重新设置 head.child 为 None
            head.next, child_head.prev = child_head, head
            head.child = None
            # jy: 如果 head.next 存在, 则将 child 的尾节点与打平后的 head.next 进行拼接
            if next:
                child_tail.next, next.prev = next, child_tail
        # jy: 如果当前节点不存在 child, 则直接递归打平 next 节点即可(如果没有 child, prev 节点不需改变);
        else:
            head.next = self.flatten_v1(head.next)

        return head

    """
解法2: 首先将链表打平放入一个栈中, 然后依次出栈从后往前构造双向链表;

JY: 也可以使用双向队列, 打平后放入双向队列, 随后不断左侧出队, 将节点不断拼接到链表末尾
    """
    def flatten_v2(self, head: 'Node') -> 'Node':
        stack = []
        dummy = Node(-1, None, None, None)
        # jy: 将链表打平放入一个栈中, 打平后栈中的元素顺序即链表节点的先后顺序;
        self._flatten_to_stack(head, stack)
        # jy: 不断出栈末尾元素, 并逐个元素放入到 dummy 的 next 中, 即不断从后往前构造双向链表;
        while stack:
            current = stack.pop()
            next = dummy.next
            dummy.next, current.prev = current, dummy
            current.child = None

            if next:
                current.next, next.prev = next, current

        if dummy.next:
            dummy.next.prev = None

        return dummy.next

    def _flatten_to_stack(self, head: Node, stack):
        if not head:
            return
        current = head
        while current:
            stack.append(current)
            if current.child:
                self._flatten_to_stack(current.child, stack)
            current = current.next


    """
解法3: 在解法 2 的基础上, 可以在构造栈的同时也构造双向链表;
一开始将 head 加入栈中, 同时创建一个 prev 节点, 其 next 指针指向 head, 只要栈不为空, 则执行出栈(记为 root),
root 就是 prev 的下一个元素, 将 root 的 prev 指针指向 prev, 将 prev 的 next 指针指向 root; 然后先将 root 
的 next 节点入栈, 随后 root 的 child 节点入栈, 这样就保证了 child 节点先出栈, 即深度优先, 最后将 prev 赋值为 root;
    """
    def flatten_v3(self, head: 'Node') -> 'Node':
        if not head:
            return

        stack = [head]
        prev = Node(-1, None, head, None)

        while stack:
            # jy: 第一次出栈的节点为 head 节点;
            root = stack.pop()
            root.prev, prev.next = prev, root

            if root.next:
                stack.append(root.next)
                root.next = None

            if root.child:
                stack.append(root.child)
                root.child = None

            prev = root

        head.prev = None

        return head



def build_multilevel_doubly_linked_list(ls_):
    """
    根据列表构建多层双向链表
    """
    def build_doubly_linked_list(ls_level):
        """根据列表构建双向链表"""
        dummy = Node(-1, None, None, None)
        prev_ = dummy
        for i in ls_level:
            if i is None:
                continue
            else:
                current_node = Node(i, prev_, None, None)
                prev_.next = current_node
                prev_ = current_node
        return dummy.next

    if not ls_:
        return None

    levels_ls = []
    level_ = []
    for i in ls_:
        if i is not None or len(level_) == 0 or level_[-1] == None:
            level_.append(i)
        else:
            levels_ls.append(level_)
            level_ = []
    if level_:
        levels_ls.append(level_)
    # print(levels_ls)

    levels_doubly_list_node = [build_doubly_linked_list(ls_level_) for ls_level_ in levels_ls]
    head_ = levels_doubly_list_node[0]
    # print(levels_doubly_list_node)
    for idx, level_ls in enumerate(levels_ls):
        if idx == 0:
            continue
        else:
            prev_doubly_list_node = levels_doubly_list_node[idx-1]
            for i in level_ls:
                if i is None:
                    prev_doubly_list_node = prev_doubly_list_node.next
                    continue
                else:
                    prev_doubly_list_node.child = levels_doubly_list_node[idx]
                    break
    return head_




ls_ = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12]
head = build_multilevel_doubly_linked_list(ls_)
"""
print(head.val)
print(head.child)
print(head.next.val)
print(head.next.child)
print(head.next.next.val)
print(head.next.next.child)
print(head.next.next.child.val)
"""
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
res = Solution().flatten_v1(head)
showDoublyLinkedListValue(res)
# print(res.next.next.next.next.next.val)


ls_ = [1, 2, None, 3]
head = build_multilevel_doubly_linked_list(ls_)
# Output: [1,3,2]
res = Solution().flatten_v1(head)
showDoublyLinkedListValue(res)


ls_ = []
head = build_multilevel_doubly_linked_list(ls_)
# Output: []
res = Solution().flatten_v1(head)
showDoublyLinkedListValue(res)


