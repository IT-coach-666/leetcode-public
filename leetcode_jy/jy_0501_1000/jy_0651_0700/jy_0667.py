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
title_jy = "Beautiful-Arrangement-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two integers n and k, construct a list answer that contains n different positive integers ranging from 1 to n and obeys the followng requirement:
Suppose this list is answer = [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k dstinct integers.
Return the list answer. If there multiple valid answers, return any of them.

Example 1:
Input: n = 3, k = 1
Output: [1,2,3]
Explanation: The [1,2,3] has three different positive integers ranging from 1 to 3, and the [1,1] has exactly 1 distinct integer: 1

Example 2:
Input: n = 3, k = 2
Output: [1,3,2]
Explanation: The [1,3,2] has three different positive integers ranging from 1 to 3, and the [2,1] has exactly 2 distinct integers: 1 and2.


Constraints:
1 <= k < n <= 10^4
"""


from typing import List


class Solution:
    """
对于 n 个数, 差值最少的序列为 1, 2, 3, ..., n, 差值最多的序列为 1, n, 2, n - 1, 3, ...,, 有 n - 1 个, 根据这个规律先构造 k + 1 长度的序列, 这样就有 k 个不同的差值, 参与构造 k + 1 长度序列的数字为 1, 2, 3, ..., k + 1, 然后对于剩下的 k + 2, k + 3, ..., n 个数, 直接依次放到构造好的序列后即可, 此时完整的序列为 1, k + 1, 2, k, 3, k - 1, ..., k + 2, k + 3, ..., n, 其中 k + 2, k + 3, ..., n 这段序列的差值都为1, 该差值已经包含在了前半段序列中, 唯一需要判断的是前半段序列的最后一个数字和 k + 2 的差值是否已经在序列中, 这个也必然存在, 因为前半段 k + 1长度的差值分比为 k, k - 1, k - 2, ..., 1, 前半段的最后一个数为:
1. , k 为偶数
2. , k 为奇数
不管哪种和 k - 2 的绝对值差都在差值序列 k, k - 1, k - 2, ..., 1 中
    """
    def constructArray(self, n: int, k: int) -> List[int]:
        low, high = 1, k + 1
        result = []

        for i in range(k + 1):
            if i & 1 == 0:
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1

        for i in range(k + 1, n):
            result.append(i + 1)

        return result

