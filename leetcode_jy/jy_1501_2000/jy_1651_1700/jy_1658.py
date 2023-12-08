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
title_jy = "Minimum-Operations-to-Reduce-X-to-Zero(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
"""

from typing import List


class Solution:
    """
解法1
该题要从数组头和数组尾分别找一段连续的子数组, 其和为 x, 等价于从数组中找一段连续的子数组, 使其和为 sum(nums) - x, 即 560. Subarray Sum Equals K; 只是这里 sum_mapping 保存的不再是子数组相同和的个数, 而是子数组和对应的数组下标位置, 因为数组中所有元素都是正数, 所以无需考虑重复;
    """
    def minOperations(self, nums: List[int], x: int) -> int:
        target = -x + sum(nums)
        total_sum = 0
        sum_mapping = {0: -1}
        max_length = 0

        if target == 0:
            return len(nums)

        for i, n in enumerate(nums):
            total_sum += n

            if total_sum - target in sum_mapping:
                current_length = i - sum_mapping.get(total_sum - target)
                max_length = max(max_length, current_length)

            sum_mapping[total_sum] = i

        return -1 if max_length == 0 else len(nums) - max_length


from typing import List


class Solution:
    """
解法2
也可以使用滑动窗口求解, 使用两个指针 low 和 high 表示窗口的起始位置, 初始 low 和 high 都指向0, 如果当前窗口的和小于 -x + sum(nums), 则 high 向右移动一位, 如果窗口的和大于等于 -x + sum(nums), 则判断是否要更新窗口和为 -x + sum(nums) 的窗口长度, 并尝试剔除窗口起始的元素, low 向右移动一位;
    """
    def minOperations(self, nums: List[int], x: int) -> int:
        target = -x + sum(nums)

        if target == 0:
            return len(nums)

        if target < 0:
            return -1

        low, high = 0, 0
        total_sum = 0
        max_length = 0

        while high < len(nums):
            if total_sum < target:
                total_sum += nums[high]

            while total_sum >= target:
                if total_sum == target:
                    max_length = max(max_length, high - low + 1)

                total_sum -= nums[low]
                low += 1

            high += 1

        return -1 if max_length == 0 else len(nums) - max_length


