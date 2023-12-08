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
title_jy = "Course-Schedule-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There are a total of ``numCourses`` courses you have to take, labeled from 0 to
``numCourses`` - 1. You are given an array ``prerequisites`` where prerequisites[i] = [ai, bi]
indicates that you must take course ``bi`` first if you want to take course ``ai``.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid
answers, return any of them. If it is impossible to finish all courses, return an empty array.


Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should
             have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have
             finished both courses 1 and 2. Both courses 1 and 2 should be taken after
             you finished course 0. So one correct course order is [0,1,2,3]. Another
             correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""


import collections
from typing import List


class Solution:
    """
解法1: 在 207_Course-Schedule.py 的解法 1 的基础上额外传入一个参数维护结课的课程列表
    """
    def findOrder_v1(self, numCourses: int, prerequisites: List[List[int]]) \
            -> List[int]:
        dependency = collections.defaultdict(list)
        order = []
        finished = set()

        for course, prerequisite in prerequisites:
            dependency[course].append(prerequisite)

        for i in range(numCourses):
            if not self._can_finish(i, dependency, set(), finished, order):
                return []

        return order

    def _can_finish(self, course, dependency, visited, finished, order):
        if course in visited and course not in finished:
            return False

        if course in finished:
            return True

        visited.add(course)

        if course in dependency:
            for prerequisite in dependency[course]:
                if not self._can_finish(prerequisite, dependency,
                                        visited, finished, order):
                    return False

        finished.add(course)
        order.append(course)

        return True

    """
解法2: 在 207_Course-Schedule.py 的解法 2 的基础上额外维护结课的课程列表
    """
    def findOrder_v2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependency = collections.defaultdict(list)
        degrees = [0] * numCourses
        # jy: 记录课程的完成顺序;
        order = []

        # 用字典 dependency 记录依赖于课程 prerequisite 的所有课程(列表保存)
        for course, prerequisite in prerequisites:
            dependency[prerequisite].append(course)
            degrees[course] += 1

        # jy: 初始化队列为不依赖其他课程的课(即对应课程编号的课程依赖数是 0 的课程)
        queue = collections.deque([course for course, degree in enumerate(degrees) if degree == 0])
        # jy: 如果队列中有不依赖于其他课程的课, 则优先完成(出队)该课程, 并获取依赖于该课程的
        #     所有其它课程 next_course, 将其依赖的课程数减 1(如果减 1 后依赖的课程数为 0, 表
        #     明该课程不依赖于其它课程, 将其入队, 后续继续完成(出队)并获取依赖于该课程的课程;
        while queue:
            course = queue.popleft()
            order.append(course)
            for next_course in dependency[course]:
                degrees[next_course] -= 1

                if degrees[next_course] == 0:
                    queue.append(next_course)
        # jy: 当队列为空时, 如果 degrees 中所有的课程均不再有依赖数, 则表明可以完成所有课程;
        return order if sum(degrees) == 0 else []



numCourses = 2
prerequisites = [[1, 0]]
# Output: [0,1]


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# Output: [0,2,1,3]


numCourses = 1
prerequisites = []
# Output: [0]


