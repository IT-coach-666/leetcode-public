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
title_jy = "Sentence-Similarity-III(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. For example, "Hello World", "HELLO", "hello world hello world" are all sentences. Words consist of only uppercase and lowercase English letters.
Two sentences sentence1 and sentence2 are similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. For example, sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in sentence2.
Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

Example 1:
Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

Example 2:
Input: sentence1 = "of", sentence2 = "A lot of words"
Output: false
Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.

Example 3:
Input: sentence1 = "Eating right now", sentence2 = "Eating"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.

Example 4:
Input: sentence1 = "Luky", sentence2 = "Lucccky"
Output: false


Constraints:
1 <= sentence1.length, sentence2.length <= 100
sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
The words in sentence1 and sentence2 are separated by a single space.
"""


class Solution:
    """
解法1
将两个句子转为列表, 遍历列表直到两个列表对应位置的单词不同, 记 sentence1 单词下标为 i, sentence2 单词下标为 j, 对 sentence2 从后向前遍历寻找单词等于 i 处单词的位置, 从该位置开始判断 sentence1 和 sentence2 剩下的单词是否相同;
    """
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(' ')
        words2 = sentence2.split(' ')
        i = j = 0

        if len(words1) > len(words2):
            words1, words2 = words2, words1

        while i < len(words1) and j < len(words2) and words1[i] == words2[j]:
            i += 1
            j += 1

        if i == len(words1):
            return True

        for k in range(len(words2) - 1, j - 1, -1):
            if words1[i] == words2[k]:
                j = k

                break

        while i < len(words1) and j < len(words2) and words1[i] == words2[j]:
            i += 1
            j += 1

        return i == len(words1) and j == len(words2)

class Solution:
    """
解法2
在解法1的基础上进行优化, 不需要对 sentence2 从后向前遍历寻找单词等于 i 处单词的位置, 根据 sentence1 还剩下几个单词, 直接定位到 sentence2 同样长度的位置, 判断两者剩下的单词是否相同;
    """
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(' ')
        words2 = sentence2.split(' ')
        i = j = 0

        if len(words1) > len(words2):
            words1, words2 = words2, words1

        while i < len(words1) and j < len(words2) and words1[i] == words2[j]:
            i += 1
            j += 1

        j = len(words2) - len(words1) + i

        while i < len(words1) and j < len(words2) and words1[i] == words2[j]:
            i += 1
            j += 1

        return i == len(words1) and j == len(words2)


import collections


class Solution:
    """
解法3
使用两个双端队列, 只要两个队列头的元素相同则持续从队首出队, 然后只要两个队列尾的元素相同则持续从队尾出队, 最后判断是否有一个队列为空;
    """
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        deque1 = collections.deque(sentence1.split(' '))
        deque2 = collections.deque(sentence2.split(' '))

        while deque1 and deque2 and deque1[0] == deque2[0]:
            deque1.popleft()
            deque2.popleft()

        while deque1 and deque2 and deque1[-1] == deque2[-1]:
            deque1.pop()
            deque2.pop()

        return not deque1 or not deque2


