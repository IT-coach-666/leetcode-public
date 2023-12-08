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
title_jy = "Excel-Sheet-Column-Number(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...


Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
"""



class Solution:
    """
解法1: 即 26 进制运算;
    """
    def titleToNumber_v1(self, s: str) -> int:
        # jy: 够造字典, 将 A-Z 作为 key, 其对应的数值作为 value;
        letters = dict(zip([chr(x) for x in range(65, 91)], [x for x in range(1, 27)]))
        number = 0
        # jy: 从左到右遍历字母字符串, 先将左侧子串转换为对应的数值, 如果后续不断有字母字符
        #    被遍历到, 则将左侧的子串对应的数字乘以 26, 然后再加上新遍历的字符的对应数值
        #    即可;
        for c in s:
            number *= 26
            number += letters[c]

        return number

    def titleToNumber_2022_02_27(self, columnTitle: str) -> int:
        dict_ = {}
        for i in range(26):
            # jy: 65 对应字符 "A";
            dict_[chr(65 + i)] = i + 1

        res = 0
        for char in columnTitle:
            res = res * 26 + dict_[char]

        return res


s = "A"
# Output: 1
res = Solution().titleToNumber_v1(s)
print(res)


s = "AB"
# Output: 28
res = Solution().titleToNumber_v1(s)
print(res)


s = "ZY"
# Output: 701
res = Solution().titleToNumber_v1(s)
print(res)




