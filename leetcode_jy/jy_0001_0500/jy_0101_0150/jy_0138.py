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
title_jy = "Copy-List-with-Random-Pointer(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null. Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node
is represented as a pair of [val, random_index] where:
• val: an integer representing Node.val
• random_index: the index of the node (range from 0 to n-1) where random pointer
  points to, or null if it does not point to any node.



Example 1:    https://www.yuque.com/frederick/dtwi9g/ghtpg1
Input: head = [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
Output: [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]

Example 2:    https://www.yuque.com/frederick/dtwi9g/ghtpg1
Input: head = [[1, 1], [2, 1]]
Output: [[1, 1], [2, 1]]

Example 3:    https://www.yuque.com/frederick/dtwi9g/ghtpg1
Input: head = [[3, null], [3, 0], [3, null]]
Output: [[3, null], [3, 0], [3, null]]

Example 4:
Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.



Constraints:
• -10000 <= Node.val <= 10000
• Node.random is null or pointing to a node in the linked list.
• Number of Nodes will not exceed 1000.
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None, random_idx: int = None):
        self.val = int(x)
        self.next = next
        self.random = random
        # jy: 由于参数中以及后面代码应用中将 random 属性视为 Node, 故实际上其不代表 index 值, 故此处
        self.random_idx = random_idx

def get_ls_node_jy(ls_):
    ls_node = [Node(i[0]) for i in ls_]
    for i in range(len(ls_node)-1):
        ls_node[i].next = ls_node[i+1]
    for idx, j in enumerate(ls_):
        ls_node[idx].random = ls_node[j[1]] if j[1] is not None else None
        ls_node[idx].random_idx = j[1]

    return ls_node[0]


def show_ls_node_jy(node):
    res_ = []
    while node:
        #'''
        res_.append([node.val, node.random_idx])
        '''
        if node.random is not None:
            res_.append([node.val, node.random.val])
        else:
            res_.append([node.val, None])
        '''
        node = node.next
    print(res_)


class Solution:
    """
如果只是单纯的链表复制则比较简单, 为了快速找到随机指针指向的结点, 可以使用 Map 来保存原链
表的结点到新链表的结点的映射; 首先遍历原链表, 构建新链表和 Map, 然后再次遍历原链表, 根据 Map 给
新链表的结点设置随机指针;
    """
    def copyRandomList(self, head: Node) -> Node:
        current = head
        dummy = Node(-1)
        prev = dummy
        old_new_list_mapping = {}
        # jy: 遍历链表;
        while current:
            # jy: 对新链表的 val 属性赋值(值与当前链表相同)
            prev.next = Node(current.val)
            # jy: 定义一个字典, key 为老链表节点, value 为新链表节点(当前只有 val 属性有值)
            old_new_list_mapping[current] = prev.next
            prev = prev.next
            current = current.next
        current, new_current = head, dummy.next
        while current:
            # jy: 再次循环链表, 对 random 属性赋值;
            if current.random:
                new_current.random = old_new_list_mapping[current.random]
                # jy: 补充对 random_idx 的赋值;
                new_current.random_idx = current.random_idx
            # jy: 对 next 属性赋值;
            current, new_current = current.next, new_current.next
        return dummy.next


ls_ = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
# Output: [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
head = get_ls_node_jy(ls_)
show_ls_node_jy(head)
res = Solution().copyRandomList(head)
show_ls_node_jy(res)


ls_ = [[1, 1], [2, 1]]
# Output: [[1, 1], [2, 1]]


ls_ = [[3, None], [3, 0], [3, None]]
# Output: [[3, None], [3, 0], [3, None]]


ls_ = []
# Output: []


