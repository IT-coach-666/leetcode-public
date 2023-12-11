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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Subarrays-with-K-Different-Integers(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array nums of positive integers, call a (contiguous, not necessarily distinct) subarray of nums good if the number of different integers in that subarray is exactly k.
(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
Return the number of good subarrays of nums.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
Note:
1. 1 <= nums.length <= 20000
2. 1 <= nums[i] <= nums.length
3. 1 <= k <= nums.length
"""

import collections
from typing import List


class Solution:
    """
求解 k 个不同等价于求解至多 k 个不同减去至多 k - 1 个不同, 题目就转化为 340. Longest Substring with At Most K Distinct Characters, 不过这里求的是个数而不是最长的子数组长度; 需要注意的是计算 count 时 count 的增量是 end - start + 1 而不是1, 考虑子数组, 当加入到子数组时, 新增满足至多 k 个不同的数字的子数组为:
1.
2.
3. ...
4.
5.
正好是子数组的长度, 即 end - start + 1 个;
    """
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self._at_most_k(nums, k) - self._at_most_k(nums, k - 1)

    def _at_most_k(self, nums, k):
        counter = collections.defaultdict(int)
        count = 0
        start = 0

        for end, n in enumerate(nums):
            counter[n] += 1

            while len(counter) > k:
                counter[nums[start]] -= 1

                if counter[nums[start]] == 0:
                    counter.pop(nums[start])

                start += 1

            count += end - start + 1

        return count


