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
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Integer-to-Roman(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "贪心 | 暴力"


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

For example, 2 is written as II in Roman numeral, just two one's added
together. 12 is written as XII, which is simply X + II. The number 27 
is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is 
written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. 

There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

 

Example 1:
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.


Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.


Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:
1 <= num <= 3999
"""

class Solution:
    """
解法 1: 贪心法则; 时间复杂度和空间复杂度均为 O(1)
每次尽量使用最大的数来表示; 比如对于 1994 这个数, 如果每次尽量用最大的数来表
示, 依次选 1000、900、90、4, 会得到正确结果 MCMXCIV

所以, 将哈希表按从大到小的顺序排列, 然后遍历哈希表, 直到表示完整个输入
    """
    def intToRoman_v1(self, num: int) -> str:
        # jy: 使用哈希表, 按照从大到小顺序排列
        hashmap = {1000:'M', 
                   900: 'CM',
                   500: 'D',
                   400: 'CD',
                   100: 'C',
                   90: 'XC',
                   50: 'L',
                   40: 'XL',
                   10: 'X',
                   9: 'IX',
                   5: 'V',
                   4: 'IV',
                   1: 'I'}
        res = ''
        # jy: 遍历字典中的 key
        for key in hashmap:
            if num // key != 0:
                # 比如输入 4000, 则 count 为 4
                count = num // key 
                res += hashmap[key] * count 
                num %= key
        return res


    """
解法 2: 暴力匹配; 时间复杂度和空间复杂度均为 O(1)
因为题目中说输入在 1 - 3999 的范围内, 所以把 1 到 9、10 到 90、100 到 900、
1000 到 3000 对应的罗马数字都表示出来, 最后对于任何输入, 需要做的就是把找
到的罗马数字组合起来即可; 比如输入是 2359, 找到 2000、300、50、9 对应的罗
马数字为 MM、CCC、L、IX, 组合后得到结果为 MMCCCLIX

该方法相当于牺牲了一部分空间复杂度换取了时间复杂度, 运行时间更快
    """
    def intToRoman_v2(self, num: int) -> str:
        # jy: 1000、2000、3000
        M = ["", "M", "MM", "MMM"] 
        # jy: 100 - 900
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        # jy: 10 - 90
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        # jy: 1 - 9
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]


num = 3
# jy: "III"
res = Solution().intToRoman_v1(num)
print(res)


num = 58
# jy: "LVIII"
res = Solution().intToRoman_v1(num)
print(res)


num = 1994
# jy: "MCMXCIV"
res = Solution().intToRoman_v2(num)
print(res)



