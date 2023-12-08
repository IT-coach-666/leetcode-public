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
title_jy = "Valid-Mountain-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers ``arr``, return true if and only if it is a valid mountain
array. Recall that arr is a mountain array if and only if:
1) arr.length >= 3
2) There exists some i with 0 < i < arr.length - 1 such that:
3) arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
4) arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true


Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 104
"""


from typing import List


class Solution:
    """
解法1: 首先遍历数组找到 i 使得 arr[0] < arr[1] < ... < arr[i - 1] < arr[i], 然后从 i+1 处
继续遍历数组, 判断下一个数是否都比前一个数小;
    """
    def validMountainArray_v1(self, arr: List[int]) -> bool:
        top, length = -1, len(arr)

        # jy: 先找 mountain 的 top 位置, 如果 top 小于或等于 0(如果 top 为 -1, 表明 top 是
        #    初始值, 没有被更新过, 即表明数组的最后一个值是真正 top), 直接返回 False;
        for i in range(1, length):
            if arr[i] > arr[i-1]:
                continue
            else:
                top = i-1
                break
        if top <= 0:
            return False
        # jy: 如果 top 有效(非首尾位置), 则判断 top 之后的元素是否递减;
        for i in range(top + 1, length):
            if arr[i] >= arr[i-1]:
                return False
        # jy: 此处直接返回 True 即可, 因为执行到此处时, top 必然是小于等于 length - 1 的了;
        return True
        # return top < length - 1


    """
解法2: 使用两个指针分别指向数组首尾:
头指针向右移动找到 i 使得 arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
尾指针向左移动找到 j 使得 arr[j] > arr[j + 1] > ... > arr[arr.length - 1]
最后判断 i 是否等于 j 即可;
    """
    def validMountainArray_v2(self, arr: List[int]) -> bool:
        low, high = 0, len(arr) - 1
        # jy: 从 low 开始找 top, while 循环结束时的 low 值即为 top;
        # jy: 注意, 此处的条件为 low + 1 < len(arr) -1 , 故 low 的最大值也只能是 len(arr)-2 ;
        while low + 1 < len(arr) - 1:
            if arr[low] >= arr[low + 1]:
                break
            low += 1
        # jy: 从 high 开始找 top, while 循环结束时的 high 值即为 top;
        #    注意, 由于此处的条件为 high-1 >= 0, 故有可能最后更新之后 high 值为 0;
        while high - 1 >= 0:
            if arr[high - 1] <= arr[high]:
                break
            high -= 1
        # jy: 两种方式找到的 top 必定是相等的, 且不为首个位置;
        return low == high and low != 0



arr = [2,1]
# Output: false
res = Solution().validMountainArray_v1(arr)
print(res)


arr = [3,5,5]
# Output: false
res = Solution().validMountainArray_v2(arr)
print(res)


arr = [0,3,2,1]
# Output: true
res = Solution().validMountainArray_v2(arr)
print(res)

