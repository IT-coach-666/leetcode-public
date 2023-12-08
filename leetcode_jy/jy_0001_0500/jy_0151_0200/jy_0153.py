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
title_jy = "Find-Minimum-in-Rotated-Sorted-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you
beforehand. (i.e., [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2]). Find
the minimum element. You may assume no duplicate exists in the array.


Example 1:
Input: [3, 4, 5, 1, 2]
Output: 1

Example 2:
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0
"""



from typing import List
class Solution:
    """
二分查找: 如果 nums[middle] 大于 nums[high], 说明最小值位于旋转数组的后半段, 否则最小值
位于旋转数组的前半段;
    """
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            middle = low + (high - low) // 2
            # jy: 如果 nums[middle] 大于 nums[high], 说明最小值位于旋转数组的后半段, low 设
            #    置为 middle 的下一位;
            if nums[middle] > nums[high]:
                low = middle + 1
            # jy: 如果 nums[middle] 小于 nums[high](由于没有重复数值, 故不存在 nums[middle] 等
            #    于 nums[high] 的情况), 说明最小值位于旋转数组的前半段, 将 high 设置为 middle (因
            #    为 middle 可能是最小值, 此处不需要 middle-1)
            else:
                high = middle

        return nums[high]


nums = [3, 4, 5, 1, 2]
# Output: 1
res = Solution().findMin(nums)
print(res)

nums = [4, 5, 6, 7, 0, 1, 2]
# Output: 0
res = Solution().findMin(nums)
print(res)


