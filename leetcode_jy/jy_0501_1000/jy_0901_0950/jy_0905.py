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
title_jy = "Sort-Array-By-Parity(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array ``A`` of non-negative integers, return an array consisting of all
the even elements of ``A``, followed by all the odd elements of ``A``. You may
return any answer array that satisfies this condition.


Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:
1 <= A.length <= 5000
0 <= A[i] <= 5000
"""



from typing import List



class Solution:
    """
解法1: 因为题目不要求新数组中奇数的顺序, 所以和 283_Move-Zeroes.py 的解法 2 类似,
记 tail 为新数组中第一个奇数的位置, 遍历数组, 如果当前数字为偶数, 交换 tail 和 i
处的数字即可, 并将 tail 加 1;
    """
    def sortArrayByParity_v1(self, A: List[int]) -> List[int]:
        # jy: 假设数组中第一个元素为奇数;
        tail = 0
        # jy: 遍历数组, 如果当前元素为偶数(与 1 进行与操作为 0), 则与 tail 位置交换后, tail 进 1;
        for i in range(len(A)):
            if A[i] & 1 == 0:
                A[tail], A[i] = A[i], A[tail]
                tail += 1

        return A


    """
解法2: 分别使用 low 和 high 两个指针指向数组的首尾:
如果 low 指向的数字为偶数则对 low 加 1, 直到 low 指向的数为奇数;
如果 high 指向的数字为奇数则对 high 减 1, 直到high 指向的数为偶数;
然后交换 low 和 high 处的数字;
    """
    def sortArrayByParity_v2(self, A: List[int]) -> List[int]:
        low, high = 0, len(A) - 1

        while low < high:
            # jy: 如果 low 为偶数, 则不断进 1, 直到 low 位置为奇数为止;
            while low < len(A) and A[low] & 1 == 0:
                low += 1
            # jy: 如果 high 为奇数, 则不断左移 1 位, 直到 high 为偶数为止;
            while high >= 0 and A[high] & 1 == 1:
                high -= 1
            # jy: 如果 low 小于 high, 则交换 low 和 high 后, low 进 1, high 左移 1 位, 继续循环;
            if low < high:
                A[low], A[high] = A[high], A[low]
                low += 1
                high -= 1

        return A


A = [3,1,2,4]
# Output: [2,4,3,1]
res = Solution().sortArrayByParity_v1(A)
print(res)


A = [3,1,2,4]
# Output: [2,4,3,1]
res = Solution().sortArrayByParity_v2(A)
print(res)


