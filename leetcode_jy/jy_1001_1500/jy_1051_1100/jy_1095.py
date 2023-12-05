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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Find-in-Mountain-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
(This problem is an interactive problem.)
You may recall that an array ``A`` is a mountain array if and only if:
1) A.length >= 3
2) There exists some i with 0 < i < A.length - 1 such that:
   A[0] < A[1] < ... A[i-1] < A[i]
   A[i] > A[i+1] > ... > A[A.length - 1]

Given a mountain array ``mountainArr``, return the minimum index such that
mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array
using a MountainArray interface:
MountainArray.get(k) :   returns the element of the array at index k (0-indexed).
MountainArray.length() : returns the length of the array.

Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.



Example 1:
Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:
Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.



Constraints:
3 <= mountain_arr.length() <= 10000
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9
"""


"""
This is MountainArray's API interface.
You should not implement it, or speculate about its implementation
"""
class MountainArray:

    def __init__(self, array):
        self.array = array

    def get(self, index: int) -> int:
        return self.array[index]

    def length(self) -> int:
        return len(self.array)



class Solution:
    """
因为题目中规定了调用 MountainArray.get 的次数不能超过 100 次, 所以不能使用遍历的方式;

直观的解法是先找到山顶, 然后以山顶为界, 分别对数组的左半部分和右半部分进行二分查找, 找
山顶的解法同 852_Peak-Index-in-a-Mountain-Array.py;
    """
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # jy: 找出 mountain 数组的山顶对应的下标;
        peak = self._find_peak(0, mountain_arr.length() - 1, mountain_arr)

        if mountain_arr.get(peak) == target:
            return peak
        # jy: 在山顶左侧部分对应的升序数组中, 二分查找目标值;
        left = self.binary_search(0, peak - 1, mountain_arr, target, True)
        # jy: 如果山顶左侧部分能查找到目标值, 直接返回目标值下标, 否则在山顶右侧部分进行二分查找;
        return left if left != -1 else self.binary_search(peak + 1, mountain_arr.length() - 1, mountain_arr, target, False)


    def _find_peak(self, low, high, mountain_arr: 'MountainArray'):
        """找出 mountain 数组的山顶对应的下标"""
        while low < high:
            middle = low + (high - low) // 2

            if mountain_arr.get(middle) < mountain_arr.get(middle + 1):
                low = middle + 1
            else:
                high = middle

        return low

    def binary_search(self, low, high, mountain_arr: 'MountainArray', target, increasing):
        """有序数组(升序或降序均可)中二分查找目标值 target"""
        while low <= high:
            middle = low + (high - low) // 2
            value = mountain_arr.get(middle)

            if value == target:
                return middle
            elif (value > target and increasing) or (value < target and not increasing):
                high = middle - 1
            else:
                low = middle + 1

        return -1



array = MountainArray([1, 2, 3, 4, 5, 3, 1])
target = 3
# Output: 2
res = Solution().findInMountainArray(target, array)
print(res)


array = MountainArray([0, 1, 2, 4, 2, 1])
target = 3
# Output: -1
res = Solution().findInMountainArray(target, array)
print(res)


