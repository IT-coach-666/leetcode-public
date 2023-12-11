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
title_jy = "Partition-Equal-Subset-Sum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a non-empty array ``nums`` containing only positive integers, find if the array can be
partitioned into two subsets such that the sum of elements in both subsets is equal.


Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""


from typing import List


class Solution:
    """
我们能想到的, 例如基于贪心算法的「将数组降序排序后, 依次将每个元素添加至当前元素和较小的子集中」之类的方法
都是错误的, 可以轻松地举出反例; 因此, 我们必须尝试非多项式时间复杂度的算法, 例如时间复杂度与元素大小相关的
动态规划;

这道题可以换一种表述: 给定一个只包含正整数的非空数组 nums[0], 判断是否可以从数组中选出一些数字, 使得这些数
字的和等于整个数组的元素和的一半; 因此这个问题可以转换成 0−1 背包问题; 这道题与传统的 0−1 背包问题的区别在
于, 传统的 0−1 背包问题要求选取的物品的重量之和不能超过背包的总容量, 这道题则要求选取的数字的和恰好等于整个
数组的元素和的一半; 类似于传统的 0−1 背包问题, 可以使用动态规划求解;

在使用动态规划求解之前, 首先需要进行以下判断:
1) 根据数组的长度 n 判断数组是否可以被划分, 如果 n<2, 则不可能将数组分割成元素和相等的两个子集, 因此直接返
   回 false;
2) 计算整个数组的元素和 sum 以及最大元素 maxNum; 如果 sum 是奇数, 则不可能将数组分割成元素和相等的两个子集.
   因此直接返回 false; 如果 sum 是偶数, 则令 target = sum / 2, 需要判断是否可以从数组中选出一些数字, 使得这
   些数字的和等于 target; 如果 maxNum > target, 则除了 maxNum 以外的所有元素之和一定小于 target, 因此不可能
   将数组分割成元素和相等的两个子集, 直接返回 false;

创建二维数组 dp, 包含 n 行和 target+1 列, 其中 dp[i][j] 表示从数组的 [0,i] 下标范围内选取若干个正整数(可以是
0 个), 是否存在一种选取方案使得被选取的正整数的和等于 j; 初始时 dp 中的全部元素都是 false;
在定义状态之后, 需要考虑边界情况; 以下两种情况都属于边界情况:
1) 如果不选取任何正整数, 则被选取的正整数等于 0; 因此对于所有 0≤i<n, 都有 dp[i][0]=true;
2) 当 i==0 时, 只有一个正整数 nums[0] 可以被选取, 因此 dp[0][nums[0]]=true。

对于 i>0 且 j>0 的情况, 如何确定 dp[i][j] 的值? 需要分别考虑以下两种情况:
1) 如果 j≥nums[i], 则对于当前的数字 nums[i], 可以选取也可以不选取, 两种情况只要有一个为 true, 就有 dp[i][j]=true;
   a) 如果不选取 nums[i], 则 dp[i][j] = dp[i−1][j]
   b) 如果选取 nums[i], 则   dp[i][j] = dp[i−1][j−nums[i]]
   即:  dp[i][j] = dp[i−1][j] ∣ dp[i−1][j−nums[i]]
2) 如果 j < nums[i], 则在选取的数字的和等于 j 的情况下无法选取当前的数字 nums[i], 因此有:
   dp[i][j] = dp[i−1][j]

通过以上两种情况即可构建状态转移方程; 最终得到 dp[n−1][target] 即为答案;

参考: https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/
    """
    def canPartition_v1(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False

        target = total // 2
        if maxNum > target:
            return False

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target]

    """
解法2: 解法 1 的空间复杂度是 O(n×target); 但是可以发现在计算 dp 的过程中, 每一行的 dp 值都只与上一行
的 dp 值有关, 因此只需要一个一维数组即可将空间复杂度降到 O(target); 此时的转移方程为:
dp[j] = dp[j] ∣ dp[j−nums[i]]

且需要注意的是第二层的循环我们需要从大到小计算, 因为如果我们从小到大更新 dp 值, 那么在计算 dp[j] 值的
时候, dp[j−nums[i]] 已经是被更新过的状态, 不再是上一行的 dp 值;

    """
    def canPartition_v2(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[target]


nums = [1, 5, 11, 5]
# Output: true
res = Solution().canPartition(nums)
print(res)


nums = [1, 2, 3, 5]
# Output: false
res = Solution().canPartition(nums)
print(res)


