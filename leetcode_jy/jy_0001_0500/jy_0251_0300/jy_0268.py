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
title_jy = "Missing-Number(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
that is missing from the array.


Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?


Example 1:
Input: nums = [3, 0, 1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0, 3]. 2 is the missing number
             in the range since it does not appear in nums.

Example 2:
Input: nums = [0, 1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0, 2]. 2 is the missing number in
             the range since it does not appear in nums.

Example 3:
Input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0, 9]. 8 is the missing number in
             the range since it does not appear in nums.

Example 4:
Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the
             range since it does not appear in nums.


Constraints:
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.
"""



from typing import List



class Solution:
    """
解法1: 构造一个长度为 len(nums) + 1 的数组, 遍历 nums, 将数组中下标为 nums 的位置标记为 1, 最后数组
中为 0 的下标即缺少的数字;
    """
    def missingNumber_v1(self, nums: List[int]) -> int:
        digits = [0] * (len(nums) + 1)

        for n in nums:
            digits[n] = 1

        for i, n in enumerate(digits):
            if n == 0:
                return i


    """
解法2: 使用 Set 判断数字是否存在;
    """
    def missingNumber_v2(self, nums: List[int]) -> int:
        digits = set(nums)
        all_digits = set([i for i in range(len(nums) + 1)])

        for n in all_digits:
            if n not in digits:
                return n


    """
解法3: 前两种解法的时间和空间复杂度都是 O(n), 而 Follow up 中要求空间复杂度为 O(1); 因为只少了一个
数字, 所以求出 0 到 n 的和然后减去 nums 的和就是缺少的数;
    """
    def missingNumber_v3(self, nums: List[int]) -> int:
        n = len(nums)
        return (n + 1) * n // 2 - sum(nums)
        # return (n + n * (n-1) // 2) - sum(nums)



    """
解法4: 记数组的长度为 n, 遍历数组, 将下标和当前的数字与 n 进行异或, 最后 n 的结果就是缺少的数字;
因为在不缺少数字的情况下, [0, n] 个数字可以放在一个长度为 n+1 的数组中, 数组下标和对应位置的数字
组成的集合中, 每个数字都出现了两次, 而现在缺少了一个数字, 相当于在一堆数中找到只出现一次的数,
即 136_Single-Number.py;

jy: 异或运算的特点: 相同数值的异或运算为 0, 且异或运算符合;
    """
    def missingNumber_v4(self, nums: List[int]) -> int:
        result = len(nums)
        # jy: result 为 nums 的长度, 即数组中的最大数值;
        for i, n in enumerate(nums):
            result ^= i
            result ^= n

        return result


nums = [3, 0, 1]
# Output: 2
res = Solution().missingNumber_v1(nums)
print(res)

nums = [0, 1]
# Output: 2
res = Solution().missingNumber_v1(nums)
print(res)

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# Output: 8
res = Solution().missingNumber_v1(nums)
print(res)

nums = [0]
# Output: 1
res = Solution().missingNumber_v1(nums)
print(res)


