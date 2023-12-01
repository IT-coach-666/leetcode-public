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
title_jy = "Design-HashMap(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design a HashMap without using any built-in hash table libraries.
Implement the MyHashMap class:
MyHashMap() :                  initializes the object with an empty map.
void put(int key, int value) : inserts a (key, value) pair into the HashMap. If the key already
                               exists in the map, update the corresponding value.
int get(int key) :             returns the value to which the specified key is mapped, or -1 if
                               this map contains no mapping for the key.
void remove(key) :             removes the key and its corresponding value if the map contains the
                               mapping for the key.

Example 1:
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1);   # The map is now [[1,1]]
myHashMap.put(2, 2);   # The map is now [[1,1], [2,2]]
myHashMap.get(1);      # return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);      # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1);   # The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);      # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2);   # remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);      # return -1 (i.e., not found), The map is now [[1,1]]



Constraints:
0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.
"""


from collections import deque


"""
在 705_Design-HashSet.py 的基础上稍加修改即可;
"""
class Node:
    def __init__(self, key, value, left=None, right=None):
        # jy: 在 705_Design-HashSet.py 的基础上增加一个 key 属性, 并基于
        #    key 属性构造二叉搜索树, value 只是该 key 对应的值;
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def add(self, node):
        """往当前 Node 添加节点 node"""
        # jy: 如果待添加的 node 节点的 key 属性值大于当前节点(根节点)的 key 属性值, 则将
        #    待添加的 node 节点加入当前节点的右子树;
        if node.key > self.key:
            if not self.right:
                self.right = node
            else:
                self.right.add(node)
        # jy: 如果待添加的 node 节点的 key 属性值小于当前节点(根节点)的 key 属性值, 则将
        #    待添加的 node 节点加入当前节点的左子树;
        elif node.key < self.key:
            if not self.left:
                self.left = node
            else:
                self.left.add(node)
        # jy: 如果待添加的 node 节点的 key 属性值等于当前节点(根节点)的 key 属性值, 则直接将
        #    当前节点(根节点)的 value 属性值更新为待添加的 node 节点的 value 属性值即可;
        else:
            self.value = node.value

    def get(self, key):
        """获取当前字典类的相应 key 对应的 value"""
        # jy: 如果当前节点(根节点)的 key 属性值等于待查找的 key 值, 则直接返回当前节点的 value 属性值;
        if self.key == key:
            return self.value
        # jy: 如果根节点的 key 值大于待查找的 key 值, 则应该在左子树(左子节点)中查找(前提是左子节点存在)
        elif self.key > key:
            return self.left.get(key) if self.left else -1
        # jy: 如果根节点的 key 值小于待查找的 key 值, 则应该在右子树(右子节点)中查找(前提是右子节点存在)
        else:
            return self.right.get(key) if self.right else -1

    def remove(self, key):
        """从根节点(self 代表根节点)中删除值为 key 的节点"""
        # jy: 如果根节点 key 值等于待删除的 key 值, 则分三种情况:
        #    1) 如果根节点均无左右子树, 则删除后直接返回 None
        #    2) 如果根节点只有左子树或右子树, 则删除后直接返回左子节点或右子节点(即为删除后的根节点)
        #    3) 如果根节点左右子树均存在, 则先获取右子树中 key 值最小的节点, 并将根节点的 key 值更新
        #       为该值, 同时在右子树中删除该值;
        if self.key == key:
            if not self.left and not self.right:
                return None
            elif not self.left or not self.right:
                return self.left or self.right
            else:
                min_node = self.right._find_min()
                self.key = min_node.key
                self.value = min_node.value
                self.right = self.right.remove(self.key)
        # jy: 如果根节点的 key 值大于待删除的 key 值, 则应该在根节点的左子树中找该待删除
        #    的 key 值并删除(在左子树存在的情况下, 如果不存在, 则直接忽略, 因为待删除的
        #    key 值不存在)
        elif self.key > key and self.left:
            self.left = self.left.remove(key)
        # jy: 如果根节点的 key 值小于待删除的 key 值, 同理, 从右子树中找该待删除的 key 值并删除
        elif self.key < key and self.right:
            self.right = self.right.remove(key)

        return self

    def traverse(self):
        """遍历以当前节点 (self) 为根节点的树中的所有节点, 将这些节点存放入列表中返回"""
        queue = deque([self])
        nodes = []

        while queue:
            node = queue.popleft()
            nodes.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return nodes

    def _find_min(self):
        """找出以当前节点(self)为根节点树中的 key 值最小的节点"""
        current = self
        while current.left:
            current = current.left
        return current


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = [None] * 16
        self.size = 0
        self.load_factor = 0.75

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # jy: 依据 key 值进行哈希, 找出其对应节点要存放到 self.nodes 中的位置
        h = self._hash(key)
        # jy: 将待插入的 key 和 value 键值对构造成树节点
        new_node = Node(key, value)
        # jy: 如果 self.nodes 中对应的位置暂为空, 则直接将新节点存放入该位置(即作为该位置的根节点)
        if not self.nodes[h]:
            self.nodes[h] = new_node
        # jy: 如果 self.nodes 中对应的位置已经有根节点, 则将新节点插入到对应的二叉搜索树中;
        else:
            self.nodes[h].add(new_node)
        # jy: 插入后 size 值(即 self.nodes 列表中所有树的所有节点个数)大小加 1
        self.size += 1

        # jy: 如果 self.nodes 列表中所有树的总节点个数已经超过 self.nodes 长度的 3/4, 则对所有树
        #    进行重哈希处理(避免存在某些树深入太深, 架构复杂, 影响效率; 但也不一定如此, 得看数据
        #    特征, 如 leetcode 测试用例中, 此部分注释掉的执行效率更高, 因为特定数据特征下, 此部
        #    分可能显得多余, 执行也会浪费时间);
        if self.size > self.load_factor * len(self.nodes):
            self._rehash()

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key
        """
        # jy: 依据 key 值进行哈希, 找出其对应节点要存放到 self.nodes 中的位置
        h = self._hash(key)
        # jy: 如果该位置有根节点存在, 则从该根节点的树中找 key 属性值为 key 的节点对应的 value 属性值;
        if self.nodes[h]:
            return self.nodes[h].get(key)
        # jy: 如果该位置没有根节点, 即为 None, 则直接返回 -1;
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key
        if this map contains a mapping for the key
        """
        # jy: 依据 key 值进行哈希, 找出其对应节点要存放到 self.nodes 中的位置
        h = self._hash(key)
        # jy: 如果对应的位置根节点存在, 则从该根节点对应的树中删除值为 key 的节点, 删
        #    除后, self.size 值减 1;
        if self.nodes[h]:
            self.nodes[h] = self.nodes[h].remove(key)
            self.size -= 1

    def _rehash(self):
        """重新哈希构造 MyHashMap 类: 调整该类的属性值以及节点分布"""
        # jy: 将原有 self.nodes 备份, 新 self.nodes 调整为原先的两倍, 并先初始化为均 None;
        new_nodes = [None] * (len(self.nodes) * 2)
        old_nodes = self.nodes
        self.nodes = new_nodes
        # jy: 遍历原有 self.nodes 中的所有二叉搜索树(列表非 None 即表示是二叉搜索树), 并获
        #    取其中的所有节点, 将其重新添加到 MyHashMap 类(对应的 self.nodes 为更新后的,
        #    长度比原来的大一倍, 而 self.size 不变, 因为只是对原有 self.nodes 进行重构, 不
        #    影响总节点个数);
        for node in old_nodes:
            if not node:
                continue
            for n in node.traverse():
                self.put(n.key, n.value)

    def _hash(self, key):
        return key % len(self.nodes)



class MyHashMap_jy:
    """
    字典: 以列表的下标作为 key, 下标对应的值为 value, 这样确保一个 key 只有一个 value与之对应
    集合: 以列表的下标作为集合中的元素, 当对应下标的值为 None 时, 表示集合中的该元素不存在, 否
          则该元素存在, 由于下标只有一个, 故集合中的元素也不会重复出现
    """
    def __init__(self):
        # jy: 因为找不到时返回 -1, 初始化直接初始化为 -1;
        self.jy_list = [-1] * 1000001


    def put(self, key: int, value: int) -> None:
        self.jy_list[key] = value


    def get(self, key: int) -> int:
        return self.jy_list[key]


    def remove(self, key: int) -> None:
        self.jy_list[key] = -1


# myHashMap = MyHashMap()
# myHashMap.put(1, 1)          # The map is now [[1,1]]
# myHashMap.put(2, 2)          # The map is now [[1,1], [2,2]]
# print(myHashMap.get(1))      # return 1, The map is now [[1,1], [2,2]]
# print(myHashMap.get(3))      # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1)          # The map is now [[1,1], [2,1]] (i.e., update the existing value)
# print(myHashMap.get(2))      # return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2)          # remove the mapping for 2, The map is now [[1,1]]
# print(myHashMap.get(2))      # return -1 (i.e., not found), The map is now [[1,1]]


myHashMap = MyHashMap_jy()
myHashMap.put(1, 1)          # The map is now [[1,1]]
myHashMap.put(2, 2)          # The map is now [[1,1], [2,2]]
print(myHashMap.get(1))      # return 1, The map is now [[1,1], [2,2]]
print(myHashMap.get(3))      # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1)          # The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.get(2))      # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2)          # remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2))      # return -1 (i.e., not found), The map is now [[1,1]]


