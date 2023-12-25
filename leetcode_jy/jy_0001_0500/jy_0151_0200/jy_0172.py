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
title_jy = "Factorial-Trailing-Zeroes(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer `n`, return the number of trailing zeroes in `n!`.

Note that: n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

 

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0
 

Constraints:
0 <= n <= 10^4
 

Follow up: Could you write a solution that works in logarithmic time complexity?
"""


class Solution:
    """
解法 1: 要在末位产生 0, 则必然是 5×2, 即使是原数中包含的 0 也可以分解, 因此将题目简化为寻找阶乘中 5 的个数，即 n // 5, 但这只找到了 n 中是 5 的倍数的所有数, 例如在 25! 中找到了 5 个是 5 的倍数的数分别为 5、10、15、20、25, 但这之中的 25 依然可以分解为 5 的倍数 (含两个 5), 因此 n//5 其实少计入了一部分情况; 要对这部分情况进行统计，我们可以对 n 取 25 的商, 即 n//25, 这样就找到了包含有 2 个 5 的数 (且因为是对 5×5 取商, 没有重复计入), 依此类推, 可以循环对 n 取 5、25、125... 的商, 将所有的情况都包括, 最终将所有的商汇总即 0 的个数

n // 25 == n // 5 // 5, 因此可以对 n 循环取 5 的商, 其效果是一样的

    """
    def trailingZeroes_v1(self, n: int) -> int:
        p = 0
        while n >= 5:
            n = n // 5
            p += n
        return p
    
    
n = 3
res = Solution().trailingZeroes_v1(n)
# jy: 0
print(res)


n = 5
res = Solution().trailingZeroes_v1(n)
# jy: 1
print(res)


n = 0
res = Solution().trailingZeroes_v1(n)
# jy: 0
print(res)
    