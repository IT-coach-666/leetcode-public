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
title_jy = "Unique-Paths(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "动态规划 | 递归 + 缓存 | 相似题: arr_dim_2_path"


"""
There is a robot on an `m x n` grid. The robot is initially located at 
the top-left corner (i.e., grid[0][0]). The robot tries to move to the 
bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move 
either down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique
paths that the robot can take to reach the bottom-right corner. The test
cases are generated so that the answer will be less than or equal to 2 * 10^9.


Example 1:  
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach
             the bottom-right corner:
             1) Right -> Down -> Down
             2) Down -> Down -> Right
             3) Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6


Constraints:
1 <= m, n <= 100
"""


class Solution:
    """
解法 1: 动态规划

记 dp[i][j] 表示机器人从 (0, 0) 走到 (i, j) 的路径数; 因为能往右或往
下走, 位置 (i, j) 的上一个位置只能是 (i-1, j) 或 (i, j-1), 因此有:
dp[i][j] = dp[i-1][j] + dp[i][j-1]
    """
    def uniquePaths_v1(self, m: int, n: int) -> int:
        # jy: 初始化 dp, 其中 dp[0][0] 为 1, 表示位置 (0, 0) 只有 1 种走法
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                top = dp[i-1][j] if i-1 >= 0 else 0
                left = dp[i][j-1] if j-1 >= 0 else 0
                dp[i][j] = top + left

        return dp[m-1][n-1]


    """
解法 2: 同解法 1, 但少了些边界的判断, 因为从位置 (0, 0) 走到第一行或第一列
的任何位置的路径始终只有 1 种, 因此当 i = 0 或 j = 0 时, dp[i][j] 始终为 1
    """
    def uniquePaths_v2(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # jy: 从上到下遍历每一行, 从左到右遍历每一列
        for i in range(m):
            for j in range(n):
                # jy: 从位置 (0, 0) 走到第一行或第一列的任何位置的路径始终只
                #     有 1 种, 因此当 i = 0 或 j = 0 时, dp[i][j] 始终为 1
                if i == 0 or j == 0:
                    dp[i][j] = 1
                # jy: 其它情况时, dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


    """
解法 3: 递归
    """
    def uniquePaths_v3(self, m, n):
        def _dfs(position, m, n):
            """
            求从当前位置 position 走到最后一个位置 (m-1, n-1) 的不同路径走法
            """
            print(position)
            # jy: 如果对应位置属于最后一行或最后一列, 则走向右下角的方式
            #     只有 1 种
            if position[0] == m-1 or position[1] == n-1:
                return 1

            # jy: 从当前位置 position 走向右下角位置的走法有两种:
            #     1) 先向右走一步, 即来到了 (position[0], position[1] + 1) 位置
            #     2) 先向下走一步, 即来到了 (position[0] + 1, position[1]) 位置
            #     因此, 从位置 position 走到右下角的所有方式等价于从以上两个位
            #     置走到右下角位置的总和
            return _dfs((position[0], position[1] + 1), m, n) + \
                   _dfs((position[0] + 1, position[1]), m, n)

        res = _dfs((0, 0), m, n)
        return res


    """
解法 4: 递归 (超时)
    """
    def uniquePaths_v4(m, n):
        def dfs(i, j):
            """
            从位置 (0, 0) 走到位置 (i, j) 的所有路径数
            """
            # jy: 从位置 (0, 0) 走到第一行 (i 为 0) 或第一列 (j 为 0) 的任意
            #     一个位置均只有 1 种路径走法
            if i == 0 or j == 0:
                return 1
            # jy: 从位置 (0, 0) 走到位置 (i, j) 有两种走法:
            #     1) 从位置 (0, 0) 走到位置 (i-1, j), 再往下走一步即可
            #     2) 从位置 (0, 0) 走到位置 (i, j-1), 再往右走一步即可 
            return dfs(i-1, j) + dfs(i, j-1)
 
        # jy: 返回从 (0, 0) 走到 (m-1, n-1) 的所有路径数
        return dfs(m-1, n-1)


    """
解法 5: 对解法 4 的改写, 且位置下标从 1 开始, 即初始位置下标为 (1, 1)
    """
    def uniquePaths_v5(m, n):
        """
        从位置 (1, 1) 走到位置 (m, n) 的所有走法
        """
        # jy: 走到第一行或第一列的任意一个位置的走法均只有 1 种
        if m == 1 or n == 1:
            return 1
        # jy: 从位置 (1, 1) 走到位置 (m, n) 的走法有以下两种:
        #     1) 先从位置 (1, 1) 走到位置 (m-1, n), 再向下走一步
        #     2) 先从位置 (1, 1) 走到位置 (m, n-1), 再向右走一步 
        return self.uniquePaths_v3(m-1, n) + self.uniquePaths_v3(m, n-1)


    """
解法 6: 递归 + 缓存 (类似动态规划), 对解法 4 进行优化

以上递归解法 3-5 均会超时, 因为有很多子问题被不断重复计算
    """
    def uniquePaths_v6(self, m: int, n: int) -> int:
        dict_ = {}
        def dfs(i, j):
            if i == 0 or j == 0:
                return 1

            if (i, j) in dict_:
                return dict_[(i, j)]

            dict_[(i, j)] = dfs(i-1, j) + dfs(i, j-1) 
            return dict_[(i, j)]


        return dfs(m-1, n-1)


m = 3
n = 7
# Output: 28
res = Solution().uniquePaths_v1(m, n)
print(res)


m = 3
n = 2
# Output: 3
res = Solution().uniquePaths_v1(m, n)
print(res)


m = 7
n = 3
# Output: 28
res = Solution().uniquePaths_v2(m, n)
print(res)


m = 3
n = 3
# Output: 6
res = Solution().uniquePaths_v3(m, n)
print(res)


m = 23
n = 12
# Output: 6
res = Solution().uniquePaths_v4(m, n)
print(res)


m = 23
n = 12
# Output: 6
res = Solution().uniquePaths_v5(m, n)
print(res)


m = 23
n = 12
# Output: 6
res = Solution().uniquePaths_v6(m, n)
print(res)

