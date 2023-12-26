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
title_jy = "Maximum_Product_Subarray(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "动态规划 | 相似题: 0053 (Maximum-Subarray)"


"""
Given an integer array `nums`, find a subarray that has the largest product,
and return the product. The test cases are generated so that the answer will
fit in a 32-bit integer.


Example 1:
Input: [2, 3, -2, 4]
Output: 6
Explanation: [2, 3] has the largest product 6.

Example 2:
Input: [-2, 0, -1]
Output: 0
Explanation: The result cannot be 2, because [-2, -1] is not a subarray.


Constraints:
1) 1 <= nums.length <= 2 * 10^4
2) -10 <= nums[i] <= 10
3) The product of any prefix or suffix of `nums` is guaranteed to fit in a
   32-bit integer.
"""


class Solution:
    """
解法 1: 动态规划

求以 nums[i] 结尾的子数组的最大乘积, 等价于求以 nums[i-1] 结尾的子数组的最大乘
积和 nums[i] 相乘后的值与 nums[i] 取较大值, 即: max(dp[i-1] * nums[i], nums[i])

由于 nums[i] 可能小于 0, 且计算乘积过程中, 如果 num[i] 为负值, 且截止 nums[i-1]
的子数组的数值的乘积为一个很小的负值 (绝对值很大), 则两数相乘的结果可能是当前的
最大值; 所以 dp[i] 需保存两个元素: 以 nums[i] 结尾的子数组的乘积的最大值 (通常为
正数) 和最小值 (通常为负最小值)
    """
    def maxProduct_v1(self, nums: List[int]) -> int:
        # jy: dp[i] 需记录两个元素: 
        #     dp[i][0]: 以 nums[i] 结尾的子数组的正的最大乘积
        #     dp[i][1]: 以 nums[i] 结尾的子数组的负的最小乘积
        dp = [[0, 0] for _ in range(len(nums))]
        # jy: 将 dp[0] 中的两个数初始化为数组中的初始元素
        dp[0] = [nums[0], nums[0]]
        # jy: 从数组的第二个元素开始遍历
        for i in range(1, len(nums)):
            value = nums[i]
            # jy: 获取以 nums[i] 结尾的子数组的最大乘积
            dp[i][0] = max(dp[i-1][0] * value,
                           dp[i-1][1] * value,
                           value)
            # jy: 获取以 nums[i] 结尾的子数组的最小乘积
            dp[i][1] = min(dp[i-1][0] * value,
                           dp[i-1][1] * value,
                           value)
        # jy: 返回 dp[i][0] 中的最大值
        return max(x[0] for x in dp)


    """
解法 2: 优化解法 1 (优化空间复杂度)
    """
    def maxProduct_v2(self, nums: List[int]) -> int:
        max_product = nums[0]
        max_product_end_i = nums[0]

        min_product = nums[0]
        min_product_end_i = nums[0]

        # jy: 从数组的第二个元素开始遍历
        for i in range(1, len(nums)):
            value = nums[i]

            # jy: 注意, 此处需要引入中间临时变量, 不能直接更新
            #     max_product_end_i, 因为以下计算最小值时也需要
            #     使用上一轮的 max_product_end_i, 因此需要基于
            #     上一轮的 max_product_end_i 和 min_product_end_i
            #     计算得到最大值和最小值后, 再更新这两个值
            tmp_max = max(max_product_end_i * value, 
                          min_product_end_i * value,
                          value)
            if tmp_max > max_product:
                max_product = tmp_max

            tmp_min = min(max_product_end_i * value,
                          min_product_end_i * value,
                          value)
            if tmp_min < min_product:
                min_product = tmp_min

            max_product_end_i = tmp_max
            min_product_end_i = tmp_min

        return max_product


    """
解法 3: 在解法 1 的基础上, 获取乘积最大值的具体子数组
    """
    def maxProduct_v3(self, nums: List[int]) -> int:
        # jy: 在解法 1 的基础上增加两个数值, 保存最大值和最小值的子
        #     数组的 low, high 下标
        dp = [[[0, -1, -1], [0, -1, -1]] for _ in range(len(nums))]
        dp[0] = [[nums[0], 0, 0], [nums[0], 0, 0]]
        for i in range(1, len(nums)):
            value = nums[i]

            # jy: 更新子数组的乘积最大值以及子数组的下标位置
            if dp[i-1][0][0] * value >= max(dp[i-1][1][0] * value, value):
                dp[i][0][0] = dp[i-1][0][0] * value
                dp[i][0][1] = dp[i-1][0][1]
                dp[i][0][2] = i
            elif dp[i-1][1][0] * value >= max(dp[i-1][0][0] * value, value):
                dp[i][0][0] = dp[i-1][1][0] * value
                dp[i][0][1] = dp[i-1][1][1]
                dp[i][0][2] = i
            else:
                dp[i][0][0] = value
                dp[i][0][1] = i
                dp[i][0][2] = i


            # jy: 更新子数组的乘积最小值以及子数组的下标位置
            if dp[i-1][0][0] * value < min(dp[i-1][1][0] * value, value):
                dp[i][1][0] = dp[i-1][0][0] * value
                dp[i][1][1] = dp[i-1][0][1]
                dp[i][1][2] = i
            elif dp[i-1][1][0] * value < min(dp[i-1][0][0] * value, value):
                dp[i][1][0] = dp[i-1][1][0] * value
                dp[i][1][1] = dp[i-1][1][1]
                dp[i][1][2] = i
            else:
                dp[i][1][0] = value
                dp[i][1][1] = i
                dp[i][1][2] = i
        # jy: 基于最大值位置排序, 随后返回最后一个数值
        return sorted(dp, key=lambda x: x[0][0])[-1][0]
        #return max(x[0][0] for x in dp)



nums = [2, 3, -2, 4]
res = Solution().maxProduct_v1(nums)
print(res)


nums = [-2, 0, -1]
res = Solution().maxProduct_v1(nums)
print(res)


nums = [-4, -3, -2]
res = Solution().maxProduct_v2(nums)
print(res)


nums = [2, 3, -2, 4]
res = Solution().maxProduct_v3(nums)
print(res)


nums = [-2, 0, -1]
res = Solution().maxProduct_v3(nums)
print(res)


