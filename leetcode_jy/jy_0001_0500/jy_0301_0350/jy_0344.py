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
title_jy = "Reverse-String(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place
with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]

Example 2:
Input: ["H", "a", "n", "n", "a", "h"]
Output: ["h", "a", "n", "n", "a", "H"]
"""


from typing import List


class Solution:
    """
解法1: 使用双指针法, low 和 high 分别指向数组的首尾, 交换 s[low] 和 s[high], 然后 low 向
右移动一位,  high 向左移动一位, 继续交换 s[low] 和 s[high], 直到 low >= high;
    """
    def reverseString_v1(self, s: List[str]) -> None:
        low, high = 0, len(s)-1

        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1


    """
解法2: 递归求解;
    """
    def reverseString_v2(self, s: List[str]) -> None:
        self._reverse(s, 0, len(s)-1)


    def _reverse(self, s, low, high):
        if low >= high:
            return

        s[low], s[high] = s[high], s[low]

        self._reverse(s, low+1, high-1)


s = ["h", "e", "l", "l", "o"]
# Output: ["o", "l", "l", "e", "h"]
Solution().reverseString_v1(s)
print(s)


s = ["H", "a", "n", "n", "a", "h"]
# Output: ["h", "a", "n", "n", "a", "H"]
Solution().reverseString_v1(s)
print(s)


