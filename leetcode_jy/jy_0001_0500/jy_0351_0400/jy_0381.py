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
title_jy = "Insert-Delete-GetRandom_Duplicates-allowed(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Implement the RandomizedCollection class:
RandomizedCollection(): Initializes the RandomizedCollection object.
bool insert(int val): Inserts an item val into the multiset if not present.
                      Returns true if the item was not present, false otherwise.
bool remove(int val): Removes an item val from the multiset if present. Returns true if the item was
                      present, false otherwise. Note that if val has multiple occurrences in the
                      multiset, we only remove one of them.
int getRandom(): Returns a random element from the current multiset of elements (it's guaranteed that
                 at least one element exists when this method is called). The probability of each element
                 being returned is linearly related to the number of same values the multiset contains.


Example 1:
RandomizedCollection randomizedCollection = new RandomizedCollection();
randomizedCollection.insert(1);     # return True. Inserts 1 to the collection. Returns true as the
                                    # collection did not contain 1.
randomizedCollection.insert(1);     # return False. Inserts another 1 to the collection. Returns false
                                    # as the collection contained 1. Collection now contains [1, 1].
randomizedCollection.insert(2);     # return True. Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
randomizedCollection.getRandom();   # getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
randomizedCollection.remove(1);     # return True. Removes 1 from the collection, returns true. Collection now contains [1,2].
randomizedCollection.getRandom();   # getRandom should return 1 and 2 both equally likely.


Constraints:
-2^31 <= val <= 2^31 - 1
At most 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.


Follow up: Could you implement the functions of the class with each function works in average O(1) time?
"""



"""
在 380_Insert-Delete-GetRandom.py  O(1) 的基础上, 使用 Map 保存每个数字在列表中的位置的时候, Map 的值类型
为 Set, 因为一个数字有可能出现多次:
insert: 直接将 val 放到列表末尾, 然后将 val 对应的列表位置放到 Map 中, 最后判断 Map 中 val 的位置的长度是否只有 1 个;
remove: 首先通过 Map 知道要删除的元素在列表中的位置 (因为有可能有多个, 随意取一个即可, 这里使用 pop), 然后将该
        位置的元素和列表的最后一个元素进行交换, 然后更新最后一个元素的索引位置, 最后删除列表的最后一个元素即可;
getRandom: 根据列表的长度生成随机数作为要返回元素的下标, 然后返回该元素
"""
import random

class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.position = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection.
        Returns true if the collection did not already contain the specified element.
        """
        # jy: 将待插入的值 val 插入到列表的末尾;
        self.values.append(val)
        # jy: 如果待插入的值 val 已经在 positions 字典中, 则在原有该值的位置集合中再次添加新位置;
        if val in self.position:
            self.position[val].add(len(self.values) - 1)
        # jy: 如果待插入的值 val 还不在 positions 字典中, 即表示第一次插入, 将该值记录到 positions
        #    字典中, 并初始化一个集合, 存放该值在列表中出现的位置;
        else:
            self.position[val] = {len(self.values) - 1}
        # jy: 如果位置集合中的位置只有 1 个, 表明之前没有该值, 是此次添加进去的, 返回 True;
        return len(self.position[val]) == 1


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection.
        Returns true if the collection contained the specified element.
        """
        # jy: 如果该值不存在于列表中, 直接返回 False;
        if val not in self.position or not self.position[val]:
            return False
        # jy: 获取该值在列表中出现的位置 i, 以及列表中最后一个值;
        i, last = self.position[val].pop(), self.values[-1]
        # jy: 将列表中最后一个值更新到位置 i 中(即将原位置 i 的值删除)
        self.values[i] = last
        # jy: 由于最后一个值被重新放置到位置 i 中(原最后的数值在以下会被删除), 故需要更新该
        #    值在列表中所在的位置: 添加该值的新位置 i, 并删除该值的老位置(即列表的最后值下
        #    标);  以下的 if 判断可直接去掉(已测试), 因为 last 代表的最后一个值肯定是存在的;
        if self.position[last]:
            self.position[last].add(i)
            self.position[last].remove(len(self.values) - 1)
        # jy: 从列表中删除最后一个值(已经被移动到位置 i 中了)
        self.values.pop()

        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.values[random.randint(0, len(self.values) - 1)]


randomizedCollection = RandomizedCollection()
print(randomizedCollection.insert(1))     # return True. Inserts 1 to the collection. Returns true as the
                                          # collection did not contain 1.
print(randomizedCollection.insert(1))     # return False. Inserts another 1 to the collection. Returns false
                                          # as the collection contained 1. Collection now contains [1,1].
print(randomizedCollection.insert(2))     # return True. Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
print(randomizedCollection.getRandom())   # getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
print(randomizedCollection.remove(1))     # return True. Removes 1 from the collection, returns true. Collection now contains [1,2].
print(randomizedCollection.getRandom())   # getRandom should return 1 and 2 both equally likely.


