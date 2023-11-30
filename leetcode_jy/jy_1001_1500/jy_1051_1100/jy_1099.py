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
title_jy = "Two-Sum-Less-Than-K(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array ``A`` of integers and integer ``K``, return the maximum S such that 
there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this
equation, return -1.



Example 1:
Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.

Example 2:
Input: A = [10,20,30], K = 15
Output: -1
Explanation: In this case it's not possible to get a pair sum less that 15.


Note:
1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""



class Solution:
    """
这道题不再是求两数之和等于 K, 而是求两数之和小于 K 中的最大值; 

在 167_Two-Sum-II_Input-array-is-sorted.py 中, 我们使用双指针法使两数之和逐渐逼近目
标值来求解, 此题同样可以使用双指针法, 记 max_sum 为所求之和, 初始值为 -1, 如果两个指
针所在数之和大于 K, 则高位指针减 1, 否则低位指针加 1, 同时 max_sum 赋值为 max_sum 和
当前两数之和的最大值;

由于双指针法需要数组有序, 所以需要先对数组进行排序, 最终算法复杂度为 O(n*lgn);
    """
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        # jy: 对数组进行排序;
        A.sort()
        max_sum = -1
        i, j = 0, len(A) - 1

        while i < j:
            current_sum = A[i] + A[j]

            if current_sum >= K:
                j -= 1
            else:
                i += 1
                max_sum = max(max_sum, current_sum)

        return max_sum


A = [34,23,1,24,75,33,54,8]
K = 60
# Output: 58
res = Solution().twoSumLessThanK(A, K)
print(res)


A = [10,20,30]
K = 15
# Output: -1
res = Solution().twoSumLessThanK(A, K)
print(res)




