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
tag_jy = ""


"""
Given an integer array nums, find the contiguous subarray within an
array (containing at least one number) which has the largest product.


Example 1:
Input: [2, 3, -2, 4]
Output: 6
Explanation: [2, 3] has the largest product 6.

Example 2:
Input: [-2, 0, -1]
Output: 0
Explanation: The result cannot be 2, because [-2, -1] is not a subarray.
"""



from typing import List
class Solution:
    """
此题类似: 053_Maximum-Subarray.py
动态规划: 对于求以 nums[i] 结尾的子数组的最大乘积来说, 等价于求以 nums[i-1] 结尾的子数组的最大乘积
和 nums[i] 相乘后的值与 nums[i] 取较大值, 即 max(dp[i-1] * nums[i], nums[i]), 由于 nums[i] 有可能是
小于 0, 所以实际的 dp 是一个二维数组, 每一个数组元素分别保存以 nums[i] 结尾的子数组的乘积的正的最大
值和负的最小值;
    """
    def maxProduct(self, nums: List[int]) -> int:
        # jy: 用 dp[i] 是一个含有两个数值的列表, 用来表示以 nums[i] 结尾的子数组的正的最大乘积(第 1 个
        #    数值)和负的最小乘积(第 2 个数值); 由于计算乘积过程中, 如果 num[i] 为负值, 且 dp[i-1] 中
        #    负的最小乘积也为负值, 则两数相乘的结果可能是当前的最大值, 故需要保留截至当前为止子数组的
        #    负的最小乘积, 实现两负数相乘后做对比;
        dp = [[0, 0] for _ in range(len(nums))]
        # jy: 将 dp[0] 中的两个数初始化为数组中的初始元素;
        dp[0] = [nums[0], nums[0]]
        # jy: 从数组的第二个元素开始遍历;
        for i in range(1, len(nums)):
            value = nums[i]
            # jy: 获取以 nums[i] 结尾的子数组的最大乘积;
            dp[i][0] = max(dp[i-1][0] * value, dp[i-1][1] * value, value)
            # jy: 获取以 nums[i] 结尾的子数组的最小乘积;
            dp[i][1] = min(dp[i-1][0] * value, dp[i-1][1] * value, value)
        # jy: 返回 dp[i][0] 中的最大值;
        return max(x[0] for x in dp)


    """
jy: 以上方法不能获取乘积最大值的对应子数组, 此处改进, 获取该子数组;
    """
    def maxProduct_jy(self, nums: List[int]) -> int:
        # jy: 在解法 1 的基础上增加两个数值, 用于保存最大值和最小值的子数组的 low, high 下标;
        dp = [[[0, -1, -1], [0, -1, -1]] for _ in range(len(nums))]
        dp[0] = [[nums[0], 0, 0], [nums[0], 0, 0]]
        for i in range(1, len(nums)):
            value = nums[i]
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
        return sorted(dp, key=lambda x: x[0][0])[-1][0]
        #return max(x[0][0] for x in dp)

nums = [2, 3, -2, 4]
res = Solution().maxProduct(nums)
print(res)


nums = [-2, 0, -1]
res = Solution().maxProduct(nums)
print(res)


nums = [2, 3, -2, 4]
res = Solution().maxProduct_jy(nums)
print(res)


nums = [-2, 0, -1]
res = Solution().maxProduct_jy(nums)
print(res)


