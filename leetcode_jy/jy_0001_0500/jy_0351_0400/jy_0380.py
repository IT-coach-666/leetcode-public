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
title_jy = "Insert-Delete-GetRandom(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Implement the RandomizedSet class:
RandomizedSet(): Initializes the RandomizedSet object.
bool insert(int val): Inserts an item val into the set if not present.
                      Returns true if the item was not present, false otherwise.
bool remove(int val): Removes an item val from the set if present.
                      Returns true if the item was present, false otherwise.
int getRandom(): Returns a random element from the current set of elements (it's guaranteed that
                 at least one element exists when this method is called). Each element must have
                 the same probability of being returned.


Example 1:
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1);   # Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2);   # Returns false as 2 does not exist in the set.
randomizedSet.insert(2);   # Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); # getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1);   # Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2);   # 2 was already in the set, so return false.
randomizedSet.getRandom(); # Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:
-2^31 <= val <= 2^31 - 1
At most 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.


Follow up: Could you implement the functions of the class with each function works in average O(1) time?
"""




import random

"""
使用列表保存所有的数字, 再使用一个 Map 保存每个数字在列表中的位置;
insert: 判断 val 是否在 Map 中, 如果不存在则将 val 添加到列表的末尾, 并放到 Map 中;
remove: 这里有个技巧, 为了避免在随机访问列表中删除某个元素带来的定位和元素移动的开
        销, 这里首先通过 Map 知道要删除的元素在列表中的位置, 然后将该位置的元素和列
        表的最后一个元素进行交换, 最后删除列表的最后一个元素即可;
getRandom: 根据列表的长度生成随机数作为要返回元素的下标, 然后返回该元素;
"""
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # jy: 列表用于保存所有数字, 字典用于保存每个数字在列表中的位置;
        self.values = []
        self.position = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set.
        Returns true if the set did not already contain the specified element.
        """
        if val in self.position:
            return False

        self.values.append(val)
        self.position[val] = len(self.values) - 1
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set.
        Returns true if the set contained the specified element.
        """
        if val not in self.position:
            return False
        # jy: i 为 val 值在列表中的下标, last 为列表中的最后一个数值;
        i, last = self.position[val], self.values[-1]
        # jy: 将列表中最后一个数值与下标为 i 的数值进行交换, 随后 pop 掉列表最后的数值, 即
        #    删除(删除时同时删除字典中的 val 值);
        self.values[i], self.position[last] = last, i
        self.values.pop()
        self.position.pop(val)

        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # jy: 依据列表长度生成一个有效的随机下标, 然后依据该随机下标获取随机数;
        return self.values[random.randint(0, len(self.values) - 1)]


randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))   # Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomizedSet.remove(2))   # Returns false as 2 does not exist in the set.
print(randomizedSet.insert(2))   # Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.getRandom()) # getRandom() should return either 1 or 2 randomly.
print(randomizedSet.remove(1))   # Removes 1 from the set, returns true. Set now contains [2].
print(randomizedSet.insert(2))   # 2 was already in the set, so return false.
print(randomizedSet.getRandom()) # Since 2 is the only number in the set, getRandom() will always return 2.


