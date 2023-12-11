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
title_jy = "3Sum-Smaller(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of n integers nums and a target, find the number of index
triplets i, j, k with 0 <= i < j < k < n that satisfy the condition:
nums[i] + nums[j] + nums[k] < target


Example:
Input: nums = [-2, 0, 1, 3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2, 0, 1]
             [-2, 0, 3]


Follow up: Could you solve it in O(n^2) runtime?
"""


from typing import List

class Solution:
    """
同 015_3Sum.py: 先将数组排序, 然后将问题转化为 Two Sum, 使用双指针求解;
使用双指针时, 遇到 nums[low] + nums[high] 小于给定值时, 由于数组是有序
的, 则 [low + 1, high -1] 区间的数和 nums[low] 相加都会小于给定值, 所以
直接给 count 加上 high - low 即可, 由于两层循环, 时间复杂度是 O(n^2);
    """
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # jy: 先对数组进行排序;
        nums.sort()
        count = 0
        # jy: 由于是三数之和, 外层循环只需要遍历到倒数第三个数即可;
        for i in range(0, len(nums)-2):
            # jy: 先求出目标值与 nums[i] 的差值, 将求解目标转化为找出 nums[i+1:] 中
            #    两数之和小于 k 的两个数值组合的个数;
            k = target - nums[i]
            # jy: 双指针法, 将 low 设置为 i+1, high 则为数组最后一个数值的下标;
            low, high = i+1, len(nums)-1
            # jy: 在双指针区间中找出所有满足两数之和小于 k 的两个数值的组合;
            while low < high:
                # jy: 如果 nums[low] + nums[high] < k, 表明 nums[low] 和 nums[high] 是
                #    一组符合要求的组合; 由于数组是升序排序, 则 [low + 1, high -1] 区
                #    间的数和 nums[low] 相加也是符合要求的; 即 nums[low] 与 [low + 1, high]
                #    区间的数值(共 high-low 个数值)都满足要求; 随后 low 进 1, 继续查找
                #    是否存在其它组合;
                if nums[low] + nums[high] < k:
                    count += high - low
                    low += 1
                # jy: 如果 nums[low] + nums[high] 大于 k, 则将 high 减 1;
                else:
                    high -= 1

        return count

nums = [-2, 0, 1, 3]
target = 2
# Output: 2
res = Solution().threeSumSmaller(nums, target)
print(res)


