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
title_jy = "Design-Linked-List(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design your implementation of the linked list. You can choose to use a singly or doubly
linked list. A node in a singly linked list should have two attributes: val and next.
val is the value of the current node, and next is a pointer/reference to the next node.

If you want to use the doubly linked list, you will need one more attribute prev to
indicate the previous node in the linked list. Assume all nodes in the linked list
are 0-indexed.


Implement the MyLinkedList class:
MyLinkedList() :                      Initializes the MyLinkedList object.
int get(int index) :                  Get the value of the index-th node in the linked list. If
                                      the index is invalid, return -1.
void addAtHead(int val) :             Add a node of value val before the first element of the linked
                                      list. After the insertion, the new node will be the first node
                                      of the linked list.
void addAtTail(int val) :             Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) : Add a node of value val before the indexth node in the linked list.
                                      If index equals the length of the linked list, the node will be
                                      appended to the end of the linked list. If index is greater than the
                                      length, the node will not be inserted.
void deleteAtIndex(int index) :       Delete the indexth node in the linked list, if the index is valid.


Example 1:
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);      # linked list becomes 1->2->3
myLinkedList.get(1);                # return 2
myLinkedList.deleteAtIndex(1);      # now the linked list is 1->3
myLinkedList.get(1);                # return 3


Constraints:
0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.
"""



class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None     # jy: 单向列表中忽略该属性即可
        self.next = None

"""
解法1: 单链表;
"""
class MyLinkedList_v1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # jy: self.head 属性总是指向头节点;
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        # jy: current 指向头结点, 对应的 index 为 0;
        i = 0
        current = self.head
        # jy: 当 current 不为空, 且 i 仍小于目标 index 时, current 指向下一个节点, i 同时加 1;
        while current and i < index:
            current = current.next
            i += 1
        # jy: 如果以上退出 while 循环, 则有两种情况: current 为空(此时直接返回 -1) 或 i 为
        #    index (此时返回 current 节点的值)
        return current.value if current else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of
        the linked list.
        """
        # jy: 构造值为 val 的节点, 并将其置为头节点, 同时该节点的 next 值为原头节点值;
        new_head = Node(val)
        self.head, new_head.next = new_head, self.head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # jy: 先将 current 指向头节点;
        current = self.head
        # jy: 如果当前节点和其下一节点都存在, 则将当前节点指向其下一节点;
        #    该 while 循环结束后, current 即为末尾节点(因为 current.next 会
        #    优先为 None)
        while current and current.next:
            current = current.next
        # jy: 如果末尾节点存在, 则将待插入的节点添加到末尾节点的下一个;
        if current:
            current.next = Node(val)
        # jy: 如果末尾节点为 None (即链表尾空链表), 则直接在链表头插入待插入的节
        #    点(或直接 self,head = Node(val));
        else:
            self.addAtHead(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        # jy: 先找出目标 index (由于要在该位置中插入, 因此需要找到该位置的节点以及其前一个节点);
        #    先将 current 指向头节点, 其对应的下标设置为 0 (此时 prev 为 None);
        i = 0
        prev = None
        current = self.head
        # jy: 如果 i 小于目标 index, 则不断指向下一个节点(前提是当前节点要存在, 才能指向下一个节
        #    点; 即使当前节点是最后一个节点, 也能指向下一个节点, 只是下一个节点为 None), 同时不
        #    断更新 prev 为上一个 current;
        while current and i < index:
            prev, current = current, current.next
            i += 1
        # jy: 如果经过以上 while 循环后, i 不为 index, 表明对应的 index 不合法(超出了链表最后一个
        #   节点的下一个位置所对应的下标), 则直接返回;
        if i != index:
            return
        # jy: 如果 prev 存在(当链表为空时, prev 就不存在), 则构造新节点, 并将 prev 的 next 指向新
        #    节点, 同时新节点的 next 指向 current;
        if prev:
            new_node = Node(val)
            prev.next, new_node.next = new_node, current
        # jy: 如果 prev 节点为 None (即链表尾空链表时, 或当链表中有一个节点, 且插入的位置就在 index
        #     为 0 的位置上插入时, prev 会为空, 这两种情况都可以看做是在链表头中插入待插入节点), 直
        #     接在链表头插入待插入的节点(不能直接: self.head = Node(val), 因为该操作只考虑了其中一种
        #     情况);
        else:
            self.addAtHead(val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # jy: 删除指定位置的节点时同样需要用到其前一个节点
        i = 0
        prev = None
        current = self.head

        while current and i < index:
            prev, current = current, current.next
            i += 1

        if i != index:
            return
        # jy: 如果 prev 和 current (待删除的节点) 均存在, 则将 prev 的next 指向 current
        #    的 next, 同时将 current 的 next 设置为 None (即 current 被删除);
        if prev and current:
            prev.next, current.next = current.next, None
        # jy: 如果 prev 不存在但 current 存在 (即待删除的就是头节点(且头节点不为 None)时, 此时
        #    的 prev 均是 None, 此时不能直接设置 self.head = None, 因为不确定链表是否仅有一个节点)
        elif current:
            current.next, self.head = None, current.next
            # self.head = None  # jy: 不正确的做法




"""
解法2: 双向链表;
"""
class MyLinkedList_v2:
    # jy: 同单向列表;
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
    # jy: 同单向列表;
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        i = 0
        current = self.head
        while current and i < index:
            current = current.next
            i += 1
        return current.value if current else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of
        the linked list.
        """
        new_head = Node(val)
        self.head, new_head.next = new_head, self.head
        # jy: 比单向列表多了以下步骤: 如果头节点的下一个节点存在,
        if self.head.next:
            print("==========jy============")
            self.head.next.prev = self.head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        current = self.head

        while current and current.next:
            current = current.next

        if current:
            new_tail = Node(val)
            # jy: 与单链表相比, 双向链表最后节点添加后, 还需要多一个步骤:
            #    将新末尾节点的 prev 指向原末尾节点;
            current.next, new_tail.prev = new_tail, current
        else:
            self.addAtHead(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        i = 0
        prev = None
        current = self.head

        while current and i < index:
            prev, current = current, current.next
            i += 1

        if i != index:
            return

        if prev:
            new_node = Node(val)
            prev.next, new_node.next = new_node, current

            # jy: 与单链表相比, 多了以下步骤:
            #    1) 将新插入的节点的 prev 指向原当前位置节点的前一个节点;
            #    2) 如果原当前位置对应的节点存在, 插入后其为后一个节点, 其对应的 prev 应指向新插入的节点
            new_node.prev = prev
            if current:
                current.prev = new_node
        else:
            self.addAtHead(val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        i = 0
        prev = None
        current = self.head

        while current and i < index:
            prev, current = current, current.next
            i += 1

        if i != index:
            return

        if prev and current:
            prev.next, current.next = current.next, None

            # jy: 与单链表相比, 多了一下步骤: 如果删除当前位置的节点后, 新的当前位置节
            #    点(即以上更新后的 prev.next)存在, 则将该节点的 prev 属性指向原当前位
            #    置节点的前一个节点(此处用 prev 变量保存)
            if prev.next:
                prev.next.prev = prev
        # jy: 如果 prev 不存在但 current 存在 (即待删除的就是头节点(且头节点不为 None)时, 此时
        #    的 prev 均是 None, 此时不能直接设置 self.head = None, 因为不确定链表是否仅有一个
        #    节点), 此时的 current 即指向头节点, 即删除头节点;
        elif current:
            current.next, self.head = None, current.next
            # jy: 与单链表相比, 多了一下步骤: 如果删除头节点后, 新的头节点(即以上更新后的 self.head)存
            #     在, 则将该节点的 prev 属性设置为 None (头节点的 prev 数值值为 None)
            if self.head:
                self.head.prev = None


myLinkedList = MyLinkedList_v1()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)             # linked list becomes 1->2->3
print(myLinkedList.get(1))                # return 2
myLinkedList.deleteAtIndex(1)             # now the linked list is 1->3
print(myLinkedList.get(1))                # return 3

print("="*88)

myLinkedList = MyLinkedList_v2()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)             # linked list becomes 1->2->3
print(myLinkedList.get(1))                # return 2
myLinkedList.deleteAtIndex(1)             # now the linked list is 1->3
print(myLinkedList.get(1))                # return 3



print("="*88)

myLinkedList = MyLinkedList_v1()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)             # linked list becomes 1->2->3
print(myLinkedList.get(1))                # return 2
myLinkedList.deleteAtIndex(0)             # now the linked list is 2->3
print(myLinkedList.get(0))                # return 2


