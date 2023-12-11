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
title_jy = "Moving-Stones-Until-Consecutive(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There are three stones in different positions on the X-axis. You are given three integers a, b, and c, the positions of the stones.
In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints. Formally, let's say the stones are currently at positions x, y, and z with x < y < z. You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.
The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).
Return an integer array answer of length 2 where:
answer[0] is the minimum number of moves you can play, and
answer[1] is the maximum number of moves you can play.

Example 1:
Input: a = 1, b = 2, c = 5
Output: [1,2]
Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

Example 2:
Input: a = 4, b = 3, c = 2
Output: [0,0]
Explanation: We cannot make any moves.

Example 3:
Input: a = 3, b = 5, c = 1
Output: [1,2]
Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.


Constraints:
1 <= a, b, c <= 100
a, b, and c have different values.
"""

from typing import List


class Solution:
    """
首先将数组排序, 如果要想移动次数最大, 那么先从一端(哪一端无所谓, 假设为 a)开始每次移动一格, 直到移动到中间的数字 b 的右边, 然后 a 和 b 交替向 c 靠拢, 移动次数等于 c - a - 2; 要想移动次数最少, 需要先判断是否有两个数字相邻, 如果存在, 则只需要将第三个数字移动到相邻的位置即可, 移动次数为1, 如果不存在, 则先将一端的数字移动到和中间数字相邻, 然后将第三个数字移动到相邻位置, 移动次数为2;
    """
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = sorted([a, b, c])
        a, b, c = stones

        if b - a == c - b == 1:
            return [0, 0]
        else:
            return [1 if min(b - a, c - b) <= 2 else 2, c - a - 2]


