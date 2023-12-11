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
title_jy = "Find-Pivot-Index(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of
the index is equal to the sum of all the numbers strictly to the index's right. If the
index is on the left edge of the array, then the left sum is 0 because there are no
elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.


Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.


Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0



Constraints:
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
"""


from typing import List


class Solution:
    """
首先计算出数组所有元素的和, 然后遍历数组, 判断以当前位置为 pivot 时是否满足条件;
    """
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        # jy: 初始化左侧和为 0, 并计算数组所有元素和 all_sum;
        left_sum, all_sum = 0, sum(nums)
        # jy: 遍历数组元素和下标(因为如果是目标元素, 要返回其下标), 并不断求解并记录当前元素
        #    左侧的所有元素的总和;
        for i, n in enumerate(nums):
            # jy: all_sum 减去当前元素值 n 再减去其左侧元素总和 left_sum 即为右侧元素总和, 如
            #    果与左侧元素总和相等, 则直接返回其下标;
            if all_sum - n - left_sum == left_sum:
                return i
            # jy: left_sum 加上当前元素值, 作为下一个元素值的左侧元素总和;
            else:
                left_sum += n

        return -1


nums = [1,7,3,6,5,6]
# Output: 3
res = Solution().pivotIndex(nums)
print(res)


nums = [1,2,3]
# Output: -1
res = Solution().pivotIndex(nums)
print(res)


nums = [2,1,-1]
# Output: 0
res = Solution().pivotIndex(nums)
print(res)


