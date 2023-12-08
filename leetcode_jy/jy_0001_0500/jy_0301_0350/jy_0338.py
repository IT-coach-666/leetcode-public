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
title_jy = "Counting-Bits(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a non negative integer number ``num``, for every numbers i in the range 0 ≤ i ≤ num
calculate the number of 1's in their binary representation and return them as an array.


Example 1:
Input: 2
Output: [0, 1, 1]

Example 2:
Input: 5
Output: [0, 1, 1, 2, 1, 2]


Follow up:
1) It is very easy to come up with a solution with run time O(n*sizeof(integer)). But
   can you do it in linear time O(n)/possibly in a single pass?
2) Space complexity should be O(n).
3) Can you do it like a boss? Do it without using any builtin function like
   __builtin_popcount in c++ or in any other language.
"""


from typing import List


class Solution:
    """
解法1: 第一种解法就是遍历 0 到 num 的数, 调用 191_Number-of-1-Bits.py 的方法计算每个数
各自包含几个 1 即可;
    """
    def countBits_v1(self, num: int) -> List[int]:
        return [self._hammingWeight(x) for x in range(num+1)]

    def _hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            # jy: n & (n-1) 会消掉 n 最低位的 1;
            n = n & (n-1)
            count += 1
        return count

    """
解法2: 核心思想是计算第 k 个数的时候, 复用 k 之前的数的计算结果; 这里同样用到
了 191_Number-of-1-Bits.py 中解法 2 的位运算性质: n & (n-1) 会消掉 n 最低位
的 1; 执行 k & (k-1) 后, 相当于 k 的二进制表示中少了最低位的 1, 所以我们只要
找到 k & (k-1) 对应的数有多少个 1 之后, 再加上 1 就是 k 的二进制有多少个 1;
    """
    def countBits_v2(self, num: int) -> List[int]:
        count = [0] * (num+1)

        for i in range(1, num+1):
            count[i] = count[i & (i-1)] + 1

        return count


num = 2
# Output: [0, 1, 1]
res = Solution().countBits_v1(num)
print(res)


num = 5
# Output: [0, 1, 1, 2, 1, 2]
res = Solution().countBits_v2(num)
print(res)


