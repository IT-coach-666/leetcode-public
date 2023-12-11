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
title_jy = "Course-Schedule-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There are ``n`` different online courses numbered from 1 to n. You are given an array
``courses`` where ``courses[i] = [durationi, lastDayi]`` indicate that the ``ith``
course should be taken continuously for ``durationi`` days and must be finished before
or on ``lastDayi``. You will start on the 1st day and you cannot take two or more courses
simultaneously. Return the maximum number of courses that you can take.



Example 1:
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation: There are totally 4 courses, but you can take 3 courses at most:
1) take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

Example 2:
Input: courses = [[1,2]]
Output: 1

Example 3:
Input: courses = [[3,2],[4,3]]
Output: 0


Constraints:
1 <= courses.length <= 10^4
1 <= durationi, lastDayi <= 10^4
"""


import heapq
from typing import List


class Solution:
    """
将课程按照截止时间从小到大排序, 使用大顶堆维护当前已选的课程的持续时间, 遍历排序后的课程, 记录当前所选课程完成需要的总时间, 如果总时间大于当前课程的截止时间, 则从大顶堆中剔除堆顶的元素, 即需要花费时间最多的课程, 最后堆的大小就是能完成的课程数
    """
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        sorted_courses = sorted(courses, key=lambda x: x[1])
        total_time = 0

        for course in sorted_courses:
            total_time += course[0]
            heapq.heappush(heap, -course[0])

            if total_time > course[1]:
                total_time -= -heapq.heappop(heap)

        return len(heap)


