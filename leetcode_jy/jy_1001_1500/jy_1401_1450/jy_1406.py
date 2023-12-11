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
title_jy = "Stone-Game-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.
Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2 or 3 stones from the first remaining stones in the row.
The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.
The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.
Assume Alice and Bob play optimally.
Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end the game with the same score.

Example 1:
Input: values = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.

Example 2:
Input: values = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. The next move Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. The next move Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.

Example 3:
Input: values = [1,2,3,6]
Output: "Tie"
Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.

Example 4:
Input: values = [1,2,3,-1,-2,-3,7]
Output: "Alice"

Example 5:
Input: values = [-1,-2,-3]
Output: "Tie"


Constraints:
1 <= values.length <= 50000
-1000 <= values[i] <= 1000
"""


import sys
from typing import List


class Solution:
    """
使用动态规划求解, 记 dp[i] 表示先手从 stoneValue[i] 中拿石头比对方多的个数, 从后向前构造 dp, 对于某个位置 i 来说, 分别尝试拿1, 2, 3堆石头, 同 1140. Stone Game II, 当前玩家先拿取的石头为 sum(stoneValue[i:j + 1]), 对手在剩下的石头中拿取的最大石头个数为 dp[j + 1], 则当前玩家的石头比对方多 sum(stoneValue[i:j + 1]) - dp[j + 1] 个, 最后判断 dp[0] 和0的大小决定谁赢;
    """
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [-sys.maxsize] * n

        for i in range(n - 1, -1, -1):
            take = 0

            for j in range(i, min(n, i + 3)):
                take += stoneValue[j]
                dp[i] = max(dp[i], take - dp[j + 1] if j + 1 < n else take)

        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'


