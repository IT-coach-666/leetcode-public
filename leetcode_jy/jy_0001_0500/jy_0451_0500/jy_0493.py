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
title_jy = "Reverse-Pairs(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array nums, return the number of reverse pairs in the array.
A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].


Example 1:
Input: nums = [1,3,2,3,1]
Output: 2

Example 2:
Input: nums = [2,4,3,5,1]
Output: 3


Constraints:
1 <= nums.length <= 5 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""


from typing import List


class Solution:
    """
类似 315_Count-of-Smaller-Numbers-After-Self.py, 使用归并排序将数组从小到大排序,
在合并时, 由于左右两部分都是排好序的, 如果当前左半部分的数大于当前右半部分的数的
两倍, 则更新个数;
    """
    def reversePairs(self, nums: List[int]) -> int:
        # jy: count 其实只需要是个数值即可, 此处将其用一个元素的数组表示, 是为了在
        #    递归方法的调用中更新值后保留最新更新的结果;
        count = [0]
        # jy: 递归调用(分治算法, 分而治之), 该方法返回的是一个排好序后的数组;
        jy_res = self._divide(nums, count)
        # print("jy_res============== ", jy_res)
        # print("count=============== ", count)
        return count[0]


    def _divide(self, nums, count):
        '''
        传入的 count 参数为含有一个值的列表, 该值代表最目标结果的数量
        '''
        # jy: 如果列表中只有一个值, 表明有序, 直接返回;
        if len(nums) <= 1:
            return nums

        # jy: 分半递归分治; 左半部分进行递归时, 会对原始的数组的左半部分进行递归归并排序, 排序
        #    过程中会在左半部分范围中统计符合目标要求的 count 数; 右半部分同理, 会在右半部分中
        #    统计符合目标要求的 count 数, 且左半部分内与右半部分内的情况数肯定都不重复, 最后当
        #    左半部分和右半部分均统计完之后, 返回左半部分有序数组以及右半部分有序数组, 接着统计
        #    左半部分有序数组中找出 num[i], 右半部分有序数组中找出 nums[j], 统计满足情况的数量
        #    更新到 count 中(由于之前的左半部分, 右半部分中统计时, 满足要求的 nums[i] 和 nums[j]
        #    均在左半侧, 右半侧, 而此时的 nums[i] 在左半侧, nums[j] 在右半侧, 故肯定也不与之前的
        #    统计结果重复);
        middle = len(nums) // 2
        left = self._divide(nums[:middle], count)
        # print("left=====", left)
        right = self._divide(nums[middle:], count)
        # print("right====", right)
        # jy: left 和 right 均为有序列表; count 为目标结果的数量, 在 _conquer 方法中更新;
        return self._conquer(left, right, count)


    def _conquer(self, left, right, count):
        """
        对两个有序数组 left 和 right 进行整合, 整合成一个新的有序数组并返回; count 则是一
        个只含有一个元素的列表, 该元素值记录符合目标要求的情况数;
        """
        count[0] += self._count(left, right)

        sorted_nums = []
        i = j = 0
        # jy: 对两个有序数组进行整合, 整合成为一个新的有序数组并返回;
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_nums.append(left[i])
                i += 1
            else:
                sorted_nums.append(right[j])
                j += 1
        sorted_nums.extend(left[i:] or right[j:])

        return sorted_nums


    def _count(self, left, right):
        """
        判断 left 和 right 有序列表中, 符合要求的目标结果数;
        """
        i = j = 0
        count = 0

        while i < len(left) and j < len(right):
            # jy: 由于 left 和 right 均为有序数组, 如果当前的 left[i] 和 right[j] 满足条
            #    件, 则下标 i 以及之后的元素(共 len(left)-i 个)均能与 right[j] 满足条件,
            #    此时 count 数加上 len(left)-i, 并更新 j 为下一个值;  如果当前 left[i] 和
            #    right[j] 不能满足条件, 则表明 left[i] 还太小了, 将 i 后移后继续判断;
            # if left[i] / 2 > right[j]:
            if left[i] > 2 * right[j]:
                count += len(left) - i
                j += 1
            else:
                i += 1

        return count

    """
JY: 超时
    """
    def reversePairs_jy(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    count += 1
        return count



nums = [1,3,2,3,1]
# Output: 2
res = Solution().reversePairs(nums)
print(res)

res = Solution().reversePairs_jy(nums)
print(res)


nums = [2,4,3,5,1]
# Output: 3
res = Solution().reversePairs(nums)
print(res)

res = Solution().reversePairs_jy(nums)
print(res)


