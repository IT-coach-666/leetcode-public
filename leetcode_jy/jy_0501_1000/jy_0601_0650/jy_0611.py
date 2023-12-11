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
title_jy = "Valid-Triangle-Number(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array ``nums``, return the number of triplets chosen from the
array that can make triangles if we take them as side lengths of a triangle.


Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 2,3,4 (using the first 2)
                                     2,3,4 (using the second 2)
                                     2,2,3

Example 2:
Input: nums = [4,2,3,4]
Output: 4


Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""


from typing import List


class Solution:
    """
组成三角形的条件是两边之和大于第三边, 首先将数字进行排序, 然后从数组尾向前遍历, 对于
位置 i, 判断 0 到 i-1 中是否存在两个数字满足大于当前数字;
    """
    def triangleNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        count = 0

        for i in range(len(sorted_nums) - 1, 1, -1):
            low, high = 0, i-1

            while low < high:
                if sorted_nums[low] + sorted_nums[high] > sorted_nums[i]:
                    count += high - low
                    high -= 1
                else:
                    low += 1

        return count


nums = [2, 2, 3, 4]
# Output: 3
res = Solution().triangleNumber(nums)
print(res)


nums = [4,2,3,4]
# Output: 4
res = Solution().triangleNumber(nums)
print(res)

# 求数组中能构成三角形的三元组的个数


