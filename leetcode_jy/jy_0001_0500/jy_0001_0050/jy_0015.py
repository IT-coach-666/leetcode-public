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
from typing import List
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "3Sum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "转换为两数之和 (参考 0001 和 0167)"




"""
Given an array nums of `n` integers, are there elements `a`, `b`, `c` in nums
such that `a + b + c = 0`? Find all unique triplets in the array which gives
the sum of zero. 

Note: The solution set must not contain duplicate triplets.
注意: 数值可以重用, 但组成的三元组不能相同


Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[ [-1, 0, 1],
  [-1, -1, 2]]
"""


class Solution:
    """
解法 1 (超时): a + b + c = 0 等价于 b + c = -a, 所以问题就转化为
0001_two-sum.py; 遍历数组, 判断其余的数组元素中是否存在两个数的和
为当前元素的相反数;

由于 Two sum 的时间复杂度是 O(n), 所以算上外层的循环三数之和的时间
复杂度为 O(n^2), 导致此题超时; 此外, 符合条件的三个数的组合不能重
复, 多了一步去重的工作, 也进一步加大了算法的时间复杂度
    """
    def threeSum_v1(self, nums: List[int]) -> List[List[int]]:
        sums = []
        # jy: 遍历列表中的元素
        for i, value in enumerate(nums):
            # jy: 从列表 nums 中找出两个值为 -value 的下标
            #     (下标为 i 的值不被考虑)
            two_sums = self._two_sum(nums, i, -value)
            # jy: 如果 two_sums 这样的值存在(可能存在多组), 则 3 数之
            #     和为 0 的组合存在
            if two_sums:
                # jy: 将下标转换为相应的数值列表, 并添加到 three_sums 列表中
                for two_sum in two_sums:
                    three_sum = [value] + two_sum
                    # jy: 判断 sums 组合列表中是否已经包含 three_sum 组合, 如
                    #     果包含则不再重复加入
                    if not self._has_three_sum(sums, three_sum):
                        sums.append(three_sum)
        return sums


    def _two_sum(self, nums: List[int], current_index: int,
                 target: int) -> List[List[int]]:
        """
        从列表 nums 中找出两个值为 target 的下标, 并确保找到的二元组不重复 
        (查找过程中忽略下标为 current_index 的值)
        """
        mapping = {}
        two_sums = []
        # jy: 用于记录已获取的数值, 便于去重
        set_done = set()
        for i, value in enumerate(nums):
            if i == current_index:
                continue

            if target - value in mapping and value not in set_done:
                two_sums.append([target - value, value])
                set_done.add(value)
                set_done.add(target - value)
            else:
                mapping[value] = i
        return two_sums


    def _has_three_sum(self, three_sums: List[List[int]],
                       three_sum: List[int]) -> bool:
        """
        判断 three_sums 的组合列表中是否已经包含 three_sum 组合
        """
        for sum_ in three_sums:
            #if sorted(sum_) == sorted(three_sum):
            if set(sum_) == set(three_sum):
                return True
        return False


    """
解法 2: 也是将问题转化为 Tow Sum, 只是求解时不再使用 Map 而是同 
167_two-sum-II_input-array-is-sorted.py, 先将数组排序, 然后遍历
数组, 在当前元素之后的数中使用双指针查询和为当前元素的相反数的两
个数; 需要注意以下几点: 
1) 外层遍历数组时, 如果当前元素值大于 0, 则可以直接退出循环, 因为数组
   是有序排列, 当前元素后的数必然也是大于 0, 不可能存在三数之和为 0
2) 如果当前元素的值和前一个元素的值相同, 则直接跳过当前元素, 因为最终
   的三元组不能重复 (如果当前元素符合条件则在上一轮操作时已包含了这个数)
3) 使用双指针遍历处理 Two Sum 时同理, 如果指针的下一个元素的值同当前元
   素, 则跳过下一个元素
4) 对于外层循环下标为 i 的元素来说, 为什么双指针处理只需要查找 [k+1, L-1]
   区间 (L 为数组的长度) 的元素即可? 因为假设存在满足条件的结果集中有一个
   元素的下标小于 k, 记为 k', 则这个组合已经在外层循环到 k' 时就已经找到
   了这个组合, 所以无需再次处理

涉及到的排序算法最好能自己实现
    """
    def threeSum_v2(self, nums: List[int]) -> List[List[int]]:
        # jy: 对数组进行排序
        nums.sort()
        sums = []
        # jy: 不断遍历列表中的元素, 找出 nums[i+1: ] 中与 nums[i] 能组合成
        #     3 数为 0 的所有组合 (双指针法查找)
        for i in range(0, len(nums)-2):
            # jy: 3 数之和为 0, 必定以负数开始; 由于数组已经排序, 因此当遍
            #     历至大于 0 的数值时, 即可终止 (等于 0 时不能终止, 因为可
            #     能后续有两个数为 0, 此时三个 0 也能满足条件)
            if nums[i] > 0:
                break

            # jy: 如果当前数值与前一个数值相同, 则跳过; 因为如果当前数值与
            #     之后的数值能组成满足要求的一组数, 则在遍历上一个数值时就
            #     都已经找到相应的组合了 (不管遍历上一个数值时是否包含该相
            #     同的数值), 避免重复查找
            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue

            # jy: target 为剩余两数之和; 剩余两数从 i+1 到 len(nums)-1 的
            #     下标中找 (双指针即初始化为这两个下标)
            target = - nums[i]
            low, high = i+1, len(nums)-1
            while low < high:
                # jy: 如果两值相等, 则将符合要求的 3 数列表加入 sums 列表组合中
                if nums[low] + nums[high] == target:
                    sums.append([- target, nums[low], nums[high]])

                    # jy: 跳过相同的数值, 避免重复计算
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1

                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < target:
                    low += 1
                else:
                    high -= 1
        return sums



nums = [-1, 0, 1, 2, -1, -4]
res = Solution().threeSum_v1(nums)
print(nums, " === ", res)

nums = [-1, 0, 1, 2, -1, -4]
res = Solution().threeSum_v2(nums)
print(nums, " === ", res)


