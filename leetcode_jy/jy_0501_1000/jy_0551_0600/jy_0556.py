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
title_jy = "Next-Greater-Element-III(number)"
# jy: 记录不同解法思路的关键词
tag_jy = "理解题意后的技巧解法 | 参考 0031"


"""
Given a positive integer `n`, find the smallest integer which has exactly the
same digits existing in the integer `n` and is greater in value than `n`. If
no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a 
valid answer but it does not fit in 32-bit integer, return -1.


Example 1:
Input: n = 12
Output: 21

Example 2:
Input: n = 21
Output: -1


Constraints:
1 <= n <= 2^31 - 1
"""


class Solution:
    """
解法 1: 将数字转为数组, 然后从数组末尾开始从右到左找一段递增的子序列:
a) 如果子序列最后结束于数组开头 (即数值已经由数字高到低排序组成), 说明
   不可能找到更大的数字, 返回 -1; 可以以 n = 21 为例进行思考
b) 如果子序列最后结束于下标 i (i != 0), 则有 nums[i-1] < nums[i], 为了
   找到比当前数字大的数, 可以在递减的子序列 nums[i: len(nums)] (从右到
   左递增, 因此从左到右是递减) 中找到一个比 nums[i-1] 大的数中最小的数,
   将其和 nums[i-1] 互换, 最后反转 nums[i:len(nums)]; 可以以 12321 为例
   进行思考
    """
    def nextGreaterElement_v1(self, n: int) -> int:
        # jy: 将数字转为数组形式
        digits = list(str(n))
        # jy: 从数组末尾开始从右向左找到一段递增的子序列, 如果这段子序
        #     列最后结束于数组头, 直接返回 -1
        i = len(digits) - 1
        while i-1 >= 0 and digits[i] <= digits[i-1]:
            i -= 1
        if i == 0:
            return -1

        # jy: 当前下标位置 i (i > 0) 满足 digits[i-1] < digits[i]
        j = i
        # jy: 在递减的子序列 digits[i: len(digits)] 中找到比 digits[i-1]
        #     大的数中的最小值 digits[j], 将其与 digits[i-1] 交换, 交换
        #     后 digits[i:len(digits)] 仍为递减子序列, 将其进行倒序, 使得
        #     进一步缩小数字
        while j + 1 < len(digits) and digits[j+1] > digits[i-1]:
            j += 1
        digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1]

        # jy: 将结果列表拼接成数值
        result = int(''.join(digits))
        # jy: 如果结果小于 2^31, 则返回该结果, 否则返回 -1
        return result if result < 1 << 31 else -1


n = 12
# Output: 21
res = Solution().nextGreaterElement_v1(n)
print(res)

n = 121
# Output: 211
res = Solution().nextGreaterElement_v1(n)
print(res)

n = 12321
# Output: 13122
res = Solution().nextGreaterElement_v1(n)
print(res)

n = 21
# Output: -1
res = Solution().nextGreaterElement_v1(n)
print(res)


