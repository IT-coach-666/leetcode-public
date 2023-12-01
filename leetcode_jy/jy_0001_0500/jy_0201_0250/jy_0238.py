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
title_jy = "Product-of-Array-Except-Self(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Example 1:
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Example 2:
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]


Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30


Follow up:
Could you solve it in O(n) time complexity and without using division?
Could you solve it with O(1) constant space complexity? (The output array does not count as extra space for
space complexity analysis.)
"""



from typing import List



class Solution:
    """
解法1(超时): 直接循环会导致超时;
    """
    def productExceptSelf_v1(self, nums: List[int]) -> List[int]:
        return [self._product(i, nums) for i in range(len(nums))]

    def _product(self, i, nums: List[int]) -> int:
        product = 1

        for j, n in enumerate(nums):
            if j != i:
                product *= n

        return product


    """
解法2: 事先求得所有数的乘积, 将总的乘积除以当前的数, 就是除了当前数之外的乘积; 注意需要处理数组
中 0 的个数的情况, 如果只有一个 0, 那么 0 所在位置的值就等于除了 0 外的所有数的乘积, 如果有 2 个
及以上的 0, 则所有位置的乘积都是 0;
    """
    def productExceptSelf_v2(self, nums: List[int]) -> List[int]:
        product = 1
        # jy: 记录 0 的个数;
        zeros = 0

        # jy: 统计 0 的个数, 以及除 0 之外其它数值的乘积;
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                product *= n
        # jy: 如果有一个 0, 则除了 0 所在位置对应的目标值为非零数的乘积外, 其它非 0 位置的目标值均为 0;
        if zeros == 1:
            return [0 if n != 0 else product for n in nums]
        # jy: 如果有两个 0, 则每个位置对应的目标值均为 0;
        elif zeros >= 2:
            return [0] * len(nums)
        # jy: 如果没有 0, 则每个位置对应的目标值为所有数乘积除以该位置的原来的值;
        else:
            return [product // n for n in nums]


    """
解法3: Follow up 中要求我们不能使用除法, 所以不能先求得所有数字的乘积; 额外创建两个数组, 数组中的每
一位的值为数组头到当前位置的所有数字的乘积, 即 a_i = nums[1] * nums[2] * ... * nums[i], 其中一个数组
从左往右计算, 另一个数组从右往左计算, 分别记为 L 和 R; 则对于最终结果中的数字 b_i, 它的值等于
(nums[1] * nums[2] * ... * nums[i-1]) * (nums[i+1] * ... * nums[n-1] * nums[n])
即: L[i-1] * R[len(nums) - i]

JY: 注意, 以上的解析说明中数组下标是以 1-based 的;
    """
    def productExceptSelf_v3(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        left_products = [1] * length
        right_products = [1] * length

        for i in range(length):
            # jy: left_products[i] 为数组前 i+1 个元素的乘积;
            left_products[i] = nums[i] if i == 0 else nums[i] * left_products[i-1]
            # jy: right_products[i] 为数组末尾 i+1 个元素的乘积;
            right_products[i] = nums[length - i-1] if i == 0 else nums[length - i-1] * right_products[i-1]

        for i in range(length):
            # jy: 如果 i 为 0, 则该位置的结果值为数组末尾 length - 1 个元素的乘积, 对应值为 right_products[length - 2]
            if i == 0:
                result[i] = right_products[length - i-2]
            # jy: 如果 i 为末尾下标, 则该位置的结果值为数组前 length -1 个元素的乘积, 对应值为 left_products[length - 2]
            elif i == length - 1:
                result[i] = left_products[i-1]
            # jy: 如果 i 非首尾下标, 则对应位置的结果值为数组前 i-1 个元素乘积, 再乘以包含 i+1 下标之后后的所有数值
            #    的乘积(即数组末尾 length - i-1 个元素的乘积, 即 right_products[length - i-2]);
            else:
                result[i] = left_products[i-1] * right_products[length - i-2]

        return result

    """
解法4: 更进一步, 题目中要求空间复杂度为 O(1), 所以除了最后返回的数组外, 不能创建其他的辅助数组;

遍历数组, 记 left 为从左往右至当前位置前所有数字的乘积(即不包含当前位置的前 i 个数值乘积), right
为从右往左至当前位置后所有数字的乘积(即不包含当前位置的后 i 个元素乘积), 记最终的数组为 result,
初始化所有值为 1;
更新 result[i] 为 result[i] * left
更新 result[i] 对称位置的数 (即 result[len(nums) - i-1] ) 为 result[len(nums) - i-1] * right

在 left 和 right 相遇前:
result[i] 的值等于 left
result[len(nums) - i-1] 的值等于 right

当 left 和 right 相遇以后(如以下代码的 for 循环中, i 为 0 与 i 为 length-1 时 left 与 right 相遇):
对于 result[i] 来说, 该位置的值已经不再是 1, 已经被 right 更新过, 所以此时的 result[i] * left 就
等于除了 nums[i] 以外的所有数的乘积; result[len(nums) - i-1] 同理;
    """
    def productExceptSelf_v4(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        left = right = 1

        for i in range(length):
            # jy: 每次 for 循环更新两个 result 的值, 两值的特点: 下标加和为数组长度(即下标之和为 length-1);
            #    且更新时都从首尾两端不断向另一端夹进, 使得一轮循环下来, 每个 result[j] 下标都会被更新两次,
            #    一次是乘以 j 左侧的数值的乘积, 另一次是乘以 j 右侧的数值的乘积; 使得一轮循环下来得到目标值;
            result[i] *= left
            result[length - i-1] *= right
            left *= nums[i]
            right *= nums[length - i-1]

        return result


nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
res = Solution().productExceptSelf_v1(nums)
print(res)

res = Solution().productExceptSelf_v3(nums)
print(res)

nums = [-1, 1, 0, -3, 3]
# Output: [0, 0, 9, 0, 0]
res = Solution().productExceptSelf_v2(nums)
print(res)


res = Solution().productExceptSelf_v3(nums)
print(res)


res = Solution().productExceptSelf_v4(nums)
print(res)


