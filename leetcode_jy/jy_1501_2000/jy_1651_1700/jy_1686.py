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
title_jy = "Stone-Game-VI(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Alice and Bob take turns playing a game, with Alice starting first.
There are n stones in a pile. On each player's turn, they can remove a stone from the pile and receive points based on the stone's value. Alice and Bob may value the stones differently.
You are given two integer arrays of length n, aliceValues and bobValues. Each aliceValues[i] and bobValues[i] represents how Alice and Bob, respectively, value the ith stone.
The winner is the person with the most points after all the stones are chosen. If both players have the same amount of points, the game results in a draw. Both players will play optimally. Both players know the other's values.
Determine the result of the game, and:
If Alice wins, return 1.
If Bob wins, return -1.
If the game results in a draw, return 0.

Example 1:
Input: aliceValues = [1,3], bobValues = [2,1]
Output: 1
Explanation:
If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
Bob can only choose stone 0, and will only receive 2 points.
Alice wins.

Example 2:
Input: aliceValues = [1,2], bobValues = [3,1]
Output: 0
Explanation:
If Alice takes stone 0, and Bob takes stone 1, they will both have 1 point.
Draw.

Example 3:
Input: aliceValues = [2,4,3], bobValues = [1,6,7]
Output: -1
Explanation:
Regardless of how Alice plays, Bob will be able to have more points than Alice.
For example, if Alice takes stone 1, Bob can take stone 2, and Alice takes stone 0, Alice will have 6 points to Bob's 7.
Bob wins.


Constraints:
n == aliceValues.length == bobValues.length
1 <= n <= 10^5
1 <= aliceValues[i], bobValues[i] <= 100
"""

from typing import List


class Solution:
    """
将 aliceValues[i] + bobValues[i] 倒序排序, 因为 Alice 取一块石头等价于 Bob 不能拿那块石头, 所以将两者分值和排序来保证 Alice 尽可能拿的分多, 排序时保留石头在数组中的原始位置; 之后遍历分值, 按照 Alice 先 Bob 后的顺序计算两人的分数;
    """
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        scores = [(aliceValues[i] + bobValues[i], i)
                  for i in range(len(aliceValues))]
        scores.sort(reverse=True)

        alice_score, bob_score = 0, 0

        for i in range(len(scores)):
            _, j = scores[i]

            if i & 1 == 0:
                alice_score += aliceValues[j]
            else:
                bob_score += bobValues[j]

        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        else:
            return 0


