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
title_jy = "Contains-Duplicate-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array nums and two integers k and t, return true if there are two distinct
indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i-j) <= k.


Example 1:
Input: nums = [1, 2, 3, 1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1, 0, 1, 1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1, 5, 9, 1, 5, 9], k = 2, t = 3
Output: false


Constraints:
0 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31
- 10 <= k <= 10^4
0 <= t <= 2^31- 1
"""

import bisect
from typing import List


class Solution:
    """
核心思想和 219_Contains-Duplicate-II.py 一致: 维护一个大小为 k+1 的窗口, 只是这个窗口使用二分搜索
树实现, 遍历数组, 对于每个数字 nums[i], 判断在窗口中是否存在数字 n 满足 abs(nums[i] - n) <= t, 等
价于 -t <= n - nums[i] <= t, 即: nums[i] - t <= n <= nums[i] + t, 在二分搜索树中搜索 nums[i] - t 和
nums[i] + t, 如果对应数字的索引不相同, 则存在满足条件的数字;
    """
    def containsNearbyAlmostDuplicate_v1(self, nums: List[int], k: int, t: int) -> bool:
        bst = []

        for i, n in enumerate(nums):
            if i > k:
                del bst[bisect.bisect_left(bst, nums[i - k - 1])]

            left = bisect.bisect_left(bst, nums[i] - t)
            right = bisect.bisect_right(bst, nums[i] + t)

            if left != right:
                return True

            bisect.insort(bst, n)

        return False



    """
JY: 思路同 v1, 代码不同, 但使用了 2 层 for 循环, 时间复杂度更高些;
    """
    def containsNearbyAlmostDuplicate_v2(self, nums: List[int], k: int, t: int) -> bool:
        jy_set = set()

        for i, n in enumerate(nums):
            if i > k:
                jy_set.remove(nums[i - k - 1])

            for num_j in jy_set:
                if num_j - t <= n and n <= num_j + t:
                    return True
            jy_set.add(n)

        return False


nums = [1, 2, 3, 1]
k = 3
t = 0
# Output: true
res = Solution().containsNearbyAlmostDuplicate_v1(nums, k, t)
print(res)
res = Solution().containsNearbyAlmostDuplicate_v2(nums, k, t)
print(res)

nums = [1, 0, 1, 1]
k = 1
t = 2
# Output: true
res = Solution().containsNearbyAlmostDuplicate_v1(nums, k, t)
print(res)
res = Solution().containsNearbyAlmostDuplicate_v2(nums, k, t)
print(res)

nums = [1, 5, 9, 1, 5, 9]
k = 2
t = 3
# Output: false
res = Solution().containsNearbyAlmostDuplicate_v1(nums, k, t)
print(res)

res = Solution().containsNearbyAlmostDuplicate_v2(nums, k, t)


