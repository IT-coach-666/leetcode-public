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
title_jy = "Pow_x_n(number)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 循环/迭代"


"""
Implement pow(x, n), which calculates `x` raised to the power `n` (x^n).


Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25


Constraints:
-100.0 < x < 100.0
`n` is a 32-bit signed integer, within the range [−2^31, 2^31−1]
Either `x` is not zero or `n > 0`.
-10^4 <= x^n <= 10^4
"""


class Solution:
    """
解法 1: 递归 + 二分法

由于 x^n = x^(2 * n/2), 因此可将 pow(x, n) 分解为 pow(x^2, n/2), 从而递归求解
(注意: n 有可能是负数, 如果 n < 0, 则参与计算的 x 变为 1/x, n 变为 -n 即可)

注意: 该递归过程中不会出现相同的子问题, 故不会重复计算, 不可用缓存提升效率
    """
    def myPow_v1(self, x: float, n: int) -> float:
        # jy: 当 n 为负数时, 相当于求解 1/x 的 -n 次方
        return self._pow_v1(x, n) if n >= 0 else self._pow_v1(1/x, -n)

    def _pow_v1(self, x: float, n: int) -> float:
        """
        递归实现 x^n 的计算

        x: 任意数值
        n: 非负整数 (可以为 0)
        """
        # jy: 任何数值的 0 次方均为 0
        if n == 0:
            return 1
        # jy: 数值的 1 次方即为数值本身
        elif n == 1:
            return x
        # jy: 以下对应 n >= 2 的代码逻辑:
        #     1) 如果 n 为偶数, 则 x^n 可转换为 x^(2 * n // 2), 即 (x^2)^(n//2)
        #        注意: 不是: x^2 * x^(n//2) , 该方式是等价于 x^(2 + n//2)
        #     2) 如果 n 为奇数, 则 x^n 直接转换为 x^(2 * (n-1)//2 + 1), 即
        #        (x^2)^((n-1)//2) * x
        elif n % 2 == 0:
            return self._pow_v1(x * x, n // 2)
        else:
            return self._pow_v1(x * x, (n-1) // 2) * x


    """
解法 2: 将解法 1 中的思路用循环/迭代实现
    """
    def myPow_v2(self, x: float, n: int) -> float:
        return self._pow_v2(x, n) if n > 0 else self._pow_v2(1/x, -n)

    def _pow_v2(self, x: float, n: int) -> float:
        """
        循环实现 x^n 的计算

        x: 任意数值
        n: 非负整数 (可以为 0)
        """
        result = 1
        while n > 0:
            # jy: 如果 n 为奇数
            if n & 1:
            #if n % 2 == 1:
                result *= x
                # jy: 此处 n -= 1 可以省略, 因为如果为奇数, 则后续在
                #     n = n//2 时, 不管有没有提前减去 1, 结果都一样
                n -= 1
            x *= x
            # jy: n 整除 2 (两种写法)
            n = n // 2
            #n >>= 1
        return result


    """
解法 3: 改写解法 2
    """
    def myPow_v3(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0

        if n < 0: 
            x, n = 1/x, -n

        result = 1
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result


    """
解法 4: 改写解法 1
    """
    def myPow_v4(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow_v4(1/x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
     
        if n % 2:
            return x * self.myPow_v4(x*x, n//2)
        else:
            return self.myPow_v4(x*x, n//2)



x = 2.00000
n = 10
# jy: 1024.00000
res = Solution().myPow_v1(x, n)
print(res)


x = 2.10000
n = 3
# jy: 9.26100
res = Solution().myPow_v2(x, n)
print(res)


x = 2.00000
n = -2
# jy: 0.25000
res = Solution().myPow_v3(x, n)
print(res)


x = 2.00000
n = -2
# jy: 0.25000
res = Solution().myPow_v4(x, n)
print(res)


