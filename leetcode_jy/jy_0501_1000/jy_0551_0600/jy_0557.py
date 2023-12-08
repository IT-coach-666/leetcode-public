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
title_jy = "Reverse-Words-in-a-String-III(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a string, you need to reverse the order of characters in each word  within a sentence
while still preserving whitespace and initial word  order.


Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"


Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


from typing import List
from collections import deque

class Solution:
    """
遍历字符串, 遇到完整的单词后反转这个单词;
    """
    def reverseWords_v1(self, s: str) -> str:
        i = 0
        n = len(s)
        words = ''
        # jy: 遍历字符串 s;
        while i < n:
            # jy: 如果当前字符为空字符, 则直接将其加入到 words 字符串后, 并将下标跳
            #    转到下一个字符的对应下标后, 跳过后续步骤进行下一轮循环;
            if s[i].isspace():
                words += ' '
                i += 1
                continue
            # jy: 记录临时的单词, 如果字符不为空字符, 则将其加入到单词列表中, 并继续
            #    遍历下一个单词, 直到碰到空字符或者到达最后一个字符, 则退出循环;
            word = []
            while i < n and not s[i].isspace():
                word.append(s[i])
                i += 1
            # jy: 将单词取反后加入单词字符串;
            words += ''.join(self._reverse_word(word))

        return words


    def _reverse_word(self, s: List[str]):
        low, high = 0, len(s) - 1

        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

        return s

    """
JY: 使用双向队列, 可以去掉反转字符串操作; 经 LeetCode 验证, 性能上比方法 1 好些;

还可以先反转整个字符串, 再对反转的结果进一步处理;
    """
    def reverseWords_jy(self, s: str) -> str:
        word = deque([])
        words = ''
        for i in s:
            if i.isspace():
                words += "".join(word) + " "
                word = deque([])
            else:
                word.appendleft(i)
        # jy: 由于最后一个空字符后可能还有单词, 此时该单词队列 word 还没被加入
        #    到 words 中, 此处补充加入;
        words += "".join(word)

        return words



s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
res = Solution().reverseWords_v1(s)
print(res)

res = Solution().reverseWords_jy(s)
print(res)


