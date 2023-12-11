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
title_jy = "Find-Minimum-in-Rotated-Sorted-Array-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2]). Find the minimum element. The
array may contain duplicates.

Example 1:
Input: [1, 3, 5]
Output: 1

Example 2:
Input: [2, 2, 2, 0, 1]
Output: 0


Note: This is a follow up problem to 153_Find-Minimum-in-Rotated-Sorted-Array.py. Would allow
duplicates affect the run-time complexity? How and why?
"""

from typing import List
class Solution:
    """
middle 与 high 值之间的比较
因为多了重复数字, 所以原来的方法无法区分 [1, 3, 3, 3] 和 [3, 1, 3, 3], 在原来的基础上, 如果遇
到 nums[middle] == nums[high], 则将 high 向左移动一位, 去掉一位重复数字的影响; 如果输入全部都
是重复数字, 算法的时间复杂度则会退化到 O(n);
    """
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        # jy: 二分查找, 确定 middle, 判断 low high 的具体变动;
        while low < high:
            middle = low + (high - low) // 2

            # jy: 如果 nums[middle] 大于 nums[high], 说明最小值在 middle 右侧, low = middle + 1;
            if nums[middle] > nums[high]:
                low = middle + 1
            # jy: 如果 nums[middle] 小于 nums[high], 说明最小值在 middle 左侧, 且 nums[middle] 可
            #    能是最小值, 故 high = middle
            elif nums[middle] < nums[high]:
                high = middle
            # jy: 如果 nums[middle] 等于 nums[high], 则 high 往左移 1 位, 减少重复的数值后再进行比较;
            else:
                high -= 1
        # jy: 最后返回 nums[high], 为什么不是 nums[low]? 因为退出 while 循环时, 可能是以 low > high;
        #    但在该题的逻辑中, 退出循环时只可能是 low == high, 故返回 nums[low] 也没问题(已经过 leetcode
        #    原题测试)
        #return nums[low]
        return nums[high]

nums = [1, 3, 5]
# Output: 1
res = Solution().findMin(nums)
print(res)


nums = [2, 2, 2, 0, 1]
# Output: 0
res = Solution().findMin(nums)
print(res)


