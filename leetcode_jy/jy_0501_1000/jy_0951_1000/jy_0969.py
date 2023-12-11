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
title_jy = "Pancake-Sorting(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers arr, sort the array by performing a series of pancake flips.
In one pancake flip we do the following steps:
Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[0...k-1] (0-indexed).
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.
Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

Example 1:
Input: arr = [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k = 4): arr = [1, 4, 2, 3]
After 2nd flip (k = 2): arr = [4, 1, 2, 3]
After 3rd flip (k = 4): arr = [3, 2, 1, 4]
After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.

Example 2:
Input: arr = [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.


Constraints:
1 <= arr.length <= 100
1 <= arr[i] <= arr.length
All integers in arr are unique (i.e. arr is a permutation of the integers from 1 to arr.length).
"""

from typing import List


class Solution:
    """
首先找到数组的最大值所在的位置, 然后反转数组起始位置到当前位置的子数组将最大值调到数组头, 接着反转整个数组将最大值放到数组末尾, 然后继续对第二大的数字重复操作;
    """
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        largest = len(arr)

        while largest != 0:
            i = self._find(arr, largest)

            self._flip(arr, i)
            self._flip(arr, largest - 1)

            result.append(i + 1)
            result.append(largest)

            largest -= 1

        return result

    def _find(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i

        return -1

    def _flip(self, arr, i):
        low, high = 0, i

        while low < high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1


