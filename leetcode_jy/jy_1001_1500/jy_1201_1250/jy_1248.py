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
title_jy = "Count-Number-of-Nice-Subarrays(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16


Constraints:
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""


from typing import List


class Solution:
    """
解法1
类似 992. Subarrays with K Different Integers, k 个的问题可转化为至多 k 个减去至多 k - 1 个的问题;
    """
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self._at_most_k(nums, k) - self._at_most_k(nums, k - 1)

    def _at_most_k(self, nums, k):
        start, count = 0, 0
        odd_count = 0

        for end, n in enumerate(nums):
            if n & 1 == 1:
                odd_count += 1

            while odd_count > k:
                if nums[start] & 1 == 1:
                    odd_count -= 1

                start += 1

            count += end - start + 1

        return count

from typing import List


class Solution:
    """
解法2: 将数组中的偶数变为0, 奇数变为1, 则题目就变成了 560. Subarray Sum Equals K;
    """
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [1 if n & 1 == 1 else 0 for n in nums]
        sum_so_far = 0
        count = 0
        sum_mapping = {0: 1}

        for n in nums:
            sum_so_far += n

            if sum_so_far - k in sum_mapping:
                count += sum_mapping[sum_so_far - k]

            sum_mapping[sum_so_far] = sum_mapping.get(sum_so_far, 0) + 1

        return count


