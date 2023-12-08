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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Word-Ladder(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A transformation sequence from word ``beginWord`` to word ``endWord`` using a dictionary
``wordList`` is a sequence of words ``beginWord -> s1 -> s2 -> ... -> sk`` such that:
1) Every adjacent pair of words differs by a single letter.
2) Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in
   wordList.
3) sk == endWord

Given two words, ``beginWord`` and ``endWord``, and a dictionary ``wordList``, return the
number of words in the shortest transformation sequence from beginWord to endWord, or 0 if
no such sequence exists.


Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog",
             which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation
             sequence.


Constraints:
1) 1 <= beginWord.length <= 10
2) endWord.length == beginWord.length
3) 1 <= wordList.length <= 5000
4) wordList[i].length == beginWord.length
5) beginWord, endWord, and wordList[i] consist of lowercase English letters.
6) beginWord != endWord
7) All the words in wordList are unique.
"""


import sys
from typing import List
import collections
import string


class Solution:
    """
解法1(超时): 递归暴力求解: 依次遍历字典, 判断入参单词和当前单词是否只差一个字母, 如
果是, 则使用当前单词继续寻找
    """
    def ladderLength_v1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # jy: 递归判断 beginWord 是否可以通过 wordList 转换为 endWord, 如果可以则返回
        #     其最短路径, 否则返回 0;
        min_length = self._dfs(beginWord, endWord, wordList, 1, set())
        return min_length if min_length < sys.maxsize else 0

    def _dfs(self, begin_word, end_word, word_list, length, visited):
        """
        begin_word 为截止当前变换为止的单词(length = 变换的次数 + 1, 即不同单词个数, 初始时仅有原先的一个单词)
        end_word   为目标单词
        word_list  为单词列表
        visited    记录 word_list 中已经被访问过的单词
        """
        # jy: 如果 begin_word 等于 end_word, 则返回当前路径的长度 length, 终止递归;
        if begin_word == end_word:
            return length

        # jy: min_length 记录转换过程的最短路径;
        min_length = sys.maxsize
        # jy: 遍历 word_list 中的 word (如果该 word 已经遍历过, 则跳过), 如果 word 与当前的
        #     begin_word 相差一个字符, 则将 word 加入 visited 集合中, 并将该 word 作为新的
        #     begin_word 继续递归查找(下一轮递归调用时 length 加 1), 并在递归后从 visited 中
        #     移除该 word, 防止对后续的递归过程造成干扰(回溯);
        for word in word_list:
            if word in visited:
                continue
            # jy: 如果 begin_word 与当前遍历的 word 相差一个字符, 表明可以从 begin_word
            #     转换为 word, 则将 word 加入 visited 集合(后续递归中在 visited 中的单词
            #     就不再遍历), 并递归判断从 word 开始, 是否可以通过 wordList 转换为 endWord
            #     如果可以则返回其路径长度; 以下逻辑中会通过 min() 函数获取长度最短的路径;
            if self._is_one_letter_diff(begin_word, word):
                visited.add(word)
                min_length = min(min_length, self._dfs(word, end_word, word_list, length + 1, visited))
                # jy: 以上已经实现了去除当前 word 后实现递归, 此时从 visited 中去除该单词,
                #     防止对后续的其它递归判断产生影响(回溯)
                visited.remove(word)
        return min_length

    def _is_one_letter_diff(self, a, b):
        """
        判断相同长度的 a 和 b 字符串是否仅仅有一个字符不相同;
        """
        # jy: count 用于统计不同字符的个数;
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
            if count > 1:
                return False
        return count == 1

    """
解法2: 将要搜索的单词和至今的转换次数放入队列中, 每次出队时, 尝试替换出队单词的每一个字
符, 如果替换后的单词在字典中, 则将替换后的单词放入队列, 如果出队的单词等于最终的单词, 则
表明已经找到
    """
    def ladderLength_v2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        visited = set()
        # jy: 将当前单词以及当前的长度组成元组入队;
        queue = collections.deque([(beginWord, 1)])
        # jy: letters 得到的是 'abcdefghijklmnopqrstuvwxyz'
        letters = string.ascii_lowercase

        # jy: 队列不为空, 则左侧出队(确保总是先进先出), 故第一个出队的满足要求的结果即是
        #     路径最短的;
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length

            # jy: 最多替换的字符数为 word 的字符总数;
            for i in range(len(word)):
                # jy: 遍历 26 个英文字符, 将当前 word 的每个位置都用 26 个字符英文字符尝试
                #     替换(即尝试替换一个字符), 如果替换后的单词在 words 中, 且原先没有被访
                #     问过(即 visited 中不存在), 则将替换后的单词加入到队列中, 路径长度加 1,
                #     并加入 visited 中, 标记为已访问;
                for c in letters:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in words and new_word not in visited:
                        queue.append((new_word, length + 1))
                        visited.add(new_word)
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# Output: 5
res = Solution().ladderLength_v1(beginWord, endWord, wordList)
print(res)

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
# Output: 0
res = Solution().ladderLength_v2(beginWord, endWord, wordList)
print(res)


