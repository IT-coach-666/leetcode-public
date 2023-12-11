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
title_jy = "Group-Shifted-Strings(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
We can shift a string by shifting each of its letters to its successive letter.
For example, "abc" can be shifted to be "bcd".

We can keep shifting the string to form a sequence.
For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

Given an array of strings ``strings``, group all strings[i] that belong to the same shifting sequence.
You may return the answer in any order.


Example 1:
Input: strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
Output: [["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]]

Example 2:
Input: strings = ["a"]
Output: [["a"]]


Constraints:
1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
"""


from typing import List

class Solution:
    """
创建一个 Map, 键为字符串中后一个字符相对前一个字符的距离之差, 如 abc 对应的键为 (1, 1), 只要字符
串的键相同, 那么它们就一定是同一个序列;
    """
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mapping = {}
        # jy: 遍历列表中的字符串;
        for s in strings:
            key = ()
            # jy: 遍历字符串中的字符(最后一字符不用遍历), 构造该字符串对应的 key 值;
            for i in range(len(s)-1):
                diff = ord(s[i+1]) - ord(s[i])
                key += (diff % 26,)
                # print("=============key: ", key)
            # jy: 将属于相同 key 值的字符串添加到字典中;
            mapping[key] = mapping.get(key, []) + [s]
        return list(mapping.values())


strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
# Output: [["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]]
res = Solution().groupStrings(strings)
print(res)

strings = ["a"]
# Output: [["a"]]
res = Solution().groupStrings(strings)
print(res)


