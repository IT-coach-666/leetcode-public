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
title_jy = "Next-Permutation(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "运算技巧 | 参考 0556"


"""
A permutation(排列, 组合) of an array of integers is an arrangement of its
members into a sequence or linear order. For example, for arr = [1,2,3], the
following are all the permutations of arr: 
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically
greater permutation of its integer. More formally, if all the permutations
of the array are sorted in one container according to their lexicographical
order, then the next permutation of that array is the permutation that follows
it in the sorted container. If such arrangement is not possible, the array 
must be rearranged as the lowest possible order (i.e., sorted in ascending
order).


For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].

While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does
not have a lexicographical larger rearrangement.

Given an array of integers `nums`, find the next permutation of `nums`.

The replacement must be in place and use only constant extra memory.




Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:
Input: nums = [1]
Output: [1]


Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""




class Solution:
    """
解法 1: 参考 0556 (Next-Greater-Element-III), 当不存在下一个较大值时将数组反转

函数不返回任何值, 因为是 in-place 置换
    """
    def nextPermutation_v1(self, nums: List[int]) -> None:
        # jy: 如果数组是降序排序, 反转其为升序并返回
        i = len(nums) - 1
        while i-1 >= 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i == 0:
            # jy: 在 0556 的基础上补充对数组进行倒序排列 (可自行实现反转效果)
            nums.reverse()
            return

        j = i
        while j+1 < len(nums) and nums[j+1] > nums[i-1]:
            j += 1

        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = nums[i:][::-1]



nums = [1,2,3]
Solution().nextPermutation_v1(nums)
# jy: [1,3,2]
print(nums)


nums = [3,2,1]
Solution().nextPermutation_v1(nums)
# jy: [1,2,3]
print(nums)


nums = [1,1,5]
Solution().nextPermutation_v1(nums)
# jy: [1,5,1]
print(nums)


nums = [1]
Solution().nextPermutation_v1(nums)
# jy: [1]
print(nums)


