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
title_jy = "Linked-List-Cycle(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer ``pos`` which
represents the position (0-indexed) in the linked list where tail connects to.
If ``pos`` is -1, then there is no cycle in the linked list.


Example 1:
Input: head = [3, 2, 0, -4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1, 2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Follow up:
Can you solve it using O(1) (i.e. constant) memory?
"""

from about_ListNode import *


class Solution:
    """
解法1: 这道题和 001_Two-Sum.py 类似, 遍历链表, 同时使用一个 Set 存储遍历过的结点, 对于当前结
点, 判断其 next 指针指向的结点是否在 Set 中即可;
    """
    def hasCycle_v1(self, head: ListNode) -> bool:
        # jy: visited 是用于存放已遍历的节点的集合;
        visited, current = set(), head
        # jy: 遍历链表, 判断节点是否已经在 visited 集合中, 如果在, 则返回 True, 否则将其加入集合;
        while current:
            #if current.next and current.next in visited:
            if current in visited:
                return True
            else:
                visited.add(current)
            current = current.next
        return False

    """
解法2: 解法 1 的空间复杂度为 O(n), 而题目中希望我们使用空间复杂度为 O(1) 的解法; 这个解法十分巧
妙, 初始化两个指针指向头结点, 记为 slow 和 fast, slow 每次在链表中移动一位, fast 每次在链表中移
动 2 位, 如果链表中有环, 则最终 slow 和 fast 会相遇 (当 slow 和 fast 都在环内时, 假设从环的顺时针
来看 fast 落后 slow k 步, 而每一次移动 fast 都向 slow 靠近一步, 所以 k 次移动后 slow 和 fast 即
相遇), 如果 fast 最后为空(即表示链表的结尾), 则表示链表无环;
    """
    def hasCycle_v2(self, head: ListNode) -> bool:
        slow, fast = head, head
        while slow and fast:
            slow = slow.next
            fast = fast.next if not fast.next else fast.next.next
            if fast and slow == fast:
                return True
        return False


ls_ = [3, 2, 0, -4]
pos = 1
# Output: true
head = getListNodeFromList(ls_, pos)
res = Solution().hasCycle_v1(head)
print(res)

ls_ = [1, 2]
pos = 0
# Output: true
head = getListNodeFromList(ls_, pos)
res = Solution().hasCycle_v1(head)
print(res)

ls_ = [1]
pos = -1
# Output: false
head = getListNodeFromList(ls_, pos)
res = Solution().hasCycle_v1(head)
print(res)



