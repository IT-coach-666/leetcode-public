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
title_jy = "Kill-Process(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
You have n processes forming a rooted tree structure. You are given two integer
arrays ``pid`` and ``ppid``, where ``pid[i]`` is the ID of the ``ith`` process
and ``ppid[i]`` is the ID of the ``ith`` process's parent process. Each process
has only one parent process but may have multiple children processes. Only one
process has ``ppid[i]`` = 0, which means this process has no parent process (the
root of the tree).

When a process is killed, all of its children processes will also be killed.

Given an integer ``kill`` representing the ID of a process you want to kill, return
a list of the IDs of the processes that will be killed. You may return the answer
in any order.


Example 1:
Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
Output: [5,10]
Explanation: The processes colored in red are the processes that should be killed.

Example 2:
Input: pid = [1], ppid = [0], kill = 1
Output: [1]


Constraints:
n == pid.length
n == ppid.length
1 <= n <= 5 * 10^4
1 <= pid[i] <= 5 * 10^4
0 <= ppid[i] <= 5 * 10^4
Only one process has no parent.
All the values of pid are unique.
kill is guaranteed to be in pid.
"""


import collections
from typing import List


class Solution:
    """
解法1: 首先建立父进程和子进程的映射，然后根据 kill 找到所有的直接子进程，然后使
用广度优先搜索找到剩下的后代进程
    """
    def killProcess_v1(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent_to_children = collections.defaultdict(list)

        for i, id in enumerate(pid):
            parent_to_children[ppid[i]].append(id)

        processes = [kill]
        queue = collections.deque(parent_to_children[kill])

        while queue:
            process = queue.popleft()
            processes.append(process)

            for child in parent_to_children[process]:
                queue.append(child)

        return processes

    """
解法2: 基于栈的深度优先搜索
    """
    def killProcess_v2(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent_to_children = collections.defaultdict(list)

        for i, id in enumerate(pid):
            parent_to_children[ppid[i]].append(id)

        processes = []
        stack = [kill]

        while stack:
            process = stack.pop()
            processes.append(process)

            for child in parent_to_children[process]:
                stack.append(child)

        return processes


pid = [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
# Output: [5,10]
res = Solution().killProcess_v1(pid, ppid, kill)
print(res)


pid = [1]
ppid = [0]
kill = 1
# Output: [1]
res = Solution().killProcess_v1(pid, ppid, kill)
print(res)


