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
tag_jy = "最小编辑距离 | 动态规划 | IMP"


"""
Given two words `word1` and `word2`, find the minimum number of operations
required to convert `word1` to `word2`.

You have the following 3 operations permitted on a word:
1) Insert a character
2) Delete a character
3) Replace a character


Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: horse -> rorse (replace 'h' with 'r')
             rorse -> rose (remove 'r')
             rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: intention -> inention (remove 't')
             inention -> enention (replace 'i' with 'e')
             enention -> exention (replace 'n' with 'x')
             exention -> exection (replace 'n' with 'c')
             exection -> execution (insert 'u')
"""

class Solution:
    """
解法 1: 动态规划

题意: 将 word1 通过插入、删除、替换转换为 word2

定义 dp[i][j] 表示将 word1 的前 i 个字符编辑为 word2 的前 j 个字符的最少
编辑数, 则有:
1) 如果 word1[i] == word2[j], 表明当前的位置不需要编辑, 因此将 word1 的
   前 i 个字符编辑为 word2 的前 j 个字符的最小编辑数 (即 dp[i][j]) 等同
   于将 word1 的前 i-1 个字符编辑为 word2 的前 j-1 个字符的最小编辑数
   (即 dp[i-1][j-1]):
   dp[i][j] = dp[i-1][j-1]
2) 如果 word1[i] != word2[j], 表明需要对 word1 进行插入、删除、替换操作:
   dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
   其中:
   dp[i][j-1] + 1:   先将 word1 的前 i 个字符转换为 word2 的前 j-1 个字符,
                     再往 word1 中插入 word2 的第 j 个字符
   dp[i-1][j] + 1:   先将 word1 的前 i-1 个字符转换为 word2 的前 j 个字符,
                     再将 word1 的第 i 个字符删除
   dp[i-1][j-1] + 1: 先将 word1 的前 i-1 个字符转换为 word2 的前 j-1 个字符,
                     再将 word1 的第 i 个字符替换为 word2 的第 j 个字符
    """
    def minDistance_v1(self, word1: str, word2: str) -> int:

        # jy: LeetCode 官网上提交该行代码验证: "将 word1 编辑为 word2" 与
        #     "将 word2 编辑为 word1" 所需要的最小编辑数是相同的
        #word1, word2 = word2, word1

        m, n = len(word1), len(word2)
        # jy: 初始化 dp 为一个二维数组, 维度为 m+1 行 n+1 列; dp[0][0] = 0
        #     表示将 word1 的前 0 个字符 (空字符) 转换为 word2 的前 0 个字
        #     符 (空字符) 无需任何编辑操作
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # jy: 将 word1 的前 i 个字符转换为 word2 的前 0 个字符 (空字符) 最
        #     少需要 i 步 (即删除 word1 中的每一个字符)
        for i in range(1, m+1):
            dp[i][0] = i
        # jy: 将 word1 的前 0 个字符 (空字符) 转换为 word2 的前 j 个字符最
        #     少需要 j 步 (即往空字符中插入 word2 中的每一个字符)
        for j in range(1, n+1):
            dp[0][j] = j

        # jy: 逐行逐列遍历求解
        for i in range(1, m+1):
            for j in range(1, n+1):
                # jy: 注意: word1 中字符的下标位置与 dp 中代表第几个字符的
                #     下标之间相差 1
                # jy: 如果 word1 的第 i 个字符与 word2 的第 j 个字符相等, 表
                #     明 "将 word1 的前 i 个字符编辑为 word2 的前 j 个字符需
                #     要的最小编辑数" 等同于 "将 word1 的前 i-1 个字符编辑为
                #     word2 的前 j-1 个字符需要的最小编辑数"
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # jy: 如果 word1 的第 i 个字符与 word2 的第 j 个字符不相等,
                #     表明需要对 word1 进行插入、删除、替换操作
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[m][n]


    """
解法 2: 递归 + 缓存 (如果没有缓存, 则会超时)
    """
    import functools
    @functools.lru_cache(None)
    def minDistance_v2(self, word1: str, word2: str) -> int:
        """
        求将 word1 编辑为 word2 所需要的最小编辑数
        """
        # jy: 如果有一个字符串为空, 则另一个字符串中字符的个数即为
        #     最小需要的编辑数
        if not word1 or not word2:
            return len(word1) + len(word2)

        # jy: 如果当前字符相同, 则需要的最小编辑数等同于后续其它字
        #     符编辑为相同时的最小编辑数
        if word1[0] == word2[0]:
            return self.minDistance_v2(word1[1:], word2[1:])
        # jy: 如果当前字符不同, 则需要对当前字符进行插入、修改、删除操作
        else:
            # jy: 先将 word1 编辑为 word2[1:], 再在 word2[1:] 之前插入 word2[0]
            inserted = 1 + self.minDistance_v2(word1, word2[1:])
            # jy: 先将 word1[1:] 编辑为 word2, 再将 word1[0] 删除
            deleted = 1 + self.minDistance_v2(word1[1:], word2)
            # jy: 先将 word1[1:] 编辑为 word2[1:], 再将 word1[0] 替换为 word2[0]
            replace = 1 + self.minDistance_v2(word1[1:], word2[1:])
            # jy: 取以上三种编辑操作中编辑数最小的
            return min(inserted, deleted, replace)


    """
解法 3: 优化解法 2

解法 2 中使用字符串切片, 时间复杂度为 O(n), 当前解法改成使用索引
    """
    def minDistance_v3(self, word1: str, word2: str) -> int:
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            """
            求将 word1[i: ] 编辑为 word2[j: ] 需要的最小编辑数
            """
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j

            if word1[i] == word2[j]:
                return helper(i+1, j+1)
            else:
                inserted = 1 + helper(i, j+1)
                deleted = 1 + helper(i+1, j)
                replaced = 1 + helper(i+1, j+1)
                return min(inserted, deleted, replaced)
        # jy: 返回将 word1[0:] 编辑为 word2[0:] 需要的最小编辑数
        return helper(0, 0)
        


word1 = "intention"
word2 = "execution"
res = Solution().minDistance_v1(word1, word2)
# jy: 5
print(5)


word1 = "horse"
word2 = "ros"
res = Solution().minDistance_v2(word1, word2)
# jy: 3
print(3)



word1 = "horse"
word2 = "ros"
res = Solution().minDistance_v3(word1, word2)
# jy: 3
print(3)


