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
title_jy = "Ugly-Number-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer ``n``, return the ``nth`` ugly number.


Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.


Constraints:
1 <= n <= 1690
"""


import heapq


class Solution:
    """
解法1: 每个 ugly 数字都可由之前的某个较小的 ugly 数字乘上 2 或 3 或 5 后得到, 维护一个
最小堆用于保存遇到的 ugly 数字, 每次弹出堆顶的数字, 将数字乘以 2、3、5 后再放入堆, 同时
维护一个 Set 用于保存已经出现过的数字
    """
    def nthUglyNumber_v1(self, n: int) -> int:
        ugly_numbers = [1]
        heapq.heapify(ugly_numbers)
        # jy: 初始 ugly number 为 1, 其加不加入到 visited 集合中都可以(后续不会再遍历到值
        #     为 1 的 ugly number, 因此不加入 visited 中也可以)
        ugly = 1
        visited = set()
        # jy: 每循环一次都会从最小堆的堆顶中出一个最小的 ugly number (堆中始终保持
        #     有 ugly number 加入), 最后一次循环出堆的 ugly number 即为第 n 个 ugly
        #     number;
        for _ in range(n):
            ugly = heapq.heappop(ugly_numbers)
            # jy: 将当前的 ugly number 不断乘以 2、3、5, 当得到的 ugly number 之前没
            #     有被访问过时, 则将其加入到最小堆中, 并添加到 visited 中, 表示该数值
            #     已被访问, 后续再次出现则不再加入最小堆中;
            for i in [2, 3, 5]:
                next_ugly = ugly * i
                if next_ugly not in visited:
                    visited.add(next_ugly)
                    heapq.heappush(ugly_numbers, next_ugly)
        return ugly

    """
解法2: 记 dp[i] 表示第 i 个 ugly 数字(从 0 开始计数), 因为 ugly 数字由当前的 ugly 数
字集合乘以 2、3、5 得到, 所以记 ugly_2、ugly_3、ugly_5 表示当前可以用来乘以 2、3、5 的
ugly 数字的位置, 每次比较 dp[ugly_2] * 2, dp[ugly_3] * 3, dp[ugly_5] * 5 取最小值, 并
将相应指针移动一位
    """
    def nthUglyNumber_v2(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        ugly_2 = ugly_3 = ugly_5 = 0

        for i in range(1, n):
            ugly = min(dp[ugly_2] * 2, dp[ugly_3] * 3, dp[ugly_5] * 5)
            dp[i] = ugly

            if ugly == dp[ugly_2] * 2:
                ugly_2 += 1
            if ugly == dp[ugly_3] * 3:
                ugly_3 += 1
            if ugly == dp[ugly_5] * 5:
                ugly_5 += 1

        return dp[-1]


n = 10
# Output: 12, [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
res = Solution().nthUglyNumber_v1(n)
print(res)


n = 1
# Output: 1
res = Solution().nthUglyNumber_v2(n)
print(res)


