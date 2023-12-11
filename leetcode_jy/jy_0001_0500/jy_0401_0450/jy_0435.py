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
title_jy = "Non-overlapping-Intervals(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of intervals ``intervals`` where intervals[i] = [start_i, end_i], return the
minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:
1 <= intervals.length <= 10^5
intervals[i].length == 2
-5 * 10^4 <= starti < endi <= 5 * 10^4
"""


from typing import List


class Solution:
    """
将区间按照结束时间排序, 记录上一个区间的结束时间, 从第二个区间开始遍历, 如果上一个区间
的结束时间大于当前区间的开始时间, 说明存在重叠, 需要将当前区间删除, 否则将当前区间的结
束时间作为新的上一个区间的结束时间
    """
    def eraseOverlapIntervals_v1(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        end = sorted_intervals[0][1]
        count = 0

        for i in range(1, len(sorted_intervals)):
            if end > sorted_intervals[i][0]:
                count += 1
            else:
                end = sorted_intervals[i][1]

        return count


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
# Output: 1
res = Solution().eraseOverlapIntervals_v1(intervals)
print(res)


intervals = [[1, 2], [1, 2], [1, 2]]
# Output: 2
res = Solution().eraseOverlapIntervals_v1(intervals)
print(res)


intervals = [[1, 2], [2, 3]]
# Output: 0
res = Solution().eraseOverlapIntervals_v1(intervals)
print(res)


