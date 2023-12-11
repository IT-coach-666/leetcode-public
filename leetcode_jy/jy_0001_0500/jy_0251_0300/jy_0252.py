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
title_jy = "Meeting-Rooms(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.


Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true


Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti < endi <= 10^6
"""


from typing import List


class Solution:
    """
将区间按照结束时间排序后遍历区间判断是否有重叠
    """
    def canAttendMeetings_v1(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])

        for i, interval in enumerate(sorted_intervals):
            if i + 1 < len(sorted_intervals) and interval[1] > sorted_intervals[i+1][0]:
                return False
        return True

    def canAttendMeetings_jy(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        for idx in range(len(sorted_intervals) - 1):
            if sorted_intervals[idx][1] > sorted_intervals[idx + 1][0]:
                return False
        return True


intervals = [[0, 30], [5, 10], [15, 20]]
# Output: false
res = Solution().canAttendMeetings_v1(intervals)
print(res)


intervals = [[7, 10], [2, 4]]
# Output: true
res = Solution().canAttendMeetings_jy(intervals)
print(res)


