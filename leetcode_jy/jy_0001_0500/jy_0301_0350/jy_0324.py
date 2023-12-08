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
title_jy = "Wiggle-Sort-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array ``nums``, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
You may assume the input array always has a valid answer.


Example 1:
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.

Example 2:
Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]


Constraints:
1 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 5000
It is guaranteed that there will be an answer for the given input nums.


Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
"""


from typing import List


class Solution:
    """
在 280_Wiggle-Sort.py 的基础上去掉了相等的条件:
1) 将数组排序保存在辅助数组中
2) 将排序后的数组从后往前依次放在原数组的奇数位上
3) 将剩下的元素依次放在原数组的偶数位上
    """
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums) - 1
        # jy: 对数组进行排序并放在辅助数组 numbers 中;
        numbers = sorted(nums)
        # jy: 将排序后的数组从后往前依次放在原数组的奇数位上
        for i in range(1, len(nums), 2):
            nums[i] = numbers[end]
            end -= 1
        # jy: 将剩下的排序后的数组从后往前依次放在原数组的偶数位上
        for i in range(0, len(nums), 2):
            nums[i] = numbers[end]
            end -= 1


nums = [1, 5, 1, 1, 6, 4]
# Output: [1,6,1,5,1,4], Explanation: [1,4,1,5,1,6] is also accepted.
Solution().wiggleSort(nums)
print(nums)


nums = [1, 3, 2, 2, 3, 1]
# Output: [2,3,1,3,1,2]
Solution().wiggleSort(nums)
print(nums)


