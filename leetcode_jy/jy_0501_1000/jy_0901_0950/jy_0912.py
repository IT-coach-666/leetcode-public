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
title_jy = "Sort-an-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers nums, sort the array in ascending order.


Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]


Constraints:
1 <= nums.length <= 5 * 10^4
-5 * 10^4 <= nums[i] <= 5 * 10^4
"""


from typing import List


class Solution:
    """
解法1: 归并排序;
    """
    def sortArray_v1(self, nums: List[int]) -> List[int]:
        self._merge_sort(nums, 0, len(nums) - 1)
        return nums


    def _merge_sort(self, nums, low, high):
        # jy: 如果 low 大于或等于 high, 则终止递归;
        if low >= high:
            return
        # jy: 将数组分为两部分;
        middle = low + (high - low) // 2
        # jy: 先对数组的前半部分(下标为 low 到 middle)进行排序;
        self._merge_sort(nums, low, middle)
        # jy: 再对数组的后半部分(下标为 middle+1 到 high)进行拍戏;
        self._merge_sort(nums, middle + 1, high)
        # jy: 再对整个数组进行排序(数组的 low 到 middle, 以及 middle+1 到 high 已经有序)
        self._merge(nums, low, middle, high)


    def _merge(self, nums, low, middle, high):
        # jy: 由于数组的 low 到 middle 部分已经有序, middle+1 到 high 也已经有序,
        #    如果 middle 小于 middle+1, 表明数组已经整体有序, 无需再次排序;
        if nums[middle] <= nums[middle + 1]:
            return
        # jy: 记录左半部分有序数组的起始位置;
        left = low
        # jy: 记录右半部分有序数组的起始位置;
        right = middle + 1
        # jy: 一个临时数组, 用于存放左半部分和右半部分有序数组排序后的结果;
        merged = []

        while left <= middle or right <= high:
            if left <= middle and right <= high:
                if nums[left] <= nums[right]:
                    merged.append(nums[left])
                    left += 1
                else:
                    merged.append(nums[right])
                    right += 1
            elif left <= middle:
                merged.append(nums[left])
                left += 1
            else:
                merged.append(nums[right])
                right += 1

        # jy: 将对 nums 的 low 到 high 部分进行排序后的结果(暂存于 merged 临时数组中, 起始
        #    下标总是为 0)更新到 nums 中(更新的部分的 nums 的起始下标为 low);
        for i in range(low, high + 1):
            nums[i] = merged[i - low]


    """
解法2: 快速排序;
    """
    def sortArray_v2(self, nums: List[int]) -> List[int]:
        self._quick_sort(nums, 0, len(nums) - 1)
        return nums

    def _quick_sort(self, nums, low, high):
        if low >= high:
            return

        pivot = self._partition(nums, low, high)

        self._quick_sort(nums, low, pivot - 1)
        self._quick_sort(nums, pivot, high)


    def _partition(self, nums, low, high):
        middle = low + (high - low) // 2
        pivot = nums[middle]

        while low <= high:
            while nums[low] < pivot:
                low += 1

            while nums[high] > pivot:
                high -= 1
            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1

        return low


nums = [5,2,3,1]
# Output: [1,2,3,5]
res = Solution().sortArray_v1(nums)
print(res)


nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
res = Solution().sortArray_v1(nums)
print(res)


