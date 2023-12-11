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
title_jy = "Contains-Duplicate-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the
array such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:
Input: nums = [1, 2, 3, 1], k = 3
Output: true

Example 2:
Input: nums = [1, 0, 1, 1], k = 1
Output: true

Example 3:
Input: nums = [1, 2, 3, 1, 2, 3], k = 2
Output: false


Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
"""

from typing import List
class Solution:
    """
解法1: 遍历数组, 使用 Map 保存数字和其对应在数组中的位置, 如果当前数值已经在 Map 中,
表明该数值与之前的数值相等; 此时判断当前数字和 Map 中的数字的距离是否小于等于 k;
    """
    def containsNearbyDuplicate_v1(self, nums: List[int], k: int) -> bool:
        mapping = {}

        for i, n in enumerate(nums):
            if n in mapping and abs(i - mapping[n]) <= k:
                return True
            mapping[n] = i
        return False


    """
解法2: 维护一个长度为 k+1 的窗口(即数组下标为 0 到 k, 此时如果该窗口中出现重复元素, 则能满足要求), 遍
历数组, 使用 Set 保存遇到的数字, 如果窗口长度超过 k则剔除最左边的数字, 如果当前数字已经在 Set 中, 说
明找到了满足条件的数字;
    """
    def containsNearbyDuplicate_v2(self, nums: List[int], k: int) -> bool:
        numbers = set()
        # jy: 循环遍历 nums;
        for i, n in enumerate(nums):
            # jy: 如果 i 大于 k, 表明 numbers 中原先已经包含 k+1 个元素了(因为原先的值都没有重复, 否则返回 True)
            #    则先移除 nums[i-k-1] (即 k+1 个元素中最先始被加入的), 此时集合有 k 个元素:
            if i > k:
                numbers.remove(nums[i-k-1])
            # jy: 再判断当前元素是否在 numbers 集合中, 如果在, 直接返回 True; 如果不在, 则将该元素继续加入集合中,
            #    因此集合中仍然为 k+1 个元素;
            if n in numbers:
                return True
            numbers.add(n)

        return False



nums = [1, 2, 3, 1]
k = 3
# Output: true
res = Solution().containsNearbyDuplicate_v1(nums, k)
print(res)


nums = [1, 0, 1, 1]
k = 1
# Output: true
res = Solution().containsNearbyDuplicate_v1(nums, k)
print(res)

nums = [1, 2, 3, 1, 2, 3]
k = 2
# Output: false
res = Solution().containsNearbyDuplicate_v2(nums, k)
print(res)


