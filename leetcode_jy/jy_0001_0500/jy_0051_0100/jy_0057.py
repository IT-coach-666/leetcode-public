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
title_jy = "Insert-Interval(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an array of non-overlapping intervals ``intervals`` where
intervals[i] = [start_i, end_i] represent the start and the end of the i-th interval
and ``intervals`` is sorted in ascending order by start_i. You are also given an
interval ``newInterval = [start, end]`` that represents the start and end of another
interval. Insert ``newInterval`` into ``intervals`` such that ``intervals`` is still
sorted in ascending order by start_i and ``intervals`` still does not have any
overlapping intervals (merge overlapping intervals if necessary). Return intervals
after the insertion.


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]


Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""


from typing import List


class Solution:
    """
解法1: 将 newInterval 加入到 intervals 并按区间起始位置排序, 相应问题变为 056_Merge-Intervals.py
    """
    def insert_v1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sorted_intervals = sorted(intervals + [newInterval], key=lambda x: x[0])
        merged = [sorted_intervals[0]]
        # jy: 对区间进行合并(区间已按开始时间进行排序)
        for i in range(1, len(sorted_intervals)):
            top = merged[-1]
            current = sorted_intervals[i]
            # jy: current[0] 必须是在 top[0] 到 top[1] 之间才会重合, 重合区间的顶
            #    是 top[1] 和 current[1] 中的较大值(可画图理解);
            if top[0] <= current[0] <= top[1]:
                merged[-1][1] = max(merged[-1][1], current[1])
            else:
                merged.append(current)

        return merged

    """
解法2:
1) 遍历 intervals, 跳过和 newInterval 不相交的区间
2) 将 intervals 和 newInterval 相交的区间不断更新到 newInterval 上, 直到 intervals 和
   newInterval 不相交, 最后添加上 intervals 剩下的区间;
    """
    def insert_v2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i, n = 0, len(intervals)
        # jy: 遍历 intervals, 跳过和 newInterval 不相交的区间(将不相交的区间先加入 merged 结果中)
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        # jy: 将 intervals 和 newInterval 相交的区间不断更新到 newInterval 上, 直到 intervals
        #    和 newInterval 不相交;
        # jy: 经过以上 while 循环, 有: intervals[i][1] >= newInterval[0], 即此时的 intervals[i][1]
        #    肯定是跟 newInterval[0] 有重合的, 将此时的 intervals[i] 与 newInterval 合并为新的
        #    newInterval, 接着判断下一个新的 intervals[i] 是否与新的 newInterval 有重合, 如果还重
        #    合, 则继续将 intervals[i] 与 newInterval 合并(直到下一个 intervals[i][0] > newInterval[1]
        #    时, 不会重合, 此时先加入 newInterval, 再将剩余的 intervals 加入排序结果中)
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        merged.append(newInterval)

        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged

    """
JY: 思路同解法 2;
    """
    def insert_jy(self, intervals: List[List[int]], new_i: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            # jy: 如果当前区间的 end 小于待插入区间的 start, 表明区间不重合, 且
            #    当前区间排在前面, 先将其加入结果列表;
            if interval[1] < new_i[0]:
                res.append(interval)
            # jy: 如果当前区间的 start 大于待插入区间的 end, 表明区间不重合, 且
            #    待插入区间排在前面, 先将其加入结果列表;
            elif interval[0] > new_i[1]:
                res.append(new_i)
                new_i = interval
            # jy: 其它情况则表明当前区间与待插入的区间有重合, 基于当前 interval 对 new_i 进行更新;
            else:
                new_i = [min(interval[0], new_i[0]), max(interval[1], new_i[1])]
        res.append(new_i)
        return res



intervals = [[1,3],[6,9]]
newInterval = [2,5]
# Output: [[1,5],[6,9]]
res = Solution().insert_v1(intervals, newInterval)
print(res)


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
res = Solution().insert_v1(intervals, newInterval)
print(res)


intervals = []
newInterval = [5,7]
# Output: [[5,7]]
res = Solution().insert_v1(intervals, newInterval)
print(res)


intervals = [[1,5]]
newInterval = [2,3]
# Output: [[1,5]]
res = Solution().insert_v2(intervals, newInterval)
print(res)


intervals = [[1,5]]
newInterval = [2,7]
# Output: [[1,7]]
res = Solution().insert_v2(intervals, newInterval)


