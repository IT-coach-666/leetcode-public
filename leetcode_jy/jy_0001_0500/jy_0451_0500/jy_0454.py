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
title_jy = "4Sum-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there
are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500.
All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at
most 2^31 - 1.


Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
Output: 2
Explanation: The two tuples are:
(0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
(1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""


from typing import List

class Solution:
    """
这道题的核心思想和 001_Two-Sum.py 一致, 将四个数之和拆成两个两数之和:
1) 首先将 A 和 B 的两数之和保存在 Map 中, 键为两数之和, 值为出现的次数
2) 然后将 C 和 D 的两数之和保存在另一个 Map 中,
3) 最后遍历其中一个 Map, 判断当前值的相反数是否在另一个 Map 中即可;
    """
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        length = len(A)
        mapping1, mapping2 = {}, {}
        # jy: 将 A 和 B 的两数之和保存到字典的 key 中, value 为出现的次数; C 和 D 同理;
        for i in range(length):
            for j in range(length):
                sum1 = A[i] + B[j]
                sum2 = C[i] + D[j]

                if sum1 in mapping1:
                    mapping1[sum1] = mapping1[sum1] + 1
                else:
                    mapping1[sum1] = 1

                if sum2 in mapping2:
                    mapping2[sum2] = mapping2[sum2] + 1
                else:
                    mapping2[sum2] = 1
        # jy: 遍历其中一个字典, 判断 key 的相反数是否在另一个字典中存在, 存在则两者次数
        #    相乘; 多种情况进行累加;
        for key, value in mapping1.items():
            count += value * mapping2.get(-key, 0)

        return count

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
res = Solution().fourSumCount(A, B, C, D)
print(res)


