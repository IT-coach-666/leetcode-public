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
title_jy = "Longest-Uncommon-Subsequence-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of strings ``strs``, return the length of the longest uncommon
subsequence between them. If the longest uncommon subsequence does not exist,
return -1.

An uncommon subsequence between an array of strings is a string that is a
subsequence of one string but not the others. A subsequence of a string ``s``
is a string that can be obtained after deleting any number of characters from
``s``.  For example, "abc" is a subsequence of "aebdc" because you can delete
the underlined characters in "aebdc" to get "abc".   Other subsequences of
"aebdc" include "aebdc", "aeb", and "" (empty string).


Example 1:
Input: strs = ["aba","cdc","eae"]
Output: 3

Example 2:
Input: strs = ["aaa","aaa","aa"]
Output: -1


Constraints:
1 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] consists of lowercase English letters.
"""


from typing import List


class Solution:
    """
首先将字符串按照长度倒序排序, 然后遍历字符串, 判断当前字符串是否是其他字符串的
子串, 如果当前字符串不是其他任一字符串的子串, 则找到了最长的字符串
    """
    def findLUSlength(self, strs: List[str]) -> int:
        n = len(strs)
        # jy: 按字符串列表中的字符串长度进行倒序排序(长度越长的排越前面);
        strs = sorted(strs, key=lambda x: len(x), reverse=True)

        for i in range(n):
            # jy: miss_match_count 初始化为 0, 表示非当前字符串的子序列的个数;
            miss_match_count = 0

            for j in range(n):
                if i == j:
                    continue
                # jy: 判断当前字符串 strs[i] 是否是其它字符串 strs[j] 的子序列,
                #     如果不是, 则 miss_match_count 加 1;
                if not self._is_sub_sequence(strs[i], strs[j]):
                    miss_match_count += 1
                # jy: 补充如下 break 语句进行优化, 因为以上 if 判断如果不总是成立的
                #     话, miss_match_count 肯定是不等于 n - 1 的了, 没必要再进行下去;
                else:
                    break
            # jy: 如果当前字符串均不是其它字符串的子串, 则当前字符串的长度即为目标最长长度;
            if miss_match_count == n - 1:
                return len(strs[i])
        return -1

    def _is_sub_sequence(self, a, b):
        """
        判断字符串 a 是否是 b 的子序列;
        """
        i = 0
        n = len(a)
        for c in b:
            if i < n and c == a[i]:
                i += 1
        return i == n


strs = ["aba", "cdc", "eae"]
# Output: 3
res = Solution().findLUSlength(strs)
print(res)


strs = ["aaa", "aaa", "aa"]
# Output: -1
res = Solution().findLUSlength(strs)
print(res)



