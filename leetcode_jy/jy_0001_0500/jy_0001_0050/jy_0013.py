# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
from typing import List
# jy: 记录该题的难度系数
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Roman-to-Integer(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "字典 mapping (需明确规则以及映射的优先顺序)"


"""
Roman numerals are represented by seven different symbols: 
I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added
together. Twelve is written as, XII, which is simply X + II. The number
twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is 
written as IV.  Because the one is before the five we subtract it making 
four. The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
1) I can be placed before V (5) and X (10) to make 4 and 9. 
2) X can be placed before L (50) and C (100) to make 40 and 90. 
3) C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be
within the range from 1 to 3999.


Example 1:
Input: "III"
Output: 3


Example 2:
Input: "IV"
Output: 4


Example 3:
Input: "IX"
Output: 9


Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.


Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution:
    """
将所有的罗马数字和阿拉伯数字的对应关系放到 Map 中, 遍历字符串, 先尝试获取当
前两个字符的罗马数字是否在 Map 中, 如果不在则只转换一个罗马数字
    """
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            # jy: 以下为 6 类特殊的形式;
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        i, n = 0, len(s)
        count = 0
        while i < n:
            # jy: 优先考虑两个字符组成的情况;
            if i+1 < n and romans.get(s[i] + s[i+1]):
                count += romans[s[i] + s[i+1]]
                i += 2
            else:
                count += romans[s[i]]
                i += 1
        return count


s = "III"
res = Solution().romanToInt(s)
print(s, " === ", res)

s = "IV"
res = Solution().romanToInt(s)
print(s, " === ", res)

s = "IX"
res = Solution().romanToInt(s)
print(s, " === ", res)

s = "LVIII"
res = Solution().romanToInt(s)
print(s, " === ", res)

s = "MCMXCIV"
res = Solution().romanToInt(s)
print(s, " === ", res)

