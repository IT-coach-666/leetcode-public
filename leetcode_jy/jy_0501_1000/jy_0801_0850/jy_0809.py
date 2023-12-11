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
title_jy = "Expressive-Words(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


# 求单词列表中有多少个单词可以重复某个字符（如果重复，则该字符需至少出现 3 次）使得其成为目标字符串
"""
Sometimes people repeat letters to represent extra feeling. For example:
"hello" -> "heeellooo"
"hi" -> "hiiii"

In these strings like "heeellooo", we have groups of adjacent letters that
are all the same: "h", "eee", "ll", "ooo".  You are given a string ``s`` and
an array of query strings ``words``. A query word is stretchy if it can be
made to be equal to ``s`` by any number of applications of the following extension
operation: choose a group consisting of characters ``c``, and add some number
of characters ``c`` to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to
get "hellooo", but we cannot get "helloo" since the group "oo" has a size less
than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".
If s = "helllllooo", then the query word "hello" would be stretchy because of these
two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.

Return the number of query strings that are stretchy.


Example 1:
Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation: We can extend "e" and "o" in the word "hello" to get "heeellooo". We can't
             extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

Example 2:
Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3


Constraints:
1 <= s.length, words.length <= 100
1 <= words[i].length <= 100
s and words[i] consist of lowercase letters.
"""


from typing import List


class Solution:
    """
解法1: 遍历单词列表, 逐个单词判断是否可以扩展为 s;
    """
    def expressiveWords_v1(self, s: str, words: List[str]) -> int:
        count = 0

        for word in words:
            i = j = 0

            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    break

                length1 = 1
                length2 = 1

                while i+1 < len(s) and s[i] == s[i+1]:
                    i += 1
                    length1 += 1

                while j+1 < len(word) and word[j] == word[j+1]:
                    j += 1
                    length2 += 1

                if (length1 == length2) or (length1 >= 3 and length2 < length1):
                    i += 1
                    j += 1
                else:
                    break

            if i == len(s) and j == len(word):
                count += 1

        return count


s = "heeellooo"
words = ["hello", "hi", "helo"]
# Output: 1
res = Solution().expressiveWords_v1(s, words)
print(res)


s = "zzzzzyyyyy"
words = ["zzyy","zy","zyy"]
# Output: 3
res = Solution().expressiveWords_v1(s, words)
print(res)


