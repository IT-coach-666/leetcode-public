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
title_jy = "Time-Based-Key-Value-Store(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Create a time-based key-value store class ``TimeMap``, that supports two operations.
1) set(string key, string value, int timestamp) : Stores the key and value, along with
                                                  the given timestamp.
2) get(string key, int timestamp) : Returns a value such that set(key, value, timestamp_prev)
                                    was called previously, with timestamp_prev <= timestamp.
                                    If there are multiple such values, it returns the one with
                                    the largest timestamp_prev.
                                    If there are no values, it returns the empty string ("").

Example 1:
kv = TimeMap()
kv.set("foo", "bar", 1)   # store the key "foo" and value "bar" along with timestamp = 1
kv.get("foo", 1)          # output "bar"
kv.get("foo", 3)          # output "bar" since there is no value corresponding to foo at timestamp
                          # 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4)
kv.get("foo", 4)          # output "bar2"
kv.get("foo", 5)          # output "bar2"


Example 2:
kv = TimeMap()
kv.set("love", "high", 10)
kv.set("love", "low", 20)
kv.get("love", 5)          # output ""
kv.get("love", 10)         # output "high"
kv.get("love", 15)         # output "high"
kv.get("love", 20)         # output "low"
kv.get("love", 25)         # output "low"


Note:
All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
"""


import collections


class TimeMap:
    """
Map 加二分查找, 使用 Map 保存不同 key 对应的值(值用列表存储, 因为相同 key 可能包含多
个时间戳的对应结果); 由于该题设计的是基于时间的 KV 数据库, 所以对于各个 key 的操作,
时间戳是递增的, 所以 Map 中保存的都是有序列表, 在有序列表中搜索可以使用二分查找;
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.kv = collections.defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        # jy: 二分查找, 在 values 列表(列表中的值为一个元组, 第一个元素值为时间戳)中找出
        #    时间戳小于或等于 timestamp 的最大值;
        values = self.kv[key]
        low, high = 0, len(values)

        while low < high:
            middle = low + (high - low) // 2

            # jy: version-1: 如果相同的 timestamp 不会有重复值, 则以下即可;
            # if values[middle][0] == timestamp:
            #     return values[middle][1]
            # elif values[middle][0] < timestamp:
            #     low = middle + 1
            # else:
            #     high = middle

            # jy: version-2:
            if values[middle][0] <= timestamp:
                low = middle + 1
            else:
                high = middle

        return '' if high == 0 else values[high - 1][1]



kv = TimeMap()
kv.set("foo", "bar", 1)   # store the key "foo" and value "bar" along with timestamp = 1
print(kv.get("foo", 1))   # output "bar"
kv.get("foo", 3)          # output "bar" since there is no value corresponding to foo at timestamp
                          # 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4)
kv.set("foo", "bar3", 4)
print(kv.get("foo", 4))   # output "bar2"
print(kv.get("foo", 5))   # output "bar2"



kv = TimeMap()
kv.set("love", "high", 10)
kv.set("love", "low", 20)
kv.get("love", 5)          # output ""
kv.get("love", 10)         # output "high"
kv.get("love", 15)         # output "high"
kv.get("love", 20)         # output "low"
kv.get("love", 25)         # output "low"


