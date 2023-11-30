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
title_jy = "LRU-Cache(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should
support the following operations: get and put.
1) get(key): Get the value (will always be positive) of the key if the key exists in
             the cache, otherwise return -1.
2) put(key, value): Set or insert the value if the key is not already present. When the
                   cache reached its capacity, it should  invalidate the least recently
                   used item before inserting a new item.

The cache is initialized with a positive capacity.


Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


Follow up: Could you do both operations in O(1) time complexity?
"""


from collections import OrderedDict


class Node:
    """双向链表节点"""
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    """
Least Recently Used (LRU) cache, 指定缓存容量的最近最少使用缓存(get 和 put 都算是使用操
作, 如果容量不足, 删除缓存中最近没被使用过的元素);
使用 Map 和双向链表实现(不断将最近使用到的元素添加到链表表头, 链表表尾为最近没使用过的元素):
1) put 时如果 key 在 Map 中, 则更新 key 对应结点的值, 然后将该结点移动到链表的头部, 如
   果 key 不存在, 则新建一个结点, 放入 Map 并插入链表的头部, 如果此时 Map 的长度超过
   capacity, 则删除链表的尾结点并删除该节点在 Map 中的记录;
2) get 时如果 key 不在 Map 中, 则返回 -1; 如果存在, 则将该结点移动到链表的头部并返回该
   结点的值;
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        # jy: 保存链表中已有的 Node, 保存方式为 {node.key: node, ...}
        self.caches = {}
        # jy: 初始化该类时, 会初始化一个双向链表(含两个 Node 节点, 分别为 head 和 tail, 其
        #     对应的 key 和 value 属性值均为 -1, 便于后续那往双向链表中添加或删除元素);
        #     后续添加节点后, 真正的头节点为 self.head.next, 真正的尾节点为 self.tail.prev;
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node: Node) -> None:
        """
        将 node 节点添加到链表头(即添加到 self.head 的下一个元素)
        """
        # jy: 改变 node 的 prev 和 next 节点;
        node.prev, node.next = self.head, self.head.next
        # jy: 改变 self.head 的下一节点和 self.head.next 的前一节点;
        self.head.next.prev, self.head.next = node, node

    def _remove_node(self, node: Node) -> None:
        """
        从双向链表中删除 node 节点: 将 node 的前节点的下一节点设置为 node 的下
        一节点, 并将 node 的后一节点的前一节点设置为 node 的前一节点;
        """
        node.prev.next, node.next.prev = node.next, node.prev

    def _move_to_head(self, node: Node) -> None:
        """
        将 node 节点移动到双向链表的表头: 先删除该节点, 再将该节点添加到头节点;
        """
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self) -> Node:
        """
        删除尾部 node 节点(即 self.tail 的前一个节点);
        """
        # jy: self.tail 并非真正的尾部节点, 其前一个节点才是;
        tail = self.tail.prev
        self._remove_node(tail)
        return tail

    def get(self, key: int) -> int:
        # jy: 如果要获取的 key 在链表中暂不存在, 则返回 -1;
        if key not in self.caches:
            return -1
        # jy: 先从 caches 中获取相应 key 对应的 Node 节点, 再将该节点移动至链表头(链表头的
        #     节点表示最近使用的节点), 随后返回该节点的 value 值
        node = self.caches[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # jy: 如果 key 值已经在缓存中了, 则获取该 key 对应的 Node 节点(链表中的节点), 并将
        #     该节点的 value 属性值更新为传入的 value 值, 同时将该节点移动到链表头节点(表示
        #     最近使用的节点);
        if key in self.caches:
            node = self.caches[key]
            node.value = value
            self._move_to_head(node)
        # jy: 如果 key 不在缓存字典中, 则使用新传入的 key 和 value 初始化一个链表节点, 并将其
        #     加入到缓存字典中, 同时将其添加到双向链表的头节点(表示最近使用到); 此时如果缓存字
        #     典中长度超过了 capacity, 则删除链表的尾部节点, 同时在缓存字典中删除该节点;
        else:
            new_node = Node(key, value)
            self.caches[key] = new_node
            self._add_to_head(new_node)
            if len(self.caches) > self.capacity:
                tail = self._pop_tail()
                self.caches.pop(tail.key)


class LRUCache_v2:
    def __init__(self, capacity: int):
        # jy: 记录 cache 的容量
        self.capacity = capacity
        # jy: 有序字典记录缓存信息, 从左到右中越是右侧的为最近使用的;
        self.lru_dict = OrderedDict()

    def get(self, key: int) -> int:
        # jy: 如果 key 在有序字典缓存中, 先获取该值, 并删除后重新插入, 确保当前该值置于
        #     有序字典最右侧(即更新为最近使用的元素), 最后返回原先记录的值;
        if key in self.lru_dict:
            # jy: 通过删除并重新赋值使得其排到最后
            '''
            val = self.lru_dict[key]
            del self.lru_dict[key]
            self.lru_dict[key] = val
            return val
            '''
            # jy: 直接移动到最后
            self.lru_dict.move_to_end(key)
            return self.lru_dict[key]

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # jy: 如果 key 在有序字典缓存中, 先删除后重新插入, 确保当前该值置于有序字典最
        #     右侧(即更新为最近使用的元素);
        if key in self.lru_dict:
            # jy: 直接移动到最后;
            self.lru_dict[key] = value
            self.lru_dict.move_to_end(key)

            # jy: 通过删除后重新赋值移动到最后
            '''
            del self.lru_dict[key]
            self.lru_dict[key] = value
            '''
        # jy: 如果当前缓存容量已经是最大容量, 且当前 key 不在缓存中, 则删除最近最少访问
        #     的元素(即缓存有序字典的最左侧), 然后插入当前元素值; 如果容量没达到上限, 直
        #     接插入即可;
        else:
            if len(self.lru_dict) == self.capacity:
                self.lru_dict.popitem(0)
            self.lru_dict[key] = value


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

from collections import OrderedDict

a = OrderedDict()
a["a"] = 33
a["b"] = 34
print(a.move_to_end("a"))
# print(a.popitem(0))
print(a)
# del a["a"]
#
# print(a)


