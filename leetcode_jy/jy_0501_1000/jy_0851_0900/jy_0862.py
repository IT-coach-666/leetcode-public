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
title_jy = "Shortest-Subarray-with-Sum-at-Least-K(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Return the length of the shortest, non-empty, contiguous subarray of nums with sum at least k.
If there is no non-empty subarray with sum at least k, return -1.

Example 1:
Input: nums = [1], k = 1
Output: 1

Example 2:
Input: nums = [1,2], k = 4
Output: -1

Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3
Note:
1. 1 <= nums.length <= 50000
2. -10^5 <= nums[i] <= 10^5
3. 1 <= k <= 10^9
"""

import heapq
import sys
from typing import List


class Solution:
    """
解法1
209. Minimum Size Subarray Sum 的进阶版, 依然是借助前缀和, 不过这道题求的最短子数组长度, 对前缀和搜索时还需要知道前缀和对应的数组截止位置, 所以使用最小堆来同时保存前缀和及其对应的数组截止位置; 满足两个条件则持续移除堆顶的元素:
1. 堆顶的元素的值小于等于 sum_so_far - k, 只有这样两个前缀和相减的差才可能大于等于 k, 即找到了一组解, 进一步判断长度即可
2. 堆顶元素对应的数组位置距离当前数组的位置已经超过了至今的最短子数组长度, 此时堆顶元素移除不影响最终结果
    """
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        heap, min_length, sum_so_far = [], sys.maxsize, 0
        heapq.heappush(heap, (0, -1))

        for i, num in enumerate(nums):
            sum_so_far += num
            diff = sum_so_far - k

            while heap and \
                    (heap[0][0] <= diff or i - heap[0][1] >= min_length):
                pre_sum, pre_index = heapq.heappop(heap)

                if i - pre_index < min_length:
                    min_length = i - pre_index

            heapq.heappush(heap, (sum_so_far, i))

        return min_length < sys.maxsize and min_length or -1


import sys
from typing import List


class Solution:
    """
解法2
和解法1类似, 使用栈维护了一个单调递增的前缀和, 使用二分查找定位 sum_so_far - k
    """
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        stack = [(0, -1)]
        sum_so_far = 0
        min_length = sys.maxsize

        for i, n in enumerate(nums):
            sum_so_far += n

            while stack and stack[-1][0] >= sum_so_far:
                stack.pop()

            j = self._find_left(stack, sum_so_far - k)

            if j > 0:
                min_length = min(min_length, i - stack[j - 1][1])

            stack.append((sum_so_far, i))

        return min_length < sys.maxsize and min_length or -1

    def _find_left(self, stack, target):
        low, high = 0, len(stack)

        while low < high:
            middle = low + (high - low) # 2

            if stack[middle][0] <= target:
                low = middle + 1
            else:
                high = middle

        return low


