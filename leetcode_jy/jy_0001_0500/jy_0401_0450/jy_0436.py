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
title_jy = "Find-Right-Interval(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an array of intervals, where intervals[i] = [start_i, end_i] and each
``start_i`` is unique. The right interval for ``intervals[i]`` is ``intervals[j]``
such that ``start_j`` >= ``end_i`` and ``start_j`` is minimized.

Return an array of right interval indices for each interval ``i``. If no right interval
exists for interval ``i``, then put -1 at index ``i``.

Example 1:
Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
             The right interval for [2,3] is [3,4] since start_0 = 3 is the smallest start that is >= end_1 = 3.
             The right interval for [1,2] is [2,3] since start_1 = 2 is the smallest start that is >= end_2 = 2.

Example 3:
Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: There is no right interval for [1,4] and [3,4].
             The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.


Constraints:
1 <= intervals.length <= 2 * 10^4
intervals[i].length == 2
-10^6 <= starti <= endi <= 10^6
The start point of each interval is unique.
"""


from typing import List


class Solution:
    """
题解: 将区间按照开始时间排序, 同时记录各区间对应的位置, 遍历排序后的区间, 使用
二分查找寻找后续区间满足开始时间大于等于当前区间的结束时间, 注意搜索时需要包括
当前区间, 因为题目描述中的 i 和 j 可以相等
    """
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sorted_intervals = [(interval, i) for i, interval
                            in enumerate(intervals)]
        sorted_intervals = sorted(sorted_intervals, key=lambda x: x[0][0])
        result = [-1] * n

        for i, interval in enumerate(sorted_intervals):
            end = interval[0][1]
            j = self._binary_search(sorted_intervals, i, n - 1, end)

            if j < n:
                result[interval[1]] = sorted_intervals[j][1]

        return result

    def _binary_search(self, intervals, low, high, target):
        while low <= high:
            middle = low + (high - low) # 2
            start, end = intervals[middle][0]

            if start == target:
                return middle
            elif start > target:
                high = middle - 1
            else:
                low = middle + 1

        return low


intervals = [[1, 2]]
# Output: [-1]
res = Solution().findRightInterval(intervals)
print(res)


intervals = [[3, 4], [2, 3], [1, 2]]
# Output: [-1,0,1]
res = Solution().findRightInterval(intervals)
print(res)


intervals = [[1, 4], [2, 3], [3, 4]]
# Output: [-1,2,-1]
res = Solution().findRightInterval(intervals)
print(res)


