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
title_jy = "Combination-Sum-IV(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of distinct integers ``nums`` and a target integer ``target``, return the number of
possible combinations that add up to target. The answer is guaranteed to fit in a 32-bit integer.


Example 1:
Input: nums = [1, 2, 3], target = 4
Output: 7
Explanation:
The possible combination ways are (Note that different sequences are counted as different combinations.):
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Example 2:
Input: nums = [9], target = 3
Output: 0


Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000


Follow up:
What if negative numbers are allowed in the given array? How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""


import functools
from typing import List


class Solution:
    """
解法1: 本质和 039_Combination-Sum.py 一样, 由求解具体组合变为求组合的个数, 另外由于本
题的限制范围变大了, 所以递归求解时需要增加缓存才能不超时;
    """
    def combinationSum4_v1(self, nums: List[int], target: int) -> int:
        # jy: 传入递归方法中的第一个参数可以是 list 或 tuple, 但为了使用 lru_cache, 此次传入
        #     为 tuple 类型;
        return self._dfs(tuple(nums), target)

    @functools.lru_cache(None)
    def _dfs(self, candidates, target):
        """
        从候选数值列表 candidates 中找出数值相加后结果为 target 的所有组合;
        """
        # jy: 如果 target 为 0, 表明找到一个目标组合, 返回 1;
        if target == 0:
            return 1
        count = 0
        # jy: 遍历元组中的候选数值, 如果遍历的数值大于目标值, 直接跳过遍历下一个, 否则在
        #     目标值的基础上减去当前值, 并递归求解;
        for n in candidates:
            if n > target:
                continue
            count += self._dfs(candidates, target - n)

        return count

    """
解法2: 只求个数不求具体的解适合用动态规划求解, 在 039_Combination-Sum.py 已经观察到,
该题等价于: 从 nums 中挑选一个数 k, 然后继续在 nums 中挑选几个数, 使其和为 target - k;

记 dp[i] 表示 nums 中和为 i 的解的个数, 这里同样事先将 nums 排序用于提前结束循环;
    """
    def combinationSum4_v2(self, nums: List[int], target: int) -> int:
        # jy: dp[i] 表示 nums 中和为 i 的解的个数, 并初始化 dp 的长度为 target + 1,
        #    且 dp[0] 为 1(后续计算 dp[i] 需要用到), 其余值均为 0;
        dp = [0] * (target + 1)
        dp[0] = 1
        # jy: 对 nums 进行排序;
        sorted_nums = sorted(nums)
        # jy: i 从 1 到 target 不断遍历, 陆续求出 dp[i], 最终返回 dp[target] 即可;
        for i in range(1, len(dp)):
            # jy: 遍历已排序的数组中的值;
            for n in sorted_nums:
                # jy: 如果 i-n 等于 0, 则表明遍历数组时发现数组中的当前值 n 正好为目标组合中的
                #    一种, dp[i] 直接加 1 (即加上 dp[0], 即 dp[i-n]);
                #    如果 i-n 大于 0, 则同样满足 dp[i] = dp[i] + dp[i-n], 因为 dp[i] 的最开始
                #    的值为 0, 如果循环过程中发现 i-n 大于 0, 而 dp[i] 表示的是 nums 中和为 i 的
                #    解的个数, dp[i-n] 则表示 nums 中和为 i-n 的个数, 要求解 dp[i] 时, 则是在其
                #    最初始的值 0 的基础上, 不断加上 dp[i-n] 的值(即表示先从数组中挑出一个数 n 后,
                #    再继续从数组中挑几个数, 使其和为 i-n 的个数), 即不断循环有序数组中的值 n, 并
                #    获取原先计算得到的数组中和为 i-n 的组合的个数(即 dp[i-n]), 不断循环累加, 最终
                #    即可求得数组中和为 i 的所有组合的个数(由于 dp[i-n] 肯定在 dp[i] 之前就求得,
                #    且如何数组中没有和为 i-n 的组合, 则其还是初始值 0, 累加也不影响最终结果)
                if i-n >= 0:
                    dp[i] += dp[i-n]
                else:
                    break

        return dp[target]


nums = [1, 2, 3]
target = 4
# Output: 7
res = Solution().combinationSum4_v1(nums, target)
print(res)

nums = [9]
target = 3
# Output: 0
res = Solution().combinationSum4_v2(nums, target)
print(res)


