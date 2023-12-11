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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Array-Partition-I(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""

"""
Given an integer array ``nums`` of 2n integers, group these integers into n
pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for
all i is maximized. Returnthe maximized sum.


Example 1:
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.

Example 2:
Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.


Constraints:
1 <= n <= 10^4
nums.length == 2 * n
-10^4<= nums[i] <= 10^4
"""




from typing import List



class Solution:
    """
将数组排序后求奇数位的数字之和

JY: 排序后从左到右按位两两组合的情况下, pair 中的小的值与大的值最为接近, 此时所
有 pair 的最小值加和结果是最大的;
    """
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0

        for i in range(0, len(nums), 2):
            max_sum += nums[i]

        return max_sum


nums = [1,4,3,2]
# Output: 4
res = Solution().arrayPairSum(nums)
print(res)


nums = [6,2,6,5,1,2]
# Output: 9
res = Solution().arrayPairSum(nums)
print(res)


