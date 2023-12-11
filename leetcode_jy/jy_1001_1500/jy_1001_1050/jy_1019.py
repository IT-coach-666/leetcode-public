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
title_jy = "Next-Greater-Node-In-Linked-List(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
You are given the head of a linked list with n nodes.
For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.
Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

Example 1:

Input: head = [2,1,5]
Output: [5,5,0]

Example 2:

Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]


Constraints:
The number of nodes in the list isn.
1 <= n <= 10^4
1 <= Node.val <= 10^9
"""


from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
解法1: 和 503_Next-Greater-Element-II.py 类似, 不过要先求出链表的长度;
    """
    def nextLargerNodes_v1(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []

        stack = []
        result = [0] * self._get_length(head)
        numbers = []
        current = head
        i = 0

        while current:
            while stack and numbers[stack[-1]] < current.val:
                result[stack.pop()] = current.val

            stack.append(i)
            numbers.append(current.val)
            current = current.next
            i += 1

        return result

    def _get_length(self, head):
        current = head
        length = 0

        while current:
            length += 1
            current = current.next

        return length


from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
解法2: 直接将链表转为数组代码更简洁
    """
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        numbers = self._convert_to_list(head)
        stack, result = [], [0] * len(numbers)

        for i, n in enumerate(numbers):
            while stack and numbers[stack[-1]] < n:
                result[stack.pop()] = n

            stack.append(i)

        return result

    def _convert_to_list(self, head):
        current = head
        result = []

        while current:
            result.append(current.val)
            current = current.next

        return result

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
解法3
减少一次链表转数组的时间, 栈中同时存储元素在数组中的位置和值
    """
    def nextLargerNodes_v3(self, head: Optional[ListNode]) -> List[int]:
        stack, result = [], []
        i = 0
        current = head

        while current:
            result.append(0)

            while stack and stack[-1][1] < current.val:
                result[stack.pop()[0]] = current.val

            stack.append((i, current.val))
            current = current.next
            i += 1

        return result




