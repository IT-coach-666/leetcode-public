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
title_jy = "Find-Two-Non-overlapping-Sub-arrays-Each-With-Target-Sum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers arr and an integer target.
You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.
Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

Example 1:
Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.

Example 2:
Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.

Example 3:
Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.

Example 4:
Input: arr = [5,5,4,4,5], target = 3
Output: -1
Explanation: We cannot find a sub-array of sum = 3.

Example 5:
Input: arr = [3,1,1,1,5,1,2,1], target = 3
Output: 3
Explanation: Note that sub-arrays [1,2] and [2,1] cannot be an answer because they overlap.


Constraints:
1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8
"""

import collections
import sys
from typing import List


# Time Limit Exceeded!
class Solution:
    """
解法1(超时)
在 560. Subarray Sum Equals K 的基础上, 先求出每个数组和为 target 的子数组区间, 然后遍历所有区间, 判断区间之和的最小值, 不过会超时, 极限情况下当数组中的每一个数字都等于 target 时, 则满足条件的区间有 n 个, 双重遍历区间就是的时间复杂度;
    """
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        sum_so_far = 0
        sum_mapping = collections.defaultdict(list)
        sum_mapping[0] = [-1]
        intervals = []
        min_length = sys.maxsize

        for i, n in enumerate(arr):
            sum_so_far += n

            if sum_so_far - target in sum_mapping:
                for j in sum_mapping[sum_so_far - target]:
                    intervals.append((j + 1, i))

            sum_mapping[sum_so_far].append(i)

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[i][1] >= intervals[j][0]:
                    continue

                current_length = intervals[i][1] - intervals[i][0] + 1 \
                    + intervals[j][1] - intervals[j][0] + 1
                min_length = min(min_length, current_length)

        return -1 if min_length == sys.maxsize else min_length


import collections
import sys
from typing import List


class Solution:
    """
解法2
在解法1中通过判断 sum_so_far - target 是否在 Map 中来求得子数组和等于 target 的数组长度, 同样的也可以通过判断 sum_so_far + target 是否在 Map 中来判断在子数组 [i + 1, n) 中是否存在子数组其和为 target; 所以, 首先遍历数组将所有子数组的前缀和放入 Map, 然后再次遍历数组判断 sum_so_far - target 是否在 Map 中, 求得数组遍历至今遇到的最短子数组其和为 target, 而另一个子数组则通过判断 sum_so_far + target 是否在 Map 中来更新两个子数组的最小长度和, 因为数组中的所有元素都是正数, 所以这两个子数组必然不会有重合部分, 极限情况是两个子数组正好相邻, 即某次遍历中 sum_so_far - target 和 sum_so_far + target 都在 Map 中;
    """
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        sum_so_far = 0
        sum_mapping = collections.defaultdict(int)
        sum_mapping[0] = -1
        min_left_size = sys.maxsize
        min_length = sys.maxsize

        for i, n in enumerate(arr):
            sum_so_far += n
            sum_mapping[sum_so_far] = i

        sum_so_far = 0

        for i, n in enumerate(arr):
            sum_so_far += n

            if sum_so_far - target in sum_mapping:
                min_left_size = min(
                    min_left_size, i - sum_mapping[sum_so_far - target])

            if sum_so_far + target in sum_mapping \
                    and min_left_size != sys.maxsize:
                current_length = sum_mapping[sum_so_far + target] - i \
                                 + min_left_size
                min_length = min(min_length, current_length)

        return -1 if min_length == sys.maxsize else min_length

import sys
from typing import List


class Solution:
    """
解法3
使用滑动窗口求解, 当窗口中的数字总和大于 target, 则从窗口中剔除窗口起始位置的数字, 并将窗口起始位置向右移动一位; 同时, 记 dp[i] 表示 arr[0: i + 1] 中子数组和为 target 的最小窗口长度, 当窗口内数字总和等于 target 时, 需要判断之前是否存在另一个窗口其数字总和也为 target, 假设当前窗口起始位置为 start, 则 dp[start - 1] 表示当前窗口之前的所有窗口中满足条件的最小窗口, 两个窗口之和即为至今的最优解;
    """
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        dp = [sys.maxsize] * len(arr)
        sum_so_far, best_so_far = 0, sys.maxsize
        min_length, start = sys.maxsize, 0

        for i, n in enumerate(arr):
            sum_so_far += n

            while sum_so_far > target:
                sum_so_far -= arr[start]
                start += 1

            if sum_so_far == target:
                current_window_length = i - start + 1

                if start > 0 and dp[start - 1] != sys.maxsize:
                    min_length = min(min_length,
                                     dp[start - 1] + current_window_length)

                best_so_far = min(best_so_far, current_window_length)

            dp[i] = best_so_far

        return min_length if min_length != sys.maxsize else -1



