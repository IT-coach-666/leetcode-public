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
title_jy = "Insert-into-a-Sorted-Circular-Linked-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a node from a Circular Linked List which is sorted in ascending order, write a
function to insert a value ``insertVal`` into the list such that it remains a sorted
circular list. The given node can be a reference to any single node in the list, and
may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert
the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular
list and return the reference to that single node. Otherwise, you should return the
original given node.



Example 1:  (图: https://www.yuque.com/frederick/dtwi9g/gaotl6)
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are
             given a reference to the node with value 3, and we need to insert 2 into the list.
             The new node should be inserted between node 1 and node 3. After the insertion, the
             list should look like this, and we should still return node 3.

Example 2:
Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and
             return the reference to that single node.

Example 3:
Input: head = [1], insertVal = 0
Output: [1, 0]


Constraints:
0 <= Number of Nodes <= 5 * 10^4
-10^6 <= Node.val <= 10^6
-10^6 <= insertVal <= 10^6
"""


from about_ListNode import *


class Solution:
    """
维护两个指针表示上一个节点和当前节点, 记为 prev 和 current, 初始 prev 指向 head, current 指
向 head.next, 从 current 处遍历链表, 一直到 current 回到头节点为止; 遍历链表时:
1) 如果 prev.val <= insertVal <= current.val,  则说明 prev 和 current 之间正好是要插入的节
   点的位置;
2) 如果 prev.val > current.val, 说明 prev 为所有节点的最大值, 此时:
   a) 如果 prev.val <= insertVal or insertVal <= current.val, 说明 prev 和 current 之间
      正好是要插入的节点的位置;
   b) 如果在遍历链表的过程中未能插入节点, 则说明链表是单节点, 不管要插入的节点的值是比
      该节点大还是小, 都是将节点插入到 prev 和 current 之间;
    """
    def insert(self, head: 'ListNode', insertVal: int) -> 'ListNode':
        if not head:
            node = ListNode(insertVal)
            # jy: 单独节点独自成环;
            node.next = node
            return node

        # jy: 维护两个指针, 初始 prev 指向 head, current 指向 head.next
        prev, current = head, head.next
        # jy: 从 current 处遍历链表, 一直到 current 回到头节点为止;
        while current is not head:
            # jy: 1) 如果 prev.val <= insertVal <= current.val,  则说明 prev 和 current 之
            #       间正好是要插入的节点位置, 直接将 prev 的 next 属性指向 insertVal 对应
            #       的节点, 且在初始化该节点时设置其 next 为 current 节点, 即此时的 insertVal
            #       对应的节点正好插入到 prev 和 current 中间, 插入完成后直接返回 head;
            if prev.val <= insertVal <= current.val:
                prev.next = ListNode(insertVal, current)
                return head
            # jy: 2) 如果 prev.val > current.val, 说明 prev 为所有节点的最大值, 此时:
            #       a) 如果满足: prev.val <= insertVal 或 insertVal <= current.val, 则
            #          表明 prev 和 current 之间正好是要插入的节点的位置;
            if prev.val > current.val and (prev.val <= insertVal or insertVal <= current.val):
                prev.next = ListNode(insertVal, current)
                return head
            # jy: 将 prev 和 current 前进一位;
            prev, current = current, current.next
        # jy:        b) 如果在遍历链表的过程中未能插入节点, 则说明链表是单节点, 不管要插
        #              入的节点的值是比该节点大还是小, 都是将节点插入到 prev 和 current
        #              之间(此时的 prev 和 current 均为头节点, 单点成环);
        prev.next = ListNode(insertVal, current)
        return head



ls_ = [3, 4, 1]
insertVal = 2
# Output: [3,4,1,2]
head_ = getListNodeFromList(ls_)
head_.next.next.next = head_   # jy: 将 1 和 3 连接成环
res = Solution().insert(head_, insertVal)
showCircleLnValue(res)


ls_ = []
insertVal = 1
head_ = getListNodeFromList(ls_)
# showCircleLnValue(head_)
# Output: [1]
res = Solution().insert(head_, insertVal)
showCircleLnValue(res)


ls_ = [1]
insertVal = 0
head_ = getListNodeFromList(ls_)
head_.next = head_                  # jy: 将以上的单链表独自元素成环;
showCircleLnValue(head_)
# Output: [1, 0]
res = Solution().insert(head_, insertVal)
showCircleLnValue(res)


