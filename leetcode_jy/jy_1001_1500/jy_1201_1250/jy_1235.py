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
title_jy = "Maximum-Profit-in-Job-Scheduling(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i],
obtaining a profit of profit[i].  You're given the ``startTime``, ``endTime`` and ``profit``
arrays, return the maximum profit you can take such that there are no two jobs in the subset
with overlapping time range.  If you choose a job that ends at time X you will be able to
start another job that starts at time X.


Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
             Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
             Profit obtained 150 = 20 + 70 + 60.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6


Constraints:
1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""


from typing import List
import bisect


class Solution:
    """
将任务按照开始时间排序, 记 dp[i] 表示从第 i 个任务到最后一个任务调度执行的最大利润; 即目标求 dp[0];
从任务尾向前遍历, 对于某处的任务 i 来说, 有两种情况:
1) 执行当前任务, 则利润为执行当前任务的利润加上执行后续任务的利润
2) 不执行当前任务, 则利润为执行后续任务的利润
两者的较大值即 dp[i] 的值
    """
    def jobScheduling_v1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [()] * len(startTime)

        # jy: 将任务的开始时间, 结束时间, 以及完成该任务的利润组成一个元组, 并按开始时间进行排序;
        for i in range(len(startTime)):
            jobs[i] = (startTime[i], endTime[i], profit[i])
        jobs.sort(key=lambda x: x[0])
        # jobs = sorted(jobs, key=lambda x: x[0])

        # jy: 初始化 dp 为任务长度, 且初始化均为 0, 最后一个值为完成最后一个任务得到的利润;
        #     dp[i] 表示第 i 个任务到最后一个任务调度执行的最大利润;
        dp = [0] * len(startTime)
        dp[-1] = jobs[-1][2]
        # jy: 最后一个任务已处理统计, 从倒数第二个任务开始往前遍历;
        for i in range(len(jobs) - 2, -1, -1):
            # jy: 从 jobs 的第 i 个任务之后找出第一个能在该任务 i 之后执行的任务;
            next_job = self._find_next_available_job(i, jobs)
            # jy: 如果下一个任务存在, 则 dp[i] 为以下两者取其大:
            #    1) 做当前任务, 得到利润为 jobs[i][2], 加上下一个能做的任务开始到最后一个任务
            #       调度执行得到的最大利润;
            #    2) dp[i+1], 即当前任务 i 不做, 获取第 i+1 个到最后一个任务调度执行的最大利润;
            dp[i] = max(jobs[i][2] + (0 if next_job == -1 else dp[next_job]), dp[i+1])
        return dp[0]

    def _find_next_available_job(self, start, jobs):
        """
        从 jobs 中的第 start + 1 个任务开始找, 找出第一个能在 start 个任务之后执行的任
        务(如果任务 i 的开始时间大于或等于任务 start 的结束时间, 则表明该任务符合要求);
        """
        for i in range(start + 1, len(jobs)):
            if jobs[i][0] >= jobs[start][1]:
                return i
        return -1

    """
JY: 同解法1, 但实用了 bisect, 效率大大提高;

记 dp[i] 表示从第 i 个任务到最后一个任务调度执行的最大利润, 则 dp[0] 就是调度所有任务的最大利润;

以 startTime 排序, 从右往左遍历, 并往右探, 二分加速查找前一状态
    """
    def jobScheduling_v2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        # jy: 总共有 n 个任务(对应标号为 0 到 n-1);
        jobs = [i for i in range(n)]
        # jy: 对 n 个 job 按开始时间排序(第 i 个 job 的开始时间为 startTime[i])
        jobs.sort(key=lambda i: startTime[i])
        # print(jobs)
        # jy: 对 startTime 进行排序, 经过排序后, jobs 和 startTime 即一一对应, 即第 jobs[i] 个任务
        #    (任务标号不一定为 i)的开始时间为 startTime[i];
        startTime.sort()
        # print(startTime)

        dp = [0 for _ in range(n)]
        # jy: 先初始化完成经过按开始时间排序后的最后一个任务(即第 n-1 个: jobs[n-1])时的利润;
        dp[n-1 ] = profit[jobs[n-1]]
        for i in range(n-2, -1, -1):
            # jy: 查找有序数组 startTime 中, 插入 endTime[jobs[i]] 时对应的插入位置, 如果出现相同值, 则
            #    插入到尽可能左侧的地方;
            insert_idx = bisect.bisect_left(startTime, endTime[jobs[i]])
            # jy: 如果插入位置 insert_idx 等于 n, 表示后续没有满足要求的可调度的 job, 利润则在当前 job 的
            #    利润的基础上加 0, 否则表明后续有满足要求的可调度 job, 利润则由当前 job 的利润加上后续一
            #    个可调度的任务到最后一个任务调度执行的最大利润(即 dp[insert_idx]);
            choose_i = profit[jobs[i]] + (0 if insert_idx == n else dp[insert_idx])
            # jy: 如果不做当前 jobs[i], 则当前任务到最后一个任务调度执行的最大利润则为 dp[i+1]
            non_choose_i = dp[i+1]
            # jy: 真正的 dp[i] 等于以上两种情况中的较大利润者;
            dp[i] = max(non_choose_i, choose_i)

        return dp[0]

    """
记 dp[i] 表示前 i 个任务调度执行的最大利润, 则 dp[n-1] 就是调度所有任务的最大利润;
以 endTime 从小到大排序, 从左往右遍历, 往左看, 二分加速查找, 前一状态
    """
    def jobScheduling_v3(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        # jy: 先对 n 个任务进行标号, 再对 n 个标号好的任务按 endTime 进行排序, 同时也对 endTime 进行
        #    排序, 使得排序后的 jobs[i] 与 endTime[i] 一一对应;
        jobs = [i for i in range(n)]
        # jy: 按结束时间排序
        jobs.sort(key=lambda i: endTime[i])
        endTime.sort()

        dp = [0 for _ in range(n)]
        # jy: 先初始化第一个任务调度执行后得到的利润;
        dp[0] = profit[jobs[0]]
        for i in range(1, n):
            # jy: 查找有序数组 endTime 中, 插入 startTime[jobs[i]] 时对应的插入位置, 如果出现相同值, 则
            #    插入到尽可能右侧的地方; insert_idx 为插入的位置的前一个(确保 dp[insert_idx] 之前已求得)
            insert_idx = bisect.bisect_right(endTime, startTime[jobs[i]]) - 1
            choose_i = (0 if insert_idx == -1 else dp[insert_idx]) + profit[jobs[i]]
            non_choose_i = dp[i-1]
            dp[i] = max(non_choose_i, choose_i)

        return dp[n-1]


startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]
# Output: 120
res = Solution().jobScheduling_v1(startTime, endTime, profit)
print(res)


startTime = [1, 2, 3, 4, 6]
# startTime = [2, 1, 3, 4, 6]
endTime = [3, 5, 10, 6, 9]
profit = [20, 20, 100, 70, 60]
# Output: 150
res = Solution().jobScheduling_v2(startTime, endTime, profit)
print(res)


startTime = [1, 1, 1]
endTime = [2, 3, 4]
profit = [5, 6, 4]
# Output: 6
res = Solution().jobScheduling_v3(startTime, endTime, profit)
print(res)


