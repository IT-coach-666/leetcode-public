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
title_jy = "Stone-Game-V(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.
In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.
The game ends when there is only one stone remaining. Alice's is initially zero.
Return the maximum score that Alice can obtain.

Example 1:
Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

Example 2:
Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28

Example 3:
Input: stoneValue = [4]
Output: 0


Constraints:
1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 10^6
"""

from typing import List


class Solution:
    """
由于需要计算子数组的和, 先构造前缀和数组; 对于区间 [0, n - 1], 依次对区间进行截断, 判断两断区间的数组和, 如果左区间比右区间大, 则继续在右区间进行游戏; 如果左区间比右区间小, 则继续在左区间进行游戏; 如果两个区间一样大, 则在两个区间都进行游戏取分值较大者; 此外还需要一个优化, 否则会超时, 当左区间和右区间数组和的较小值小于等于至今最高分值的一半时, 则跳过当次循环, 没有必要继续下去;
    """
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix_sum = [i for i in stoneValue]

        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]

        return self._dfs(0, n - 1, prefix_sum, {})

    def _dfs(self, start, end, prefix_sum, memo):
        if start == end:
            return 0

        if (start, end) in memo:
            return memo[(start, end)]

        max_score = 0

        for i in range(start, end):
            left_start, left_end = start, i
            right_start, right_end = i + 1, end
            left_sum = prefix_sum[left_end] - (prefix_sum[left_start - 1]
                                               if left_start - 1 >= 0 else 0)
            right_sum = prefix_sum[right_end] - prefix_sum[right_start - 1]
            score = 0

            if 2 * min(left_sum, right_sum) <= max_score:
                continue
            elif left_sum > right_sum:
                score = right_sum + self._dfs(
                    right_start, right_end, prefix_sum, memo)
            elif right_sum > left_sum:
                score = left_sum + self._dfs(
                    left_start, left_end, prefix_sum, memo)
            else:
                left_score = left_sum + self._dfs(
                    left_start, left_end, prefix_sum, memo)
                right_score = right_sum + self._dfs(
                    right_start, right_end, prefix_sum, memo)
                score = max(left_score, right_score)

            max_score = max(max_score, score)

        memo[(start, end)] = max_score

        return max_score


