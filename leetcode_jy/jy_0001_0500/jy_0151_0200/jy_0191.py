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
title_jy = "Number-of-1-Bits(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Write a function that takes an unsigned integer and return the number of '1' bits it
has (also known as the Hamming weight).


Example 1:
Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.


Note: Note that in some languages such as Java, there is no unsigned integer type. In this case, the
input will be given as signed integer type and should not affect your implementation, as the internal
binary representation of the integer is the same whether it is signed or  unsigned.

In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in
Example 3 above the input represents the signed integer -3.
"""


class Solution:
    """
解法1: 将 n 和 2 取模(即 n % 2)或和 1 做与运算(即 n & 1), 如果结果为 1, 则表示末位为 1, 然
后 n 右移一位后继续判断末位是否为 1, 直到 n 为 0 为止;

JY: 性能普通
    """
    def hammingWeight_v1(self, n: int) -> int:
        count = 0
        while n > 0:
            # jy: 按位与运算, 如果两个相应位都为 1, 则该位的结果为 1,否则为 0;
            if n & 1:
            # if n % 2:
                count += 1
            # jy: 将 ">>" 左边的数 n 的二进制表示结果右移 1 位(即除以 2, 注意需要整除);
            n >>= 1
            # n //= 2
        return count

    """
解法2: 位运算(与运算)的性质: n & (n-1) 会消掉 n 最低位(最右侧)的 1
所以可以不断执行这个运算, 执行一次表示有一个 1, 直到 n 等于 0;

JY: 性能更好
    """
    def hammingWeight_v2(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        return count



# jy: "0o" 开头表示是 8 进制表示法
n = 0o00000000000000000000000000001011
print("====== ", n)
# Output: 3
res = Solution().hammingWeight_v1(n)
print(res)


n = 0o00000000000000000000000010000000
# Output: 1
res = Solution().hammingWeight_v1(n)
print(res)


n = 0o11111111111111111111111111111101
# Output: 31
res = Solution().hammingWeight_v2(n)
print(res)

n = 0o11111111111111111111111111111101
# Output: 31
print(str(n))  # jy: 转换为字符串后的结果并非以上看到的结果的字符串形式, 故不能通过统计字符串中有多少个 "1" 来求解




print(0o7 >>1 >>1>>1)

n = 0o00000000000000000000000000001011
print(n)
n = n & (n-1)
print(n)
n = n & (n-1)
print(n)
n = n & (n-1)
print(n)

