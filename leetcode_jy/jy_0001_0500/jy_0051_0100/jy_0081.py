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
title_jy = "Search-in-Rotated-Sorted-Array-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There is an integer array nums sorted in non-decreasing order (not necessarily
with distinct values). Before being passed to your function, nums is rotated at
an unknown pivot index k (0 <= k < nums.length) such that the resulting array
is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0, 1, 2, 4, 4, 4, 5, 6, 6, 7] might be rotated at pivot index 5 and
become [4, 5, 6, 6, 7, 0, 1, 2, 4, 4].

Given the array nums after the rotation and an integer target, return true if
target is in nums, or false if it is not in nums.


Example 1:
Input: nums = [2, 5, 6, 0, 0, 1, 2], target = 0
Output: true

Example 2:
Input: nums = [2, 5, 6, 0, 0, 1, 2], target = 3
Output: false


Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4


Follow up: This problem is the same as 033_search-in-rotated-sorted-array.py, where
nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""


from typing import List
class Solution:
    """
在 033_search-in-rotated-sorted-array.py 的基础上增加了重复的数字, 不能直接使用 033 的解法, 由
原来的判断 nums[middle] 和 target 的关系改变为判断 nums[middle] 和 nums[low] 的关系;

jy: 该解法同样可用于 033 中;
033: 根据 middle  target  high 的所处情况进行分类讨论;
081: 根据 middle  target  low  的所处情况进行分类讨论;
    """
    def search(self, nums: List[int], target: int) -> bool:
        # jy: 获取数组的首尾下标;
        low, high = 0, len(nums)-1
        while low <= high:
            # jy: 计算 middle 下标;
            middle = low + (high-low) // 2
            if nums[middle] == target:
                return True

            # jy: 如果 middle 值大于 low 值, 表明前半部分严格升序; 此时, 如果目标值在 low 和
            #    middle 中间, 则设置 high 为 middle-1, 否则 low 为 middle+1;
            if nums[middle] > nums[low]:  # jy: 此处是 if 或 elif 均可;
            #elif nums[middle] > nums[low]:
                # jy: "=" 需存在, 因为可能存在 nums[low] == target, 此时要更新 high; 如果不带
                #    "=", 则当 nums[low] == target 时, 会走 else 部分逻辑, low 被更新, 导致
                #    错过正确值;【trick】
                if nums[low] <= target < nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            # jy: 如果 middle 值小于 low 值, 表明后半部分严格升序; 此时, 如果目标值小于 low 但
            #    大于 middle, 表明目标值在后半部分, low 更新为 middle+1, 否则表明目标值在前半
            #    部分, high 更新为 middle-1;
            elif nums[middle] < nums[low]:
                # jy: nums[low] == target 的情况已被上面考虑到了, 故此处不再需要考虑, 且不能在
                #    此处考虑, 因为此处更新的是 low 值, 如果也加 "=", 则当 nums[low] == target
                #    时还对 low 进行更新, 显然错过了正确值;【trick】
                if nums[middle] < target < nums[low]:
                    low = middle + 1
                else:
                    high = middle - 1
            # jy: 如果 middle 值等于 low 值, 表明 row 到 middle 之间的值都是相等的(且不为目标值, 否
            #    则已返回了), 此时 low 往前进 1;
            else:
                #low += 1
                low = middle + 1  # jy: 改写以上;
        return False


    #def


nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
res = Solution().search(nums, target)
print(res)

nums = [2, 5, 6, 0, 0, 1, 2]
target = 3
res = Solution().search(nums, target)
print(res)


print("=============【033】===============")

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
res = Solution().search(nums, target)
print(nums, " === ", target, " === ", res)

target = 3
res = Solution().search(nums, target)
print(nums, " === ", target, " === ", res)


nums = [3, 4, 5, 6, 7, 0, 1, 2]
target = 4
res = Solution().search(nums, target)
print(nums, " === ", target, " === ", res)


