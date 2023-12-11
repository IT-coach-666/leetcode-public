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
title_jy = "Remove-Interval(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).
You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.
Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]

Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]

Example 3:
Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
Output: [[-5,-4],[-3,-2],[4,5],[8,9]]


Constraints:
1 <= intervals.length <= 10^4
-10^9 <= ai < bi <= 10^9
"""


from typing import List


class Solution:
    """
解法1
首先遍历区间直接添加和 toBeRemoved 没有相交的区间, 然后判断当前区间是否和 toBeRemoved 相交对当前区间进行截断, 接着忽略所有被 toBeRemoved 覆盖的区间, 之后再次判断当前区间是否和 toBeRemoved 相交对当前区间进行截断, 最后添加剩下的区间
    """
    def removeInterval(self, intervals: List[List[int]],
                       toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)

        while i < n and intervals[i][1] <= toBeRemoved[0]:
            result.append(intervals[i])
            i += 1

        if i < n and intervals[i][0] <= toBeRemoved[0] \
                and toBeRemoved[1] <= intervals[i][1]:
            if intervals[i][0] != toBeRemoved[0]:
                result.append([intervals[i][0], toBeRemoved[0]])

            if intervals[i][1] != toBeRemoved[1]:
                result.append([toBeRemoved[1], intervals[i][1]])

            i += 1
        elif i < n and intervals[i][0] <= toBeRemoved[0] <= intervals[i][1]:
            result.append([intervals[i][0], toBeRemoved[0]])

            i += 1

        while i < n and toBeRemoved[0] <= intervals[i][0] \
                and intervals[i][1] <= toBeRemoved[1]:
            i += 1

        if i < n and intervals[i][0] <= toBeRemoved[1] <= intervals[i][1]:
            result.append([toBeRemoved[1], intervals[i][1]])
            i += 1

        result.extend(intervals[i:])

        return result

from typing import List


class Solution:
    """
解法2
更简洁的版本;
    """
    def removeInterval(self, intervals: List[List[int]],
                       toBeRemoved: List[int]) -> List[List[int]]:
        result = []

        for start, end in intervals:
            if end <= toBeRemoved[0] or start >= toBeRemoved[1]:
                result.append([start, end])
            elif start >= toBeRemoved[0] and end <= toBeRemoved[1]:
                continue
            else:
                if start < toBeRemoved[0] < end:
                    result.append([start, toBeRemoved[0]])

                if start < toBeRemoved[1] < end:
                    result.append([toBeRemoved[1], end])

        return result


