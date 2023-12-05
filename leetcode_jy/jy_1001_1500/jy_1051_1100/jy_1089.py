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
title_jy = "Duplicate-Zeros(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a fixed length array ``arr`` of integers, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from
your function.



Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]



Note:
1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""


from typing import List


class Solution:
    """
解法1: 遍历数组, 如果当前数字为 0, 则将后续的数字整体向后移动一位, 然后将后一位数字置为 0;
    """
    def duplicateZeros_v1(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, length = 0, len(arr)
        # jy: 遍历数组, 如果数组当前位置值为 0, 且后一位有效, 则将后一位开始的数值均
        #    后移一位, 随后将后一位置为 0;
        while i < length:
            if arr[i] == 0 and i+1 < length:
                i += 1
                self._shift(arr, i)
                arr[i] = 0
            i += 1

    def _shift(self, arr: List[int], i: int) -> None:
        """将 arr 中的下标为 i 的数值以及之后的数值均后移 1 位"""
        for j in range(len(arr) - 1, i, -1):
            arr[j] = arr[j-1]

    """
解法2: 首先遍历数组, 计算出 0 的个数, 记为 zeros; 然后从数组尾向前遍历数组;

之所以要从后往前遍历数组, 是因为对于数组中所有排在最后一个 0 之后的数来说, 在
不考虑数组越界的情况下, 它们向右移动了 zeros 次, 所以这部分数在新数组中的位置
为 i + zeros, i 为这部分数在原数组中的下标, 依此类推, 第 (zeros-1) 个 0 和第
zeros 个 0 之间的数在新数组中的位置为 i + (zeros - 1); 如果在遍历时当前数字为
0, 则需要将当前 0 和复制的 0 移动到新数组中的位置, 对于复制的 0 来说, 因为它需
要在当前 0 的后面复制, 所以在新数组中的位置为 i + 1 + (zeros - 1), (zeros - 1)
表示因为前面的 (zeros - 1) 个 0 而需要移动 (zeros - 1) 次, 对于当前 0 来说, 它
在新数组中的位置为 i + zeros - 1, 然后将 zeros 减少 1 继续循环;
    """

    def duplicateZeros_v2(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # jy: 统计 0 的个数;
        zeros = len(list(filter(lambda x: x == 0, arr)))
        length = len(arr)

        for i in range(length - 1, -1, -1):
            # jy: 将当前字符先移动 zeros 位(如果移动后超出数组范围, 则忽略);
            if i + zeros < length:
                arr[i + zeros] = arr[i]
            # jy: 如果当前位置为 0, 其原先的 0 已经被移动到 i+zeros 位置了, 则该位置的前面
            #    一个位置的值也应该是 0(此过程 zeros 减 1, 表示该为 0 的位置之前的元素需要
            #    向后移动的位数);
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < length:
                    arr[i + zeros] = 0



arr = [1,0,2,3,0,4,5,0]
# After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Solution().duplicateZeros_v1(arr)
print(arr)


arr = [1,0,2,3,0,4,5,0]
# After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Solution().duplicateZeros_v2(arr)
print(arr)


arr = [1,2,3]
# After calling your function, the input array is modified to: [1,2,3]
Solution().duplicateZeros_v2(arr)
print(arr)


