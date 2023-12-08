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
title_jy = "Two-Sum-III_Data-structure-design(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design and implement a TwoSum class. It should support the following operations: add and find.
add  - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.


Example 1:
add(1);
add(3);
add(5);
find(4) -> true
find(7) -> false

Example 2:
add(3);
add(1);
add(2);
find(3) -> true
find(6) -> false
"""



class TwoSum_v1:
    """
解法1: 最直观的解法是直接复用 001_Two-Sum.py 的代码, 内部同样使用一个数组来存储数字; 不过
最后提交的时候这种解法只比三分之一的人快, 所以必然有更高效的解法;
    """
    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:
        mapping = {}

        for index, v in enumerate(self.nums):
            if value - v in mapping:
                return True
            else:
                mapping[v] = index

        return False



class TwoSum_v2:
    """
解法2: 本题和原来的 001_Two-Sum.py 的区别在于不需要返回满足条件的两个数的下标, 只要知道是否存在即可; 所
以可以直接使用哈希表作为内部的数据结构, 哈希表的键为数字, 值为该数字出现的次数; 然后遍历哈希表, 对于哈希
表中的每一个元素 n, 判断 value - n 是否在哈希表中, 如果存在且不等于 n, 或者存在但等于 n 且 n 在哈希表中
的个数大于 1, 则返回 true;
    """
    def __init__(self):
        self.nums = {}

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value: int) -> bool:
        for v in self.nums:
            diff = value - v
            if diff in self.nums and (diff != v or self.nums[diff] > 1):
                return True

        return False

res = TwoSum_v1()
res.add(1)
res.add(3)
res.add(5)
print(res.find(4)) #-> true
print(res.find(7)) #-> false


res = TwoSum_v2()
res.add(3)
res.add(1)
res.add(2)
print(res.find(3)) #-> true
print(res.find(6)) #-> false


