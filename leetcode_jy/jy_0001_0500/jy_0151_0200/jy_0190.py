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
title_jy = "Reverse-Bits(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Reverse bits of a given 32 bits unsigned integer.

Note:
1) Note that in some languages such as Java, there is no unsigned integer type.
   In this case, both input and output will be given as a signed integer type.
   They should not affect your implementation, as the integer's internal binary
   representation is the same, whether it is signed or unsigned.
2) In Java, the compiler represents the signed integers using 2's complement
   notation. Therefore, in Example 2 above, the input represents the signed
   integer -3 and the output represents the signed integer -1073741825.


Follow up:
If this function is called many times, how would you optimize it?


Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the
             unsigned integer 43261596, so return 964176192 which its binary representation
             is 00111001011110000010100101000000.

Example 2:
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the
             unsigned integer 4294967293, so return 3221225471 which its binary representation
             is 10111111111111111111111111111111.


Constraints:
The input must be a binary string of length 32
"""


class Solution:
    """
遍历 32 次, 每次遍历时将 n 与 1 进行与运算得到最后一位比特位, 然后将 n 右移
一位, 将最终结果左移一位后加上当前的比特位
    """
    def reverseBits_v1(self, n: int) -> int:
        result = 0
        for i in range(32):
            # jy: 取出数值 n 最左侧的一位比特位值
            bit = n & 1
            n = n >> 1
            # jy: 将 result 左移一位, 使得最右侧的一位用来放置当前比特位 bit;
            result = (result << 1) + bit
        return result

    def reverseBits_jy(self, n):
        res = ""
        while n:
            tmp = n & 1
            if tmp == 1:
                # jy: 求 n 对应的二进制表示
                # res = "1" + res
                # jy: 求 n 对应的二进制表示的倒序结果
                res += "1"
            else:
                # jy: 求 n 对应的二进制表示
                # res = "0" + res
                # jy: 求 n 对应的二进制表示的倒序结果
                res += "0"
            n >>= 1
        # jy: 注意反转二进制结果表示时, 右边不满 32 位需要用 "0" 进行补齐;
        res = res + "0" * (32 - len(res))
        return int(res, 2)


n = int("00000010100101000001111010011100", 2)
# Output:    964176192 (00111001011110000010100101000000)
res = Solution().reverseBits_v1(n)
print(res)


n = int("11111111111111111111111111111101", 2)
# Output:   3221225471 (10111111111111111111111111111111)
res = Solution().reverseBits_v1(n)
print(res)


n = int("00000010100101000001111010011100", 2)
# Output:   964176192 (00111001011110000010100101000000)
res = Solution().reverseBits_jy(n)
print(res)


