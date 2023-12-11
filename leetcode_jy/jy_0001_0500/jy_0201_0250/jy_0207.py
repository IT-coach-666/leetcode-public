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
title_jy = "Course-Schedule(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There are a total of ``numCourses`` courses you have to take, labeled from 0 to
``numCourses`` - 1. You are given an array ``prerequisites`` where:
prerequisites[i] = [ai, bi] indicates that you must take course ``bi`` first if
you want to take course ``ai``.

For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1. Return true if you can finish all courses. Otherwise, return false.


Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.  To take course 1 you should have
             finished course 0, and to take course 0 you should also have finished
             course 1. So it is impossible.


Constraints:
1 <= numCourses <= 10^5
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""


import collections
from typing import List


class Solution:
    """
解法1: 使用 Map 保存各课程的依赖课程, 遍历每门课程, 判断它是否可以完成;
判断课程是否完成时, 使用两个 Set 标记访问过的课程和完成的课程, 依次判断
当前课程的依赖课程是否能完成, 如果一门课程第二次被访问但是又没有完成, 说
明出现了循环依赖, 则该课程无法完成
    """
    def canFinish_v1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency = collections.defaultdict(list)
        finished = set()
        # jy: 使用字典存放课程 course 的所有依赖课程;
        for course, prerequisite in prerequisites:
            dependency[course].append(prerequisite)
        # jy: 遍历每一个课程;
        for i in range(numCourses):
            # jy: 依据课程依赖关系 dependency, 判断当前课程 i 是否能完成;
            if not self._can_finish(i, dependency, set(), finished):
                return False
        return True

    def _can_finish(self, course, dependency, visited, finished):
        """
        依据课程依赖关系 dependency, 判断课程 course 是否能完成
        """
        # jy: 如果当前课程已完成, 则直接返回 True;
        if course in finished:
            return True
        # jy: 如果 course 没有完成, 但已经被访问过, 则直接返回 False;
        elif course in visited:
            return False
        # jy: 将当前课程标记为已访问过;
        visited.add(course)
        # jy: 如果完成当前课程时, 需要完成其它课程, 则递归判断其依赖的所有课程是否均能完
        #     成, 如果有一个不能完成, 则直接返回 False;
        if course in dependency:
            for prerequisite in dependency[course]:
                if not self._can_finish(prerequisite, dependency, visited, finished):
                    return False
        # jy: 如果能完成当前课程, 则将当前课程标记为已完成(加入 finished 集合), 并返回 True;
        finished.add(course)
        return True

    """
解法2: 构造一个数组用于存储每门课所依赖的课程的数量, 同时保存每门课及依赖该课程的其他
课程. 初始化队列为不依赖其他课程的课, 每次出队课程时, 遍历依赖当前课程的其他课程, 将其
依赖的课程数量减 1, 如果依赖的课程数量为 0, 说明该课程可以结束, 将其加入到队列中, 最后
如果所有可能都没有依赖的课程, 则说明可以完成所有课程;

JY: 性能较高, 占用内存较少
    """
    def canFinish_v2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # jy-version-1-Begin ----------------------------------------------------------------
        dependency = collections.defaultdict(list)
        degrees = [0] * numCourses

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
            for next_course in dependency[course]:
                degrees[next_course] -= 1

                if degrees[next_course] == 0:
                    queue.append(next_course)
        # jy: 当队列为空时, 如果 degrees 中所有的课程均不再有依赖数, 则表明可以完成所有课程;
        return sum(degrees) == 0
        # jy-version-1-End ------------------------------------------------------------------
        # jy-version-2-Begin ----------------------------------------------------------------
        # jy: degrees 用字典记录(并不会节省内存空间, 故建议还是用 version-1 中的 list 记录)
        '''
        dependency = collections.defaultdict(list)
        # degrees = [0] * numCourses
        degrees = collections.defaultdict(int)

        # 用字典 dependency 记录依赖于课程 prerequisite 的所有课程(列表保存)
        for course, prerequisite in prerequisites:
            dependency[prerequisite].append(course)
            degrees[course] += 1

        # jy: 初始化队列为不依赖其他课程的课(即对应课程编号的课程依赖数是 0 的课程)
        queue = collections.deque([course for course in range(numCourses) if degrees[course] == 0])
        # jy: 如果队列中有不依赖于其他课程的课, 则优先完成(出队)该课程, 并获取依赖于该课程的
        #     所有其它课程 next_course, 将其依赖的课程数减 1(如果减 1 后依赖的课程数为 0, 表
        #     明该课程不依赖于其它课程, 将其入队, 后续继续完成(出队)并获取依赖于该课程的课程;
        while queue:
            course = queue.popleft()
            for next_course in dependency[course]:
                degrees[next_course] -= 1

                if degrees[next_course] == 0:
                    queue.append(next_course)
        # jy: 当队列为空时, 如果 degrees 中所有的课程均不再有依赖数, 则表明可以完成所有课程;
        return sum(degrees.values()) == 0
        '''
        # jy-version-2-End ------------------------------------------------------------------

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency = collections.defaultdict(list)
        # degrees = [0] * numCourses
        degrees = collections.defaultdict(int)

        # 用字典 dependency 记录依赖于课程 prerequisite 的所有课程(列表保存)
        for course, prerequisite in prerequisites:
            dependency[prerequisite].append(course)
            degrees[course] += 1

        # jy: 初始化队列为不依赖其他课程的课(即对应课程编号的课程依赖数是 0 的课程)
        # queue = collections.deque([course for course, degree in enumerate(degrees) if degree == 0])
        queue = collections.deque([course for course in range(numCourses) if degrees[course] == 0])
        # jy: 如果队列中有不依赖于其他课程的课, 则优先完成(出队)该课程, 并获取依赖于该课程的
        #     所有其它课程 next_course, 将其依赖的课程数减 1(如果减 1 后依赖的课程数为 0, 表
        #     明该课程不依赖于其它课程, 将其入队, 后续继续完成(出队)并获取依赖于该课程的课程;
        while queue:
            course = queue.popleft()
            for next_course in dependency[course]:
                degrees[next_course] -= 1

                if degrees[next_course] == 0:
                    queue.append(next_course)
        # jy: 当队列为空时, 如果 degrees 中所有的课程均不再有依赖数, 则表明可以完成所有课程;
        print(degrees)
        return sum(degrees) == 0


numCourses = 2
prerequisites = [[1, 0]]
# Output: true
res = Solution().canFinish_v1(numCourses, prerequisites)
print(res)


numCourses = 2
prerequisites = [[1, 0], [0, 1]]
# Output: false
res = Solution().canFinish_v1(numCourses, prerequisites)
print(res)


numCourses = 2
prerequisites = [[1, 0]]
# Output: true
res = Solution().canFinish_v2(numCourses, prerequisites)
print(res)


