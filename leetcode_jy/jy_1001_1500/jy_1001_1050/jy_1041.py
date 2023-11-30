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
title_jy = "Robot-Bounded-In-Circle(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot 
can receive one of three instructions:
"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.

The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot 
never leaves the circle.



Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns 
             to (0,0). When repeating these instructions, the robot remains in the circle 
             of radius 2 centered at the origin.

Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.

Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...



Constraints:
1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
"""



class Solution:
    """
使用 dx, dy 表示机器人向 x 和 y 轴前进时的向量增量, 初始 dx = 0, dy = 1 (因为机器人初
始朝向北, 前进时 y 轴向量进 1), 遍历指令, 计算最后机器人所在的位置和 dx, dy, 如果 dx, dy 不是 (0, 1), 则说明最终机器人发生了转向,
不管是转向左还是转向右, 最终都会再次转到原点; 

另一种情况是机器人最后又回到了原点, 不管面向何方, 最终也陷入环中; 
    """
    def isRobotBounded(self, instructions: str) -> bool:
        # jy: dx 和 dy 表示机器人向 x 和 y 轴前进时的向量增量, 初始 dx = 0, dy = 1(因为机器人
        #    初始朝向北, 前进时 y 轴向量进 1);
        dx, dy = 0, 1
        # jy: 记录机器人当前所在坐标位置;
        x = y = 0

        for instruction in instructions:
            # jy: 如果指令为 'G', 则机器人的坐标位置更新为 (x + dx, y + dy)
            if instruction == 'G':
                x, y = x + dx, y + dy
            # jy: 如果指令为 'L', 则 dx 变为原先的 -dy, dy 变为原先的 dx; 如当前朝向为
            #    北(即 dx = 0, dy = 1), 则向左转后, dx = -1, dy = 0;
            elif instruction == 'L':
                dx, dy = -dy, dx
            # jy: 如果指令为 'R', 
            elif instruction == 'R':
                dx, dy = dy, -dx

        return (dx, dy) != (0, 1) or (x == 0 and y == 0)


instructions = "GGLLGG"
# Output: true
res = Solution().isRobotBounded(instructions)
print(res)


instructions = "GG"
# Output: false
res = Solution().isRobotBounded(instructions)
print(res)


instructions = "GL"
# Output: true
res = Solution().isRobotBounded(instructions)
print(res)



