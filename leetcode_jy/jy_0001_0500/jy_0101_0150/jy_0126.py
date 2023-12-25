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
title_jy = "Word-Ladder-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

Every adjacent pair of words differs by a single letter.
Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
`sk` == `endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return all the shortest transformation sequences from `beginWord` to `endWord`, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
Output: [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
Explanation: There are 2 shortest transformation sequences:
             "hit" -> "hot" -> "dot" -> "dog" -> "cog"
             "hit" -> "hot" -> "lot" -> "log" -> "cog"
             
Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log"]
Output: []
Explanation: The endWord "cog" is not in `wordList`, therefore there is no valid transformation sequence.
 

Constraints:
1) 1 <= beginWord.length <= 5
2) endWord.length == beginWord.length
3) 1 <= wordList.length <= 500
4) wordList[i].length == beginWord.length
5) `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
6) beginWord != endWord
7) All the `words` in `wordList` are unique.
8) The sum of all shortest transformation sequences does not exceed 10^5.
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/word-ladder-ii/solutions/279018/cong-bfssi-xiang-kai-shi-de-jin-hua-zhi-lu-2400msy/
    """
    def findLadders_v1(self, beginWord, endWord, wordList):
        se=set(wordList)
        if not endWord in se:
            return []
        def edges(word):
            arr=list(word)
            for i in range(len(arr)):
                c=arr[i]
                for j in range(97,123):
                    arr[i]=chr(j)
                    newWord=''.join(arr)
                    if newWord in se and not newWord in marked:
                        yield newWord
                arr[i]=c
        res=[]
        marked=set()
        queue=[[beginWord]]
        while queue:
            temp=[]
            found=False
            for words in queue:
                marked.add(words[-1])
            for words in queue:
                for w in edges(words[-1]):
                    v=words+[w]
                    if w == endWord:
                        res.append(v)
                        found=True
                    temp.append(v)
            if found:          #找到就不再遍历了，即使再有endWord，路径也会更长
                break
            queue=temp
        return res

    
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
res = Solution().findLadders_v1(beginWord, endWord, wordList)
# jy: [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
print(res)
         
    

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
res = Solution().findLadders_v1(beginWord, endWord, wordList)
# jy: []
print(res)
