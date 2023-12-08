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
title_jy = "Target-Sum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an integer array ``nums`` and an integer ``target``. You want to
build an expression out of ``nums`` by adding one of the symbols '+' and '-'
before each integer in ``nums`` and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and
concatenate them to build the expression "+2-1". Return the number of different
expressions that you can build, which evaluates to ``target``.


Example 1:
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1


Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""


from typing import List
from functools import lru_cache


class Solution:
    """
解法1(超时): 直接深度优先搜索遍历, 遍历时记录深度, 当深度等于数组长度时, 判断当前累加
的值是否等于目标值, 如果相等则返回 1 (表示找到了一种组合), 否则返回 0;
    """
    def findTargetSumWays_v1(self, nums: List[int], target: int) -> int:
        return self._dfs_v1(nums, 0, 0, target)

    # jy: 参数中含有 list (unhashable 类型), 不能适用 lru_cache; 可以考虑是否可以将所有
    #     list 类型的参数转换为元组后使用(如果不可转换, 则使用不了);
    # @lru_cache(None)
    def _dfs_v1(self, nums, i, sum_so_far, target):
        # jy: 用 i 记录已经将多少个数值加上操作符("+" 或 "-"), 当 i 等于数组长度时表明所有
        #     数值都已经加上操作符; 此时如果 sum_so_far 为目标值, 则表明找到了一种添加运算
        #     符的方案, 返回 1;
        if i == len(nums):
            return 1 if sum_so_far == target else 0
        # jy: 递归求解在当前数值 nums[i] 前加上 "+" 和 "-" 时, 最终满足要求的方案各多少, 两
        #     者的方案数加和结果即为目标所求结果;
        return self._dfs_v1(nums, i+1, sum_so_far + nums[i], target) + \
               self._dfs_v1(nums, i+1, sum_so_far - nums[i], target)

    """
解法2: 在解法 1 的基础上引入缓存, 避免重复计算; 定义缓存字典 memo, 用 memo[(i, sum_so_far)]
记录满足从第 0 位到第 i 位之和为 sum_so_far 的组合个数; 如果后续递归过程中遇到的 (i, sum_so_far)
已经在 memo 中存在, 则直接返回其结果即可(避免重复运算);
    """
    def findTargetSumWays_v2(self, nums: List[int], target: int) -> int:
        memo = {}
        return self._dfs(nums, 0, 0, target, memo)

    def _dfs(self, nums, i, sum_so_far, target, memo):
        # jy: 如果缓存中已有记录, 则直接返回;
        if (i, sum_so_far) in memo:
            return memo[(i, sum_so_far)]

        # jy: 递归操作后, 当前 i 如果已经等于 nums 列表的长度了, 表明上一个 i 已经是
        #    列表中的最后一个元素了, 即表明以经完成为最后一个元素进行可选的符号操作;
        #    此时判断当前的 sum_so_far 与目标值是否相等, 如果相等, 则返回 1, 表示符合
        #    要求的组合数加 1;
        if i == len(nums):
            return 1 if sum_so_far == target else 0

        memo[(i, sum_so_far)] = self._dfs(nums, i+1, sum_so_far + nums[i], target, memo) + \
                                self._dfs(nums, i+1, sum_so_far - nums[i], target, memo)
        return memo[(i, sum_so_far)]

    """
JY: 对解法 1 进行优化(减少不必要的变量)
    """
    def findTargetSumWays_jy(self, nums: List[int], target: int) -> int:
        nums = tuple(nums)
        return self._dfs_jy(0, nums, target)

    # jy: 注意, 由于 list, set, dict 是不可哈希的类型(unhashable type), 故使用 lru_cache 对
    #     相关函数/方法进行装饰时, 不可哈希的类型不能当做参数传入函数/方法, 可根据数据特点判
    #     断是否可以将不可哈希类型转换为可哈希类型(如 int, float, str, tuple); lru_cache 构
    #     建的缓存是基于哈希存储的;
    @lru_cache(None)
    def _dfs_jy(self, i, nums, target):
        # jy: 用 i 记录已经将多少个数值加上操作符("+" 或 "-"), 当 i 等于数组长度时表明所有
        #     数值都已经加上操作符; 此时如果当前 target 为 0, 则表明找到了一种添加运算符的
        #     方案, 返回 1;
        if i == len(nums):
            return 1 if target == 0 else 0
        return self._dfs_jy(i + 1, nums, target - nums[i]) + self._dfs_jy(i + 1, nums, target + nums[i])

    """
JY: 对解法 2 进行优化(减少不必要的变量)
    """
    def findTargetSumWays_jy2(self, nums: List[int], target: int) -> int:
        memo_ = {}
        return self._dfs_jy2(0, nums, target, memo_)

    def _dfs_jy2(self, i, nums, target, memo_):
        if i == len(nums):
            return 1 if target == 0 else 0
        # jy-version-1-Begin-------------------------------------------------------
        if (i, target) in memo_:
            return memo_[(i, target)]

        memo_[(i, target)] = self._dfs_jy2(i + 1, nums, target - nums[i], memo_) + \
                             self._dfs_jy2(i + 1, nums, target + nums[i], memo_)
        return memo_[(i, target)]
        # jy-version-1-End---------------------------------------------------------
        # jy-version-2-Begin-------------------------------------------------------
        """
        if (i + 1, target - nums[i]) in memo_:
            res_add = memo_[(i + 1, target - nums[i])]
        else:
            res_add = self._dfs_jy2(i + 1, nums, target - nums[i], memo_)

        if (i + 1, target + nums[i]) in memo_:
            res_minus = memo_[(i + 1, target + nums[i])]
        else:
            res_minus = self._dfs_jy2(i + 1, nums, target + nums[i], memo_)

        memo_[(i, target)] = res_add + res_minus
        return res_add + res_minus
        """
        # jy-version-2-End---------------------------------------------------------

    """
解法3: 动态规划; 记数组中所有元素之和为 total, 那么数组中所有数字组合的和的范围为
[-total, total], 最多共 (2 * total + 1) 种可能(当数组中值均为 1 时, 有最多种组合情况);

记 dp[i][j] 为前 i 个数的组合结果(即为前 i 个数赋予 "+" 或 "-" 后的运算结果)等于 j 的组合数;
则有(其中 nums[i-1] 即表示第 i 个数):
dp[i][j] = dp[i-1][j + nums[i-1]] + dp[i-1][j - nums[i-1]]

目标即求 dp[len(nums)][target]; 因为 dp 数组下标不能为负数, 所以将 [-total, total] 中的每个数字向右
偏移 total 个单位, 得到 [0, 2 * total] 即 j 的范围, 相应地, 目标所求转换为 dp[len(nums)][total + target]

初始化 dp[0][0 + total] = 1, 表示 0 个数字相加为 0 的只有一种解法, 然后遍历
每个数字, 对每个数字遍历 [0, 2 * total], 计算 dp[i][j];
    """
    def findTargetSumWays_v3(self, nums: List[int], target: int) -> int:
        # jy: 题目中表明 nums 均为非负数, 故直接加和得到的 total 所对应的数值范围 [-total, total]
        #     即为可能的数值范围;
        total = sum(nums)
        # jy: 如果目标值 target 不在 [-total, total] 范围内, 表明没有满足条件的目标值, 返回 0;
        if target < -total or target > total:
            return 0

        # jy: 初始化 dp, i 的范围为 0 到 len(nums), 共有 len(nums) + 1 行; j 的范围为 0 到 2 * total,
        #     共有 2 * total + 1 列;
        dp = [[0] * (2 * total + 1) for _ in range(len(nums) + 1)]
        # jy: 初始化 dp[0][0 + total] = 1, 表示 0 个数字相加为 0 的只有一种解法(由于 j 向右移了 total
        #     个单位, 原先的 0 即为此时的 total)
        dp[0][0 + total] = 1

        for i in range(1, len(nums) + 1):
            for j in range(2 * total + 1):
                # jy: dp[i][j] 表示前 i 个数的组合结果为 j 的组合数, 有 (nums[i-1] 即为第 i 个数):
                #     dp[i][j] = dp[i-1][j + nums[i-1]] + dp[i-1][j - nums[i-1]]
                #     以下的 i 和 j 都是大于 0 的数值, 而 dp[i][j] 中的 j 的有效范围是 0 到 2 * total + 1;
                if j + nums[i-1] < 2 * total + 1:
                    # jy: 如果前 i-1 个数的组合结果为 j + nums[i-1] 的组合数有 dp[i-1][j + nums[i-1]] 种,
                    #     则可以在前 i-1 个数的基础上减去当前第 i 个数 nums[i-1], 则可使得前 i 个数的组合
                    #     结果为 j (前提是需要确保 dp[i-1][j + nums[i-1] 存在, 即 j + nums[i-1] 有效);
                    dp[i][j] += dp[i-1][j + nums[i-1]]
                if j - nums[i-1] >= 0:
                    # jy: 如果前 i-1 个数的组合结果为 j - nums[i-1] 的组合数有 dp[i-1][j - nums[i-1]] 种,
                    #     则可以在前 i-1 个数的基础上加上当前第 i 个数 nums[i-1], 则可使得前 i 个数的组合
                    #     结果为 j (前提是需要确保 dp[i-1][j - nums[i-1] 存在, 即 j - nums[i-1] 有效);
                    dp[i][j] += dp[i-1][j - nums[i-1]]

        return dp[len(nums)][total + target]

    """
解法 4: 动态规划(转换为 01 背包问题后进行动态规划, 性能极佳);
01 背包问题是选或者不选, 但本题是必须选选 "+" 或 "-"; 先将本问题转换为 01 背包问题;

假设所有添加 "+" 的元素和为 x, 所有添加 "-" 的元素和的绝对值是 y; 则有:
target = x - y
而已知 x 与 y 的和是数组元素的总和 sum_:
sum_ = x + y
因此, 有:
x = (target + sum_) / 2  (或: y = (sum_ - target) / 2)
即将目标转换为: 求 nums 数组中和为 x 的所有目标组合; 于是就转化成了求容量为 x 的 01 背包
问题, 即要装满容量为 x 的背包, 有几种方案;

特例判断:
1) 如果 target 大于 sum_ 或 target 小于 -sum_, 不可能实现, 返回 0
2) 如果 x 不是整数(即 target + sum_ 不是偶数), 不可能实现, 返回 0

定义 dp[j] 表示 nums 数组中和为 j 的所有目标组合数; 即将以上问题转换为求解 dp[x]
因为和为 0 的目标组合数有且只有一种(即不存放任何 nums 中的数值), 所以 dp[0] = 1
状态转移: dp[j] = dp[j] + dp[j - num]，
当前填满容量为 j 的包的方法数 = 之前填满容量为 j 的包的方法数 + 之前填满容量为 j - num 的包的方法数
也就是当前数 num 的加入, 可以把之前和为 j - num 的方法数加入进来; 返回 dp[-1], 也就是 dp[x]

参考:
https://leetcode-cn.com/problems/target-sum/solution/494-mu-biao-he-dong-tai-gui-hua-zhi-01be-78ll/
https://leetcode-cn.com/problems/target-sum/solution/gong-shui-san-xie-yi-ti-si-jie-dfs-ji-yi-et5b/
    """
    def findTargetSumWays_v4(self, nums: List[int], target: int) -> int:
        sum_ = sum(nums)
        # jy: 特例判断(target 小于 -sum_ 的情况必须提前考虑, 否则后续得到的 x 可能是负数, 导致 dp 可
        #     能为空列表, 出错):
        #     1) 如果 target 大于 sum_ 或 target 小于 -sum_, 不可能实现, 返回 0
        #     2) 如果 x 不是整数(即 target + sum_ 不是偶数), 不可能实现, 返回 0
        if target > sum_ or target < -sum_ or (target + sum_) % 2:
            return 0

        # x = (target + sum_) // 2    # jy: 此处的 x 即代表添加 "+" 符号的数值之和;
        x = (sum_ - target) // 2      # jy: 此处的 x 即为以上题解分析中的 y, 即添加 "-" 符号的数值之和;

        # jy: 定义 dp[j] 表示 nums 数组中和为 j 的所有目标组合数; 即将以上问题转换为求解 dp[x]
        #     因为和为 0 的目标组合数有且只有一种(即不存放任何 nums 中的数值), 所以 dp[0] = 1
        dp = [0] * (x + 1)
        dp[0] = 1
        # jy: 遍历 nums 中的所有数值;
        for num in nums:
            # jy: 注意, j 必须是降序遍历, 即 j 由大到小, 因为 nums 中同的每一个数值只能使用一次, 所以
            #     当前 dp[j] 的计算是依赖于上一轮 for 循环的 num 数值计算得到的 dp[j - num], 如果 j 从
            #     小到大遍历, 则计算 dp[j] 时, 由于 j - num 比 j 小, 当前轮中的 dp[j - num] 可能已经被
            #     提前更新, 则计算 dp[j] 时加上的 dp[j - num] 不一定还是上一轮 for 循环对应的 num 数值
            #     的计算结果, 导致出错; 这是与 518_Coin-Change-2.py 中解法 1 的主要区别;
            for j in range(x, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[x]


nums = [1, 1, 1, 1, 1]
target = 3
# Output: 5
res = Solution().findTargetSumWays_v1(nums, target)
print(res)


res = Solution().findTargetSumWays_v2(nums, target)
print(res)


res = Solution().findTargetSumWays_v3(nums, target)
print(res)


nums = [1]
target = 1
# Output: 1
res = Solution().findTargetSumWays_v1(nums, target)
print(res)

nums = [22, 36, 7, 44, 38, 32, 16, 32, 1, 16, 25, 45, 49, 45, 27, 9, 41, 31, 10, 15]
target = 1
res = Solution().findTargetSumWays_jy2(nums, target)
print(res)


res = Solution().findTargetSumWays_v4(nums, target)
print(res)


nums = [100]
target = -200
res = Solution().findTargetSumWays_v4(nums, target)
print(res)


