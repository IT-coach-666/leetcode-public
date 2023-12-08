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
title_jy = "Intersection-of-Two-Arrays-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
appear as many times as it shows in both arrays and you may return the result in any order.


Example 1:
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2, 2]

Example 2:
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [4, 9]
Explanation: [9, 4] is also accepted.


Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


Follow up:
1) What if the given array is already sorted? How would you optimize your algorithm?
2) What if nums1's size is small compared to nums2's size? Which algorithm is better?
3) What if elements of nums2 are stored on disk, and the memory is limited such that
   you cannot load all elements into the memory at once?
"""


import collections
from typing import List


class Solution:
    """
解法1: 使用 Map 保存两个数组中每个元素出现的次数, 然后遍历第一个 Map, 保留两个 Map 中公共的元素;
    """
    def intersect_v1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        result = []

        for key, value in counter1.items():
            if key in counter2:
                result.extend([key] * min(value, counter2[key]))

        return result


    """
解法2: 将两个数组排好序, 然后使用两个指针分别指向两个数组的头部, 如果第一个数组的元素的值小于
第二个数组, 则第一个数组的指针向右移动一位, 如果第一个数组的元素的值大于第二个数组, 则第二个
数组的指针向右移动一位, 如果两个数组的值相等, 则将当前元素添加的最终结果中, 同时两个数组的指
针都向右移动一位;
    """
    def intersect_v2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted1 = sorted(nums1)
        sorted2 = sorted(nums2)
        result = []
        i = j = 0

        while i < len(sorted1) and j < len(sorted2):
            if sorted1[i] < sorted2[j]:
                i += 1
            elif sorted1[i] > sorted2[j]:
                j += 1
            else:
                result.append(sorted1[i])
                i += 1
                j += 1

        return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
# Output: [2, 2]
res = Solution().intersect_v1(nums1, nums2)
print(res)


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
# Output: [4, 9]
res = Solution().intersect_v2(nums1, nums2)
print(res)


