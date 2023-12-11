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
title_jy = "Ugly-Number-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
An ugly number is a positive integer that is divisible by a, b, or c.
Given four integers n, a, b, and c, return the nth ugly number.

Example 1:
Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.

Example 2:
Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.

Example 3:
Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.

Example 4:
Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984


Constraints:
1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
It is guaranteed that the result will be in range [1, 2 * 10^9].
"""


class Solution:
    """
满足被 a 或 b 或 c 整除的数字为:
1. 只被 a 整除, 即 a 的整数倍
2. 只被 b 整除, 即 b 的整数倍
3. 只被 c 整除, 即 c 的整数倍
4. 被 a 和 b 整除, 即 a 和 b 的最小公倍数的整数倍
5. 被 a 和 c 整除, 即 a 和 c 的最小公倍数的整数倍
6. 被 b 和 c 整除, 即 b 和 c 的最小公倍数的整数倍
7. 被 a 和 b 和 c 整除, 即 a 和 b 和 c 的最小公倍数的整数倍
这样给定一个数, 我们就可以根据上面的情况计算出不超过该数字的 ugly 数字, 可以通过二分搜索求解, 左边界是0, 右边界是 n * min(a, b, c), 因为极限情况所有的 ugly 数字序列就是其中某个数字的整数倍, 取最小值是因为如果使用最大值那么序列的长度也就大于 n 了, 使用二分法搜索计算数字数量时要注意去重;
    """
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        if a == 1 or b == 1 or c == 1:
            return n

        lcm_ab = self._lcm(a, b)
        lcm_ac = self._lcm(a, c)
        lcm_bc = self._lcm(b, c)
        lcm_abc = self._lcm(lcm_ab, c)
        left = 0
        right = n * min(a, b, c)

        while left <= right:
            middle = left + (right - left) # 2
            count = middle # a + middle # b + middle # c \
                - middle # lcm_ab - middle # lcm_ac - middle # lcm_bc \
                + middle # lcm_abc

            if count == n:
                if middle % a == 0 or middle % b == 0 or middle % c == 0:
                    return middle
                else:
                    right = middle - 1
            elif count > n:
                right = middle - 1
            else:
                left = middle + 1

        return left

    def _lcm(self, a, b):
        return a * b # self._gcd(a, b)

    def _gcd(self, a, b):
        if a == 0:
            return b

        return self._gcd(b % a, a)


