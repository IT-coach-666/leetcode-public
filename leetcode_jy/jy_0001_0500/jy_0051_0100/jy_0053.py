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
title_jy = "Maximum-Subarray(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "动态规划 | 分治算法 (递归) IMP | 相似题: 0152(Maximum_Product_Subarray)"


"""
Given an integer array `nums`, find the subarray with the largest sum,
and return its sum.

 
Example 1:
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5, 4, -1, 7, 8]
Output: 23
Explanation: The subarray [5, 4, -1, 7, 8] has the largest sum 23.
 

Constraints:
1) 1 <= nums.length <= 10^5
2) -10^4 <= nums[i] <= 10^4
 

Follow up: If you have figured out the O(n) solution, try coding another 
solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    """
解法 1: 动态规划, 时间复杂度 O(n), 空间复杂度 O(n)

用 dp[i] 表示以 nums[i] 结尾的子数组的最大和, 则:
dp[i] = max(dp[i-1] + nums[i], nums[i])

最大连续子数组即 dp 中的最大值
    """
    def maxSubArray_v1(self, nums: List[int]) -> int:
        # jy: 初始化 dp 值均为 0, dp[0] 为数组中第一个元素的值
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)


    """
解法 2: 类似解法 1, 使用一个临时变量记录以 nums[i] 结尾的子数组的最大
和, 同时与迄今为止的最大子数组和进行比较并更新, 减少空间复杂度

时间复杂度 O(n), 空间复杂度 O(1)
    """
    def maxSubArray_v2(self, nums: List[int]) -> int:
        max_sum = nums[0]
        max_sum_end_i = nums[0]
        for i in range(1, len(nums)):
            max_sum_end_i = max(max_sum_end_i + nums[i], nums[i])
            max_sum = max(max_sum_end_i, max_sum)
        return max_sum


    """
解法 3: 同解法 2, 更新最大子数组时同时更新下标信息
    """
    def maxSubArray_v3(self, nums: List[int]) -> int:
        max_sum = nums[0]
        idx_b = idx_e = 0
        max_sum_end_i = nums[0]
        for i in range(1, len(nums)):
            if max_sum_end_i + nums[i] >= nums[i]:
                max_sum_end_i = max_sum_end_i + nums[i]
                if max_sum_end_i > max_sum:
                    max_sum = max_sum_end_i
                    idx_e = i
            else:
                max_sum_end_i = nums[i]
                if max_sum_end_i > max_sum:
                    max_sum = max_sum_end_i
                    idx_b = idx_e = i
        return max_sum, idx_b, idx_e


    """
解法 4: 分治算法 (递归), 时间复杂度 O(n logn)

最大子序和要么在左半边, 要么在右半边, 要么是穿过中间; 对于左右边的序列情况
也是一样, 因此可以用递归处理; 中间部分的则可以直接计算出来
    """
    def maxSubArray_v4(self, nums: List[int]) -> int:
        n = len(nums)
        # jy: 递归终止条件
        if n == 1:
            return nums[0]

        # jy: 递归计算左半边最大子数组的和
        max_left = self.maxSubArray_v4(nums[0: len(nums) // 2])
        # jy: 递归计算右半边最大子数组的和
        max_right = self.maxSubArray_v4(nums[len(nums) // 2: len(nums)])
        
        # jy: 计算中间的最大子数组的和, 从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)

        # jy: 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)


    """
解法 5: 分治算法, 时间复杂度 O(n), 空间复杂度 O(log n)

分治的核心思路是将大问题拆分成更小且相似的子问题, 通过递归解决这些子问题, 最
终合并子问题的解来得到原问题的解

实现分治的关键在于对递归函数的设计 (明确入参、返回值), 在涉及数组的分治题中,
左右下标 low 和 high 必然会作为函数入参, 因为它能用于表示当前所处理的区间,
即小问题的范围

对于本题, 仅将最大子数组之和 (答案) 作为返回值并不足够, 因为单纯从小区间的解无
法直接推导出大区间的解, 因此需要一些额外信息来辅助求解; 可以将返回值设计成四元
组 [sum, lm, rm, max], 分别代表: [区间和, 前缀最大值, 后缀最大值, 最大子数组和]

有了完整的函数签名 int[] dfs(int[] nums, int l, int r), 接下来考虑如何实现分治

根据当前区间 [low, high] 的长度进行分情况讨论:
1) 如果数组中的值均小于或等于 0, 则直接返回最大值即可
2) 若 low == high, 表明只有一个元素, 区间和为 nums[low], 而 "最大子数组和"、
   "前缀最大值" 和 "后缀最大值" 由于均确保不小于 0 (可以将 0 理解为空数组的
   和, 假设允许空数组), 因此为 max(nums[low], 0),
3) 若 low != high, 将当前问题划分为两个子问题, 通常会划分为两个相同大小的子
   问题: [low, mid] 和 [mid+1, high], 递归求解, 其中 mid = (low + high) // 2

随后考虑如何用 "子问题" 的解合并成 "原问题" 的解:
1) 合并区间和 (sum)
   当前问题的区间和等于左右两个子问题的区间和之和: sum = left[0] + right[0]
2) 合并前缀最大值 (lm)
   当前问题的前缀最大值可以是 "左子问题的前缀最大值" 或 "左子问题的区间和加上
   右子问题的前缀最大值", 即: lm = max(left[1], left[0] + right[1])
3) 合并后缀最大值 (rm)
   当前问题的后缀最大值可以是 "右子问题的后缀最大值" 或 "右子问题的区间和加上
   左子问题的后缀最大值", 即: rm = max(right[2], right[0] + left[2])
4) 合并最大子数组和 (max)
   当前问题的最大子数组可能出现在左子问题、右子问题或跨越左右两个子问题的边界,
   因此 max 可以通过 max(left[3], right[3], left[2] + right[1]) 来得到

注意: 由于在计算 lm、rm 和 max 时允许数组为空, 而答案对子数组的要求是至少包含
一个元素, 因此对于 nums 全为负数时, 会错误得出最大子数组和为 0, 针对该情况需
做特殊处理, 遍历一遍 nums, 若最大值为负数, 直接返回最大值
    """
    def maxSubArray_v5(self, nums: List[int]) -> int:
        def dfs(low, high):
            # jy: 
            if low == high:
                t = max(nums[low], 0)
                return [nums[low], t, t, t]

            # jy: 划分成两个子区间, 分别求解
            mid = (low + high) // 2
            left, right = dfs(low, mid), dfs(mid + 1, high)

            # jy: 组合左右子区间的信息, 得到当前区间的信息
            ans = [0] * 4
            # jy: 当前区间的和
            ans[0] = left[0] + right[0]
            # jy: 当前区间前缀最大值
            ans[1] = max(left[1], left[0] + right[1])
            # jy: 当前区间后缀最大值
            ans[2] = max(right[2], right[0] + left[2])
            # jy: 最大子数组的和
            ans[3] = max(left[3], right[3], left[2] + right[1]) 
            return ans
        
        # jy: 如果列表中的数值均小于或等于 0, 则直接返回其中的最大值即可
        m = max(nums)
        if m <= 0:
            return m

        # jy: 走到此处表明 nums 中有正数, 递归函数返回的结果是一个含有 4 个
        #     元素的列表, 列表中的第 4 个元素即记录最大子数组的和
        return dfs(0, len(nums) - 1)[3]



nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#nums = [-2]
#nums = [-2, 1, -3]

res = Solution().maxSubArray_v1(nums)
print(res)


res = Solution().maxSubArray_v2(nums)
print(res)


res, idx_b, idx_e = Solution().maxSubArray_v3(nums)
print(res, " === ", sum(nums[idx_b: idx_e+1]))
print(nums[idx_b: idx_e+1])


res = Solution().maxSubArray_v4(nums)
print(res)


res = Solution().maxSubArray_v5(nums)
print(res)


