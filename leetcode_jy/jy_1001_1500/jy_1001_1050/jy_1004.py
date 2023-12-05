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
title_jy = "Max-Consecutive-Ones-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array ``A`` of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.



Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
             Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]



Note:
1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1
"""


from typing import List


class Solution:
    """
滑动窗口: 维护一个 0 的个数不超过 K 的窗口(窗口可包含 1, 故长度可以大于 K), 当前窗口的
大小就是反转(即将 0 修改为 1)至多 K 个 0 后连续 1 的子数组的长度;

遍历数组, 记录当前窗口中 0 的个数, 如果当前数字为 0, 则 0 的个数加 1; 如果 0 的个数超
过 K, 则说明当前窗口不符合题目要求, 需要更新窗口至下一个符合条件的窗口;

更新窗口时, 逐步移动窗口的左边界, 因为新的窗口需要剔除掉 0, 所以在
遇到 0 之前的 1 最终也不会保留, 遇到 0 时, 则将窗口中 0 的个数减 1, 直到 0 的个数
再次不超过 K, 即找到了一个新的窗口;
    """
    def longestOnes(self, A: List[int], K: int) -> int:
        # jy: 记录滑动窗口的起始下标;
        window_start = 0
        # jy: 记录滑动窗口中 0 的个数;
        zeros = 0
        # jy: 记录最长连续 1 的子数组的长度;
        max_length = 0

        for j in range(len(A)):
            # jy: 如果当前数值为 0, 则 0 的个数加 1;
            if A[j] == 0:
                zeros += 1
            # jy: 如果 0 的个数大于 K, 表明窗口不符合要求, 将窗口最左侧的 0 剔除, 即将窗口
            #    的起始坐标替换为最左侧的 0 的坐标的下一个坐标(不需担心其左侧的 1 被剔除而
            #    导致最大的连续 1 漏比较了, 在上一轮 0 的个数等于 K 时已经获取其最大长度)
            while zeros > K:
                if A[window_start] == 0:
                    zeros -= 1
                window_start += 1
            # jy: 更新最大连续 1 子数组长度, (j - window_start + 1) 即为该有效窗口的大小;
            #    不必每次都比较得出最大长度, 当窗口中 0 的个数为 K 或者已经遍历到最后一个
            #    元素时比较即可;
            if zeros == K or j == len(A)-1:
                max_length = max(max_length, j - window_start + 1)
            # max_length = max(max_length, j - window_start + 1)

        return max_length



A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
# Output: 6 , [1,1,1,0,0,1,1,1,1,1,1]
res = Solution().longestOnes(A, K)
print(res)


A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
# Output: 10 , [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
res = Solution().longestOnes(A, K)
print(res)


