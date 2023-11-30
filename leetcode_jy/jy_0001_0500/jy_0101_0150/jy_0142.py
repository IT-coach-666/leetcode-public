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
title_jy = "Linked-List-Cycle-II(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a linked list, return the node where the cycle begins. If there is no cycle,
return null.

To represent a cycle in the given linked list, we use an integer ``pos`` which represents
the position (0-indexed) in the linked list where tail connects to. If ``pos`` is -1, then
there is no cycle in the linked list.

Note: Do not modify the linked list.


Example 1:
Input: head = [3, 2, 0, -4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1, 2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Follow-up: Can you solve it without using extra space?
"""

from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法1: 和 141_Linked-List-Cycle.py 的解法 1 几乎一样, 同样是遍历链表, 同时使用一个 Set 存储遍历
过的结点, 对于当前结点, 判断其 next 指针指向的结点是否在 Set 中, 如果存在则返回 current.next
    """
    def detectCycle_v1(self, head: ListNode) -> ListNode:
        visited, current = set(), head
        while current:
            if current in visited:
                return current
            #if current.next and current.next in visited:
            #    return current.next
            else:
                visited.add(current)
            current = current.next
        return None

    """
解法2: 是 141_Linked-List-Cycle.py 中解法 2 的延申, 同时也更为巧妙; 首先同样是使用 slow 和 fast 两
个指针, 找到两者相遇的结点, 然后开始求环的开始结点;
图见: https://www.yuque.com/frederick/dtwi9g/fornqs

假设:链表头至环的起点的距离为 x, 环的总长度为 L, slow 指针走过 x + y 距离后和 fast 指针相遇, 此时顺
时针方向 fast 指针距离环的起点为 z;

假设当 slow 走到环的起点时, 顺时针方向 fast 距离环的起点为 k (即 slow 和 fast 距离为 k), 由于每 1 次
移动 fast 都向 slow 靠近一步, 所以 k 次移动后 slow 和 fast 相遇, 此时 slow 走了 k 步 (fast 走了 2k 步),
也就是图中的 y, 由于 k <= L, 所以 slow 和 fast 相遇时, slow 在环中走过的距离不会超过环的长度, 所以 slow
至今走过的总距离为 x + y, 而 fast 有可能在环中走了好几环, 所以它至今走过的距离为 x + cL + y, 其中 c 为
正整数(由于 fast 走的比 slow 快, 所以 fast 必然是至少走了一圈才有可能和 slow 相遇), 由于 fast 的移动速
度是 slow 的两倍, 所以有 2(x+y) = x + cL + y, 将 y = L-z 代入得: x = (c-1)L + z, 也就是说 x 的长度等于
n 个 (n >= 1) 环的长度加上 z; 所以当 slow 和 fast 相遇后继续使用两个指针, 一个指向链表头, 一个指向 slow
和 fast 相遇的地方, 各自向下一个结点移动, 一定会在某一刻两者相遇, 此时的两个指针所在的位置就是环的起点;

思路总结:
1) 使用两指针 slow 和 fast, 均从头节点出发, slow 每次走 1 步, fast 每次走 2 步, 找到相遇点(如果有环必相遇);
2) 使用两指针 p1 和 p2, p1 指向头节点, p2 指向相遇点, 每次同时各走 1 步, 相遇点即为环的起点;
    """
    def detectCycle_v2(self, head: ListNode) -> ListNode:
        slow, fast = head, head
    # jy: slow 每次走 1 步, fast 每次走 2 步, 值得两者相遇则退出 while 循环 (如果有环, 则一定会相遇,
    #    此时会退出 while 循环; 如果没环, 则肯定 fast 先到末尾节点 None, 此时也会退出 while 循环);
        while slow and fast:
            slow = slow.next
            fast = fast.next if not fast.next else fast.next.next
            if fast and slow == fast:
                break
    # jy: 如果以上退出 while 循环时 fast 为 None, 则表明无环, 返回 None 即可;
        if not fast:
            return None

        # jy: 经过以上代码逻辑, 此时的 fast 即为相遇的节点; 此时使用两个指针, 分别指向链表头和相遇的节点,
    #    同时每次各走 1 步, 当两者相遇时即为链表环的起点(推理过程见答案解析);
        p1, p2 = head, fast
        while p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1


ls_ = [3, 2, 0, -4]
pos = 1
# Output: true
head = getListNodeFromList(ls_, pos)
res = Solution().detectCycle_v1(head)
print(res.val)

ls_ = [1, 2]
pos = 0
# Output: true
head = getListNodeFromList(ls_, pos)
res = Solution().detectCycle_v2(head)
print(res.val)

ls_ = [1]
pos = -1
# Output: false
head = getListNodeFromList(ls_, pos)
res = Solution().detectCycle_v1(head)
print(res)


