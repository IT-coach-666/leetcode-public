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
title_jy = "Valid-Anagram(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two strings s and t , write a function to determine if t is an anagram of s.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


Note: You may assume the string contains only lowercase alphabets.

Follow up: What if the inputs contain unicode characters? How would you adapt your
           solution to such case?
"""


class Solution:
    """
首先遍历 s, 使用一个 Map 记录 s 中每个字母出现的次数, 然后遍历 t, 如果字母不在 Map 中,
则返回 false, 否则把该字母对应的出现次数减 1, 如果次数减为 0 则从 Map 中删除整个字母,
最后如果 Map 为空则表示 s 和 t 满足条件;
    """
    def isAnagram(self, s: str, t: str) -> bool:
        char_mapping = {}
        # jy: 用字典记录 s 中字符以及该字符出现的次数;
        for c in s:
            if c in char_mapping:
                char_mapping[c] = char_mapping[c] + 1
            else:
                char_mapping[c] = 1
        # jy: 遍历 t 中的字符, 如果字符不在字典中, 则直接返回 False; 如果在, 则将字典中
        #    的该字符个数减 1, 当为 0 时删除字典中的该字符(即在准备减 1 前, 判断如果为
        #    1 即可删除, 大于 1 时则减 1); 最后看字典是否为空即可;
        for c in t:
            if c not in char_mapping:
                return False
            elif char_mapping[c] > 1:
                char_mapping[c] = char_mapping[c] - 1
            else:
                char_mapping.pop(c)

        return len(char_mapping) == 0

"""
Follow up: 由于我们使用的是 Map 保存字符出现的次数, 所以同样适用于 unicode;
"""


s = "anagram"
t = "nagaram"
# Output: true
res = Solution().isAnagram(s, t)
print(res)

s = "rat"
t = "car"
# Output: false
res = Solution().isAnagram(s, t)
print(res)



