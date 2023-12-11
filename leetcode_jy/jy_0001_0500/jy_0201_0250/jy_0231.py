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
title_jy = "Power-of-Two(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer, write a function to determine if it is a power of two.


Example 1:
Input: 1
Output: true
Explanation: 2^0 = 1

Example 2:
Input: 16
Output: true
Explanation: 2^4 = 16

Example 3:
Input: 218
Output: false
"""


class Solution:
    """
解法1: 类似 191_Number-of-1-Bits.py 的解法 1,  n 不断和 1 做位运算, 只要结
果为 1, 则返回 false, 否则 n 右移一位, 直到 n 为 0; 注意 n 为 0 或 1 的情况
是例外, 应做例外处理;
    """
    def isPowerOfTwo_v1(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True

        while n != 0:
            # jy: 偶数与 1 做位与运算, 总是等于 0, 如果是奇数, 则肯定不是 2 的 n 次方;
            if n & 1:
                return False
            # jy: n 右移一位, 相当于 n // 2
            n >>= 1


    """
解法2: 因为 2 的幂次方的二进制表示只有首位为 1, 所以借助 191_Number-of-1-Bits.py 的
解法 2 的公式, 只要判断 n & (n-1) 是否为 0 即可(该操作会消掉 n 最低位的 1), 为 0 说
明 n 的二进制表示只有一个 1;
    """
    def isPowerOfTwo_v2(self, n: int) -> bool:
        return n != 0 and n & (n - 1) == 0


n = 1
# Output: true
res = Solution().isPowerOfTwo_v1(n)
print(res)


n = 16
# Output: true
res = Solution().isPowerOfTwo_v1(n)
print(res)


n = 218
# Output: false
res = Solution().isPowerOfTwo_v1(n)
print(res)


