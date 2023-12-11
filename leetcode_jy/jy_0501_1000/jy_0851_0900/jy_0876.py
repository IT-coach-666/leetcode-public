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
title_jy = "Middle-of-the-Linked-List(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:    https://www.yuque.com/frederick/dtwi9g/wvr84g

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
使用快慢指针, 慢指针一次移动一格, 快指针一次移动2格, 只要慢指针有值, 且快指针及快指针的 next 指针有值则一直移动, 最后慢指针指向的节点就是中间节点;
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow, fast = head, head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next if fast.next else None

        return slow


