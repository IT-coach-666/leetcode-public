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
title_jy = "Moving-Stones-Until-Consecutive-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
There are some stones in different positions on the X-axis. You are given an integer array stones, the positions of the stones.
Call a stone an endpoint stone if it has the smallest or largest position. In one move, you pick up an endpoint stone and move it to an unoccupied position so that it is no longer an endpoint stone.
In particular, if the stones are at say, stones = [1,2,5], you cannot move the endpoint stone at position 5, since moving it to any position (such as 0, or 3) will still keep that stone as an endpoint stone.
The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).
Return an integer array answer of length 2 where:
answer[0] is the minimum number of moves you can play, and
answer[1] is the maximum number of moves you can play.

Example 1:
Input: stones = [7,4,9]
Output: [1,2]
Explanation: We can move 4 -> 8 for one move to finish the game.
Or, we can move 9 -> 5, 4 -> 6 for two moves to finish the game.

Example 2:
Input: stones = [6,5,4,3,10]
Output: [2,3]
Explanation: We can move 3 -> 8 then 10 -> 7 to finish the game.
Or, we can move 3 -> 7, 4 -> 8, 5 -> 9 to finish the game.
Notice we cannot move 10 -> 2 to finish the game, because that would be an illegal move.


Constraints:
3 <= stones.length <= 10^4
1 <= stones[i] <= 10^9
All the values of stones are unique.
"""


from typing import List


class Solution:
    """
对于最大移动次数, 类似 1033. Moving Stones Until Consecutive, 将数组排序后以最右端的石头为例, 首先将其移动到 stones[-2] 左边的空位处(不一定存在, 不存在则找 stones[-3] 左边的空位, 依此类推), 此时原来的 stones[-2] 成为了新的端点, 再重复上述步骤, 一直到最左端的石头, 最大移动次数为 stones[-2] - stones[0] + 1 - (n - 1), stones[-2] - stones[0] + 1 表示坐标的总长度, n - 1 表示其中有 n - 1 格已经被石头占了; 同样的, 从最左边的石头开始移动的最大总移动次数为 stones[-1] - stones[1] + 1 - (n - 1), 两者取较大值;
对于最小移动次数, 使用滑动窗口求解, 维护一个长度不超过 len(stones) 的窗口, 因为最后停止移动的条件是所有石头的排列都是连续的, 此时所有石头占据坐标的长度就是 len(stones), 当窗口有效时, 需要将窗口外的石头移动到窗口内使其连续, 需要移动的次数就是 len(stones) - 窗口内石头个数), 即有多少个空位在窗口中; 另外需要处理一个特殊情况, 当 n - 1 个石头在窗口内连续排列, 只有一个石头游离在窗口外时, 需要移动的石头次数是2而不是1, 因为题目中要求从一端移动石头后这个石头不能还是端点, 例如对于排列 3, 4, 5, 6, ..., 10, 不能将10移动到6后面, 而是要先将3移动到6后两格的位置, 然后将10移动到6和3之间;
    """
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        sorted_stones = sorted(stones)
        i, n = 0, len(sorted_stones)
        low = n
        high = max(sorted_stones[-1] - sorted_stones[1] + 1 - (n - 1),
                   sorted_stones[-2] - sorted_stones[0] + 1 - (n - 1))

        for j in range(n):
            while sorted_stones[j] - sorted_stones[i] >= n:
                i += 1

            stone_size = j - i + 1

            if stone_size == n - 1 \
                    and sorted_stones[j] - sorted_stones[i] + 1 == n - 1:
                low = min(low, 2)
            else:
                low = min(low, n - stone_size)

        return [low, high]


