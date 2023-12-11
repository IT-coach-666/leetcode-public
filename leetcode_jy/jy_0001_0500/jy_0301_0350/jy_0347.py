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
title_jy = "Top-K-Frequent-Elements(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.


Example 1:
Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(nlogn), where n is the array's size.
"""


import collections
from typing import List


class Solution:
    """
解法1: 使用 Map 保存每个数字出现的次数, 然后对 Map 中的项按照出现次数排序, 最后返回前 k 个数字;
    """
    def topKFrequent_v1(self, nums: List[int], k: int) -> List[int]:
        # jy: 统计 nums 中元素的出现次数(得到一个字典, key 为 nums 中的数值, value 为出现的次数);
        frequencies = collections.Counter(nums)
        # jy: 对 frequencies 字典基于 value (即出现次数) 进行反向排序;
        sort_by_frequency = sorted(list(frequencies.items()), key=lambda x: x[1], reverse=True)
        # jy: 返回已排序的字典的前 k 个 key 值(即 nums 中的元素);
        return list(map(lambda x: x[0], sort_by_frequency))[:k]


    """
解法2: Follow up 中要求算法时间复杂度不能为 O(nlogn), 所以不能使用普通排序; 借鉴桶排序的
思想, 建立一个长度为 len(nums) + 1 的桶, 桶下标为 i 用于保存出现次数 i 次的数字, 同样首先
使用 Map 计算出每个数字出现的次数然后更新桶; 最后从后往前遍历桶, 取前 k 个元素;
    """
    def topKFrequent_v2(self, nums: List[int], k: int) -> List[int]:
        # jy: 建立一个长度为 len(nums) + 1 的桶;
        bucket = [[] for _ in range(len(nums) + 1)]
        # jy: 统计 nums 中元素的出现次数;
        frequencies = collections.Counter(nums)
        for n, frequency in frequencies.items():
            bucket[frequency].append(n)

        top_k = []
        # jy: 倒序遍历桶号;
        for i in range(len(nums), -1, -1):
            # jy: 记录剩余需要查找的元素个数, 如果剩余 0 个, 直接终止;
            left_size = k - len(top_k)
            if left_size <= 0:
                break
            # jy: 如果出现次数为 i 的元素存在, 则将其加入 top_k 列表中, 直到加满 k 个为止;
            if bucket[i]:
                top_k += bucket[i][:min(len(bucket[i]), left_size)]

        return top_k


nums = [1, 1, 1, 2, 2, 3]
k = 2
# Output: [1, 2]
res = Solution().topKFrequent_v1(nums, k)
print(res)


nums = [1]
k = 1
# Output: [1]
res = Solution().topKFrequent_v1(nums, k)
print(res)


