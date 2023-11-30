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
title_jy = "Remove-All-Adjacent-Duplicates-In-String(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
You are given a string ``s`` consisting of lowercase English letters. A ``duplicate removal``
consists of choosing two adjacent and equal letters and removing them. We repeatedly make
``duplicate removals`` on ``s`` until we no longer can. Return the final string after all such
``duplicate removals`` have been made. It can be proven that the answer is unique.


Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation:  For example, in "abbaca" we could remove "bb" since the letters are adjacent and
              equal, and this is the only possible move.  The result of this move is that the
              string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"


Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""


from typing import List


class Solution:
    """
只要求删除重复出现 2 次的情况, 如果重复出现 3 次, 则会保留一次;
    """
    def removeDuplicates_v1(self, str_: str) -> str:
        stack = []
        for i in str_:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

    """
删除连续的相邻字符(连续出现 2 次以上则删除 2 个以上)
    """
    def removeDuplicates_other(self, str_: str) -> str:
        len_ = len(str_)
        stack = []
        i = 0
        while i < len_:
            if i + 1 < len_ and str_[i] == str_[i + 1]:
                stack.append(str_[i])
            elif stack and str_[i] == stack[-1]:
                while stack and str_[i] == stack[-1]:
                    stack.pop()
            else:
                stack.append(str_[i])
            i += 1
        return "".join(stack)


s = "abbaca"
# Output: "ca"
res = Solution().removeDuplicates_v1(s)
print(res)


s = "azxxzy"
# Output: "ay"
res = Solution().removeDuplicates_other(s)
print(res)

s = "azxxxzy"
# Output: "ay"
res = Solution().removeDuplicates_v1(s)
print(res)

res = Solution().removeDuplicates_other(s)
print(res)



