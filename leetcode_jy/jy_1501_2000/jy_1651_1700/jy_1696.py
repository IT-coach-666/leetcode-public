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
title_jy = "Jump-Game-VI(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given a 0-indexed integer array nums and an integer k.
You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.
Return the maximum score you can get.

Example 1:
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

Example 2:
Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

Example 3:
Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0


Constraints:
1 <= nums.length, k <= 10^5
-10^4 <= nums[i] <= 10^4
"""

import sys
from typing import List


# Time Limit Exceeded!
class Solution:
    """
解法1(超时)
记 dp[i] 表示从数组的起始位置跳到 i 处的最大权重, 则 dp[i] = nums[i] + max(dp[i - k], dp[i - k + 1], ..., dp[i - 1], 不过会超时;
    """
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [-sys.maxsize] * n
        dp[0] = nums[0]

        for i in range(1, n):
            for j in range(max(i - k, 0), i):
                dp[i] = max(dp[i], dp[j] + nums[i])

        return dp[-1]


import heapq
from typing import List


class Solution:
    """
解法2
解法1在计算 max(dp[i - k], dp[i - k + 1], ..., dp[i - 1]) 时, 随着 i 的移动, 每次都要遍历求解最大值, 时间复杂度为O(k), 可以将 dp[i - k], dp[i - k + 1], ..., dp[i - 1] 使用最大堆维护, 堆顶的元素就是窗口的最大值, 从而将时间复杂度降为O(lgk)  维护堆的信息时, 还需要维护元素对应在数组中的位置, 用于检查堆中的元素是否在窗口之外, 需要从堆中删除; 为什么最后不是直接返回堆顶的元素? 因为堆顶的元素不一定是跳到最后一格的对应权重;
使用 Python 实现时, 由于 Python 的堆默认为最小堆, 所以需要将数字取反来实现最大堆;
    """
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        heap = [(-nums[0], 0)]
        max_score = nums[0]

        for i in range(1, n):
            while heap[0][1] < i - k:
                heapq.heappop(heap)

            max_score = -(-nums[i] + heap[0][0])
            heapq.heappush(heap, (-max_score, i))

        return max_score


import heapq
from collections import deque
from typing import List


class Solution:
    """
解法3
使用一个双端队列来维护窗口, 和以上的解法不同, 双端队列并不是一直维护大小为 k 的窗口, 而是会判断队列的尾端元素的权重是否比当前元素小, 如果队列尾端的元素的权重比当前元素的权重小, 则剔除队列尾端的元素, 因为相比当前的元素, 队列尾端的元素已经不是最优解; 同时保证双端队列中的元素值是递减, 这样队首的元素就是窗口的最大值;
从队尾剔除元素的时间复杂度最多为O(k), 即窗口中已经存在了 k 个元素, 而当前元素比窗口中的元素都大, 不过最终算法的时间复杂度依然是O(n), 因为:
往队列中添加 k 个元素的时间复杂度为O(k), 下次循环会从队列中剔除 k 个元素, 这两个阶段的时间复杂度为 O(k) + O(k) = O(2k), 该阶段一共遍历了 k + 1 个元素, 所以在最坏的情况下, 这样的阶段一共有组, 时间复杂度为;
而, , 所以整体时间复杂度依然为O(n)
    """
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        queue = deque([0])

        for i in range(1, n):
            if queue[0] < i - k:
                queue.popleft()

            dp[i] = nums[i] + dp[queue[0]]

            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()

            queue.append(i)

        return dp[-1]


