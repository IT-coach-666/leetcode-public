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
title_jy = "Meeting-Rooms-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of meeting time intervals consisting of start and end times
[[s1, e1], [s2, e2], ...] (si < ei), find the minimum number of conference
rooms required.


Example 1:
Input: [[0, 30], [5, 10], [15, 20]]
Output: 2

Example 2:
Input: [[7, 10], [2, 4]]
Output: 1


NOTE: input types have been changed on April 15, 2019. Please reset to default
      code definition to get new method signature.
"""


from heapq import heappush, heappop
from typing import List


class Solution:
    """
按会议的开始时间进行排序, 将第一个会议的结束时间放入一个最小堆, 遍历后续的会议,
如果堆顶对应的会议结束时间小于当前会议的开始时间, 说明堆顶的会议已结束(堆顶会议
与当前会议可以安排在同一个会议室), 则删除堆顶的元素, 并将当前会议的结束时间入堆,
最后返回堆的大小;
    """
    def minMeetingRooms_v1(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # jy: 先将会议时间区间按开始时间排序;
        intervals.sort(key=lambda x: x[0])

        # jy: 将第一个会议的结束时间放入一个最小堆;
        rooms = []
        heappush(rooms, intervals[0][1])
        # jy: 遍历后续的会议, 如果堆顶的会议的结束时间小于当前的会议的开始时间, 说明堆
        #     顶的会议已结束(堆顶会议与当前会议可以安排在同一个会议室), 删除堆顶的元素,
        #     并将当前会议的结束时间加入堆;
        for interval in intervals[1:]:
            if rooms[0] <= interval[0]:
                heappop(rooms)

            heappush(rooms, interval[1])
        # jy: 最后返回堆的大小, 即表明不能共用同一间会议室的所有会议数(即为最少会议室数);
        return len(rooms)

    """
JY: 按会议开始时间进行排序, 接着从后往前遍历会议, 如果当前会议的结束时间小于或等于上
一个会议的开始时间, 则表明当前会议可与上一个会议安排在同一个会议室, 否则会议室数需要
加 1

JY: LeetCode 需会员才能验证
    """
    def minMeetingRooms_jy(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        res = 1
        intervals.sort(key=lambda x: x[0])
        prev = intervals.pop()
        while intervals:
            current = intervals.pop()
            if current[1] <= prev[0]:
                # continue
                pass
            else:
                res += 1
            prev = current

        return res


intervals = [[0, 30], [5, 10], [15, 20]]
# Output: 2
res = Solution().minMeetingRooms_v1(intervals)
print(res)
intervals = [[0, 30], [5, 10], [15, 20]]
res = Solution().minMeetingRooms_jy(intervals)
print(res)

print("-" * 66)

intervals = [[7, 10], [2, 4]]
# Output: 1
res = Solution().minMeetingRooms_jy(intervals)
print(res)
intervals = [[7, 10], [2, 4]]
res = Solution().minMeetingRooms_jy(intervals)
print(res)

print("-" * 66)

# intervals = [[0, 30], [5, 31], [15, 20]]
# intervals = [[1, 6], [2, 5], [3, 4]]
intervals = [[1, 4], [2, 5], [3, 6]]
res = Solution().minMeetingRooms_v1(intervals)
print(res)
intervals = [[1, 4], [2, 5], [3, 6]]
res = Solution().minMeetingRooms_jy(intervals)
print(res)


