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
title_jy = "Split-Array-Largest-Sum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array ``nums`` which consists of non-negative integers and an integer ``m``,
you can split the array into ``m`` non-empty continuous subarrays. Write an algorithm
to minimize the largest sum among these ``m`` subarrays.

Example 1:
Input: nums = [7, 2, 5, 10, 8], m = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays. The best way is to split
             it into [7, 2, 5] and [10, 8], where the largest sum among the two subarrays is
             only 18.

Example 2:
Input: nums = [1, 2, 3, 4, 5], m = 2
Output: 9

Example 3:
Input: nums = [1, 4, 4], m = 3
Output: 4


Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= m <= min(50, nums.length)
"""




from typing import List



class Solution:
    """
一个数组可分为 1 到 n 个子数组(n 为数组的长度):
1) 当分成 1 个子数组时, 最大子数组和为所有数字之和, 记为 high
2) 当分成 n 个子数组时, 最大子数组和为数组中的最大值, 记为 low

以 low 和 high 作为边界进行二分查找, 将 middle 作为最大子数组的和, 寻找可以将原
数组分成 m 个子数组的 middle; 对每个 middle, 遍历数组, 计算连续子数组加和后大于 middle 的个数:
1) 如果该个数大于 m, 说明 middle 不够大, 造成可以将数组切分成大于 m 的连续子数组, low 移动到 middle + 1;
2) 反之, middle 正好或太大, 将 high 置为 middle;
    """
    def splitArray(self, nums: List[int], m: int) -> int:
        # jy: low 表示将数组分为 n 份(n 为数组的长度)时的最大子数组的和;
        #    high 表示将数组分为 1 份时的最大子数组的和(即为原数组元素加和)
        # jy: 注意: low 和 high 表示的含义均为最大子数组的和;
        low, high = max(nums), sum(nums)

        while low < high:
            middle = low + (high - low) // 2
            # jy: 如果 nums 数组中能构造出至少 m 个子数组(其加和均大于 middle), 则说
            #    明 middle 相对于所有子数组中的和为最大的子数组来说, 还是小了些, 此时
            #    将 low 更新为 middle + 1;
            #    如果 nums 数组中能构造出的子数组(其加和均大于 middle)的个数小于 m, 表
            #    明如果构造 m 个子数组时, 其中加和后最大的子数组肯定小于或等于 middle,
            #    此时将 high 设置为 middle;
            if self._has_more_than_m_groups(nums, middle, m):
                low = middle + 1
            else:
                high = middle

        return low


    def _has_more_than_m_groups(self, nums: List[int], largest_sum: int, m: int) -> bool:
        """
        该方法的作用为: 判断在 nums 数组中, 是否能构造出至少 m 个子数组, 使得其加和均大于 largest_sum;
        """
        # jy: 记录数组中截止当前数值为止的所有数值的加和结果;
        current = 0
        # jy: 遍历数组中的元素;
        for num in nums:
            if current + num > largest_sum:
                m -= 1
                if m <= 0:
                    return True
                current = num
            else:
                current += num

        return False


nums = [7, 2, 5, 10, 8]
m = 2
# Output: 18
res = Solution().splitArray(nums, m)
print(res)


nums = [1, 2, 3, 4, 5]
m = 2
# Output: 9
res = Solution().splitArray(nums, m)
print(res)


nums = [1, 4, 4]
m = 3
# Output: 4
res = Solution().splitArray(nums, m)
print(res)


