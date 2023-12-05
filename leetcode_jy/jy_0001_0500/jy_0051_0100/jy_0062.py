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
tag_jy = ""


"""
A robot is located at the top-left corner of a ``m x n`` grid (marked 'Start' in the
diagram below). The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish'
in the diagram below). How many possible unique paths are there?


Example 1:  https://www.yuque.com/frederick/dtwi9g/cgisvg
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6


Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10^9.
"""


class Solution:
    """
解法1: 动态规划; 记 dp[i][j] 表示机器人从 (0, 0) 走到 (i, j) 的路径数, 则:
dp[i][j] = dp[i-1][j] + dp[i][j-1]

因为对于当前位置 (i, j), 只可能是从上一个位置 [(i-1, j), (i, j-1)] 走过来,
因为只能往右走或往下走, 当前位置的上一位置不可能有其它可能性;
    """
    def uniquePaths_v1(self, m: int, n: int) -> int:
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
解法2: 和解法1本质上一样, 只是少了些边界的判断, 因为如果 (i, j) 属于第一行或第一列,
则其从 (0, 0) 走到 (i, j) 的走法始终都只有一种;
    """
    def uniquePaths_v2(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # jy: 如果 (i, j) 属于第一行或第一列, 则其从 (0, 0) 走到 (i, j) 的走法始终都只有一种;
                if i == 0 or j == 0:
                    dp[i][j] = 1
                # jy: 如果 (i, j) 不属于第一行或第一列, 则 dp[i-1][j] 和 dp[i][j-1] 均为有效值;
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

    """
JY: 递归求解;
    """
    def uniquePaths_jy(self, m, n):

        def _dfs(position, m, n):
            # jy: 如果对应位置属于最后一行或最后一列, 则走向右下角的方式只有 1 种;
            if position[0] == m-1 or position[1] == n-1:
                return 1
            # jy: 从当前位置 position 走向右下角位置的走法有两种选择: 先向右走一步
            #    或先向下走一步; 则当前位置走到右下角的所有方式等价于向右/向下走一
            #    步后所在位置到右下角所有走法的加和;
            return _dfs((position[0], position[1]+1), m, n) + _dfs((position[0]+1, position[1]), m, n)

        position = (0, 0)
        res = _dfs(position, m, n)
        return res


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
res = Solution().uniquePaths_jy(m, n)
print(res)


