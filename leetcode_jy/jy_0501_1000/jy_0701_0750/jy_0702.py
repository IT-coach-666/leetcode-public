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
title_jy = "Search-in-a-Sorted-Array-of-Unknown-Size(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array sorted in ascending order, write a function to search target
in nums.  If target exists, then return its index, otherwise return -1. However, the
array size is unknown to you. You may only access the array using an ``ArrayReader``
interface, where ``ArrayReader.get(k)`` returns the element of the array at index k (0-indexed).


Example 1:
Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: array = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:
1) You may assume that all elements in the array are unique.
2) The value of each element in the array will be in the range [-9999, 9999].
3) The length of the array will be in the range [1, 10^4].
4) You may assume all integers in the array are less than 10000, and if you
   access the array out of bounds, ``ArrayReader.get`` will return 2147483647.
"""


class Solution:
    """
解法1: 使用二分查找, 因为不知道数组的大小, 所以 high 直接初始化为最大值 10000, 如果 middle 对应的值
是 2147483647 则说明数组越界, 将 high 移动到 middle - 1;
    """
    def search_v1(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # jy: 数组中不会超过 10000 个数值, 即下标不会超过 10000;
        low, high = 0, 10000

        while low <= high:
            middle = low + (high - low) // 2
            # jy: get 会获取 reader 数组中下标为 middle 的元素对应的值, 如果下标超出已有数
            #    组的范围, 会返回 2147483647; 如果 middle 下标超出数组范围, 或者该下标元素
            #    对应的值大于目标值, 则将 high 更新为 middle-1;
            current = reader.get(middle)
            # jy: 以下 if 判断可以简化;
            # if current > target:
            if current == 2147483647 or current > target:
                high = middle - 1
            # jy: 如果 middle 下标元素对应的值小于目标值, 则将 low 更新为 middle+1 ;
            elif current < target:
                low = middle + 1
            else:
                return middle
        return -1

    """
解法2: 优化, 解法 1 是从最右端向左开始定位有实际值的 high, 可以先定位到 target 所在的区
间, 然后在这个区间内做二分查找;

初始化 low 等于 0, high 等于 1, 只要 reader.get(high) < target, 则将 low 赋值为 high,
high 赋值为 high * 2, 这样就定位了 target 所在的区间;
    """
    def search_v2(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # jy: 初始化 low 为 0, high 为 1 , 只要 reader.get(high) < target, 则将 low 赋值
        #     为 high, high 赋值为 high*2, 当 reader.get(high) >= target 时, 即定位到
        #     target 的所属区间: [low, high]
        low, high = 0, 1
        while reader.get(high) < target:
            low = high
            high *= 2

        # jy: 补充判断: reader.get(high) == target, 因为该条件也可以使得以上 while 循环退出
        #    且如果该条件成立, 则返回的下标为 high;
        if reader.get(high) == target:
            return high
        # jy: 在有效区间里二分查找目标值;
        while low <= high:
            middle = low + (high - low) // 2
            current = reader.get(middle)

            if current > target:
                high = middle - 1
            elif current < target:
                low = middle + 1
            else:
                return middle

        return -1


array = [-1, 0, 3, 5, 9, 12]
target = 9
# Output: 4
res = Solution().search_v1(array, target)
print(res)


array = [-1, 0, 3, 5, 9, 12]
target = 2
# Output: -1
res = Solution().search_v1(array, target)
print(res)


