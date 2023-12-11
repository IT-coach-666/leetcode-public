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
title_jy = "Sort-Array-By-Parity-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array ``A`` of non-negative integers, half of the integers in ``A`` are odd,
and half of the integers are even. Sort the array so that whenever A[i] is odd, i is
odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.


Example 1:
Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""






from typing import List



class Solution:
    """
和 905_Sort-Array-By-Parity.py 的解法 2 类似, 分别使用 even 和 odd 两个指针指向数组的前
两个元素, 如果 even 指向的数字为偶数则对 even 加 2, 直到 even 指向的数为奇数; 如果 odd 指
向的数字为奇数则对 odd 加 2, 直到 odd 指向的数为偶数, 然后交换 even 和 odd 处的数字;
    """
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = 0, 1
        length = len(A)

        while even < length and odd < length:
            while even < length and A[even] & 1 == 0:
                even += 2

            while odd < length and A[odd] & 1 == 1:
                odd += 2

            if even < length and odd < length:
                A[even], A[odd] = A[odd], A[even]
                even += 2
                odd += 2

        return A


A = [4,2,5,7]
# Output: [4,5,2,7]
res = Solution().sortArrayByParityII(A)
print(res)


