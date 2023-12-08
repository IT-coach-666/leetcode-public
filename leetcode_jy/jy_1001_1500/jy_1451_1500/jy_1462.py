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
title_jy = "Course-Schedule-IV(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether the course uj is a prerequisite of the course vj or not. Note that if course a is a prerequisite of course b and course b is a prerequisite of course c, then, course a is a prerequisite of course c.
Return a boolean array answer, where answer[j] is the answer of the jth query.

Example 1:    https://www.yuque.com/frederick/dtwi9g/umqy9s

Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: course 0 is not a prerequisite of course 1 but the opposite is true.

Example 2:
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites and each course is independent.

Example 3:

Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]


Constraints:
2 <= numCourses <= 100
0 <= prerequisite.length <= (numCourses * (numCourses - 1) / 2)
0 <= ai, bi < n
ai != bi
All the pairs [ai, bi] are unique.
The prerequisites graph has no cycles.
1 <= queries.length <= 10^4
0 <= ui, vi < n
ui != vi
"""


import collections
from typing import List


class Solution:
    """
在 207. Course Schedule 解法2的基础上维护每门课程和其先修课程的映射, 不过这道题的描述有问题, 在描述中提到:
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1
即后面的课程是先修课程, 但在第一个示例中, 对于数组 [1,0], 有:
course 0 is not a prerequisite of course 1
又变成了前面的数字是先修课程, 根据实际验证和之前的题目不同, 这道题下前面的数字才是先修课程;
    """
    def checkIfPrerequisite(self, numCourses: int,
                            prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        prerequisite_courses = [set() for _ in range(numCourses)]

        for prerequisite, course in prerequisites:
            graph[prerequisite].append(course)
            degrees[course] += 1

        queue = collections.deque(
            [course for course, degree in enumerate(degrees) if degree == 0])

        while queue:
            course = queue.popleft()

            for next_course in graph[course]:
                degrees[next_course] -= 1
                prerequisite_courses[next_course].add(course)

                for prerequisite_course in prerequisite_courses[course]:
                    prerequisite_courses[next_course].add(prerequisite_course)

                if degrees[next_course] == 0:
                    queue.append(next_course)

        return [prerequisite in prerequisite_courses[course]
                for prerequisite, course in queries]


