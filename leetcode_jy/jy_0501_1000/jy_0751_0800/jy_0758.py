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
title_jy = "Bold-Words-in-String(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of keywords ``words`` and a string ``s``, make all appearances of all
keywords words[i] in s bold. Any letters between <b> and </b> tags become bold.

Return ``s`` after adding the bold tags. The returned string should use the least number
of tags possible, and the tags should form a valid combination.
 

Example 1:
Input: words = ["ab","bc"], s = "aabcd"
Output: "a<b>abc</b>d"
Explanation: Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Example 2:
Input: words = ["ab","cb"], s = "aabcd"
Output: "a<b>ab</b>cd"
 

Constraints:
1 <= s.length <= 500
0 <= words.length <= 50
1 <= words[i].length <= 10
s and words[i] consist of lowercase English letters.



Note: This question is the same as 616_Add-Bold-Tag-in-String.py
参见(不重复编写): 616_Add-Bold-Tag-in-String.py
"""


class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        pass


