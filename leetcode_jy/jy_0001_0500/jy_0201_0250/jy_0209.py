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
title_jy = "Minimum-Size-Subarray-Sum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of positive integers nums and a positive integer target, return the minimal
length of a contiguous subarray [nums_l, nums_l+1, ..., nums_r-1, nums_r] of which the sum is
greater than or equal to target. If there is no such subarray, return 0 instead.


Example 1:
Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
Output: 2
Explanation: The subarray [4, 3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1, 4, 4]
Output: 1

Example 3:
Input: target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
Output: 0



Constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5



Follow up: If you have figured out the O(n) solution, try coding another solution of which the
time complexity is O(n log(n)).
"""


import sys
from typing import List


class Solution:
    """
解法1: 从数组第一位开始维护一个窗口, 移动窗口右端, 如果当前窗口的数字和大于等于 target,
则说明找到了一组解, 判断当前窗口的长度是否是至今最小的窗口长度, 然后窗口左端向右移动一
步, 破坏当前窗口, 继续寻找下一个符合条件的窗口; 如果当前窗口的数字和小于 target, 则将窗
口的右端向右移动一步, 扩大当前窗口;
    """
    def minSubArrayLen_v1(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        # jy: 保存满足条件的最小子数组长度;
        min_length = 0
        # jy: 初始化当前窗口的开头和结尾下标;
        low, high = 0, 0
        # jy: 统计窗口对应的子数组的数值总和;
        sum_so_far = nums[0]

        while high < len(nums):
            # jy: 如果子数组和大于或等于目标值, 表明找到了符合要求的子数组;
            if sum_so_far >= target:
                # jy: 计算子数组的长度;
                current_length = high - low + 1
                # jy: 注意, 在获取最小长度的过程中, 做最小值比较需要把原先的 0 区分对
                #    待, 因为 0 总是最小, 但不是满足要求的结果;
                min_length = min(min_length, current_length) if min_length != 0 else current_length
                # jy: 将最小子数组的最左边一个数值从 sum_so_far 中减掉, 同时将窗口左侧缩小一位,
                #    为下一轮循环做准备(有可能最右侧加入的值很大, 使得左侧一个去除后(即子数组
                #    缩小), 更小的子数组可能还是满足要求的, 在下一循环中将会得到判断);
                sum_so_far -= nums[low]
                low += 1
            else:
                high += 1
                sum_so_far += nums[high] if high < len(nums) else 0

        return min_length


    """
解法2: 额外创建一个数组 sums, sums[i] = nums[0] + nums[1] + ... + nums[i]; 针对所有大于
或等于 target 的 sums[i], 都表明 [0, i] 这个子序列满足条件, 但是需要进一步缩小范围, 由
于 sums 递增的特性(因为 nums 中的值均大于 0), 使用二分查找法在 [0, i] 中查找 k, 使得
nums[k] + nums[k+1] + ... + nums[i] > target
且:
nums[k+1] + nums[k+2] + ... + nums[i] < target
    """
    def minSubArrayLen_v2(self, target: int, nums: List[int]) -> int:
        min_length = 0
        sums = [0] * len(nums)

        # jy: 初始化 sums 数组, 其中 sums[i] 记录 nums[0]~nums[i] 的和;
        for i, n in enumerate(nums):
            # jy: 如果 i==0, 即第一个元素, 则 sum[0] = nums[0] (即 i 等于 0 时的 n)
            sums[i] = sums[i-1] + n if i != 0 else n

        # jy: left 初始化为 0;
        left = 0
        # jy: 遍历 sums 数组, 如果 sums[i] 大于或等于 target, 则以该 i 为 right, 然
        #    后尽可能地将 left 往右移;
        for right, n in enumerate(sums):
            if n >= target:
                # jy: 找出满足要求的情况下 left 尽可能右移所能移动到的最右位置: 此处
                #    相当于寻找使得 sums[left] > n-target 的最小 left 值; 即表明
                #    sums[left-1] <= n-target, 即 n-sums[left-1] >= target, 其中 n
                #    即为 sums[right], 即表明 nums[left] ~ nums[right] 的和是大于
                #    或等于 target 的;
                left = self._find_left(left, right, sums, n - target)
                # jy: 计算子数组的长度;
                current_length = right - left + 1
                # jy: 更新 min_length 逻辑;
                min_length = min(min_length, current_length) if min_length != 0 else current_length

        return min_length


    def _find_left(self, left, right, sums, target):
        """在递增数组 sums[left: right+1] 中找出最小的 i, 使得 sums[i] > target"""
        while left < right:
            middle = left + (right - left) // 2

            if sums[middle] <= target:
                left = middle + 1
            else:
                right = middle

        return left


target = 7
nums = [2, 3, 1, 2, 4, 3]
# Output: 2
res = Solution().minSubArrayLen_v1(target, nums)
print(res)


target = 4
nums = [1, 4, 4]
# Output: 1
res = Solution().minSubArrayLen_v1(target, nums)
print(res)

target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
# Output: 0
res = Solution().minSubArrayLen_v2(target, nums)
print(res)


