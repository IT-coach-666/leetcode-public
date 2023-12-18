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
title_jy = "First-Missing-Positive(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "数值存储技巧 | 数值打标签技巧"


"""
Given an unsorted integer array `nums`, return the smallest missing positive
integer. You must implement an algorithm that runs in O(n) time and uses
constant extra space.


Example 1:
Input: nums = [1, 2, 0]
Output: 3

Example 2:
Input: nums = [3, 4, -1, 1]
Output: 2

Example 3:
Input: nums = [7, 8, 9, 11, 12]
Output: 1


Constraints:
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""



class Solution:
    """
解法 1: 数值存储技巧

数组的长度为 n, 则数组中共有 n 个数, 则缺失的最小正整数肯定是在 1 到 n+1 之
间; 因此可将数值范围属于 1 到 n 的数值, 放置到其对应的下标中 (假设数值为 x,
则其下标为 x-1), 则 1 至 n 的数值对应的下标为 0 至 n-1, 如果对应的下标与对应
的值没匹配, 则该值即为缺失值


注意: nums[i] 和 nums[nums[i] - 1] 交换
不能写成: nums[i], nums[nums[i] - 1]  = nums[nums[i] - 1], nums[i]
因为 python 在这个过程中会先计算右边的值 nums[i] 和 nums[nums[i] - 1], 然后
将他们赋值给一个临时元祖, 然后按顺序赋值给左边; 即会先修改 nums[i] 的值, 这
样一来 nums[i] - 1 就不是原来想要修改的下标了

应写成: nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

谨慎起见, 最好引入第三方变量进行数值交换
    """
    def firstMissingPositive_v1(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # jy: 遍历列表, 将列表中范围为 1 到 n 的数值放到其规定的下标, 随
            #     后即可通过判断数值下标与其数值是否匹配, 判断该数值是否缺失
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # jy: 将当前下标为 i 的值 nums[i] 与下标为 nums[i] - 1 的值
                #     nums[nums[i] - 1] 进行交换, 使得值为 n 的数值存放在列
                #     表的下标位置为 n-1
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp

        # jy: 从第一个下标位置开始遍历列表数值, 如果下标为 i 的数值不等于 i+1,
        #     则表明 i+1 为缺省的最小正整数
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


    """
解法 2: 两次遍历列表中的元素, 对元素进行打标签

1) 先将列表中的元素, 将其中值为 0 或负值的部分更新为一个较大值, 如 n+1 (也
   可以无限大, 只要不在 [1, n] 范围内的正数即可)
2) 再次遍历 nums 中的元素, 当数值在 1 至 n 的范围内时, 表明碰到了有效数值,
   假设该数值为 x, 此时将下标为 x-1 的位置的值打负号标签, 当所有数值都遍历
   完成后, 就可以基于负号标签判断下标为 i 的对应值 i+1 是否存在
    """
    def firstMissingPositive_v2(self, nums: List[int]) -> int:
        n = len(nums)
        # jy: 往列表中添加一个较大值, 如 n+1 (只要比 n 大即可, 也可以无限
        #     大), 使得 nums 列表的最大下标为 n; 确保后续如果列表中所有数
        #     值都是 1 至 n 的有效数值 (在后面逻辑都会打上标签), 最终结果
        #     也能返回最后一个下标位置的基础上加 1, 即 n+1
        nums.append(n + 1)
        # jy: 将所有非正数 (负数和 0) 均改为 n+1 (只要比 n 大即可, 也可以
        #     无限大, 因为后续比 n 大的数值都会忽略不处理), 使得 nums 中均
        #     为值大于 1 的正数值
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # jy: 再次遍历 nums 中的数值 (均为大于 1 的正数, 因为原先的负数
        #     和 0 均被更新为 n+1), 如果数值 num 在 [1, n] 范围内, 则将
        #     下标为 num-1 的数值打上负号标签, 使得后续可以基于下标对应
        #     的值是否有负号标签, 来判断列表中是否有 "下标+1" 的值存在 
        # jy: 注意, 虽然以上确保了 nums 中的值均为正, 但此处的 for 循环
        #     中当指定范围下标的对应值在 [1, n] 这个范围时, 则会基于该值
        #     作为下标打上标签 (对原数值进行取反)
        for num in nums:
            # jy: num 可能会在后续中被打上标签 (数值为负), 此处取 num 在
            #     后续要作为下标, 因此需要进行绝对值处理
            x = abs(num)
            # jy: 如果 x <= n, 则表明 x 范围为 [1, n], 此时将下标为 x - 1 的
            #     数值打上负号标签 (注意: 不是取反, 是打负号标签; 如果原先下
            #     标为 x-1 的数值就有负号标签了, 也不会再将负号标签去除)
            if x <= n:
                nums[x-1] = - abs(nums[x-1])

        # jy: 从下标为 0 的位置开始遍历数组, 如果数组中下标位置为 i 的值没有
        #     负号标签, 表明之前遍历数组时没碰到值为 i+1 的正数, 因此直接返回
        for i, x in enumerate(nums):
            if x > 0:
                return i + 1


    """
解法 3: 排序后横向搜索, 时间复杂度 O(n logn)

由于引入排序, 导致时间复杂度不符合要求
    """
    def firstMissingPositive_v3(self, nums: List[int]) -> int:
        nums = list(sorted(set(nums)))
        j, k = 0, 1
        
        if nums[len(nums)-1] <= 0:
            return 1
        while nums[j] <= 0:
            j += 1
        for i in range(j, len(nums)):
            if nums[i] != k:
                return k
            k += 1
        return k
            



nums = [1, 2, 0]
# Output: 3
res = Solution().firstMissingPositive_v1(nums)
print(res)


nums = [3, 4, -1, 1]
# Output: 2
res = Solution().firstMissingPositive_v1(nums)
print(res)


nums = [7, 8, 9, 11, 12]
# Output: 1
res = Solution().firstMissingPositive_v1(nums)
print(res)


nums = [3, 4, -1, 1]
# Output: 2
res = Solution().firstMissingPositive_v2(nums)
print(res)


nums = [3, 4, -1, 1]
# Output: 2
res = Solution().firstMissingPositive_v3(nums)
print(res)

