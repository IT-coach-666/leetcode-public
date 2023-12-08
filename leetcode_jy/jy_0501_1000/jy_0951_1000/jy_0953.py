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
title_jy = "Verifying-an-Alien-Dictionary(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
In an alien language, surprisingly they also use english lowercase letters, but
possibly in a different order. The order of the alphabet is some permutation of
lowercase letters.

Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted lexicographicaly
in this alien language.


Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence
             the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.)
             According to lexicographical rules "apple" > "app", because 'l' > ' ', where ' ' is
             defined as the blank character which is less than any other character (More info).


Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""


from typing import List


class Solution:
    """
因为只涉及到英文字母, 所以使用一个长度为 26 的数组来保存每个字母对应的顺序; 首先遍
历 order, 根据字母出现的顺序将其更新的顺序数组中, 然后遍历单词判断单词是否有序;
    """
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orders = [-1] * 26
        # jy: 遍历顺序字符串中的字符, 将其 ord(c)-97 的结果作为列表的下标, 对应的值为排
        #    序的优先级(ord("a") 为 97, 则 ord(c)-97 的最大值为 26);
        for i, c in enumerate(order):
            orders[ord(c) - 97] = i
        # jy: 从第二个单词开始遍历单词列表;
        for i in range(1, len(words)):
            # jy: 获取前一个单词
            word1 = words[i-1]
            # jy: 获取当前单词;
            word2 = words[i]
            # jy: 判断前一个单词(word1)是否比当前单词(word2)小
            if not self._is_smaller(word1, word2, orders):
                return False

        return True

    def _is_smaller(self, word1, word2, orders):
        j = k = 0
        # jy: 同时遍历两个单词, 比较相同位置上的字符是否排序恰当;
        while j < len(word1) and k < len(word2):
            order1 = orders[ord(word1[j]) - 97]
            order2 = orders[ord(word2[k]) - 97]

            if order1 < order2:
                return True
            elif order1 > order2:
                return False
            else:
                j += 1
                k += 1
        # jy: 如果经过以上 while 循环都没有 return, 则表明两个单词有相同的前缀部分, 且其
        #    中一个单词就是另一个单词的前缀, 如果 word1 的长度比 word2 小, 直接返回 True;
        return len(word1) <= len(word2)


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
res = Solution().isAlienSorted(words, order)
print(res)


words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
# Output: false
res = Solution().isAlienSorted(words, order)
print(res)


words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
res = Solution().isAlienSorted(words, order)
print(res)


