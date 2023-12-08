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
title_jy = "Remove-K-Digits(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a non-negative integer ``num`` represented as a string, remove k digits from
the number so that the new number is the smallest possible.

Note:
The length of ``num`` is less than 10002 and will be ≥ k.
The given ``num`` does not contain any leading zero.


Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""

class Solution:
    """
遍历字符串, 将数字放入一个栈, 如果当前数字小于栈顶的元素, 则出栈;
    """
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        i, n = 0, len(num)

        while i < n:
            # jy: 如果当前数值 num[i] 小于栈顶元素, 则栈顶元素出栈, 出栈时 k 减 1, 表
            #    示已删除一个; (栈中的数值字符为最终有效的字符, 从左到右中, 如果有更
            #    小的字符可以替换掉栈顶, 则直接用更小的替换)
            while stack and num[i] < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        # jy: 如果经过以上循环后, k 值仍大于 0, 则从栈中再出 k 个元素;
        for _ in range(k):
            stack.pop()

        # jy: 经过以上操作后, 即删除了 k 个数值; 接下来要删除当前栈中的无效前缀 "0" (逻辑
        #    删除, 即跳过无效 "0" 前缀的下标即可)
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1

        return ''.join(stack[i:]) or '0'



num = "1432219"
k = 3
# Output: "1219"
res = Solution().removeKdigits(num, k)
print(res)


num = "1432239"
k = 3
# Output: "1219"
res = Solution().removeKdigits(num, k)
print(res)


num = "10200"
k = 1
# Output: "200"
res = Solution().removeKdigits(num, k)
print(res)


num = "10"
k = 2
# Output: "0"
res = Solution().removeKdigits(num, k)
print(res)


