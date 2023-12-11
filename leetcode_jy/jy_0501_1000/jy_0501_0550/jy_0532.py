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
title_jy = "K-diff-Pairs-in-an-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers ``nums`` and an integer ``k``, return the number of
unique k-diff pairs in the array. A k-diff pair is an integer pair (nums[i], nums[j]),
where the following are true:
1) 0 <= i < j < nums.length
2) |nums[i] - nums[j]| == k; Notice that |val| denotes the absolute value of ``val``.


Example 1:
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5). Although we
             have two ``1`` in the input, we should only return the number of unique pairs.

Example 2:
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Example 4:
Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
Output: 2

Example 5:
Input: nums = [-1,-2,-3], k = 1
Output: 2


Constraints:
1 <= nums.length <= 10^4
-10^7 <= nums[i] <= 10^7
0 <= k <= 10^7
"""


import collections
from typing import List


class Solution:
    """
首先使用 Map 保存每个数字出现的次数，然后遍历 Map
1) 如果 k 等于 0, 那么需要某个数字出现 2 次以上;
2) 如果 k > 0, 如果存在 |a - b| = k, 那么 a - b = k 或者 a - b = -k,
   即 a = b + k 或者 a = b - k, 只需要判断当前数字加 k 是否在 Map 中
   (为什么不用判断当前数字减 k 在 Map 中 —— 因为 (a, b) 和 (b, a) 被视为重复)
    """
    def findPairs_v1(self, nums: List[int], k: int):
        counter = collections.Counter(nums)
        count = 0
        res = []

        for n, c in counter.items():
            if k == 0 and c >= 2:
                count += 1
                res.append((n, n))
            # jy: n + k 的数值(假设为 x)在 counter 中, 即表明 n - x = -k, 即 (n, x) 是一组
            #     满足要求的组合; 此时不需要再获取 n - x = k 的情况(即此时的 x (n - k) 的结
            #     果在 counter 中), 因为此时的 (n, n-k) 可能会与原先的 (n, n+k) 重合; 如 k
            #     等于 2, (5, 3) 和 (3, 5) 将重合;
            elif k > 0 and n + k in counter:
                count += 1
                res.append((n, n + k))

        return count, res

    """
JY: 注意, 该方法不是真正的解, 该方法的实现逻辑中, nums 列表中的数值不能重复使用来构建 pair
    """
    def findPairs_jy(self, nums, k):
        dict_ = {}
        count = 0
        # jy: |a - b| = k, 那么 a - b = k 或者 a - b = -k, 即 a + k = b 或者 a - k = b
        for i in nums:
            if i + k in dict_:
                count += 1
                dict_[i+k] -= 1
                if dict_[i+k] == 0:
                    dict_.pop(i+k)
            elif i - k in dict_:
                count += 1
                dict_[i-k] -= 1
                if dict_[i-k] == 0:
                    dict_.pop(i-k)
            else:
                dict_[i] = 1
        return count


nums = [3, 1, 4, 1, 5]
k = 2
# Output: 2
res = Solution().findPairs_v1(nums, k)
print(res)


nums = [1, 2, 3, 4, 5]
k = 1
# Output: 4
res = Solution().findPairs_v1(nums, k)
print(res)


nums = [1, 3, 1, 5, 4]
k = 0
# Output: 1
res = Solution().findPairs_v1(nums, k)
print(res)


nums = [1, 2, 4, 4, 3, 3, 0, 9, 2, 3]
k = 3
# Output: 2
res = Solution().findPairs_v1(nums, k)
print(res)


nums = [-1, -2, -3]
k = 1
# Output: 2
res = Solution().findPairs_v1(nums, k)
print(res)


