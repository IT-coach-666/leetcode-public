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
tag_jy = ""


"""
Implement pow(x, n), which calculates ``x`` raised to the power ``n`` (x^n).


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


Note:
-100.0 < x < 100.0
``n`` is a 32-bit signed integer, within the range [−2^31, 2^31−1]
"""


class Solution:
    """
解法1: 由于 x^n = x^(2 * n/2), 所以可以使用将 pow(x, n) 分解成 pow(x^2, n/2) 求解;
(注意 n 有可能是负数, 如果 n 小于 0, 则参与计算的 x 变为 1/x 即可)

JY: 注意, 该递归过程中不会出现相同的子问题, 故不会重复计算, 不可用缓存提升效率
    """
    def myPow_v1(self, x: float, n: int) -> float:
        # jy: 注意, 当 n 为负数时, 相当于求解 1/x 的 -n 次方;
        return self._pow_v1(x, n) if n >= 0 else self._pow_v1(1/x, -n)

    def _pow_v1(self, x: float, n: int) -> float:
        """
        计算 x^n , 此处 x 可以是任意数值, n 为非负整数;
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        # jy: 如果 n 的大于等于 2 的数值, 则进行如下操作:
        #     1) 如果 n 为偶数, 则 x^n 直接转换为 x^(2 * n//2), 即 (x^2)^(n//2);
        #        注意, 不是: x^2 * x^(n//2) , 该方式是等价于 x^(2 + n//2)
        elif n % 2 == 0:
            return self._pow_v1(x * x, n // 2)
        #     2) 如果 n 为奇数(且大于 2), 则 x^n 直接转换为 x^(2 * (n-1)//2 + 1),
        #        即 (x^2)^((n-1)//2) * x; 因为调用递归方法 _pow_v1 时要确保传入的
        #        第二个参数为非负整数;
        else:
            return self._pow_v1(x * x, (n-1) // 2) * x

    """
解法2: 思路同解法1, 只是将递归换成了循环;
    """
    def myPow_v2(self, x: float, n: int) -> float:
        return self._pow_v2(x, n) if n > 0 else self._pow_v2(1/x, -n)

    def _pow_v2(self, x: float, n: int) -> float:
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
                n -= 1
            x *= x
            n = n // 2
        return result


x = 2.00000
n = 10
# Output: 1024.00000
res = Solution().myPow_v1(x, n)
print(res)


x = 2.10000
n = 3
# Output: 9.26100
res = Solution().myPow_v2(x, n)
print(res)


x = 2.00000
n = -2
# Output: 0.25000
res = Solution().myPow_v1(x, n)
print(res)



