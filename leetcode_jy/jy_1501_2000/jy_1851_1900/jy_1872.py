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
title_jy = "Stone-Game-VIII(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Alice and Bob take turns playing a game, with Alice starting first.
There are n stones arranged in a row. On each player's turn, while the number of stones is more than one, they will do the following:
1. Choose an integer x > 1, and remove the leftmost x stones from the row.
2. Add the sum of the removed stones' values to the player's score.
3. Place a new stone, whose value is equal to that sum, on the left side of the row.
The game stops when only one stone is left in the row.
The score difference between Alice and Bob is (Alice's score - Bob's score). Alice's goal is to maximize the score difference, and Bob's goal is the minimize the score difference.
Given an integer array stones of length n where stones[i] represents the value of the ith stone from the left, return the score difference between Alice and Bob if they both play optimally.

Example 1:
Input: stones = [-1,2,-3,4,-5]
Output: 5
Explanation:
- Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
  value 2 on the left. stones = [2,-5].
- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
  the left. stones = [-3].
The difference between their scores is 2 - (-3) = 5.

Example 2:
Input: stones = [7,-6,5,10,5,-2,-6]
Output: 13
Explanation:
- Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to her score, and places a
  stone of value 13 on the left. stones = [13].
The difference between their scores is 13 - 0 = 13.

Example 3:
Input: stones = [-10,-12]
Output: -22
Explanation:
- Alice can only make one move, which is to remove both stones. She adds (-10) + (-12) = -22 to her
  score and places a stone of value -22 on the left. stones = [-22].
The difference between their scores is (-22) - 0 = -22.


Constraints:
n == stones.length
2 <= n <= 10^5
-10^4 <= stones[i] <= 10^4
"""


from typing import List


class Solution:
    """
注意到每次玩家选了 k 块石头后, 会在左侧放入一块石头, 其分值为拿走的 k 块石头的分值和, 所以等同于每个玩家操作时能获得的分数等于 stones[:i] 的总和, 所以可以构造前缀和数组 prefix_sum, 同时记 dp[i] 表示在石头 stones[i:n] 中先手玩家所能获得的最大分值差, 先手玩家所能获得的分值差可能为:
1. prefix_sum[i] - dp[i + 1]
2. prefix_sum[i + 1] - dp[i + 2]
3. ...
4. prefix_sum[n - 2] - dp[n - 1]
故先手玩家能获得的最大分值差为 max(prefix_sum[i] - dp[i + 1], prefix_sum[i + 1] - dp[i + 2], ..., prefix_sum[n - 2] - dp[n - 1]), 等价于 max(prefix_sum[i] - dp[i + 1], max(prefix_sum[i + 1] - dp[i + 2], ..., prefix_sum[n - 2] - dp[n - 1])), 即 max(prefix_sum[i] - dp[i + 1], dp[i + 1])
可以看到, 在整个 dp 构造过程中, 只需要用到 dp[i + 1], 所以一方面可以对数组从后往前构造 dp, 另一方面也可以省略 dp 只使用一个变量来表示 dp[i + 1];
    """
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix_sum = [n for n in stones]

        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i - 1]

        result = prefix_sum[-1]

        for i in range(len(prefix_sum) - 2, 0, -1):
            result = max(result, prefix_sum[i] - result)

        return result


