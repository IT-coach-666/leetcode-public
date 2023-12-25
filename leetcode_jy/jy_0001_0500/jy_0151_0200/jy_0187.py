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
title_jy = "Repeated-DNA-Sequences(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string `s` that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 10^5
s[i] is either 'A', 'C', 'G', or 'T'.
"""


class Solution:
    """
    布尔字典
    """
    def findRepeatedDnaSequences_v1(self, s: str) -> List[str]:
        d = {}
        for i in range(len(s) - 9):
            if s[i: i + 10] in d:
                d[s[i: i + 10]] = True
            else:
                d[s[i: i + 10]] = False
        return [*filter(lambda i: d[i], d)]
    
    
    """
    计数字典
    """
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = collections.Counter(s[i: i + 10] for i in range(len(s) - 9))
        return list(filter(lambda i: d[i] > 1, d))


    """
    整型字典
    """
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = collections.defaultdict(int)
        for i in range(len(s) - 9):
            d[s[i: i + 10]] += 1
        return [i for i in d if d[i] > 1]


    """
    两个集合
    """
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        tmp, ans = set(), set()
        for i in range(len(s) - 9):
            if s[i: i + 10] not in tmp:
                tmp.add(s[i: i + 10])
            elif s[i:i + 10] not in ans:
                ans.add(s[i: i + 10])
        return list(ans)

    


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
res = Solution().findRepeatedDnaSequences_v1(s)
# jy: ["AAAAACCCCC","CCCCCAAAAA"]
print(res)


s = "AAAAAAAAAAAAA"
res = Solution().findRepeatedDnaSequences_v1(s)
# jy: ["AAAAAAAAAA"]
print(res)

