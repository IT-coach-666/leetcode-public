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
title_jy = "Find-All-Duplicates-in-an-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array ``nums`` of length ``n`` where all the integers of ``nums`` are
in the range [1, n] and each integer appears once or twice, return an array of all the
integers that appears twice. You must write an algorithm that runs in O(n) time and uses
only constant extra space.


Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []


Constraints:
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""


from typing import List


class Solution:
    """
解法1: 使用 Set 保存遇到的数字
    """
    def findDuplicates_v1(self, nums: List[int]) -> List[int]:
        numbers = set()
        duplicates = []

        for n in nums:
            if n in numbers:
                duplicates.append(n)
            else:
                numbers.add(n)

        return duplicates

    """
解法2: 遍历数组, 如果当前数字不等于 i + 1, 说明当前数字可能不在正确的位置上, 继续
比较 nums[i] 和 nums[nums[i] - 1], 如果两者不同, 说明 nums[i] 没有放在正确的位置
上, 交换两者; 如果两者相同, 说明 nums[i] 重复
    """
    def findDuplicates_v2(self, nums: List[int]) -> List[int]:
        duplicates = set()
        n = len(nums)

        for i in range(n):
            while nums[i] != i + 1:
                j = nums[i] - 1

                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    duplicates.add(nums[i])

                    break

        return list(duplicates)


nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
res = Solution().findDuplicates_v1(nums)
print(res)


nums = [1,1,2]
# Output: [1]
res = Solution().findDuplicates_v1(nums)
print(res)


nums = [1]
# Output: []
res = Solution().findDuplicates_v1(nums)
print(res)


