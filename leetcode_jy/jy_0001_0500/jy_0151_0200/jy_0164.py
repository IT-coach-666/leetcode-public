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
title_jy = "Maximum-Gap(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array `nums`, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:
Input: nums = [3, 6, 9, 1]
Output: 3
Explanation: The sorted form of the array is [1, 3, 6, 9], either (3, 6) or (6, 9) has the maximum difference 3.

Example 2:
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

Constraints:
1) 1 <= nums.length <= 10^5
2) 0 <= nums[i] <= 10^9
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/maximum-gap/solutions/498577/python3-tong-pai-xu-by-yanghk/
    """
    def maximumGap_v1(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        
        # 一些初始化
        max_ = max(nums)
        min_ = min(nums)
        max_gap = 0
        
        each_bucket_len = max(1,(max_-min_) // (len(nums)-1))
        buckets =[[] for _ in range((max_-min_) // each_bucket_len + 1)]
        
        # 把数字放入桶中
        for i in range(len(nums)):
            loc = (nums[i] - min_) // each_bucket_len
            buckets[loc].append(nums[i])
        
        # 遍历桶更新答案
        prev_max = float('inf')
        for i in range(len(buckets)):
            if buckets[i] and prev_max != float('inf'):
                max_gap = max(max_gap, min(buckets[i])-prev_max)
            
            if buckets[i]:
                prev_max = max(buckets[i])
                
        return max_gap

    
nums = [3, 6, 9, 1]
res = Solution().maximumGap_v1(nums)
# jy: 3
print(res)

    
nums = [10]
res = Solution().maximumGap_v1(nums)
# jy: 0
print(res)
