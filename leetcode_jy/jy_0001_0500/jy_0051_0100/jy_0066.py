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
title_jy = "Plus-One(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "列表数值运算技巧"



"""
You are given a large integer represented as an integer array `digits`, where
each `digits[i]` is the i-th digit of the integer. The digits are ordered from
most significant to least significant in left-to-right order. The large integer
does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:
Input: digits = [1, 2, 3]
Output: [1, 2, 4]
Explanation: The array represents the integer 123.
             Incrementing by one gives 123 + 1 = 124.
             Thus, the result should be [1, 2, 4].

Example 2:
Input: digits = [4, 3, 2, 1]
Output: [4, 3, 2, 2]
Explanation: The array represents the integer 4321.
             Incrementing by one gives 4321 + 1 = 4322.
             Thus, the result should be [4, 3, 2, 2].

Example 3:
Input: digits = [9]
Output: [1, 0]
Explanation: The array represents the integer 9.
             Incrementing by one gives 9 + 1 = 10.
             Thus, the result should be [1, 0].
 

Constraints:
1) 1 <= digits.length <= 100
2) 0 <= digits[i] <= 9
3) digits does not contain any leading 0's.
"""


class Solution:
    """
解法 1: 从后往前加, 并结合最后的进位值判断是否要多加一位
    """
    def plusOne_v1(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        # jy: carry 用于记录进位, 初始化为 1 (因为最终目的是加 1)
        carry = 1
        i = len(digits) - 1
        # jy: 从后往前加, 在确保位有效, 且进位不为 0 时, 不断加和
        while i >= 0 and carry:
            current_sum = digits[i] + carry
            carry = current_sum // 10
            digits[i] = current_sum % 10
            i -= 1

        return digits if carry == 0 else [carry] + digits


    """
解法 2: 不需要数组的每一位都参与计算:
1) 如果当前数字小于 9, 则加 1 并不会发生进位, 将当前位加 1 后即可终止计算
2) 如果当前位为 9, 则将当前位置为 0, 产生的进位 1 将会加到下一位中
    """
    def plusOne_v2(self, digits: List[int]) -> List[int]:
        if not digits:
            return []

        # jy: 从后往前加, 如果需要进位, 直接加上进位即可
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        # jy: 如果以上代码逻辑均无返回, 则表明原数值均为 9, 全部均
        #     置为 0 后需要多补充一位最高位 1
        return [1] + digits


    """
解法 3: 参考 0369 (Plus-One-Linked-List) 中的解法 2 实现
    """
    def plusOne_v3(self, digits: List[int]) -> List[int]:
        # jy: 从低为开始往高位寻找, 找到第一个不为 9 的最高位
        last_not_9 = -1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                last_not_9 = i
                break

        # jy: 如果最低位不为 9, 则最低位加 1 即可
        if last_not_9 == len(digits)-1:
            digits[last_not_9] += 1
            return digits

        # jy: 如果所有位都为 9, 则增加一位最高位, 且其余位全置为 0
        if last_not_9 == -1:
            return [1] + [0] * len(digits)

        # jy: 在不为 9 的那一位加 1, 而后续的其余位全置为 0
        digits[last_not_9] += 1
        return digits[: last_not_9+1] + [0] * (len(digits) - last_not_9 - 1)



ls_ = [1, 2, 3]
res = Solution().plusOne_v1(ls_)
# jy: [1, 2, 4]
print(res)


ls_ = [4, 3, 2, 1]
res = Solution().plusOne_v2(ls_)
# jy: [4, 3, 2, 2]
print(res)


ls_ = [9]
res = Solution().plusOne_v2(ls_)
# jy: [1, 0]
print(res)

ls_ = [4, 3, 2, 1]
res = Solution().plusOne_v3(ls_)
# jy: [4, 3, 2, 2]
print(res)

