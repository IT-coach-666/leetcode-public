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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Largest-Number-At-Least-Twice-of-Others(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an integer array nums where the largest integer is unique. Determine whether
the largest element in the array is at least twice as much as every other number in the
array. If it is, returnthe index of the largest element, or return -1 otherwise.


Example 1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer. For every other number in the array x, 6 is at least
             twice as big as x. The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

Example 3:
Input: nums = [1]
Output: 0
Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.


Constraints:
1 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
"""


import sys
from typing import List


class Solution:
    """
解法1: 首先遍历数组求得最大值, 然后二次遍历数组判断是否满足条件;
    """
    def dominantIndex_v1(self, nums: List[int]) -> int:
        if not nums:
            return -1

        largest = -sys.maxsize
        largest_index = 0
        # jy: 找出最大值以及该值对应的下标(因为最终要返回最大值下标, 如果存在的话)
        for i, n in enumerate(nums):
            if largest < n:
                largest = n
                largest_index = i
        # jy: 再次遍历数组, 如果该值非最大值, 且该值的两倍大于最大值, 则直接返回 -1;
        for n in nums:
            if n != largest and largest < 2 * n:
                return -1
        # jy: 如果以上没有返回 -1, 表明该最大值符合要求, 返回其下标;
        return largest_index


    """
解法2: 遍历一次数组求的最大值和第二大的值, 最后判断最大值是否至少是第二
大的值的两倍;
    """
    def dominantIndex_v2(self, nums: List[int]) -> int:
        if not nums:
            return -1

        largest = -sys.maxsize
        second_largest = -sys.maxsize
        largest_index = 0
        # jy: 遍历数组, 找出最大值和第二大的值
        for i, n in enumerate(nums):
            # jy: 如果 n 大于最大值, 则将最大值更新为 n (并记录其下标 i), 第二大值则更新为原先的最大值;
            if n > largest:
                largest, second_largest = n, largest
                largest_index = i
            # jy: 如果 n 小于最大值, 但大于第二大值, 则更新第二大的值为 n;
            elif n > second_largest:
                second_largest = n
        # jy: 如果最大值比第二大的值的两倍还大, 则返回最大值的下标, 否则返回 -1;
        return largest_index if largest >= 2 * second_largest else -1


nums = [3,6,1,0]
# Output: 1
res = Solution().dominantIndex_v1(nums)
print(res)


nums = [1,2,3,4]
# Output: -1
res = Solution().dominantIndex_v2(nums)
print(res)


nums = [1]
# Output: 0
res = Solution().dominantIndex_v1(nums)
print(res)


