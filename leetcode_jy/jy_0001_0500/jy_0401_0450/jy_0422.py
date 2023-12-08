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
title_jy = "Valid-Word-Square(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of strings ``words``, return true if it forms a valid word square.

A sequence of strings forms a valid word square if the k-th row and column read the same string,
where 0 <= k < max(numRows, numColumns).

Example 1:  https://www.yuque.com/frederick/dtwi9g/glzl7b

Input: words = [
"abcd",
"bnrt",
"crmy",
"dtye"]
Output: true
Explanation:
The 1st row and 1st column both read "abcd".
The 2nd row and 2nd column both read "bnrt".
The 3rd row and 3rd column both read "crmy".
The 4th row and 4th column both read "dtye".
Therefore, it is a valid word square.

Example 2:
Input: words = [
"abcd",
"bnrt",
"crm",
"dt"]
Output: true
Explanation:
The 1st row and 1st column both read "abcd".
The 2nd row and 2nd column both read "bnrt".
The 3rd row and 3rd column both read "crm".
The 4th row and 4th column both read "dt".
Therefore, it is a valid word square.

Example 3:
Input: words = [
"ball",
"area",
"read",
"lady"]
Output: false
Explanation: The 3rd row reads "read" while the 3rd column reads "lead".
             Therefore, it is NOT a valid word square.


Constraints:
1 <= words.length <= 500
1 <= words[i].length <= 500
words[i] consists of only lowercase English letters.
"""


from typing import List

class Solution:
    """
等价于遍历数组的每个元素, 判断 words[i][j] 是否等于 words[j][i];
    """
    def validWordSquare(self, words: List[str]) -> bool:
        if not words or not words[0]:
            return True

        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False

        return True



words = ["abcd", "bnrt", "crmy", "dtye"]
# Output: true
res = Solution().validWordSquare(words)
print(res)


words = ["abcd", "bnrt", "crm", "dt"]
# Output: true
res = Solution().validWordSquare(words)
print(res)


words = ["ball", "area", "read", "lady"]
# Output: false
res = Solution().validWordSquare(words)
print(res)


