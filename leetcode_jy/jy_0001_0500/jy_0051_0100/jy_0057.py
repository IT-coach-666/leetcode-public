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
tag_jy = "IMP | 相似题: 0056"


"""
You are given an array of non-overlapping intervals `intervals` where
intervals[i] = [start_i, end_i] represent the start and the end of the
i-th interval and `intervals` is sorted in ascending order by start_i.

You are also given an interval `newInterval = [start, end]` that represents
the start and end of another interval. 

Insert `newInterval` into `intervals` such that `intervals` is still sorted
in ascending order by start_i and `intervals` still does not have any 
overlapping intervals (merge overlapping intervals if necessary). 

Return `intervals` after the insertion.


Example 1:
Input: 
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
Output: [[1, 5], [6, 9]]

Example 2:
Input: 
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
Output: [[1, 2], [3, 10], [12, 16]]
Explanation: Because the new interval [4, 8] overlaps with [3, 5], [6, 7], [8, 10].

Example 3:
Input: 
intervals = []
newInterval = [5, 7]
Output: [[5, 7]]

Example 4:
Input: 
intervals = [[1, 5]]
newInterval = [2, 3]
Output: [[1, 5]]

Example 5:
Input: 
intervals = [[1, 5]]
newInterval = [2, 7]
Output: [[1, 7]]


Constraints:
1) 0 <= intervals.length <= 10^4
2) intervals[i].length == 2
3) 0 <= start_i <= end_i <= 10^5
4) intervals is sorted by start_i in ascending order.
5) newInterval.length == 2
6) 0 <= start <= end <= 10^5
"""


class Solution:
    """
解法 1: 先将区间插入并排序, 随后进行区间合并

将 newInterval 加入到 intervals 并按区间起始位置排序, 随后进
行区间合并, 即 0056 (Merge-Intervals)
    """
    def insert_v1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sorted_intervals = sorted(intervals + [newInterval], key=lambda x: x[0])
        merged = [sorted_intervals[0]]
        # jy: 对区间进行合并(区间已按开始时间进行排序)
        for i in range(1, len(sorted_intervals)):
            top = merged[-1]
            current = sorted_intervals[i]
            if current[0] <= top[1]:
                merged[-1][1] = max(merged[-1][1], current[1])
            else:
                merged.append(current)

        return merged

    """
解法 2: 直接一轮遍历实现
1) 遍历 intervals, 跳过和 newInterval 不相交的区间
2) 将 intervals 和 newInterval 相交的区间不断更新到 newInterval 上, 直
   到 intervals 和 newInterval 不相交, 最后添加上 intervals 剩下的区间
    """
    def insert_v2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i, n = 0, len(intervals)
        # jy: 遍历 intervals, 如果 intervals[i][1] < newInterval[0], 表明
        #     newInterval 在 intervals[i] 的后面, 两个区间不相交, 将不相交
        #     的间先加入 merged 结果中)
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        # jy: 将 intervals 和 newInterval 相交的区间不断更新到 newInterval 上,
        #     直到 intervals 和 newInterval 不相交
        # jy: 经过以上 while 循环, 有: intervals[i][1] >= newInterval[0], 表明
        #     接下来的 intervals[i] 可能与 newInterval 相交:
        #     1) 如果 intervals[i][0] > newInterval[1], 表明当前 intervals[i]
        #        和 newInterval 不相交, 可将 newInterval 先加入有序区间, 随后
        #        将 intervals 中的剩余区间加入有序区间即可
        #     2) 如果 intervals[i][0] <= newInterval[1], 表明 intervals[i] 和
        #        newInterval 有重合, 此时将 intervals[i] 与 newInterval 合并为
        #        新的 newInterval, 接着判断下一个新的 intervals[i] 是否与
        #        newInterval 有重合, 如果重合则不断合并, 直到不重合为止即可将
        #        newInterval 加入有序区间, 随后再将剩余的 intervals 加入即可
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
解法 3: 解法 2 的改写
    """
    def insert_v3(self, intervals: List[List[int]], new_i: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            # jy: 如果当前区间的末尾小于待插入区间的开头, 表明区间不重合,
            #     且当前区间排在前面, 先将其加入结果列表
            if interval[1] < new_i[0]:
                res.append(interval)
            # jy: 如果当前区间的开头大于待插入区间的末尾, 表明区间不重合,
            #     且待插入区间排在前面, 先将其加入结果列表
            elif interval[0] > new_i[1]:
                res.append(new_i)
                new_i = interval
            # jy: 其它情况则表明当前区间与待插入的区间有重合, 基于当
            #     前 interval 对 new_i 进行更新
            else:
                new_i = [min(interval[0], new_i[0]), max(interval[1], new_i[1])]
        res.append(new_i)
        return res



intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
res = Solution().insert_v1(intervals, newInterval)
# jy: [[1, 5], [6, 9]]
print(res)


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
res = Solution().insert_v1(intervals, newInterval)
# jy: [[1, 2], [3, 10], [12, 16]]
print(res)


intervals = []
newInterval = [5, 7]
res = Solution().insert_v2(intervals, newInterval)
# jy: [[5, 7]]
print(res)


intervals = [[1, 5]]
newInterval = [2, 3]
res = Solution().insert_v2(intervals, newInterval)
# jy: [[1, 5]]
print(res)


intervals = [[1, 5]]
newInterval = [2, 7]
res = Solution().insert_v3(intervals, newInterval)
# jy: [[1, 7]]
print(res)

