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
title_jy = "two-sum-II__input-array-is-sorted(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers that is already sorted in ascending order, find two
numbers such that they add up to a specific target number. The function twoSum
should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.


Note:
• Your returned answers (both index1 and index2) are not zero-based.
• You may assume that each input would have exactly one solution and
  you may not use the same element twice.


Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""



from typing import List
class Solution:
    """
解法1: 001_two-sum 的第一个变种, 数组变成了按照从小到大排列的有序数组; 在有序数组
中查找元素容易想到使用二分查找, 从而可以遍历数组, 对于数组中的每一个元素 n, 利用二
分查找判断 target-n 是否在 n 之后的元素中, 算法复杂度为 O(nlg(n)); 相比于 001_two-sum
中结合哈希表的无序数组时的复杂度 O(n) 来说明显更慢了;

实际的代码中做了个优化, 对于下标为 i 的数组元素, 对 nums[i+1], nums[i+2], ... nums[n] 进
行二分查找, 找到使得 nums[j] >= target - nums[i] 的最小下标 j:
1) 如果该下标 j 最终是满足要求的(即 nums[j] == target - nums[i]), 则返回 [i+1, j+1] 即为正确结果;
2) 如果该下标 j 不满足要求(即 nums[j] > target - nums[i]), 则 j 之后的数肯定是不满足要求的了(因
   为数组是升序的, 后面的数只会更大, 离要找的目标值只会差距更大了); 此时, 进入下一轮循环(即 i+1),
   且下一轮循环的查找范围缩小为 nums[i+2], nums[i+3], ... nums[j], 因为数组是升序的, nums[i+1] 肯
   定是大于或等于 nums[i] 的值, 此时需要找一个更小的值才能使得相加等于 target, 故没必要再查找
   比 nums[j] 还大的值了;
    """
    # Time complexity: O(nlgn)
    def twoSum_v1(self, nums: List[int], target: int) -> List[int]:
        high = len(nums) - 1
        for index, value in enumerate(nums):
            # jy: 在 nums[index+1, high] 中找大于或等于 target-value 值的值对应的最小下标;
            # Find the minimum index j such that nums[j] >= target-value for all x in [j, len(nums)-1]
            j = self._binary_search(nums, index + 1, high, target - value)
            # jy: 当找不到符合要求的最小下标时, 直接进行下一轮循环(由于下一轮循环 index 会增 1, 对
            #    应的 value 也会变大(因为是升序数组), 此时 target-value 值会更小, 因此原先找不到符
            #    合要求的值, 在新一轮循环中是可能可以找到的)
            if j == -1:
                continue
            # jy: 如果找到的下标 j 正好满足: nums[index] + nums[j] == target, 则下标值均加 1 后返回(因为
            #    要求返回的下标是 "not zero-based" 的)
            if value + nums[j] == target:
                return [index+1, j+1]
            # jy: 如果此次找到的下标 j 不符合要求, 即 nums[index] + nums[j] > target, 则进行下一轮查找;
            #    由于下一轮查找时新的 nums[index] 会更大, 为了找到符合要求的新 j, 则 j 应该要比原先找到
            #    的更小了(因为数组是升序的), 此时将查找范围缩小到不大于原来找的的 j, 即通过 high = j 控
            #    制查找范围;
            high = j
        return [-1, -1]

    def _binary_search(self, nums: List[int], low: int, high: int, target: int) -> int:
        """
        二分查找: 从有序数组 nums[low: high+1] 中找大于或等于 target 值的值的对应最小下标;
        """
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            # jy: 如果 nums[middle] 小于 target, 则 low 设置为 middle+1, 进行下一轮查找;
            elif nums[middle] < target:
                low = middle + 1
            # jy:【trick】经过以上判断后如果没有返回, 可知 nums[middle] > target, 但不能确定
            #    此时的 middle 是否是满足该要求的最小下标, 因此要对 middle 的前一个下标进行
            #    判断分析: 如果其前一个下标大于等于 low, 且对应值也大于 target, 则 high 应向
            #    左移动 1 位后进如下一轮循环判断;
            elif middle-1 >= low and nums[middle-1] >= target:
                high = middle-1
            # jy: 如果执行到此处对应的逻辑, 表明 nums[middle] > target, 且 middle 的前一个下标
            #    不满足要求, 表明 middle 就是符合要求的最小下标;
            else:
                return middle
        # jy: 当找不到符合要求的结果时(例如, 假设 nums[low: high+1] 为 [1, 2, 3, 4], target 为
        #    5, 此时找不到符合要求的最小下标), 返回 -1;
        return -1


    """
解法2: 要达到 O(n) 复杂度, 可以使用双指针法: 左指针 i 指向数组的第一个元素, 同时向右移动, 右指
针 j 指向数组的最后一个元素, 同时向左移动, 直到两个指针相遇;

在移动的过程中, 判断 nums[i] + nums[j] 是否等于 target:
1) 如果是, 则返回 [i+1, j+1]
2) 如果 nums[i] + nums[j] > target, 说明两数之和过大, 则将 j 向左移动一位;
3) 如果 nums[i] + nums[j] < target, 说明两数之和过小, 则将 i 向右移动一位;

问题: 当 nums[i] + nums[j] > target 的时候, 为了减小两数之和, 既可以将 i 左移一位, 也可以将 j 左
      移一位, 为什么选择左移 j 而不是 i ?
因为一开始, i 和 j 分别指向数组的首尾, 只能各自向一端移动(确保搜索范围不断缩小);

算法开始时会连续移动 i 或连续移动 j, 在出现 nums[i] + nums[j] > target 之前(即: nums[i] + nums[j] < target 时),
必然是连续移动了 i(因为双指针的 j 最开始是数组的最后一个元素, 如果最后一个元素都不满足要求, 则向左移动该
元素只会使得 nums[j] 为更小的元素, 更不能满足要求, 因此需要左指针 i 处右移, 使得值更大些, 才有满足要求的
可能), 当 nums[i] + nums[j] > target 时 i 停止移动(开始移动 j);
    """
    def twoSum_v2(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            current_sum = nums[i] + nums[j]
            if current_sum == target:
                return [i+1, j+1]
            elif current_sum > target:
                j -= 1
            else:
                i += 1
        return [-1, -1]



nums = [2,7,11,15]
target = 9
res = Solution().twoSum_v1(nums, target)
print(nums, " === ", target, " === ", res)


res = Solution().twoSum_v2(nums, target)
print(nums, " === ", target, " === ", res)


