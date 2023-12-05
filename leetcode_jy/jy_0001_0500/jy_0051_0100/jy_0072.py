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
title_jy = "Edit-Distance(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two words word1 and word2, find the minimum number of operations
required to convert word1 to word2.

You have the following 3 operations permitted on a word:
1. Insert a character
2. Delete a character
3. Replace a character


Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution:
    """
目标: 将 word1 通过插入, 删除, 替换转换为 word2;
使用动态规划求解: 定义 dp[i][j] 表示将 word1 的前 i 个字符转为 word2 的前 j 个字符
最少需要几步, 则 dp[i][j] 等于:
  1) 如果 word1[i] == word2[j], 说明此时不需要操作, 则:
     dp[i][j] = dp[i-1][j-1]
  2) 否则需要对 word1 进行增加, 删除, 替换操作, 则:
     dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
     其中:
         dp[i][j] = 1 + dp[i][j-1]    将 word1 的前 i 个字符转换为 word2 的前 j-1 个字符最
                                      少需要的步数 + 往 word1 中插入 word2 的第 j 个字符;
         dp[i][j] = 1 + dp[i-1][j]    将 word1 的前 i-1 个字符转换为 word2 的前 j 个字符最
                                      少需要的步数 + 将 word1 的第 i 个字符删除;
         dp[i][j] = 1 + dp[i-1][j-1]  将 word1 的前 i-1 个字符转换为 word2 的前 j-1 个字符
                                      最少需要的步数 + 将 word1 的第 i 个字符替换为 word2 的
                                      第 j 个字符;
    """
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # jy: 初始化 dp, dp[i][j] 表示将 word1 的前 i 个字符转为 word2 的前 j 个字符
        #    最少需要几步, 则 dp 是一个二维数组, 维度为 m+1 行 n+1 列;
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # jy: 将 word1 的前 i 个字符转换为 word2 的前 0 个字符最少需要 i 步(删除每一个字符)
        for i in range(m+1):
            dp[i][0] = i
        # jy: 将 word1 的前 0 个字符转换为 word2 的前 i 个字符最少需要 i 步(插入每一个字符)
        for i in range(n+1):
            dp[0][i] = i
        # jy:
        for i in range(1, m+1):
            for j in range(1, n+1):
                # jy: 如果 word1 的第 i 个字符(下标为 i-1)与 word2 的第 j 个字符(下标为 j-1)相
                #    等, 则表明将 word1 的前 i 个字符转换为 word2 的前 j 个字符需要的最少步数
                #    (即 dp[i][j]) 等同于将 word1 的前 i-1 个字符转换为 word2 的前 j-1 个字符
                #    需要的最少步数(即 dp[i-1][j-1])
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # jy: 否则需要对 word1 进行增加, 删除, 替换操作;
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[m][n]


word1 = "intention"
word2 = "execution"
res = Solution().minDistance(word1, word2)
print(res, " === ", 5)
res = Solution().minDistance(word2, word1)
print(res, " === ", 5)


word1 = "horse"
word2 = "ros"
res = Solution().minDistance(word1, word2)
print(res, " === ", 3)
res = Solution().minDistance(word2, word1)
print(res, " === ", 3)


