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
title_jy = "Partition-Labels(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given a string ``s``. We want to partition the string into as many
parts as possible so that each letter appears in at most one part. Return a
list of integers representing the size of these parts.


Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation: The partition is "ababcbaca", "defegde", "hijhklij".  This is a
             partition so that each letter appears in at most one part.  A
             partition like "ababcbacadefegde", "hijhklij" is incorrect, because
             it splits ``s`` into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]


Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""


from typing import List


class Solution:
    """
解法1: 使用 Map 保存每个字符在字符串中最后一次出现的位置, 使用两个指针标记字符块
的起始和终止, 遍历字符串, 如果当前字符最后出现的位置等于当前位置, 则找到了一个字
符块, 计算字符块的长度并将其加入结果列表, 并将 left 指向字符块末尾的下一个字符位
置, 作为新字符块的开始;
    """
    def partitionLabels_v1(self, s: str) -> List[int]:
        rightmost = {c: i for i, c in enumerate(s)}
        left, right = 0, 0
        result = []

        for i, c in enumerate(s):
            right = max(right, rightmost[c])

            if i == right:
                result.append(right - left + 1)
                left = i + 1

        return result


s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
res = Solution().partitionLabels_v1(s)
print(res)


s = "eccbbbbdec"
# Output: [10]
res = Solution().partitionLabels_v1(s)
print(res)


