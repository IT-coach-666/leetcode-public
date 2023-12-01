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
title_jy = "Design-HashSet(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design a HashSet without using any built-in hash table libraries.
Implement MyHashSet class:
void add(key) :      Inserts the value ``key`` into the HashSet.
bool contains(key) : Returns whether the value ``key`` exists in the HashSet or not.
void remove(key) :   Removes the value ``key`` in the HashSet. If ``key`` does not
                     exist in the HashSet, do nothing.


Example 1:
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);        # set = [1]
myHashSet.add(2);        # set = [1, 2]
myHashSet.contains(1);   # return True
myHashSet.contains(3);   # return False, (not found)
myHashSet.add(2);        # set = [1, 2]
myHashSet.contains(2);   # return True
myHashSet.remove(2);     # set = [1]
myHashSet.contains(2);   # return False, (already removed)


Constraints:
0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.
"""


from collections import deque


"""
数组 + 二叉搜索树: 二叉搜索树的插入和删除同 701_Insert-into-a-Binary-Search-Tree.py 和
450_Delete-Node-in-a-BST.py;
"""
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add(self, node):
        """
        二叉搜索树的插入节点操作同 701_Insert-into-a-Binary-Search-Tree.py
        """
        # jy: 如果待插入的节点值大于当前的节点值(即调用该 add 方法的节点的值), 则将
        #    待插入的节点插入到当前节点的右子节点(如果右子节点为空, 则直接将该节点
        #    作为右子节点, 如果右子节点不为空, 则调用右子节点的 add 方法将待插入节
        #    点插入)
        if node.value > self.value:
            if not self.right:
                self.right = node
            else:
                self.right.add(node)
        # jy: 如果待插入节点的值小于当前节点值(即调用该 add 方法的节点的值), 则将待
        #    插入的节点插入到当前节点的左子节点(如果左子节点为空, 则直接将该节点作
        #    为左子节点, 如果左子节点不为空, 则调用左子节点的 add 方法将待插入节点
        #    插入)
        elif node.value < self.value:
            if not self.left:
                self.left = node
            else:
                self.left.add(node)

    def contains(self, value):
        # jy: 调用 contains 方法的对象是一个 Node 节点(视为根节点): 从根节点开始, 判断
        #    该树中是否包含 值为 value 的节点;
        # jy: 如果当前节点(即根节点)的值等于待查找值 value, 直接返回 True;
        if self.value == value:
            return True
        # jy: 如果当前节点(即根节点)的值大于待查找值 value, 则从根节点的左子树中查找目标
        #    值(查找时要先确保左子节点存在, 在存在的基础上才能进一步调用左子节点的 contains
        #    方法不断深入查找; 如果最终查找存在, 则返回 True, 否则会遍历到不存在的左/右子
        #    节点, 即返回 None, 即 False)
        elif self.value > value:
            # jy: 目标是要返回 False, 与 True 对立, 而以下可能返回的是 None, 修改规范
            #    化, 使得可以通过 leetcode 验证:
            # return self.left and self.left.contains(value)
            if not self.left:
                return False
            else:
                return self.left.contains(value)
        # jy: 如果根节点值小于待查找的目标值, 则应从根节点右子树中查找目标值, 查找过程同理;
        else:
            # jy: 目标是要返回 False, 与 True 对立, 而以下可能返回的是 None, 修改规范
            #    化, 使得可以通过 leetcode 验证:
            # return self.right and self.right.contains(value)
            if not self.right:
                return False
            else:
                return self.right.contains(value)

    def remove(self, value):
        """
        二叉搜索树的删除节点操作, 同 450_Delete-Node-in-a-BST.py
        """
        # jy: 如果待删除的节点值等于当前节点(根节点)值, 则判断:
        #    1) 如果根节点值均无左右子树, 则直接返回 None(删除后直接为 None)
        #    2) 如果根节点有左子树或右子树(不同时存在), 则删除根节点后直接返
        #       回左或右子节点(即为删除后的根节点)
        #    3) 如果左右子节点均存在, 则先找出右子树中的最小值, 并将当前节点(根节点)的值
        #       更新为该值(即原值已被删除), 随后将右子树中的该最小值删除;
        if self.value == value:
            if not self.left and not self.right:
                return None
            elif not self.left or not self.right:
                return self.left or self.right
            else:
                self.value = self.right._find_min().value
                self.right = self.right.remove(self.value)
        # jy: 如果待删除的节点值小于当前节点(根节点)值, 则应从左子节点(左子树)中删除该值;
        elif self.value > value and self.left:
            self.left = self.left.remove(value)
        # jy: 如果待删除的节点值大于当前节点(根节点)值, 则应从右子节点(右子树)中删除该值;
        elif self.value < value and self.right:
            self.right = self.right.remove(value)
        # jy: 最终仍返回当前节点(即根节点)
        return self

    def traverse(self):
        # jy: 调用该 traverse 方法的是一个 Node 节点(树根节点), 即 self 代表根节点,
        #    该方法会遍历整棵树的节点, 并存放入列表中最终返回;
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
        """二叉搜索树中找最小值节点: 不断遍历左子节点, 直到某节点的左子节点为空, 则该节点值为最小"""
        current = self
        while current.left:
            current = current.left
        return current



class MyHashSet_v1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # jy: 用于存放多个树, 列表值如果非 None, 则代表为一棵二叉搜索树(列表值为其根节点)
        self.nodes = [None] * 16
        # jy: 用于记录当前 HashSet 中的元素总个数(即 self.nodes 中所有树的所有节点个数);
        self.size = 0
        # jy: 用于记录当插入的值(即所有二叉搜索树节点)超过 len(self.nodes) * self.load_factor 时
        #    就要扩充 self.nodes 长度为原来的两倍;
        self.load_factor = 0.75

    def add(self, key: int) -> None:
        # jy: 判断当前待插入的 key 值被 hash 到 self.nodes 中的哪个位置(通过 key 与
        #    self.nodes 的长度相除取余数获取; self.nodes 的长度初始化设定, 为 16)
        h = self._hash(key)
        # jy: 将待插入的 key 值构造成值为 key 的树节点;
        new_node = Node(key)
        # jy: 如果 self.nodes 中的 h 位置还没有树根节点, 则直接将当前节点作为该位置
        #    的树根节点;
        if not self.nodes[h]:
            self.nodes[h] = new_node
        # jy: 如果 self.nodes 中的 h 位置已经有树根节点, 则在该树根节点(self.nodes[h])
        #    中插入当前新节点;
        else:
            self.nodes[h].add(new_node)
        # jy: 每插入一个元素后, HashSet 类的 size 属性加 1;
        self.size += 1

        # jy: 如果当前 HashSet 中的元素总个数大于当前 self.nodes 长度的 3/4, 则进行重新哈希;
        #    经验证, 此部分逻辑去除也不影响算法正常执行(leetcode 中注释掉此处代码也可正常通
        #    过), 只是去除后平均算法耗时有所增加(执行时间会平均多出大致 50ms);
        if self.size > self.load_factor * len(self.nodes):
            self._rehash()

    def remove(self, key: int) -> None:
        # jy: 判断当前待删除的 key 值被 hash 到 self.nodes 中的哪个位置(通过 key 与
        #    self.nodes 的长度相除取余数获取; self.nodes 的长度初始化设定, 为 16)
        h = self._hash(key)
        # jy: 如果 self.nodes 中的 h 位置已经有树根节点, 则在该节点基础上删除值为 key
        #    的节点(二叉搜索树删除节点后, 最终返回删除后的树根节点), 并将HashSet 类
        #    的 size 属性减 1;
        if self.nodes[h]:
            self.nodes[h] = self.nodes[h].remove(key)
            self.size -= 1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        # jy: 判断当前待查找的 key 值被 hash 到 self.nodes 中的哪个位置(通过 key 与
        #    self.nodes 的长度相除取余数获取; self.nodes 的长度初始化设定, 为 16)
        h = self._hash(key)
        # print("====h==== ", h, "====self.nodes[h].value====", self.nodes[h].value)
        # jy: 如果该位置有树的根节点存在, 则从该位置的树的根节点查找值为 key 的节点
        #    是否存在;
        if self.nodes[h]:
            print("====self.nodes[h].contains(key)===", self.nodes[h].contains(key))
            return self.nodes[h].contains(key)
        # jy: 如果该位置没有树节点, 直接返回 False
        return False

    def _rehash(self):
        # jy: 将原先的 self.nodes 先暂存起来, 并设置新的 self.nodes 为原先长度的
        #    两倍, 初始值均为 None;
        new_nodes = [None] * (len(self.nodes) * 2)
        old_nodes = self.nodes
        self.nodes = new_nodes
        # jy: 循环遍历原先的 self.nodes 中的树根节点(代表整棵树): 如果节点为空, 则直接跳过遍历下一个;
        #
        for node in old_nodes:
            if not node:
                continue
            # jy: node 代表一棵树的根节点, 调用 node 的 traverse 方法会将以 node 节点为根节点的树中
            #    的所有节点加入列表中, 最终返回(即获取以 node 为根节点的树的所有节点);  此处即将
            #    node 代表的树的所有节点重新加入到当前 MyHashSet_v1 类中(依据节点值的哈希结果加入
            #    到 self.nodes 列表的对应位置的树上);  即当 self.nodes 扩充后, 其中对于的树也在原
            #    先树的基础上进行重构;
            for n in node.traverse():
                self.add(n.value)

    def _hash(self, key):
        # jy: self.nodes 为一个长度为 16 的列表;
        return key % len(self.nodes)


"""
时间复杂度为 O(1), 空间复杂度为 O(数据范围)
"""
class MyHashSet_v2:
    def __init__(self):
        self.set = [False] * 1000001

    def add(self, key):
        self.set[key] = True

    def remove(self, key):
        self.set[key] = False

    def contains(self, key):
        return self.set[key]



myHashSet = MyHashSet_v1()
myHashSet.add(1)               # set = [1]
myHashSet.add(2)               # set = [1, 2]
print(myHashSet.contains(1))   # return True
print(myHashSet.contains(3))   # return False, (not found)
myHashSet.add(2)               # set = [1, 2]
print(myHashSet.contains(2))   # return True
myHashSet.remove(2)            # set = [1]
print(myHashSet.contains(2))   # return False, (already removed)

print("="*88)

myHashSet = MyHashSet_v2()
myHashSet.add(1)               # set = [1]
myHashSet.add(2)               # set = [1, 2]
print(myHashSet.contains(1))   # return True
print(myHashSet.contains(3))   # return False, (not found)
myHashSet.add(2)               # set = [1, 2]
print(myHashSet.contains(2))   # return True
myHashSet.remove(2)            # set = [1]
print(myHashSet.contains(2))   # return False, (already removed)


