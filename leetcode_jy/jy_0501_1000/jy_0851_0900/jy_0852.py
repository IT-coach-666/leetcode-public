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
title_jy = "Peak-Index-in-a-Mountain-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Let's call an array arr a mountain if the following properties hold:
1) arr.length >= 3
2) There exists someiwith 0 < i < arr.length - 1 such that:
   a) arr[0] < arr[1] < ... arr[i-1] < arr[i]
   b) arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Given an integer array ``arr`` that is guaranteed to be a mountain, return any i such
that arr[0] < arr[1] < ... arr[i-1] < arr[i] > arr[i+1] > ... > arr[arr.length - 1].


Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1

Example 4:
Input: arr = [3,4,5,1]
Output: 2

Example 5:
Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2


Constraints:
3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.


Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) solution?
"""


from typing import List


class Solution:
    """
解法1: 同 941_Valid-Mountain-Array.py 的解法 2, 最后返回山顶的坐标;
    """
    def peakIndexInMountainArray_v1(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1

        while low + 1 < len(arr) - 1:
            # jy: 当找到 low 大于 low+1 时跳出, 否则不断 low += 1;
            if arr[low] >= arr[low + 1]:
                break
            low += 1

        while high - 1 >= 0:
            # jy: 如果 high-1 的值大于 high, 则不断 high -= 1, 直到第一个出现 high-1 的值小
            #    于 high, 表明此时的 high 为最大值位置;
            if arr[high - 1] <= arr[high]:
                break
            high -= 1
        # jy: low 和 high 指向的最大值位置如果相等, 则返回该位置(前提是该位置不能是第一个位置),
        #    否则返回 -1;
        return low if low == high and low != 0 else -1


    """
解法2: 因为本题保证了输入的数组一定是一座山, 所以解法 1 中找山脚的过程是多余
的, 找到山顶返回即可;
    """
    def peakIndexInMountainArray_v2(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1

        while low + 1 < len(arr) - 1:
            if arr[low] >= arr[low + 1]:
                break
            low += 1
        return low

    """
解法3: 由于该数组头到山顶的元素是升序, 山顶到数组尾的元素是降序, 可以通过二分查找来寻找
山顶, 当 arr[middle - 1] < arr[middle] > arr[middle + 1] 时, 则找到了山顶;
    """
    def peakIndexInMountainArray_v3(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1

        while low < high:
            middle = low + (high - low) // 2
            # jy: 如果 middle 的值小于 middle+1 的值, 则 low 更新为 middle+1;
            if arr[middle] < arr[middle + 1]:
                low = middle + 1
            # jy: 如果 middle 的值大于 middle+1 的值, 将 high 赋值给 middle, 此
            #    时如果该 middle 是目标值, 即后续只会不断更新 low 为新的 middle+1
            #    直到 low 更新为 high 时(即目标值), 退出返回;
            else:
                high = middle

        return low


arr = [0,1,0]
# Output: 1
res = Solution().peakIndexInMountainArray_v1(arr)
print(res)


arr = [0,2,1,0]
# Output: 1
res = Solution().peakIndexInMountainArray_v1(arr)
print(res)


arr = [0,10,5,2]
# Output: 1
res = Solution().peakIndexInMountainArray_v2(arr)
print(res)


arr = [3,4,5,1]
# Output: 2
res = Solution().peakIndexInMountainArray_v3(arr)
print(res)


arr = [24,69,100,99,79,78,67,36,26,19]
# Output: 2
res = Solution().peakIndexInMountainArray_v3(arr)
print(res)


