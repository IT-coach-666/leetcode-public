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
tag_jy = "双指针 | 单指针"

"""
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing
order, and two integers `m` and `n`, representing the number of elements in 
`nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be
stored inside the array `nums1`. To accommodate this, `nums1` has a length of
`m + n`, where the first `m` elements denote the elements that should be merged,
and the last `n` elements are set to 0 and should be ignored. `nums2` has a 
length of `n`.


Example 1:
Input:
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6],          n = 3
Output: [1, 2, 2, 3, 5, 6]
Explanation: The arrays we are merging are [1, 2, 3] and [2, 5, 6]. The result
             of the merge is [1, 2, 2, 3, 5, 6]

Example 2:
Input: 
nums1 = [1], m = 1
nums2 = [],  n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
             The result of the merge is [1].

Example 3:
Input: 
nums1 = [0], m = 0
nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
             The result of the merge is [1].
             Note that because m = 0, there are no elements in `nums1`. The 0
             is only there to ensure the merge result can fit in `nums1`.


Constraints:
1) nums1.length == m + n
2) nums2.length == n
3) 0 <= m, n <= 200
4) 1 <= m + n <= 200
5) -10^9 <= nums1[i], nums2[j] <= 10^9
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""


class Solution:
    """
解法 1: 双指针 + 结尾指针

使用双指针指向有效数组的末尾, 选择两个数组末尾中较大的值放到真正的数组末尾, 循
环条件只需要判断 nums2 是否还有数字即可, 因为最后返回的是 nums1, 如果 nums2 没
有数字了, nums1 中剩下的数字本身已有序, 无需再排序

JY: 该解法的前提: 知道 nums1 中有多少个有效元素, 以及 nums1 的最终合并后的长度
    """
    def merge_v1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # jy: 双指针均指向数组末尾 (可先求得 tail, 随后直接将 m 和 n 当做末
        #     尾指针, 此时可省略变量 i 和 j)
        i, j = m - 1, n - 1
        tail = m + n - 1
        # jy: 如果 nums2 中仍有数值, 则继续挑选尾指针中的较大值放入 tail 指针对应位置;
        #    否则, 停止比较, nums1 中的数值也本身已有序;
        while j >= 0:
            # jy: 基于 i 进行取数时, 需确保下标 i 有效
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[tail] = nums1[i]
                i -= 1
            else:
                nums1[tail] = nums2[j]
                j -= 1
            tail -= 1

    def merge_v2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tail = m + n - 1
        while n > 0:
            # jy: 基于下标 m-1 取数时, 需确保该下标有效
            if m-1 >= 0 and nums1[m-1] > nums2[n-1]:
            # jy: m 是逐渐减 1 的, 如果 m 不为 0, 即表明 m >= 1
            #if m != 0 and nums1[m-1] > nums2[n-1]:
                nums1[tail] = nums1[m-1]
                m -= 1
            else:
                nums1[tail] = nums2[n-1]
                n -= 1

            tail -= 1



nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge_v1(nums1, m, nums2, n)
print(nums1)



nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge_v2(nums1, m, nums2, n)
print(nums1)


