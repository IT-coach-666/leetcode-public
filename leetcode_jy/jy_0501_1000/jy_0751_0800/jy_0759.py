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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Employee-Free-Time(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
We are given a list ``schedule`` of employees, which represents the working time
for each employee.    Each employee has a list of non-overlapping Intervals, and
these intervals are in sorted order. Return the list of finite intervals representing
common, positive-length free time for all employees, also in sorted order.

We wouldn't include intervals like [5, 5] in our answer, as they have zero length.


Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common free time intervals
             would be [-inf, 1], [3, 4], [10, inf]. We discard any intervals that contain
             inf as they aren't finite.

Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]


Constraints:
1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
"""


class Solution:
    """
解法1: 先将所有的工作时间按照开始时间, 结束时间排序, 然后遍历工作时间, 维护上一段工作时
间的最晚结束时间, 如果最晚结束时间小于当前工作的开始时间, 则找到了一段空闲时间
    """
    def employeeFreeTime_v1(self, schedule):
        if not schedule:
            return []

        ls_all_intervals = []
        free_time = []

        for ls_intervals in schedule:
            for interval in ls_intervals:
                # jy: 由于只会对 interval 进行使用, 不会修改其值, 故可直接将 interval 加入 ls_all_intervals 中
                ls_all_intervals.append(interval)
                # ls_all_intervals.append((interval[0], interval[1]))

        # jy: 对区间列表进行排序(默认情况下会按开始时间进行排序);
        ls_all_intervals.sort()
        # jy: prev_end 维护之前所有会议的最大结束时间;
        prev_end = ls_all_intervals[0][1]

        for i in range(1, len(ls_all_intervals)):
            interval = ls_all_intervals[i]

            # jy: 如果之前的会议的最大结束时间小于当前会议的开始时间, 则表明有空闲时间;
            if prev_end < interval[0]:
                free_time.append((prev_end, interval[0]))

            # jy: 注意, 此处的 prev_end 不能简单优化到以上的 if 判断里面, 因为 if 判
            #     断里面只有当 prev_end 小于 interval[0] 时才会更新, 而此处的 prev_end
            #     在 prev_end < interval[0] 时也可能是要更新的, 因为 prev_end >= interval[0]
            #     的情况下不能确保 prev_end < interval[1] ;
            prev_end = max(prev_end, interval[1])

        return free_time


schedule = [
[[1, 2], [5, 6]],
[[1, 3]],
[[4, 10]]]
# Output: [(3, 4)]
res = Solution().employeeFreeTime_v1(schedule)
print(res)


schedule = [
[[1, 3], [6, 7]],
[[2, 4]],
[[2, 5], [9, 12]]]
# Output: [(5, 6), (7, 9)]
res = Solution().employeeFreeTime_v1(schedule)
print(res)


