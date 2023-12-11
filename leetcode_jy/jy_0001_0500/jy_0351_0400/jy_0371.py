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
title_jy = "Sum-of-Two-Integers(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two integers ``a`` and ``b``, return the sum of the two integers without
using the operators "+" and "-";


Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5


Constraints:
-1000 <= a, b <= 1000
"""


def jy_bin(num):
    str_ = bin(num).lstrip("0b").rjust(32, "0")
    return str_[:8] + " " + str_[8: 16] + " " + str_[16: 24] + " " + str_[24:]


class Solution:
    """
十进制加法分三步(以 5 + 17 = 22 为例):
1) 只做个位相加不进位(不考虑进位对每一位相加), 此时相加结果为 2
   (个位数 5 和 7 相加不进位是 2; 十位数 0 和 1 相加结果是 1)
2) 做进位的运算, 5 + 7 中有进位, 进位的值是 1, 与原先的十位数的值 1 相加即为 2;
3) 将个位和十位的结果拼接即为 22

以上三步同样适用于二进制位运算:
1) 不考虑进位对每一位相加(和异或运算一样):
   0 加 0, 1 加 1 结果都是 0
   0 加 1, 1 加 0 结果都是 1
2) 考虑进位(可看成是先做位与运算, 然后向左移动一位):
   0 加 0, 0 加 1, 1 加 0 都不产生进位
   只有 1 加 1 向前产生一个进位
3) 重复以上两步, 直到进位是 0 为止

所以计算 a + b 时, 先通过 a & b << 1 求得进位, 再通过 a ^ b 求得无进位部分的和, 两
数之和就是 a + b 的值, 但由于不能使用加号, 所以需要重复上述步骤, 直到进位为 0;

注意: 由于 Python 的 int 的范围大于 32 比特表示的范围, 所以不能通过判断进位为 0 来
终止循环, 可以借助一个 mask 即 0xffffffff 将其与进位进行与运算, 如果结果为 0, 说明
进位为 0 或者超过了 32 比特表示的范围;
    """
    def getSum_v1(self, num1: int, num2: int) -> int:
        mask = 0xffffffff

        while (num2 & mask) > 0:
            # jy: 每进行 i 轮与运算, carry 最右侧的 i 个位置都会赋值为 0, 第 i 个位
            #     置的左边一位则记录进位与否;
            carry = (num1 & num2) << 1
            # jy: 每进行 i 轮异或运算(i 为 1-based), 就实现将目标结果数值的最右侧
            #     的 i 个位置赋值最终结果的二进制数(0 或 1);
            num1 = num1 ^ num2
            num2 = carry
        # jy: 返回结果不能简单返回 num1, 否则 num1 = -1, num2 = 1 时的样例在 python 中不会通过;
        #     因为如果最终 num2 大于 0, 但 num2 & mask 已经为 0, 表明 num2 对应的二进制表达式超
        #     过了 (2 ** 32 - 1), 为 2 ** n (其中 n >= 32); num1 或 num2 中出现负数就可能会产生
        #     该现象
        return num1 & mask if num2 > 0 else num1

    def getSum_v2(self, num1: int, num2: int) -> int:
        # print("-" * 88)
        # print("num1: ".rjust(12), jy_bin(num1))
        # print("num2: ".rjust(12), jy_bin(num2))
        # jy: 以下代码逻辑以 num1 和 num2 均为 3 (011) 为例进行思考(目标结果为 110):
        #     round-1: tmp  = 000
        #              num2 = 110
        #              num1 = 000  (round-1 完成对最右一位进行正确赋值)

        #     round-2: tmp  = 110
        #              num2 = 000
        #              num1 = 110  (round-2 完成对最右第二位进行正确赋值, 此时 num2 为 0, 终止)
        mask = 0xffffffff
        while num2 & mask:
            # jy: 每进行 i 轮异或运算(i 为 1-based), 就实现将目标结果数值的最右侧
            #     的 i 个位置赋值最终结果的二进制数(0 或 1);
            tmp = num1 ^ num2
            # print("=====tmp ", jy_bin(tmp))
            # jy: 每进行 i 轮与运算, num2 最右侧的 i 个位置都会赋值为 0, 第 i 个位
            #     置的左边一位则记录进位与否;
            num2 = (num1 & num2) << 1
            # print("=====num2 ", jy_bin(num2))
            num1 = tmp
            print("num1 == ", num1, " || num1 & mask == ", num1 & mask, "num2 == ", num2, " || num2 & mask == ", num2 & mask)
        print("add result: ".rjust(12), jy_bin(num1))
        # jy: 返回结果不能简单返回 num1, 否则 num1 = -1, num2 = 1 时的样例在 python 中不会通过;
        #     因为如果最终 num2 大于 0, 但 num2 & mask 已经为 0, 表明 num2 对应的二进制表达式超
        #     过了 (2 ** 32 - 1), 为 2 ** n (其中 n >= 32); num1 或 num2 中出现负数就可能会产生
        #     该现象;
        print("num2 ========== ", num2)
        return num1 & mask if num2 > 0 else num1


a = 1
b = 2
# Output: 3
res = Solution().getSum_v1(a, b)
print(res)


a = 2
b = 3
# Output: 5
res = Solution().getSum_v2(a, b)
print(res)

a = -1
b = 1
# Output: 0
res = Solution().getSum_v2(a, b)
print(res)

a = -2
b = 8
# Output: 6
res = Solution().getSum_v2(a, b)
print(res)

'''
# jy: 16 进制表示, 对应 32 位都为 1, 即 4294967295 (2 ** 32 - 1)
mask = 0xffffffff
print("\n\nmask == ", mask, " ================= mask & (2 ** 32 - 1) == ", mask & (2 ** 32 - 1))
print("mask & (2 ** 32) == ", mask & (2 ** 32), " ============ mask & (2 ** 32 + 3) == ", mask & (2 ** 32 + 3))
'''


