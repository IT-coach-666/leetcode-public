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
title_jy = "search-in-rotated-sorted-array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Suppose an array sorted in ascending order is rotated at some pivot unknown
to you beforehand. i.e.: [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2]

You are given a target value to search. If found in the array return its
index, otherwise return -1.

You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4

Example 2:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1

Example 3:
Input: nums = [3, 4, 5, 6, 7, 0, 1, 2], target = 4
Output: 1
"""


from typing import List
class Solution:
    """
二分查找:
如果是一个普通有序数组(如升序), 只需要 middle 与 target 之间的简单判断:
(1) 如果 nums[middle] == target, 则直接返回 middle 值;
(2) 如果 nums[middle] < target, 则 target 在 middle 的后半部分, low = middle+1
(3) 如果 nums[middle] > target, 则 target 在 middle 的前半部分, high = middle-1

如果是一个旋转有序数组(升序), 则需要在 middle 和 target 的基础上再结合 high 进行判断:
(1) 如果 nums[middle] == target, 则直接返回 middle 值; 否则根据 middle target high 的情况进行分类;
(2) 如果 nums[middle] > target, 根据 nums[high] 所处位置不同可分以下 3 种情况:
    1) target < nums[middle] < nums[high] , 说明 target 在旋转数组的前半部分, high 移动到 middle-1
    2) nums[high] < target < nums[middle] , 说明 target 在旋转数组的前半部分, high 移动到 middle-1
    3) target < nums[high] < nums[middle] , 说明 target 在旋转数组的后半部分, low 移动到 middle+1

(3) 如果 nums[middle] < target, 根据 nums[high] 所处位置不同可分 3 种情况: 同理如上
    """
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            # jy: 注意 middle 值的计算方式;
            middle = low + (high - low) // 2
            # jy: 如果 nums[middle] == target, 则直接返回 middle 值;
            if nums[middle] == target:
                return middle

            # jy: 如果 nums[middle] > target, 当
            elif nums[middle] > target:
                if nums[middle] < nums[high] or nums[high] < target:
                    high = middle - 1
                else:
                    low = middle + 1
            # jy: nums[middle] < target 时对应的逻辑;
            else:
                if nums[middle] >= nums[high] or nums[high] >= target:
                    low = middle + 1
                else:
                    high = middle - 1
        return -1


    """
解法2(jy): 同样基于 middle  target  high 的不同情况进行分类处理, 只是改写了以上过程, 优先
判断 middle 和 high, 更易于理解;

还可以基于 middle  target  low 的不同情况进行分类处理, 见 081_Search-in-Rotated-Sorted-Array-II.py
    """
    def search_jy(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = low + (high - low) // 2
            if nums[middle] == target:
                return middle
            # jy: 如果 middle 小于 high, 表明后半部分严格升序; 此时判断 target 是否位于严格
            #    升序部分所对应区间即可相应的判断并更新 low 和 high 值;
            #if nums[middle] < nums[high]:
            elif nums[middle] < nums[high]:  # jy: 此处为 if 或 elif 均可;
                # jy: 可能存在 target == nums[high], 此部分逻辑要更新 low, 即使
                #    当 target == nums[high] 成立时也更新 low 也不会错过正确值;
                if nums[middle] < target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1
            # jy: 如果 middle 大于 high, 表明前半部分严格升序; 此时判断 target 是否位于严格
            #    升序部分所对应区间即可相应的判断并更新 low 和 high 值;
            elif nums[middle] > nums[high]:
                if nums[low] <= target < nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            # jy: 此处逻辑即 nums[middle] == nums[high], 只有当有序 pivot 数组中允许
            #    数值重复才有可能出现该情况(如: 081_Search-in-Rotated-Sorted-Array-II.py);
            else:
                #high -= 1  # jy: 模仿 081
                high = middle - 1

        return -1

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


print("==============【search_jy】=================")
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
res = Solution().search_jy(nums, target)
print(nums, " === ", target, " === ", res)

target = 3
res = Solution().search_jy(nums, target)
print(nums, " === ", target, " === ", res)


nums = [3, 4, 5, 6, 7, 0, 1, 2]
target = 4
res = Solution().search_jy(nums, target)
print(nums, " === ", target, " === ", res)



print("==============【081】=================")
nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
res = Solution().search_jy(nums, target)
print(res)

nums = [2, 5, 6, 0, 0, 1, 2]
target = 3
res = Solution().search_jy(nums, target)
print(res)


