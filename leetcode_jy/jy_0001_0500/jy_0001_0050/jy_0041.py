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
title_jy = "First-Missing-Positive(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.


Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1


Constraints:
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""


from typing import List


class Solution:
    """
JY: 数组的长度为 n, 即数组中共有 n 个数, 则缺失的最小正整数肯定是在 1 到 n+1 之间, 将
数值范围属于 1 到 n 的数值, 放到其对应的下标中(假设数值为 x, 则放到 x-1 的下标中), 1
至 n 的数值对应的下标为 0 至 n-1, 均为有效下标;

记数组的长度为 n, 遍历数组, 如果当前数字在 [1, n] 之间且 nums[i] != nums[nums[i] - 1],
则将两者进行交换, 用于将数字放在正确的位置上(即将 k 放到数组索引 k-1 处, k >= 1), 之
后再次遍历数组, 如果当前数字不等于 i+1, 说明 i+1 就是缺失的最小正数, 否则最后返回 n+1;
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        # jy: ;
        n = len(nums)

        for i in range(n):
            # jy: 遍历列表, 将列表中属于 1 到 n 的数值放到其规定的下标, 后续即可通过下标
            #    对应的数值是否为该数值进行判断当前数值是否是缺失的最小数值;
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp

        # jy: 从第一个位置开始遍历列表数值, 如果对应的数值不等于 i+1 (i 为下标), 则
        #    表明 i+1 即为缺省的最小正整数;
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


nums = [1, 2, 0]
# Output: 3
res = Solution().firstMissingPositive(nums)
print(res)


nums = [3, 4, -1, 1]
# Output: 2
res = Solution().firstMissingPositive(nums)
print(res)


nums = [7, 8, 9, 11, 12]
# Output: 1
res = Solution().firstMissingPositive(nums)
print(res)


