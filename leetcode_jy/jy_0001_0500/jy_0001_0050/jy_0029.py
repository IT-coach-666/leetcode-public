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
title_jy = "divide-two-integers(number)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 循环迭代(递归改写) | 列竖式除法"


"""
Given two integers `dividend` and `divisor`, divide two integers without
using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its 
fractional part. For example, 8.345 would be truncated to 8, and -2.7335
would be truncated to -2.

Return the quotient(商) after dividing `dividend` by `divisor`.


Note: Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem,
if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and
if the quotient is strictly less than -2^31, then return -2^31.

 

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
"""


class Solution:
    """
解法 1: 列竖式算除法

除法和移位是两种完全不同的概念, 移位能够用于求 /2 的结果是特定进制作为除数可
以求解的结果; 如果在编译过程中不进行编译优化, 在汇编层面看对应的就是两种不同
的指令, 除法指令本身是非常慢的, 而移位本身非常快

x << i 即: x * 2^i
x >> i 即: x / 2^i
"""
    def divide_v1(self, dividend: int, divisor: int) -> int:
        # jy: 异或运算, 只有一个大于 0, 一个小于 0 时才返回 True, 表
        #     明有符号 (负号), 即最终结果为负值
        sign = (dividend > 0) ^ (divisor > 0)
        #sign = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        # jy: 把除数不断左移, 直到它大于被除数 (最终 divisor > dividend)
        while dividend >= divisor:
            count += 1
            # jy: 即 divisor = divisor * 2
            divisor <<= 1

        result = 0
        while count > 0:
            count -= 1
            # jy: divisor = divisor / 2 
            #     最开始时 divisor > dividend, 经过此处操作后 divisor < dividend
            divisor >>= 1
            if divisor <= dividend:
                # jy: result 加上 2^count 
                result += 1 << count
                dividend -= divisor

        if sign: 
            result = -result
        # jy: -(1 << 31) 即 -2^31, 为 -2147483648; (1 << 31) - 1 即 2^31 - 1,
        #     为 2147483647
        return result if -(1 << 31) <= result <= (1 << 31) - 1 else (1 << 31) - 1 
        #return result if -2**31 <= res <= 2**31-1 else 2**31 - 1

    """
解法 2: 类似解法 1
    """
    def divide_v2(self, dividend: int, divisor: int) -> int:
        if abs(dividend) < abs(divisor):
            return 0
        limit = 2**31 - 1
        neg = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        res, div, temp = 0, divisor, 1
        while dividend >= divisor:
            # jy: 使得 div * 2^i 的结果尽可能大, 但不超过 dividend
            while dividend > (div << 1):
                div <<= 1
                temp <<= 1
            dividend -= div
            div = divisor
            res += temp
            temp = 1
        res = -res if neg else res
        return res if -2**31 <= res <= 2**31-1 else limit


    """
解法 3: x << i 即 x * 2^i; 用 2^i 去作为乘法基数, 从 2^31 试到 2^0, 直到被除
数被减到比除数小, 每个能满足除要求的最大的 2 的幂都加入答案; 也可以理解为每
次计算出答案的 32 位中的某一位
    """
    def divide_v3(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # jy: b << i 即 b * 2^i; 1 << i 即 2^i 
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res


    """
解法 4: 递归 (二分搜索, 二进制搜索); 时间复杂度为 O(logn * logn), 内外
while 循环都是 logn; 空间复杂度为 O(1)

首先需要考虑正负号, 将分子分母全处理为正数; 其次在返回时要注意是否溢
出, 如果溢出要判断


每次利用加法, 将当前的 divisor 乘以两倍, 并同时用 multiple 记录下乘以
了 2 的多少次方, multiple 的变化过程是 1, 2, 4, 8, 16 ...

任何一个数都可以用二进制的方法得到, 所以可以利用二进制的思想来代表乘数
multiple, 最终得到一个 `divisor * multiple = dividend` 的 multiple

例如算 63 / 8 的过程为:
63 / 8 = (63 - 32) / 8 + 4
       = (63 - 32 - 16) / 8 + 4 + 2
       = (63 - 32 - 16 - 8) / 8 + 4 + 2 + 1
       = 7 / 8 + 4 + 2 + 1
       = 0 + 4 + 2 + 1
       = 7


二分查找算法的英文翻译是 binary search algorithm, 也可以翻译为二进制搜索, 是
一种时间复杂度为 O(logn) 的查找算法, 二分查找思想简单, 应用范围极广, 核心思想
是每次将有序数组分为一半, 则 k 次操作之后就是原数组的 n/2^k 个元素, 直到这个
值变为 1, 就查找到了那个元素

本题是以上思想的逆运算, 是从 1 开始, 不断变为二倍的搜索, 直到满足要求, 因此本
题也是考察二分查找思想的运用
    """
    def divide_v4(self, dividend: int, divisor: int) -> int:
        """
        计算 dividend / divisor 的结果 (最终结果取整)
        """
        # jy: [−2 ** 31, 2 ** 31 − 1]
        MIN_INT, MAX_INT = -2147483648, 2147483647
        # jy: 存储正负号, 并将分子分母转化为正数
        flag = 1
        # jy: 确保 dividend 和 divisor 都转为正数, 并用 flag 提前记录好最终
        #     运算结果的正负号信息
        if dividend < 0: 
            flag, dividend = -flag, -dividend
        if divisor < 0:
            flag, divisor  = -flag, -divisor 
        
        def div(dividend, divisor):
            """
            计算 dividend / divisor 的结果 (两个传入的参数均为正数, 最终结果取整)

            例如:
            1023 / 1 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 + 256 + 512

            63 / 8 = (63 - 32) / 8 + 4
	           = (63 - 32 - 16) / 8 + 4 + 2
	           = (63 - 32 - 16 - 8) / 8 + 4 + 2 + 1
                   = 7 / 8 + 4 + 2 + 1
                   = 0 + 4 + 2 + 1
                   = 7

            以下以 63 / 8 为例进行讲解
            """
            if dividend < divisor:
                return 0
            # jy: cur 初始值为 8
            cur = divisor
            multiple = 1
            # jy: 用加法求出保证 divisor * multiple <= dividend 的最
            #     大 multiple, 即 cur 分别乘以 1, 2, 4, 8, 16...2^n,
            #     即二进制搜索
            while cur + cur < dividend:
                cur += cur
                multiple += multiple
            return multiple + div(dividend - cur, divisor)

        res = div(dividend, divisor)
        # 恢复正负号
        res = res if flag > 0 else -res
        
        # 根据是否溢出返回结果
        if res < MIN_INT: 
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT
        

    """
解法 5: 迭代 (递归的改写)
    """
    def divide_v5(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647
        flag = 1 
        if dividend < 0: 
            flag, dividend = -flag, -dividend
        if divisor < 0:
            flag, divisor  = -flag, -divisor 
        
        res = 0
        while dividend >= divisor:  
            cur = divisor
            multiple = 1
            while cur + cur < dividend: 
                cur += cur 
                multiple += multiple
            dividend -= cur
            res += multiple
        
        res = res if flag > 0 else -res
        
        if res < MIN_INT:  
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT
        



dividend = 10
divisor = 3
res = Solution().divide_v1(dividend, divisor)
# jy: 3
print(res)


dividend = 7
divisor = -3
res = Solution().divide_v2(dividend, divisor)
# jy: -2
print(res)


dividend = 7
divisor = -3
res = Solution().divide_v3(dividend, divisor)
# jy: -2
print(res)


dividend = 7
divisor = -3
res = Solution().divide_v4(dividend, divisor)
# jy: -2
print(res)

