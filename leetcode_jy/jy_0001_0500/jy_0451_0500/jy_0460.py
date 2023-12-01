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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "LFU-Cache(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.
Implement the ``LFUCache`` class:
LFUCache(int capacity) :
    Initializes the object with the capacity of the data structure.
int get(int key) :
    Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) :
    Update the value of the key if present, or inserts the key if not already present.
    When the cache reaches its capacity, it should invalidate and remove the least frequently
    used key before inserting a new item. For this problem, when there is a tie (i.e., two or
    more keys with the same frequency), the least recently used key would be invalidated.

To determine the least frequently used key, a ``use counter`` is maintained for each key in the
cache. The key with the smallest ``use counter`` is the least frequently used key. When a key is
first inserted into the cache, its ``use counter`` is set to 1 (due to the put operation). The
``use counter`` for a key in the cache is incremented either a ``get`` or ``put`` operation is
called on it.

The functions ``get`` and ``put`` must each run in O(1) average time complexity.


Example 1:
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1;  cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.  cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3;  cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.  cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3;  cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4;  cache=[3,4], cnt(4)=2, cnt(3)=3


Constraints:
0 <= capacity <= 10^4
0 <= key <= 10^5
0 <= value <= 10^9
At most 2 * 10^5 calls will be made to get and put.
"""


import collections


# jy: 双向链表节点(含 prev 和 next 指针)定义, 含有 self.frequency 属性, 用于记录
#     该 key 对应的 Node 的访问频数;
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.frequency = 1
        self.prev = self.next = None


# jy: 双向链表类;
class DoublyLinkedList:
    # jy: 初始化双向链表为空链表(头和尾节点均为 None)
    def __init__(self):
        # jy: 记录双向链表的长度(节点数)
        self._size = 0
        self._head = Node(None, None)
        self._tail = Node(None, None)
        self._head.next = self._tail
        self._tail.prev = self._head

    def __len__(self):
        return self._size

    def append_head(self, node):
        """
        将 node 节点作为头节点(即 self._head.next, self._head 总是指向 None 节点, 并
        非真正的头节点)加入双向链表中, 此时双向链表的 self._size 属性值加 1;
        """
        node.next = self._head.next
        node.prev = self._head
        self._head.next.prev = node
        self._head.next = node
        self._size += 1

    def pop(self, node):
        """
        在双向链表中删除 node 节点, 此时双向链表的 self._size 属性值减 1;
        """
        if self._size == 0:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

    def pop_tail(self):
        """
        弹出双向链表的尾部节点, 即 self._tail.prev (self._tail 总是代表真正尾部节点的下一个 None 节点)
        """
        tail = self._tail.prev
        self.pop(tail)
        return tail


"""
使用和 146_LRU-Cache.py 相同的双向链表, 同时需要两个 Map, 一个用来保存 key 和节点
的映射, 用于快速找到节点, 另一个用来保存访问次数和对应节点的映射, 值为双向链表,
链表中所有的节点有着相同的访问频次, 最近访问的节点会从节点头插入, 所有链表尾的节
点是最远被访问的节点; 同时需要全局维护所有节点中被访问的最少频次, 用于缓存容量满
时剔除被访问次数最少的节点:
1) get: 如果 key 不在 Map 中, 则返回 -1, 否则将对应节点从频次 Map 中移除, 对节点频
        次加 1 后放入到新频次对应的链表中, 并根据需要更新全局最小访问频次;
2) put: 如果 key 存在, 则过程同 get 方法; 如果 key 不存在, 则判断缓存大小是否等于容
        量, 如果是则需要先根据最小频次剔除一个节点, 然后将新节点加入到频次为 1 的链
        表中, 并更新全局最小频次为 1
"""
class LFUCache_v1:
    # jy: 初始化类时传入 cache 的最大容量, 设置为该类的 self._capacity 属性
    def __init__(self, capacity: int):
        # jy: 记录 cache 中的当前容量大小;
        self._size = 0
        self._capacity = capacity
        # jy: self._node_cache 用来保存 key 和节点(Node 类, node)的映射, 用于快速找到节点
        self._node_cache = {}
        # jy: self._frequency_cache 用来保存访问次数和对应次数节点的映射, 值为双向链表, 链
        #     表中的所有节点有着相同的访问频次, 最近访问的节点会从节点头插入, 所有链表尾的
        #     节点是最远被访问的节点;
        self._frequency_cache = collections.defaultdict(DoublyLinkedList)
        # jy: 记录 cache 中最少使用的次数
        self._min_frequency = 0

    def get(self, key: int) -> int:
        # jy: 如果 key 不在 self._node_cache 中, 则直接返回 -1;
        if key not in self._node_cache:
            return -1
        # jy: 从 self._node_cache 字典中获取该 key 对应的 Node 类, 由于调用一次 get 方法时, 相
        #     应的 key (对应一个 Node 类) 的访问频次会增加 1 次, 因此此处调用 self._update 方法
        #     更新该 key 对应的 Node 类的 frequency 属性(同时会对 self._frequency_cache 进行调整);
        node = self._node_cache[key]
        self._update(node)
        # jy: 最终返回该 key 对应的 Node 类的 value 属性值;
        return node.value

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return
        # jy: 如果待插入的 key 已经在 self._node_cache 中, 这获取该 key 对应的 node, 并
        #     对该 node 进行更新, 同时将其 value 属性更新为当前传入的 value 值;
        if key in self._node_cache:
            node = self._node_cache[key]
            self._update(node)
            node.value = value
        # jy: 如果待插入的 key 不在 self._node_cache 中, 则基于 (key, value) 构建 Node 类并将其
        #     插入到 self._node_cache 字典中; 由于此时该 key 对应的 Node 类的 frequency 为 1, 需
        #     更新 self._min_frequency 的值为 1, 同时在 self._frequency_cache 字典中的出现 1 次的
        #     对应的双向链表头中加入该 Node 类;
        else:
            # jy: 如果当前容量大小已经等于最大容量, 则删除使用频率最小的节点(最小使用频率通
            #     过 self._min_frequency 记录, 可能有多个相同的频率为 self,_min_frequency 的
            #     节点, 其均被记录到 self,_frequency_cache[self._min_frequency] 对应的双向链
            #     表中, 其中的最右侧为真正的使用频率最小值, 将其从双向链表中删除);
            if self._size == self._capacity:
                node = self._frequency_cache[self._min_frequency].pop_tail()
                del self._node_cache[node.key]
                self._size -= 1
            # jy: 基于当前新的 key 和 value 构建新的 Node, 并加入到 self._node_cache 中;
            node = Node(key, value)
            self._node_cache[key] = node
            self._frequency_cache[1].append_head(node)
            self._min_frequency = 1
            self._size += 1
        # print("========self._node_cache========== ", self._node_cache)

    def _update(self, node):
        """
        更新 node 的 frequency, 同时更新 self._frequency_cache (node 的 frequency 一旦
        更新, self._frequency_cache 肯定也要更新)
        """
        # jy: 先获取 node 的 frequency, 从 self._frequency_cache 中的该 frequency 对应的
        #     双向链表中删除删除当前 node;
        frequency = node.frequency
        self._frequency_cache[frequency].pop(node)
        # jy: 如果 self._frequency_cache[frequency] 中删除该 node 后, 该 frequency 对应的
        #     双向链表为空, 且 self._min_frequency 等于当前 frequency, 则 self._min_frequency
        #     加 1;
        if self._min_frequency == frequency and not self._frequency_cache[frequency]:
            self._min_frequency += 1

        # jy: node 节点的 frequency 加 1, 并在 self._frequency_cache 中
        node.frequency += 1
        self._frequency_cache[node.frequency].append_head(node)
        # self._frequency_cache[frequency + 1].append_head(node)


"""
参考: https://leetcode-cn.com/problems/lfu-cache/solution/yi-zhang-tu-shuo-ming-bai-by-powcai/
准备两个字典:
1) key 与 freq 映射, 为了找 key 在哪个频率下;
2) key_freq 与 (key, value) 映射(以该方式记录: {key_freq: {key, value}}), 为了找 key 对应的 value
   值, 这个需要一个有序字典 OrderedDict, 为了好弹出同一个频率下, 最开始加入的 key（当然是容量不
   够，需要弹出的时候）

对于第二个字典, 可以使用 python 自带库, 也可以使用双向链表实现
思路一: 用 python 内建有序字典 OrderedDict 实现;
思路二: 双向链表, 第一个字典就是 key 对应 node 的位置(即解法 1 中的思路);
"""
class LFUCache_v2:
    def __init__(self, capacity: int):
        from collections import OrderedDict, defaultdict
        self.freq = defaultdict(OrderedDict)
        self.key_to_freq = {}
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        key_freq = self.key_to_freq[key]
        res = self.freq[key_freq].pop(key)
        if not self.freq[key_freq] and key_freq == self.min_freq:
            self.min_freq += 1
        self.freq[key_freq + 1][key] = res
        self.key_to_freq[key] = key_freq + 1
        return res

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        # key 本身就在其中
        if key in self.key_to_freq:
            key_freq = self.key_to_freq[key]
            self.freq[key_freq].pop(key)
            if not self.freq[key_freq] and key_freq == self.min_freq:
                self.min_freq += 1
            self.freq[key_freq + 1][key] = value
            self.key_to_freq[key] = key_freq + 1
        else:
            # key不在, 要弹出频率使用次数少的key
            if len(self.key_to_freq) == self.capacity:
                k, v = self.freq[self.min_freq].popitem(last=False)
                self.key_to_freq.pop(k)
            self.key_to_freq[key] = 1
            self.freq[1][key] = value
            self.min_freq = 1


lfu = LFUCache_v1(2)
lfu.put(1, 1)        # cache=[1,_], cnt(1)=1
lfu.put(2, 2)        # cache=[2,1], cnt(2)=1, cnt(1)=1
print(lfu.get(1))    # return 1;  cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3)        # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.  cache=[3,1], cnt(3)=1, cnt(1)=2
print(lfu.get(2))    # return -1 (not found)
print(lfu.get(3))    # return 3;  cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4)        # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.  cache=[4,3], cnt(4)=1, cnt(3)=2
print(lfu.get(1))    # return -1 (not found)
print(lfu.get(3))    # return 3;  cache=[3,4], cnt(4)=1, cnt(3)=3
print(lfu.get(4))    # return 4;  cache=[3,4], cnt(4)=2, cnt(3)=3

print("="*88)

lfu = LFUCache_v2(2)
lfu.put(1, 1)        # cache=[1,_], cnt(1)=1
lfu.put(2, 2)        # cache=[2,1], cnt(2)=1, cnt(1)=1
print(lfu.get(1))    # return 1;  cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3)        # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.  cache=[3,1], cnt(3)=1, cnt(1)=2
print(lfu.get(2))    # return -1 (not found)
print(lfu.get(3))    # return 3;  cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4)        # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.  cache=[4,3], cnt(4)=1, cnt(3)=2
print(lfu.get(1))    # return -1 (not found)
print(lfu.get(3))    # return 3;  cache=[3,4], cnt(4)=1, cnt(3)=3
print(lfu.get(4))    # return 4;  cache=[3,4], cnt(4)=2, cnt(3)=3


