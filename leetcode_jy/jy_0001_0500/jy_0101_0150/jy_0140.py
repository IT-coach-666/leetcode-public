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
title_jy = "Word-Break-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:
Input: s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]
Output: ["cats and dog", "cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: []
 

Constraints:
1) 1 <= s.length <= 20
2) 1 <= wordDict.length <= 1000
3) 1 <= wordDict[i].length <= 10
4) `s` and `wordDict[i]` consist of only lowercase English letters.
5) All the strings of `wordDict` are unique.
6) Input is generated in a way that the length of the answer doesn't exceed 10^5.
"""


class Solution:
    """
解法 1: 超时   
https://leetcode.cn/problems/word-break-ii/solutions/468979/python3ji-yi-hua-sou-suo-tian-jia-3xing-dai-ma-1ge/
    """
    def wordBreak_v1(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        #
        wordDict = set(wordDict)

        def dfs(wordDict,temp,pos):
            #
            if pos == len(s):
                res.append(" ".join(temp))
                return
            for i in range(pos,len(s)+1):
                if s[pos:i] in wordDict:
                    temp.append(s[pos:i])
                    dfs(wordDict,temp,i)
                    temp.pop() 
            #
                       
            
        dfs(wordDict,[],0)
        return res

    
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
res = Solution().wordBreak_v1(s, wordDict)
# jy: ["cats and dog", "cat sand dog"]
print(res)


s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
res = Solution().wordBreak_v1(s, wordDict)
# jy: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
print(res)


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
res = Solution().wordBreak_v1(s, wordDict)
# jy: []
print(res)