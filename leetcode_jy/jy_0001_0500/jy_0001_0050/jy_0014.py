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
title_jy = "Longest-Common-Prefix(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "min 和 max 操作字符串的特性"



"""
Write a function to find the longest common prefix string amongst an array of
strings. If there is no common prefix, return an empty string "".


Example 1:
Input: strs = ["flower", "flow", "flight"]
Output: "fl"


Example 2:
Input: strs = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


class Solution:
    """
解法 1: 同等位置字符判断
    """
    def longestCommonPrefix_v1(self, strs: List[str]) -> str:
        # jy: 记录最长公共前缀
        common = ''

        # jy: 如果列表为空, 则返回空字符串; 如果列表只有一个字符串, 则返回该
        #     字符串
        if len(strs) < 1:
            return ''
        elif len(strs) == 1:
            return strs[0]

        # jy: 逐个遍历第一个字符串中的字符, 以该字符串为基础查找公共前缀 (因
        #     为公共前缀顶多也就与该字符串相同)
        for i, c in enumerate(strs[0]):
            is_common = True

            # jy: 遍历其它字符串, 判断该这些字符串中的下标为 i 的字符是否与字
            #     符 c 相同, 如果不同则直接退出 (需确保下标为 i 的字符存在)
            for text in strs[1:]:
                # jy: 如果下标为 i 的字符不存在或当前字符串为空, 则直接将
                #     is_common 设置为 False, 后续会直接终止循环并返回
                is_common = text and i < len(text) and text[i] == c
                # jy: 如果不是公共字符, 则跳出循环;
                if not is_common:
                    break
            # jy: 如果内循环中已经遍历到非公共字符, 则可以跳出外循环, 终止查找
            if is_common:
                common += c
            else:
                break

        return common

    """
解法 2: min 和 max 内置函数处理字符串时, 会基于字符的大小判断字符串的大小值; 
如果最大字符串与最小字符串首字符不相同, 则公共前缀子串为空串
    """
    def longestCommonPrefix_v2(self, strs: List[str]) -> str:
        if not strs: return ""
        str0 = min(strs)
        str1 = max(strs)
        #print(str0, " == ", str1)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0


strs = ["flower", "flow", "flight"]
# Output: "fl"
#res = Solution().longestCommonPrefix_v1(strs)
res = Solution().longestCommonPrefix_v2(strs)
print(res)


strs = ["dog", "racecar", "car"]
# Output: ""
res = Solution().longestCommonPrefix_v2(strs)
print(res)


