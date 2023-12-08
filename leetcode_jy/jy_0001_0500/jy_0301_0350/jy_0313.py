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
title_jy = "Super-Ugly-Number(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A super ugly number is a positive integer whose prime factors are in the array ``primes``.
Given an integer ``n`` and an array of integers ``primes``, return the nth super ugly number.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.


Example 1:
Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly
             numbers given primes = [2,7,13,19].

Example 2:
Input: n = 1, primes = [2,3,5]
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are in the array
             primes = [2,3,5].


Constraints:
1 <= n <= 106
1 <= primes.length <= 100
2 <= primes[i] <= 1000
primes[i] is guaranteed to be a prime number.
All the values of primes are unique and sorted in ascending order.
"""


import heapq
from typing import List


class Solution:
    """
解法1(超时): 264_Ugly-Number-II.py 解法 1 的一般化版本;

最小堆: 没有很好地利用给定的 primes 是递增的这一条件, 很暴力地利用最小堆找第 n 个
    """
    def nthSuperUglyNumber_v1(self, n: int, primes: List[int]) -> int:
        ugly_numbers = [1]
        heapq.heapify(ugly_numbers)
        ugly = 1
        visited = set()
        # jy: 循环 n 次后, 会从最小堆中出 n 个元素, 每次出堆的元素均为当前堆中最小, 第 n 个出堆
        #     即为第 n 个 ugly number;
        for _ in range(n):
            # jy: 当前出堆元素即为当前轮次中的最小 ugly number, 用该最小 ugly number 乘以 primes
            #     中的元素即可求得后一批次中的 ugly number (后一批次可能都比之前批次的都大, 如果
            #     这样则下一批次中出的还是之前批次的小的 ugly number, 确保每次出堆都是当前以及后
            #     续要加入堆中的 ugly number 的最小值); 加入过程中先判断该值之前是否已经加入过;
            ugly = heapq.heappop(ugly_numbers)
            for i in primes:
                next_ugly = ugly * i
                if next_ugly not in visited:
                    visited.add(next_ugly)
                    heapq.heappush(ugly_numbers, next_ugly)
                    # jy: 注意此处不能随意 break, 因为最小堆中的堆顶元素值乘以 primes 中的第一个
                    #     数值并不一定比 primes 中的后续数值小;
                    # break
        return ugly

    """
解法2(超时): 264_Ugly-Number-II.py 解法 2 的一般化版本;

动态规划: 记录前面的丑数, 根据每个质因数当前对应的丑数进行乘积大小对比, 将最小的那个作为新的丑数, 并
更新对应的丑数; 比如 [2, 3, 5] 中, 一开始所有质因数都对应丑数 1, 最小的那个是 1*2 (在 1*2, 1*3 和 1*5
中最小), 所以我们将 2 加入丑数，并更新质因数 2 对应的丑数为 2 (不再是 1), 下一次我们对比的就是 2*2, 1*3
和 1*5 了, 以此类推, 直到我们找到了 n 个丑数

    """
    def nthSuperUglyNumber_v2(self, n: int, primes: List[int]) -> int:
        # version-1-Begin --------------------------------------------------------
        '''
        dp = [0] * n
        dp[0] = 1
        uglies = [0] * len(primes)

        for i in range(1, n):
            ugly = min(map(lambda x: dp[uglies[x]] * primes[x], range(len(primes))))
            dp[i] = ugly

            for j in range(len(primes)):
                if ugly == dp[uglies[j]] * primes[j]:
                    uglies[j] += 1
        '''
        # version-1-End ----------------------------------------------------------
        # version-2-Begin --------------------------------------------------------
        # jy: dp[i] 代表第 i+1 个丑数, 所有丑数的初始值均为无穷大 float("inf"); 第 1 个丑数值为 1;
        dp = [float("inf")] * n
        dp[0] = 1
        # jy: indexes 代表每个质因子现在应该跟哪个丑数相乘
        indexes = [0] * len(primes)

        for i in range(1, n):
            # 哪个质因子相乘的丑数将会变化
            changeIndex = 0
            for j in range(len(primes)):
                # 如果当前质因子乘它的丑数小于当前的丑数，更新当前丑数并更新变化坐标
                if primes[j] * dp[indexes[j]] < dp[i]:
                    changeIndex = j
                    dp[i] = primes[j] * dp[indexes[j]]
                # 如果相等直接变化，这样可以去重复
                elif primes[j] * dp[indexes[j]] == dp[i]:
                    indexes[j] += 1
            # 变化的坐标+1
            indexes[changeIndex] += 1
        # version-2-End -----------------------------------------------------------

        return dp[-1]

    """
解法3: 堆 + 动态规划
        """
    def nthSuperUglyNumber_v3(self, n: int, primes: List[int]) -> int:
        # jy: dp[i] 代表第 i+1 个丑数
        dp = [1] * n
        # jy: (丑数, 刚刚乘过的丑数的坐标, 质因数)
        pq = [(p, 0, i) for i, p in enumerate(primes)]

        for i in range(1, n):
            # jy: 目前最新的最小的丑数
            dp[i] = pq[0][0]
            # jy: 所有等于这个值的要全部出队列, 并根据该乘的丑数重新加入队列
            while pq and pq[0][0] == dp[i]:
                _, idx, p = heapq.heappop(pq)
                heapq.heappush(pq, (dp[idx + 1] * primes[p], idx + 1, p))
        return dp[-1]

    """
解法4: 对解法 1 的优化, 遍历 primes 时, 如果 ugly 是当前质数的整数倍, 则跳出质数循环;

记所有的质数为 p0, p1, p2 ..., 在不优化时生成的序列为:
1) p0 * p0, p0 * p1, p0 * p2, ...
2) p1 * p0, p1 * p1, p1 * p2, ...
3) p2 * p0, p2 * p1, p2 * p2, ...
观察到对于每个序列, 在 pi * pi 之后的数字都可以在后续的序列中找到, 所以通过该方法优化

JY: 该解法比解法 3 性能更优, 但内存消耗稍微大些
    """
    def nthSuperUglyNumber_v4(self, n: int, primes: List[int]) -> int:
        ugly_numbers = [1]
        heapq.heapify(ugly_numbers)
        ugly = 1
        visited = set()
        for _ in range(n):
            ugly = heapq.heappop(ugly_numbers)
            for i in primes:
                next_ugly = ugly * i
                if next_ugly not in visited:
                    visited.add(next_ugly)
                    heapq.heappush(ugly_numbers, next_ugly)
                # jy: 如果 ugly 是当前质数的整数倍, 则跳出质数循环
                if ugly % i == 0:
                    break

        return ugly


n = 12
primes = [2, 7, 13, 19]
# Output: 32
res = Solution().nthSuperUglyNumber_v1(n, primes)
print(res)

n = 1
primes = [2, 3, 5]
# Output: 1
res = Solution().nthSuperUglyNumber_v2(n, primes)
print(res)


