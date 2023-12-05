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
title_jy = "Merge-Sorted-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""

"""
Given two sorted integer arrays , merge ``nums2`` into ``nums1``
as one sorted array. Do not return anything, modify ``nums1`` in-place instead.

You are given two integer arrays ``nums1`` and ``nums2``, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in `nums1`` and ``nums2``
respectively. Merge `nums1`` and ``nums2`` into a single array sorted in non-decreasing order.

``nums1`` has a length of m + n, where the first m elements denote the elements that should
be merged, and the last n elements are set to 0 and should be ignored.


Example:
Input:
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6],          n = 3
Output: [1, 2, 2, 3, 5, 6]


Note:
1) The number of elements initialized in nums1 and nums2 are m and n respectively.
2) You may assume that nums1 has enough space (size that is greater or equal to m + n) to
  hold additional elements from nums2.
"""


from typing import List


class Solution:
    """
分别使用两个指针指向有效数组的末尾, 选择较大的值放到数组末尾, 循环条件只需要判断 nums2 是否
还有数字即可, 因为最后返回的是 nums1, 如果 nums2 没有数字了, nums1 中剩下的数字本身已有序,
无需再排序;

JY: 该方式起作用的前提是: 知道 nums1 中有多少个有效元素, 以及 nums1 的长度即为最终合并后的长度;
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # jy: 双指针均指向数组末尾(在先求解得 tail 后, 直接将 m 和 n 当做即可, 可以省略掉遍历 i 和 j);
        i, j = m - 1, n - 1
        tail = m + n - 1
        # jy: 如果 nums2 中仍有数值, 则继续挑选尾指针中的较大值放入 tail 指针对应位置;
        #    否则, 停止比较, nums1 中的数值也本身已有序;
        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[tail] = nums1[i]
                i -= 1
            else:
                nums1[tail] = nums2[j]
                j -= 1
            tail -= 1

    def merge_2022_02_23(self, A: List[int], m: int, B: List[int], n: int) -> None:
        tail = m + n - 1
        while m > 0 and n > 0:
            if A[m - 1] > B[n - 1]:
                A[tail] = A[m - 1]
                m -= 1
                tail -= 1
            else:
                A[tail] = B[n - 1]
                n -= 1
                tail -= 1
        while n > 0:
            A[tail] = B[n - 1]
            tail -= 1
            n -= 1

    def merge_2022_02_27(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tail = m + n - 1
        while n > 0:
            # jy: 当 n 大于 0 时, m 此时可能已经为 0, 但只有当 m 大于 0 的情况下才需要做相应操作;
            if m != 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[tail] = nums1[m - 1]
                m -= 1
            else:
                nums1[tail] = nums2[n - 1]
                n -= 1
            tail -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)


