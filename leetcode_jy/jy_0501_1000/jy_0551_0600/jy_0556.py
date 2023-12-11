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
tag_jy = ""


"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing
in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it
does not fit in 32-bit integer, return -1.


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
首先将数字转为数组, 然后从数组尾开始向左侧找到一段递增的子序列, 如果这段子序列最后结束于数组
头(即数值已经由数字高到低排序组成), 说明不可能找到更小的数字, 返回 -1; 否则记当前子序列的起始
位置为 i, 则有 nums[i-1] < nums[i], 为了找到比当前数字小的数, 可以在递减的子序列 nums[i:len(nums)]
中找到一个比 nums[i-1] 大的数中最小的数, 将其和 nums[i-1] 互换, 最后反转 nums[i:len(nums], 进
一步缩小数字;
    """
    def nextGreaterElement(self, n: int) -> int:
        # jy: 将数字转为数组形式;
        digits = list(str(n))
        # jy: 从数组尾开始向左侧找到一段递增的子序列, 如果这段子序列最后结束于数组头, 直接返回 -1;
        i = len(digits) - 1
        while i-1 >= 0 and digits[i] <= digits[i-1]:
            i -= 1
        if i == 0:
            return -1

        # jy: 否则记当前子序列的起始位置为 i (i > 0), 有 digits[i-1] < digits[i];
        j = i
        # jy: 在递减的子序列 digits[i:len(digits)] 中找到比 digits[i-1] 大的数中的最小值 digits[j],
        #    将其与 digits[i-1] 交换, 交换后 digits[i:len(digits)] 仍为递减子序列, 将其进行倒序,
        #    使得进一步缩小数字;
        while j + 1 < len(digits) and digits[j+1] > digits[i-1]:
            j += 1

        digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1]
        # jy: 将结果列表拼接成数值;
        result = int(''.join(digits))
        # jy: 如果结果小于 2^31, 则返回该结果, 否则返回 -1;
        return result if result < 1 << 31 else -1


n = 12
# Output: 21
res = Solution().nextGreaterElement(n)
print(res)

n = 12321
# Output: 21
res = Solution().nextGreaterElement(n)
print(res)

n = 21
# Output: -1
res = Solution().nextGreaterElement(n)
print(res)


