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
title_jy = "Meeting-Scheduler(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.
If there is no common time slot that satisfies the requirements, return an empty array.
The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.
It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

Example 1:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]

Example 2:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []


Constraints:
1 <= slots1.length, slots2.length <= 10^4
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 10^9
1 <= duration <= 10^6
"""


from typing import List


class Solution:
    """
在 986. Interval List Intersections 的基础判断当两个区间相交时, 相交部分的长度是否大于等于 duration
    """
    def minAvailableDuration(self, slots1: List[List[int]],
                             slots2: List[List[int]], duration: int) \
            -> List[int]:
        i = j = 0
        sorted_slots1 = sorted(slots1, key=lambda x: x[0])
        sorted_slots2 = sorted(slots2, key=lambda x: x[0])

        while i < len(sorted_slots1) and j < len(sorted_slots2):
            a_start, a_end = sorted_slots1[i]
            b_start, b_end = sorted_slots2[j]

            if a_start < b_end and b_start < a_end \
                    and min(a_end, b_end) - max(a_start, b_start) >= duration:
                start = max(a_start, b_start)

                return [start, start + duration]

            if a_end <= b_end:
                i += 1
            else:
                j += 1

        return []


