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
title_jy = "Maximum-Size-Subarray-Sum-Equals-k(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array nums and an integer k, return the maximum length of a subarray
that sums to k. If there isn't one, return 0 instead.


Example 1:
Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

Example 2:
Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.



Constraints:
1 <= nums.length <= 10^4
-10^4<= nums[i] <= 10^4
-10^5<= k <= 10^5


Follow Up: Can you do it in O(n) time?
"""


from typing import List


class Solution:
    """
解法1(超时): 额外创建一个数组 sums, sums[i] = nums[0] + nums[1] + ... + nums[i], 然后
双重遍历 sums, 判断 sums[j] - sums[i] 之差是否等于 k; 时间复杂度 O(n^2)
    """
    def maxSubArrayLen_v1(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        max_length = 0
        sums = [0] * len(nums)
        # jy: 构建 sums 数组;
        for i, n in enumerate(nums):
            sums[i] = sums[i-1] + n if i != 0 else n

        for i in range(len(nums)):
            if sums[i] == k:
                # jy: i 为下标, 长度需要 +1 ; 后半段多余, 可以去掉;
                # max_length = max(max_length, i + 1) if max_length != 0 else (i + 1)
                max_length = max(max_length, i+1)

            for j in range(i+1, len(nums)):
                if sums[j] - sums[i] == k:
                    current_length = j-i
                    # jy: 即使 max_length 为 0, 需要取 current_length, 也直接 max() 函数计算即可, 因此
                    #    后半部分 if 判断可以去掉;
                    # max_length = max(max_length, current_length) if max_length != 0 else current_length
                    max_length = max(max_length, current_length)

        return max_length



    """
解法2: 在解法 1 的基础上, 使用 Map 来保存连续子数组的和, 键为某个子数组的和, 值为该子
数组的结束位置, 即对于 Map[n] = i 表示 nums[0] + nums[1] + ... + nums[i] = n;

遍历数组, 判断至今的数组和与 k 的差是否在 Map 中, 如果存在则更新最大连续子数组的长度;
    """
    def maxSubArrayLen_v2(self, nums: List[int], k: int) -> int:
        sums = {}
        sum_so_far = 0
        max_length = 0

        for i, n in enumerate(nums):
            sum_so_far += n
            # jy: 如果当前连续子数组之和为 k, 则其对应的长度为 i+1;
            if sum_so_far == k:
                max_length = i+1
            # jy: 如果当前子数组之和不为 k, 则判断子数组之和减去 k 后的值是否在 sums 中有
            #    记录, 如果有则表明存在下标以非 0 为首的字数组之和为目标值, 其长度为 i - sums[sum_so_far - k];
            elif (sum_so_far - k) in sums:
                max_length = max(max_length, i - sums[sum_so_far - k])
            # jy: 如果 sum_so_far 目前在 sums 中没有记录, 则按当前下标 i 补充记录到 sums 中; 如果已经
            #    在 sums 中有记录了, 则忽略(不再更新最新子数组的下标值, 使得保留相同 sum_so_far 时子
            #    数组长度最小的那个, 因为后续该长度会被用于减法逻辑; 减小才能得大)
            if sum_so_far not in sums:
                sums[sum_so_far] = i

        return max_length



nums = [1, -1, 5, -2, 3]
k = 3
# Output: 4
res = Solution().maxSubArrayLen_v1(nums, k)
print(res)


nums = [-2, -1, 2, 1]
k = 1
# Output: 2
res = Solution().maxSubArrayLen_v2(nums, k)
print(res)


