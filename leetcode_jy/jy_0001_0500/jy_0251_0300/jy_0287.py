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
title_jy = "Find-the-Duplicate-Number(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers nums containing n+1 integers where each integer is in
the range [1, n] inclusive. There is only one repeated number in nums, return this 
repeated number.



Example 1:
Input: nums = [1, 3, 4, 2, 2]
Output: 2

Example 2:
Input: nums = [3, 1, 3, 4, 2]
Output: 3

Example 3:
Input: nums = [1, 1]
Output: 1

Example 4:
Input: nums = [1, 1, 2]
Output: 1



Constraints:
2 <= n <= 3 * 10^4
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.



Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n^2)?
"""


import collections

from typing import List



class Solution:
    """
解法1: 使用 Map 记录每个数字出现的次数, 然后遍历 Map 返回出现次数大于 1 的数, 算
法的时间和空间复杂度都是 O(n);
    """
    def findDuplicate_v1(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)

        for key, value in counts.items():
            if value > 1:
                return key



    """
解法2: 在 [1, n] 这个区间进行二分查找, 找到中间值后再遍历 nums, 计算出小于等于
middle 的个数 count:
1) 如果 count > middle, 说明 [1, middle] 区间有大于 middle 数, 即该区间存在重
   复的数字, high 移动到 middle;
2) 如果 count <= middle, 因为有 n+1-count 个数在 [middle + 1, n] 区间, 而
   n+1-count >= n+1-middle > n-middle,  n - middle 为 [middle + 1, n] 区间的大小, 所以该区
   间内存在重复的数字, 此时 low 移动到 middle + 1, 当循环终止即 low == high 时, 说明找到了
   重复的数;
    """
    def findDuplicate_v2(self, nums: List[int]) -> int:
        low, high = 1, len(nums)-1

        while low < high:
            # jy: 找出 [1, n] 的中间值;
            middle = low + (high - low) // 2
            count = 0
            # jy: 遍历数组, 统计小于等于 middle 的个数;
            for n in nums:
                if n <= middle:
                    count += 1
            # jy: 如果 count > middle, 说明 [1, middle] 区间有大于 middle 数, 即该区间
            #    存在重复的数字, high 移动到 middle;
            if count > middle:
                high = middle
            # jy: 如果 count <= middle, 则 [middle + 1, n] 区间有重复的数字, low 移动到
            #    middle + 1
            else:
                low = middle + 1

        return low


    """
解法3: 遍历数组, 将以当前数字的绝对值为下标的数字取反, 对于重复的数字来说, 在取反前, 该
位置的数字就是负数了, 说明该数字重复;
    """
    def findDuplicate_v3(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = abs(nums[i])

            if nums[n] < 0:
                return n

            nums[n] = -nums[n]


    """
解法4: 将数组的每一个元素看作是单链表中的节点, 对于 nums[i] 来说, 它的 next 指针就
是 nums[nums[i]], 因为存在重复的数字, 所以单链表必然有环, 环的起始点就是重复的数字;

题目就演变成了 142_Linked-List-Cycle-II.py, 例如对于数组 [1, 2, 1] , 它形成的有环单
链表为: 图见: https://www.yuque.com/frederick/dtwi9g/zwv7pq
    """
    def findDuplicate_v4(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast

"""
Follow up:
How can we prove that at least one duplicate number must exist in nums?
数组中每个元素的值的范围是 [1, n], 而数组的长度是 n+1, 那必然至少有一个数字是重复的;
"""

nums = [1, 3, 4, 2, 2]
# Output: 2
res = Solution().findDuplicate_v1(nums)
print(res)


nums = [3, 1, 3, 4, 2]
# Output: 3
res = Solution().findDuplicate_v2(nums)
print(res)


nums = [1, 1]
# Output: 1
res = Solution().findDuplicate_v3(nums)
print(res)


nums = [1, 1, 2]
# Output: 1
res = Solution().findDuplicate_v4(nums)
print(res)


