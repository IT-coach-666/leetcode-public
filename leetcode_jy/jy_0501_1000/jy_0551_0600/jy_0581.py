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
title_jy = "Shortest-Unsorted-Continuous-Subarray(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array ``nums``, you need to find one continuous subarray that if
you only sort this subarray in ascending order, then the whole array will be sorted
in ascending order. Return the shortest such subarray and output its length.


Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole
             array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0


Constraints:
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5


Follow up: Can you solve it in O(n) time complexity?
"""


from typing import List


class Solution:
    """
解法1: 将数组排序, 然后比较两个数组不同部分的长度
    """
    def findUnsortedSubarray_v1(self, nums: List[int]) -> int:
        sorted_numbers = sorted(nums)
        start, end = 0, len(nums) - 1

        while start < len(nums) and sorted_numbers[start] == nums[start]:
            start += 1

        while end >= 0 and sorted_numbers[end] == nums[end]:
            end -= 1

        return end - start + 1 if start != len(nums) and end != -1 else 0


    """
解法2: Follow up 中需要我们使用时间复杂度 O(n) 的解法, 首先从前往后遍历数组, 最后
找到一个点 end, 使得 nums[end + 1] <= nums[end + 2] <= ... <= nums[n-1], 同理, 从
后往前遍历数组, 最后找到一个点 start, 使得 nums[0] <= nums[1] <= ... <= nums[start - 1],
最后 start 到 end 部分的子数组就是需要调整顺序的子数组
    """
    def findUnsortedSubarray_v2(self, nums: List[int]) -> int:
        prev = nums[0]
        end = 0

        for i, n in enumerate(nums):
            if n < prev:
                end = i
            else:
                prev = n

        start = len(nums) - 1
        prev = nums[start]

        for i in range(len(nums) - 1, -1, -1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]

        return end - start + 1 if end != 0 else 0


nums = [2, 6, 4, 8, 10, 9, 15]
# Output: 5
res = Solution().findUnsortedSubarray_v1(nums)
print(res)


nums = [1, 2, 3, 4]
# Output: 0
res = Solution().findUnsortedSubarray_v2(nums)
print(res)

nums = [1]
# Output: 0
res = Solution().findUnsortedSubarray_v1(nums)
print(res)

# 对数组中的子数组进行排序使得全数组有序，最小的子数组长度


