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
tag_jy = ""



"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one
to the integer. The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contains a single digit. You may assume the integer
does not contain any leading zero, except the number 0 itself.


Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]


Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
"""


from typing import List


class Solution:
    """
解法1: 从后往前加, 最后判断进位;
    """
    def plusOne_v1(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        # jy: carry 初始化为 1, 因为最终目的是加 1;
        carry = 1
        # jy: 此处的 new_digits 可去掉, 并将后续的 new_digits 换成 digits, 可节省内存;
        new_digits = [0] * len(digits)
        # jy: 从后往前加, 如果需要进位, 直接加上进位即可;
        for i in range(len(digits)-1, -1, -1):
            current_sum = digits[i] + carry
            carry = current_sum // 10
            new_digits[i] = current_sum % 10

        return new_digits if carry == 0 else [carry] + new_digits


    """
解法2: 其实并不需要数组的每一位都参与计算, 只要当前数字小于 9, 则加 1 并不会发生进位; 将当前
位加 1 后即可终止计算; 如果当前位为 9, 则将当前位置为 0, 产生进位 1, 相当于对剩下的数字加 1;
    """
    def plusOne_v2(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        # jy: 从后往前加, 如果需要进位, 直接加上进位即可;
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1

                return digits

            digits[i] = 0
        # jy: 如果以上代码逻辑均无返回, 则表明原数值均为 9, 全部均置为 0 后需要进 1;
        return [1] + digits


    def plusOne_v3(self, digits: List[int]) -> List[int]:
        """参考 369_Plus-One-Linked-List.py 中的解法 2 进行实现"""
        last_not_9 = -1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                last_not_9 = i
                break

        if last_not_9 == len(digits)-1:
            digits[last_not_9] += 1
            return digits
        elif last_not_9 == -1:
            return [1] + [0] * len(digits)
        else:
            digits[last_not_9] += 1
            return digits[: last_not_9+1] + [0] * (len(digits) - last_not_9 - 1)


ls_ = [1, 2, 3]
# Output: [1, 2, 4]
res = Solution().plusOne_v1(ls_)
print(res)


ls_ = [4,3,2,1]
res = Solution().plusOne_v2(ls_)
print(res)


ls_ = [0]
# Output: [1]
res = Solution().plusOne_v2(ls_)
print(res)

ls_ = [4,3,2,1]
res = Solution().plusOne_v3(ls_)


