# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
from typing import List
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Reverse-Integer(number)"
# jy: 记录不同解法思路的关键词
tag_jy = "UNDO"


"""
Given a 32-bit signed integer, reverse digits of an integer.


Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21


Note:
1) Assume we are dealing with an environment which could only store integers
   within the 32-bit signed integer range: [−2^31,  2^31 − 1].
2) For the purpose of this problem, assume that your function returns 0 when
   the reversed integer overflows.
"""


class Solution:
    """
解法1: x 不断除 10 取最后一位作为新数字的高位;
(由于 Python 的取模运算负数的处理不同于 Java, 所以要区分是否是负数)
    """
    def reverse_v1(self, x: int) -> int:
        # jy: 取 x 的绝对值, 用 is_negative 变量标记其正负;
        is_negative, x = (True, -x) if x < 0 else (False, x)

        result = 0
        while x > 0:
            # jy: 获取 x 的最后一个数值, 并在不断向左移(乘以 10)
            result = result * 10 + x % 10
            # jy: 去除 x 的最后一个数值(因为其以及处理完了)
            x //= 10
            # jy: 如果结果值大于 2 ** 31 - 1, 则直接返回 0;
            if result > 2 ** 31 - 1:
                return 0
        return -result if is_negative else result

    """
解法2: 解法 1 中的 result 仍可能大于 (2 ** 31 - 1), 与题意不符; 需要修改完善 result 的判
断条件; 
判断条件确认如下(记 max_int = 2 ** 31 -1 = 2147483647, digit = x % 10), 即目标要确保: 
result * 10 + digit <= max_int
即:
result * 10 + digit <= [max_int // 10] * 10 + max_int % 10 
result * 10 + digit <= [max_int // 10] * 10 + 7
(result - [max_int // 10]) * 10 <= 7 - digit 
由于 7 - digit 是小于或等于 7 的, 要使得上面条件成立, 则必须有
1) result < max_int // 10  (此时左侧小于或等于 -10, 而右侧的取值范围为 [-2, 7], 不等式成立) 
2) result = max_int // 10  (注意到在该情况下, 当前 result 只比 max_int 少一位, 此时如果下
   如果还有要推进的数值(即更新后的 x 大于 0), 则表明原 x 数值与 max_int 有相同的位数, 由于 x
   是不大于 max_int 的数值, 因此其最高位肯定是 1 或 2, 即对应的 digit 只能为 1 或 2, 这种情
   况下不等式也肯定是满足的)
   
因此, 使不等式满足的条件为: result <= max_int // 10, 在更新 result 时判断该条件是否成立即
可, 如果不成立, 则直接返回 0 (因为此时更新 result 会导致 result > max_int)
    """
    def reverse_v2(self, x: int) -> int:
        is_negative, x = (True, -x) if x < 0 else (False, x)

        upper_max = (2 ** 31 - 1) // 10
        result = 0
        while x > 0:
            # jy: 由于此题的输入数值本身就是在有效范围内的, 故此处根据推论只需确保
            #     result <= upper_max 即可; 当 result == upper_max 时, 也肯定不
            #     会有下一个没计算的数值了, 否则原先反转前的数值肯定是无效的(这是与
            #     题目 0008 的最主要区别); 
            if result > upper_max:
                return 0
            result = result * 10 + x % 10
            x //= 10
        return -result if is_negative else result


x = -123
res = Solution().reverse_v1(x)
print(res)

x = -321
res = Solution().reverse_v2(x)
print(res)

x = 120
res = Solution().reverse_v2(x)
print(res)


