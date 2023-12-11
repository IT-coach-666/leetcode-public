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
title_jy = "Task-Scheduler(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a characters array ``tasks``, representing the tasks a CPU needs to do,
where each letter represents a different task. Tasks could be done in any order.
Each task is done in one unit of time. For each unit of time, the CPU could
complete either one task or just be idle.

However, there is a non-negative integer ``n`` that represents the cooldown period
between two same tasks (the same letter in the array), that is that there must be
at least ``n`` units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the
given tasks.


Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B
             There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: One possible solution is:
             A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A


Constraints:
1 <= task.length <= 10^4
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
"""


import collections
import heapq
from typing import List


class Solution:
    """
将任务按照个数使用大顶堆排列, 每次出堆 n+1 个任务(因为相同任务间需要有 n 个时间
单位的冷却), 将各任务的数量减1后再放入堆中, 直到堆为空;
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        heap = [[-count, task] for task, count in counter.items()]
        heapq.heapify(heap)

        units = 0

        while heap:
            current_tasks = []
            current_unit = 0

            for _ in range(n + 1):
                if not heap:
                    break

                current_tasks.append(heapq.heappop(heap))
                current_unit += 1

            for count, task in current_tasks:
                if count + 1 < 0:
                    heapq.heappush(heap, [count + 1, task])

            units += (n + 1) if heap else current_unit

        return units


tasks = ["A","A","A","B","B","B"]
n = 2
# Output: 8
res = Solution().leastInterval(tasks, n)
print(res)


tasks = ["A","A","A","B","B","B"]
n = 0
# Output: 6
res = Solution().leastInterval(tasks, n)
print(res)


