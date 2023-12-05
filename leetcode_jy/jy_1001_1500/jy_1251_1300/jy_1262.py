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
title_jy = "Greatest-Sum-Divisible-by-Three(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array ``nums`` of integers, we need to find the maximum possible sum of elements
of the array such that it is divisible by three.


Example 1:
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

Example 2:
Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.

Example 3:
Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:
1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
"""


from typing import List
import sys


class Solution:
    """
解法1: 将所有数相加记录总和为 all_sum,
1) 如果 all_sum 能被 3 整除即可直接返回;
2) 如果 all_sum 除以 3 余 1, 可以删除一个除以 3 余 1 的最小数, 或删除两个除以 3 余 2 的最小数;
3) 如果 all_sum 除以 3 余 2, 可以删除一个除以 3 余 2 的最小数, 或删除两个除以 3 余 1 的最小数;

遍历数组, 将所有数基于除以 3 得到的余数分类, 随后:
1) 将整除 3 的所有数相加
2) 对剩下两组(除以 3 余 1 或 2 的数值)进行排序
3) 基于 all_sum 除以 3 的余数列举可能的两种删除方法, 比较删除方法结果的大小即可;
4) 如果余 1 和余 2 的数数量不足, 则无法做到, 返回 0;

    """
    def maxSumDivThree_v1(self, nums: List[int]) -> int:

        all_sum = sum(nums)
        # jy: r 记录了总和除以 3 的余数;
        r = all_sum % 3
        # jy: 如果余数为 0, 则直接返回即可;
        if r == 0:
            return all_sum

        # jy: 分别统计数组中除以 3 余数为 1 和 2 的所有数值, 并对相应数值进行排序;
        ones = list()
        twos = list()
        for num in nums:
            if num % 3 == 1:
                ones.append(num)
            elif num % 3 == 2:
                twos.append(num)
        ones.sort()
        twos.sort()

        # jy: subtract 中记录可以减去的最小数值, 使得减去该值后 all_sum 就可以被 3 整除;
        subtract = list()
        # jy: 如果 all_sum 除以 3 余 1, 表明可以删除:
        #     1) 所有除以 3 余 1 的数中的最小值, 或:
        #     2) 所有除以 3 余 2 的数中的前两小(前提是这有两个这样的值存在);
        if r == 1:
            if ones:
                subtract.append(ones[0])
            if len(twos) >= 2:
                subtract.append(sum(twos[:2]))

            if not subtract:
                return 0
            else:
                return all_sum - min(subtract)
        # jy: 如果 all_sum 除以 3 余 2, 表明可以删除:
        #     1) 所有除以 3 余 2 的数中的最小值, 或:
        #     2) 所有除以 3 余 1 的数中的前两小(前提是这有两个这样的值存在);
        else:
            if twos:
                subtract.append(twos[0])
            if len(ones) >= 2:
                subtract.append(sum(ones[:2]))

            if not subtract:
                return 0
            else:
                return all_sum - min(subtract)

    def maxSumDivThree_v2(self, nums: List[int]) -> int:
        # jy: remainder[i] (其中 i 取值为 0, 1, 2) 记录除以 3 余数为 i 的最大值,
        #     初始化均为 0;
        remainder = [0] * 3
        for num in nums:
            # version-1-Begin--------------------------------------------------------
            # jy: 注意, 以下不能将其改造为 for 循环: for i in [0, 1, 2]; 因为必须得等
            #     一轮 remainder 更新完后(一轮最多更新 3 个数值)才能一轮更新 a, b, c;
            #     即不能计算得到 a 之后就更新 remainder[a % 3];
            a = remainder[0] + num
            b = remainder[1] + num
            c = remainder[2] + num
            remainder[a % 3] = max(remainder[a % 3], a)
            remainder[b % 3] = max(remainder[b % 3], b)
            remainder[c % 3] = max(remainder[c % 3], c)
            # version-1-End----------------------------------------------------------
            # version-2-Begin--------------------------------------------------------
            '''
            ls_val = [i + num for i in remainder]
            for val in ls_val:
                remainder[val % 3] = max(remainder[val % 3], val)
            '''
            # version-2-End----------------------------------------------------------
        # jy: 最终返回 remainder[0] 即可;
        return remainder[0]

    """
解法4: 动态规划(时间复杂度 & 空间复杂度均没有什么优势): 状态转移
    """
    def maxSumDivThree_v3(self, nums: List[int]) -> int:
        n = len(nums)
        # jy: 定义 dp[k+1][m]: 代表截止数组下标为 k 的数值 nums[k] 为止除以 3 余数为 m 的最大数;
        #     初始化 dp[0][0] 为 0, dp[0][1] 和 dp[0][2] 均为极小值(这样才能确保第一个除以 3 余
        #     数为 0, 1, 2 的数被正确找到, 可通过 [3, 4, 5, 6] 为例结合代码逻辑进行思考);
        # jy: 注意, 为什么 dp[0][0] 必须初始化为 0 ? 因为题目求的是余数为 0 的最大和, 如果是求余
        #     数为 1 的最大和, 则将 dp[0][1] 初始化为 0;
        dp = [[0] * 3 for _ in range(n + 1)]
        dp[0][1] = -sys.maxsize  # float("-inf")
        dp[0][2] = -sys.maxsize  # float("-inf")
        for k in range(n):
            # jy: 如果当前下标为 k 的数值 nums[k] 除以 3 的余数为 0, 则在原先 dp[k][0] 的基础上加
            #     上当前数值 nums[k] (dp[k][0] 的最小值为 0, 故得到的更新后的 dp[k+1][0] 不会可能
            #     为负值), 同样, 截止 nums[k] 为止余数为 1 和 2 的最大和也需在原先的最大值的基础上
            #     被更新(如果之前还没找到第一个余数为 1 或 2 的数值, 则此时的 dp[k][1] 和 dp[k][2]
            #     记录均为一个很大的负值, 加上当前数值 nums[k] 后仍为一个小于 0 的值, 当更新后的
            #     dp[k+1][1] 或 dp[k+1][2] 小于 0 时, 表明还没找到余数为 1 或 2 的数值之和; 后续找
            #     到了会更新为相应的数值, 使得相应数值开始大于 0, 并在后续循环中不断更新);
            if nums[k] % 3 == 0:
                dp[k + 1][0] = dp[k][0] + nums[k]  # max(dp[k][0], dp[k][0]+nums[k])
                dp[k + 1][1] = dp[k][1] + nums[k]  # max(dp[k][1], dp[k][1]+nums[k])
                dp[k + 1][2] = dp[k][2] + nums[k]  # max(dp[k][2], dp[k][2]+nums[k])
            # jy: 如果 nums[k] 除以 3 的余数为 1, 则依据相应规则更新截止该数值为止除以 3 余数为 0, 1, 2
            #     的总和最大值;
            elif nums[k] % 3 == 1:
                dp[k+1][0] = max(dp[k][0], dp[k][2] + nums[k])
                dp[k+1][1] = max(dp[k][1], dp[k][0] + nums[k])
                dp[k+1][2] = max(dp[k][2], dp[k][1] + nums[k])
            # jy: 如果 nums[k] 除以 3 的余数为 2, 则依据相应规则更新截止该数值为止除以 3 余数为 0, 1, 2
            #     的总和最大值;
            elif nums[k] % 3 == 2:
                dp[k+1][0] = max(dp[k][0], dp[k][1] + nums[k])
                dp[k+1][1] = max(dp[k][1], dp[k][2] + nums[k])
                dp[k+1][2] = max(dp[k][2], dp[k][0] + nums[k])
        # jy: 最终返回截止最后一个数值为止能被 3 整除(即余数为 0)的数值之和的最大值
        return dp[-1][0]

    def maxSumDivThree_2022_02_25(self, nums: List[int]) -> int:
        sums_ = sum(nums)
        remainder = sums_ % 3
        if remainder == 0:
            return sums_

        ls_ones = []
        ls_twos = []

        for val in nums:
            if val % 3 == 1:
                ls_ones.append(val)
            elif val % 3 == 2:
                ls_twos.append(val)

        ls_ones.sort()
        ls_twos.sort()

        substract = []
        if remainder == 1:
            if ls_ones:
                substract.append(ls_ones[0])
            if len(ls_twos) > 1:
                substract.append(sum(ls_twos[:2]))
            return sums_ - min(substract)
        else:
            if ls_twos:
                substract.append(ls_twos[0])
            if len(ls_ones) > 1:
                substract.append(sum(ls_ones[:2]))
            return sums_ - min(substract)


nums = [3, 6, 5, 1, 8]
# Output: 18
res = Solution().maxSumDivThree_v1(nums)
print(res)


nums = [4]
# Output: 0
res = Solution().maxSumDivThree_v2(nums)
print(res)


nums = [1, 2, 3, 4, 4]
# Output: 12
res = Solution().maxSumDivThree_v3(nums)
print(res)


