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
title_jy = "Intersection-of-Two-Arrays(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each
element in the result must be unique and you may return the result in any order.


Example 1:
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2]

Example 2:
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [9, 4]
Explanation: [4, 9] is also accepted.


Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""


from typing import List



class Solution:
    """
将两个数组分别转成 Set, 然后遍历第一个 Set 保留公共的元素;
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(filter(lambda x: x in set2, set1))


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
# Output: [2]
res = Solution().intersection(nums1, nums2)
print(res)


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4]
res = Solution().intersection(nums1, nums2)
print(res)


