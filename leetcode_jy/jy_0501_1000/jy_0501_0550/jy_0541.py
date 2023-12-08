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
title_jy = "Reverse-String-II(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string and an integer k, you need to reverse the first k characters for every 2k
characters counting from the start of the string.
1) If there are less than k characters left, reverse all of them.
2) If there are less than 2k but greater than or equal to k characters, then reverse the
   first k characters and left the other as original.


Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"


Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""



class Solution:
    """
344_Reverse-String.py 的变种, 由原来的反转整个字符串变为对每 2k 个字符反转前 k 个字符;
首先根据 2k 建立一个循环, 即当前字符串根据 2k 可以分为几段, 然后针对每一段对前 k 个字
符进行反转即可;
    """
    def reverseStr(self, s: str, k: int) -> str:
        # jy: 字符串不支持通过下标赋值, 故转换为数组形式;
        chars = list(s)
        # jy: i 为 [0, 2*k, 4*k] (即每 2k 一次遍历)
        for i in range(0, len(chars), 2 * k):
            # jy: 由于 k 代表个数, 转为下标时要减 1; 如果最后一个字符的下标小
            #    于 i+k-1, 则将 high 设置为最后一个字符的下标;
            low, high = i, min(i+k-1, len(chars) - 1)
            # jy: 高低位互换;
            while low < high:
                chars[low], chars[high] = chars[high], chars[low]
                low += 1
                high -= 1

        return ''.join(chars)


s = "abcdefg"
k = 2
# Output: "bacdfeg"
res = Solution().reverseStr(s, k)
print(res)


