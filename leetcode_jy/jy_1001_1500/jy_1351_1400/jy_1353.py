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
title_jy = "Maximum-Number-of-Events-That-Can-Be-Attended(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given an array of events where events[i] = [startDay_i, endDay_i]. Every event i 
starts at ``startDay_i`` and ends at ``endDay_i``. You can attend an event i at any
day d where ``startTime_i <= d <= endTime_i``. Notice that you can only attend one
event at any time d. Return the maximum number of events you can attend.


Example 1:
Input events = [[1, 2], [2, 3], [3, 4]]
Output: 3
Explanation: You can attend all the three events. One way to attend them all is as shown.
             Attend the first event on day 1.
             Attend the second event on day 2.
             Attend the third event on day 3.

Example 2:
Input: events= [[1, 2], [2, 3], [3, 4], [1, 2]]
Output: 4

Example 3:
Input: events = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
Output: 4

Example 4:
Input: events = [[1, 100000]]
Output: 1

Example 5:
Input: events = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]
Output: 7


Constraints:
1 <= events.length <= 10^5
events[i].length == 2
1 <= startDay_i <= endDay_i <= 10^5
"""


from typing import List
import heapq
from sortedcontainers import SortedList
from collections import defaultdict


class Solution:
    """
解法1: 时间复杂度 O(n^2), 超时; 
    """
    def maxEvents_v1(self,events):
        # jy: 按照结束时间升序排序;
        events.sort(key=lambda x:x[1])
        visited = set()
        # jy: 对区间所对应的 day 从前往后遍历, 如果该 day 没安排会议就添加到集合中, 表示
        #    该 day 可以参加当前的 event, 该 event 有参加了之后, break 跳出内循环, 外循
        #    环遍历下一个 event, 为下一个 event 安排 day 参加;
        # jy: 对于 100000 * [1, 100000] 这种例子不太可行, 容易超时;
        for s, e in events:
            for day in range(s, e+1):
                if day not in visited:
                    visited.add(day)
                    break
        return len(visited)

    """
本题是不能用优先队列的思想做的; 用堆/优先队列的, 给你们 events.length=10000, 
every_event=[1, 10000], 看看算法会不会超时;

解法2: 能想到的唯一健壮的解法是用 BST, 维护一个由所有可能开会的日期组成的有序数
组, 这个数组要求查询和删除都是 O(logn); 

核心思想是用二分查找对暴力解法中的第二层 for-loop 进行加速, 使查询效率达到 logn 级别;
找到空闲的日期时, 就从有序数组中把这个日期删除, 这个删除的效率也要在 logn 级别; 因此
总体时间复杂度就成 O(nlogn);
    """
    def maxEvents_v2(self, events: List[List[int]]) -> int:
        # jy: sortedcontainers 包需要提前安装, 引入 SortedList 是其中的对列表进行排序的对象
        # jy: 依据结束时间进行排序;
        events.sort(key=lambda val_list: val_list[1])
        # jy: 找出最小天和最大天;
        first_day = min(days_pair[0] for days_pair in events)
        last_day = events[-1][1]

        # jy: 维护一个最小天到最大天的列表, 并将其构造成 SortedList 对象;
        array = [val for val in range(first_day, last_day + 1)]
        sl = SortedList(array)
        # print(sl)

        res = 0
        # jy: 遍历 events (已按结束时间进行排序)
        for start_date, end_date in events:
            # jy: 二分查找 sl 中的 start_date 的插入位置, 如果该位置不在 sl 中的有效下标内(即下
            #    标值 index 等于 sl 的长度, 即应放在 sl 最后一个元素之后) 或待插入的位置的对应
            #    值大于 end_date, 则表明当前 event 无法再参见, 跳过当前循环继续进行下一轮; 否则
            #    表明当前的 event 可以用 sl[index] 对应的 date 参加, 参加后该 date 从 sl 中去除
            #    (同个 date 只能参加一个 event);
            # jy: 注意, 由于 events 是按结束时间进行排序, 循环遍历 events 时得到 start_date 并不
            #    一定是升序的, 可能后续遍历的 start_date 大于或等于当前的 start_date, 且当前 
            #    start_date 对应的 sl[index] 是要删除的, 因此后续的 start_date 对应的 sl[index]
            #    有可能是大于 end_date 的;   
            index = sl.bisect_left(start_date)
            if index == len(sl) or sl[index] > end_date:
                continue
            else:
                del sl[index]
                res += 1

        return res

    """
遍历时间 1~T 中的每一个时刻 t, 用 que_able 保存第 t 天可参加的会议(即开始时间小于 t 会
议)的结束时间; 在 que_able 中选择结束时间大于或等于 t 的会议中结束最早的来参加, 会议数
目+1; 因为每次都要取最小, 所以用优先队列维护 que_able 的插入与弹出), 首先 pop 出去结束
时间小于 t 的结束时间, 若此时 que_able 非空, 第一个的时间就是最小的结束时间;
    """
    def maxEvents_v3(self, events):
        # jy: res 记录能参加的会议数, T 记录最大的 date; 
        #    dic_evt[i] 为所有第 i 天开始的会议的结束时间; 
        res, T = 0, 0 
        dic_evt = defaultdict(list)
        for evt in events:
            dic_evt[evt[0]].append(evt[1])
            T = max(T, evt[1])

        # jy: 遍历 1~T 中的每一个 date;
        que_able = []
        for i in range(1, T+1):
            # jy: 用 que_able 保存第 i 天可参加的会议的结束时间, 并将其构造成最小堆结构;
            for end in dic_evt[i]: 
                heapq.heappush(que_able, end)
            # jy: 在最小堆 que_able 中 pop 出结束时间小于 i 的(第一轮循环时得到的 que_able
            #    肯定是均大于首个有效 i 值的, 但由于循环后 que_able 中的数值不一定是被全
            #    部清空的, 故可能后续遍历的 i 是大于 que_able 中的部分数值的); 结束时间小
            #    于当前 i 的是肯定不能完成当任务的, 故需要剔除;
            while que_able and que_able[0] < i: 
                heapq.heappop(que_able)
            # jy: 此时 que_able 中的最小 date 即可用来完成当前任务 i (因为 que_able 中的 date
            #    都是大于 i 的; que_able 中的值肯定是对应相应的任务, 如果 que_able 中有值,
            #    且也满足所有值均大于 i, 则表示该 que_able 中结束时间最小的 date 对应的任务
            #    肯定是可以通过 [i, date] 中的某个时间来完成的;
            if que_able:
                res += 1
                heapq.heappop(que_able)
        # jy: 最终返回的 res 即为能参加的最多 event 数;
        return res

    """
解法4: 按会议开始时间倒序排序, 将开始时间相同的 event 不断入最小堆, 随后不断判断当前
时间 i 是否能完成最小堆中的结束最早的任务; 时间复杂度 O(nlog(n)), 空间是 O(n), 堆占主
要存储;

JY: 思路同解法3, 但有提前结束机制, 更优;
    """
    def maxEvents_v4(self, events: List[List[int]]) -> int:
        # jy: 按会议开始时间倒序排序
        events.sort(reverse = True) 
        # jy: 初始化最小堆
        h = [] 
        res = 0
        # jy: 获取 events 的结束时间中的最大值, 并循环遍历 1 ~ max_time;
        max_time = max([t[1] for t in events])
        for i in range(1, max_time + 1):
            # jy: 将 events 中开始时间与当前 i 相同的会议的结束时间加入到 h 最小堆中;
            while events and events[-1][0] == i:
                heapq.heappush(h, events.pop()[1])
            # jy: 如果最小堆中存在元素(即存在未完成的任务), 则判断该任务是否可以通过当
            #    前 i 对应 date 完成(存在于 h 最小堆中的任务的开始时间肯定是大于等于 i
            #    的, 因为 i 随着循环不断增加); 如果其对应的结束时间大于当前 i, 则表明
            #    该任务肯定可以通过当前 i 完成, 完成后即跳出当前 while 循环(确保当前 i 
            #    只完成一个任务);
            while h:
                cur = heapq.heappop(h)
                if cur >= i:
                    res += 1
                    break
            # jy: 如果队列为空, 且没有其它待完成的 event, 则退出 for 循环, 完成;
            if not events and not h:
                break 
        return res

    """
解法5: 在解法 4 的基础上改进为无需排序的版本(且相较于解法 3, 字典经过优化, 使得也有提
前结束逻辑); 时间复杂度 O(nlog(n)), 空间复杂度 O(n), 字典占主要存储;
    """
    def maxEvents_v5(self, events: List[List[int]]) -> int:
        d = defaultdict(list)
        for i, val in enumerate(events):
            d[val[0]].append(val[1])
        print("d============ ", d)
        h = [] 
        res = 0
        max_time = max([t[1] for t in events])
        # print("max_time============ ", max_time)
        for i in range(1, max_time + 1):
            for end in d[i]:
                heapq.heappush(h, end) 
            # jy: 优化字典, 经过该优化后, 后续可判断是否提前结束外层 for 循环;
            del d[i]
            while h:
                cur = heapq.heappop(h)
                if cur >= i:
                    res += 1 
                    break
            if not d and not h:
                break
        return res

    """
解法6: 同解法 4, 只是换成数组按开始时间排序(非倒序排序), 但 pop(0) 的逻辑会导
致时间复杂度增加, 使得 LeetCode 上超时;
    """
    def maxEvents_v6(self, events: List[List[int]]) -> int:
        events.sort()
        max_time = max([t[1] for t in events])
        end = []
        res = 0
        for i in range(1, max_time + 1):
            while events and events[0][0] == i:
                heapq.heappush(end, events.pop(0)[1])

            # jy: version-1-Begin ------------------------------------
            while end:
                cur = heapq.heappop(end)
                if cur >= i:
                    res += 1
                    break
            # jy: version-1-End -------------------------------------
            # jy: version-2 -----------------------------------------
            '''
            while end and end[0] < i:
                heapq.heappop(end)
            if end:
                heapq.heappop(end)
                res += 1
            '''
            # jy: version-2-End -------------------------------------

            if not events and not end:
                break 
        return res


events = [[1, 2], [2, 3], [3, 4]]
# Output: 3
res = Solution().maxEvents_v1(events)
print(res)


events= [[1, 2], [2, 3], [3, 4], [1, 2]]
# Output: 4
res = Solution().maxEvents_v2(events)
print(res)


events = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
# Output: 4
res = Solution().maxEvents_v3(events)
print(res)


events = [[1, 100000]]
# Output: 1
res = Solution().maxEvents_v4(events)
print(res)


events = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]
# Output: 7
res = Solution().maxEvents_v5(events)
print(res)









