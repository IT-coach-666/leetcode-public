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
title_jy = "Maximum-Length-of-Repeated-Subarray(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two integer arrays nums1 and nums2, return the maximum length of a subarray
that appears in both arrays.


Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5


Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
"""



from typing import List



class Solution:
    """
使用动态规划求解, 记 dp[i][j] 表示以 nums1[i] 和 nums2[j] 结尾(但开头并非均从 nums1[0] 和
nums2[0] 开头, 而是以上一个局部最长公共子数组结束后的下一个位置为开头)的最长公共子数组;
即 dp[i][j] 记录的最长公共子数组仅仅是局部最长, 是否是全局最长不能判断;
    """
    def findLength_v1(self, nums1: List[int], nums2: List[int]) -> int:
        # jy: 如果两个数组均为空, 则最长公共子数组长度为 0;
        if not nums1 or not nums2:
            return 0
        # jy: m 为 nums1 的长度, n 为 nums2 的长度;
        m, n = len(nums1), len(nums2)
        # jy: 记录最长公共子数组的长度, 最终会返回该值;
        max_length = 0
        # jy: dp[i][j] 表示以 nums1[i] 和 nums2[j] 结尾(开头为上一个局部最长子数组结尾的下
        #    一个位置)的局部最长公共子数组的对应长度, 初始化均为 0; 由于 dp[i][j] 代表的是
        #    局部最长公共子数组的长度, 故需要一个变量(max_length)来记录全局最长子数组的长度;
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # jy: 如果数组中的对应下标的值相等, 则在原有局部最长公共子数组的基础上加 1;
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1 if i >= 1 and j >= 1 else 1
                    max_length = max(max_length, dp[i][j])
        return max_length

    """
    以下解法为一个错误示例, 并详细说明错的原因;
    """
    def findLength_jy(self, nums1: List[int], nums2: List[int]) -> int:
        """
        记 dp[i][j] 表示以 nums1[i] 和 nums2[j] 结尾的最长公共子数组, 即最终应该返
        回 dp[L1-1][L2-1] (即返回 dp[-1][-1], L1 和 L2 分别为 nums1 和 nums2 的长度);

        注意: 以下解法是错误的, 原因: 假如 nums1 和 nums2 的长度分别为 L1 和 L2, 假设
        nums1[0] 至 nums1[K1] 和 nums2[0] 至 nums2[K2] 的第一个公共子数组的长度为 n (其
        中 K1 和 K2 均有效, 且此时的 nums1[K1] == nums2[K2], 且后续的 nums1[K1+1] != nums2[K2+1]),
        按以下算法的逻辑, 假设 nums1[J1] == nums[J2], 则由于 dp[K1...J1][K2...J2] 的值均
        会更新为 n, 按照 dp[i][j] 所代表的含义, 此时是没问题的, 但此时更新 dp[J1][J2] 的
        值为  dp[J1-1][J2-1] + 1  是不正确的, 因为此时的 dp[J1-1][J2-1] 为 n, 但即使此时
        的 nums1[J1] == nums[J2], 从两个数组的开头到 nums1[J1] 和 nums2[J2] 的最长公共子
        数组的长度依然是 n, 因为此时的 nums1[J1] 虽然等于 nums[J2], 但它与之前的最长公共
        子数组并没有对接起来, 而是又重新开始一个局部的公共子数组, 因此最长公共子数组的长
        度不能直接在原最长公共子数组的长度基础上加 1)
        """
        # jy: 如果两个数组均为空, 则最长公共子数组长度为 0;
        if not nums1 or not nums2:
            return 0
        # jy: m 为 nums1 的长度, n 为 nums2 的长度;
        m, n = len(nums1), len(nums2)
        # jy: dp[i][j] 表示以 nums1[i] 和 nums2[j] 结尾的最长公共子数组的对应长度, 初始化均为 0;
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # jy: 如果数组中的对应下标的值相等, 则
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 if i >= 1 and j >= 1 else 1
                else:
                    # dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    # dp[i][j] = max(dp[i - 1][j - 1],  dp[i][j - 1])
                    dp[i][j] = dp[i][j-1]
        print("====", dp)
        return dp[-1][-1]


nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
# Output: 3
res = Solution().findLength_v1(nums1, nums2)
print(res)


nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]
# Output: 5
res = Solution().findLength_v1(nums1, nums2)
print(res)


# jy: 错误示例
"""
nums1 = [0,1,1,1,1]
nums2 = [1,0,1,0,1]
# Output: 2
res = Solution().findLength_jy(nums1, nums2)
print(res)  # 输出 3
"""


