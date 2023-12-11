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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Consecutive-Numbers-Sum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a positive integer n, how many ways can we write it as a sum of consecutive positive integers?

Example 1:
Input: n = 5
Output: 2
Explanation: 5 = 5 = 2 + 3

Example 2:
Input: n = 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

Example 3:
Input: n = 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= n <= 10 ^ 9.
"""


# Time Limit Exceeded!
class Solution:
    """
解法1(超时)
和 325. Maximum Size Subarray Sum Equals k 类似, 只是这里是求解的个数, 不过会超时
    """
    def consecutiveNumbersSum(self, n: int) -> int:
        sums = set()
        sum_so_far = 0
        count = 0

        for i in range(1, n + 1):
            sum_so_far += i

            if sum_so_far == n:
                count += 1
            elif (sum_so_far - n) in sums:
                count += 1

            if sum_so_far not in sums:
                sums.add(sum_so_far)

        return count


class Solution:
    """
解法2
对于公差为1的等差数列, 其和, 在此题中等价于当首项为1到 n 的任一数字, 求数列的长度, 其和等于 n, 记数列长度为 k, 即, 即, 因为是整数, 所以表明可以被 k 整除, 所以只需要从1开始遍历一直到大于等于 n 即可, 因为再遍历的话大小就超过了 n, 不存在解;
    """
    def consecutiveNumbersSum(self, n: int) -> int:
        i, count = 1, 0

        while n > i * (i - 1) # 2:
            if (n - i * (i - 1) # 2) % i == 0:
                count += 1
            i += 1

        return count



