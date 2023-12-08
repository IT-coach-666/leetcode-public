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
title_jy = "Squares-of-a-Sorted-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array ``nums`` sorted in non-decreasing order, return an array of
the squares of each number sorted in non-decreasing order.



Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]



Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""


from typing import List


class Solution:
    """
解法1: 直接将数组中每个数字平方后排序;
    """
    def sortedSquares_v1(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x * x, nums)))


    """
解法2: 解法 1 没有利用数组有序这个特性;
创建一个辅助数组用于存储最终结果, 然后使用两个指针 low 和 high 分别指向数组的首尾, 比
较两个指针所在的数字的绝对值的大小, 如果左指针的数的绝对值大, 说明该数为负数, 需要将其
添加到辅助数组中, 同时左指针向右移动一位; 否则, 添加右指针所在的数字到辅助数组中, 同时
右指针向左移动一位; 向辅助数组添加元素时, 同样使用一个指针标记待添加的位置, 初始化为数
组的末尾, 逐步向数组头移动;
    """
    def sortedSquares_v2(self, nums: List[int]) -> List[int]:
        # jy: 初始化辅助数组,
        result = [0] * len(nums)
        low, high = 0, len(nums) - 1
        index = len(nums) - 1

        while low <= high:
            left, right = abs(nums[low]), abs(nums[high])

            if left > right:
                result[index] = left * left
                low += 1
            else:
                result[index] = right * right
                high -= 1

            index -= 1

        return result

    """
解法3: 和解法 2 思想一致, 只是向辅助数组添加元素时, 无需额外的指针标记待添加的数组下
标, high - low 就是添加的位置, 因为 high - low 的初始值为数组的末尾, 而不管是左指针移
动还是右指针移动, high - low 每次都会减少 1, 等价于辅助数组的下标;
    """
    def sortedSquares_v3(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        low, high = 0, len(nums) - 1

        while low <= high:
            left, right = abs(nums[low]), abs(nums[high])

            if left > right:
                result[high - low] = left * left
                low += 1
            else:
                result[high - low] = right * right
                high -= 1

        return result


nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
res = Solution().sortedSquares_v1(nums)
print(res)


nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
res = Solution().sortedSquares_v2(nums)
print(res)


nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
res = Solution().sortedSquares_v3(nums)
print(res)


