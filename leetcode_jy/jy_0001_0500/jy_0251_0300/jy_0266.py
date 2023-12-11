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
title_jy = "Palindrome-Permutation(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:
Input: "code"
Output: false

Example 2:
Input: "aab"
Output: true

Example 3:
Input: "carerac"
Output: true
"""




import collections



class Solution:
    """
解法1: 首先遍历字符串并使用一个 map 保存各字符出现的次数, 如果一个字符串可以组成回
文, 那么该字符串中字符出现次数要么都是偶数, 要么至多只有一个奇数;
    """
    def canPermutePalindrome_v1(self, s: str) -> bool:
        # jy: 统计字符串 s 中每个字符出现的次数;
        counts = collections.Counter(s)
        found_odd_count = False

        for key, value in counts.items():
            # jy: 如果字符 key 出现的次数是奇数次, 如果是第一次出现, 会
            #    将 found_odd_count 设置为 True; 如果后续再次出现奇数次
            #    字符, 则直接返回 False(即确保奇数次字符只能出现 1 次);
            if value & 1 == 1:
                if found_odd_count:
                    return False
                else:
                    found_odd_count = True

        return True



    """
解法2: 相比使用 map, 也可以使用 set 来保存出现的字符; 遍历字符串, 如果当前字符
不在 set 中, 则将其加入到 set 中, 否则从 set 中移除, 对于回文来说, 最后 set 要
么是空, 要么只有一个元素;
    """
    def canPermutePalindrome_v2(self, s: str) -> bool:
        chars = set()

        for c in s:
            if c in chars:
                chars.remove(c)
            else:
                chars.add(c)

        return len(chars) <= 1


s = "code"
# Output: false
res = Solution().canPermutePalindrome_v1(s)
print(res)

s =  "aab"
# Output: true
res = Solution().canPermutePalindrome_v1(s)
print(res)

s =  "carerac"
# Output: true
res = Solution().canPermutePalindrome_v2(s)
print(res)



