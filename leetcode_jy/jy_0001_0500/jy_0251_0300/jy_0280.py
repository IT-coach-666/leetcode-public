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
title_jy = "Wiggle-Sort(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array ``nums``, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
You may assume the input array always has a valid answer.


Example 1:
Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.

Example 2:
Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]


Constraints:
1 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 10^4
It is guaranteed that there will be an answer for the given input nums.


Follow up: Could you do it without sorting the array?
"""


from typing import List


class Solution:
    """
解法1: 将数组排序后, 从第二个数字开始, 依次交换当前数字和后一个数字
    """
    def wiggleSort_v1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]

    """
解法2: Follow up 中要求不能将数组排序, 遍历数组:
1) 如果当前下标位置是偶数且当前数字大于后一个数字, 则交换两者(因为该位置要求当前数字
   小于等于后一个数字)
2) 如果当前下标位置是奇数且当前数字小于后一个数字, 则交换两者(因为当前位置要求当前数
   字大于等于后一个数字)
    """
    def wiggleSort_v2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if i % 2 == 0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif i % 2 == 1 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]


nums = [3, 5, 2, 1, 6, 4]
# Output: [3,5,1,6,2,4], Explanation: [1,6,2,5,3,4] is also accepted.
Solution().wiggleSort_v1(nums)
print(nums)


ums = [6, 6, 5, 6, 3, 8]
# Output: [6,6,5,6,3,8]
Solution().wiggleSort_v2(nums)
print(nums)


