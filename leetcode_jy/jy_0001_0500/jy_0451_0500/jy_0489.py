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
title_jy = "Robot-Room-Cleaner(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a robot cleaner in a room modeled as a grid. Each cell in the grid can be empty or blocked. The
robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90
degrees. When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it
stays on the current cell. Design an algorithm to clean the entire room using only the 4 given APIs
shown below.

All grids in the room are marked by either 0 or 1. 0 means the cell is blocked, while 1 means the
cell is accessible.

interface Robot {
    # returns true if next cell is open and robot moves into the cell.
    # returns false if next cell is obstacle and robot stays on the current cell.
    boolean move();

    # Robot will stay on the same cell after calling turnLeft/turnRight.
    # Each turn will be 90 degrees.
    void turnLeft();
    void turnRight();

    # Clean the current cell.
    void clean();
}


Example:
Input:
room = \
[ [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]],
row = 1,
col = 3
Explanation: The robot initially starts at the position of row=1, col=3. From the top left
             corner, its position is one row below and three columns right.


Notes:
1) The input is only given to initialize the room and the robot's position internally. You must solve
   this problem "blindfolded". In other words, you must control the robot using only the mentioned 4 APIs,
   without knowing the room layout and the initial robot's position.
2) The robot's initial position will always be in an accessible cell.
3) The initial direction of the robot will be facing up.
4) All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
5) Assume all four edges of the grid are all surrounded by wall.
"""


class Solution:
    """
一般类似路径探索的题需要保存已访问过的路径, 但本题无法直接访问二维数组, 所以不能
使用数组的行, 列来记录走过的路径;

可以以机器人的起始位置为原点建立坐标系, 机器人每走一步的坐标就可以通过上一步的坐
标推算而来, 例如, 机器人起始位置为 (0, 0), 机器人朝北, 向前走一步后的坐标为 (0, 1),
(注意: 此处的坐标不是二维数组的数值对应的下标位置, 而是直角坐标系的坐标; 因为此题
要求无法直接访问二维数组, 不能知道二维数组的位置坐标, 因此改用直角坐标系的方式),
这样就可以保存机器人至今走过的路径了;

因为机器人可以向四个方向探索, 不妨按照顺时针的方向(即向右)探索, 由于探索时需要计
算下一个坐标, 所以需要传递向四个方向前进时坐标的变化量, 在上, 右, 下, 左的情况下,
坐标的变化量为 (0, 1), (1, 0), (0, -1), (-1, 0), (注意: 此处的四个方向是基于直角
坐标系上的方向, 不是二维数组的数值对应的位置方向)即当前坐标加上对应方向的变化量求
得该方向上前进一步后的坐标;

在每个方向上探索时, 先判断前进方向的坐标是否已被访问, 以及机器人是否可以前进, 如果
可以前进, 则递归调用进行探索, 探索完成后需要将机器人复位的原来的位置, 这样机器人才
能转向去下一个方向探索, 否则机器人打扫不了所有的房间, 如下面的例子:
room = [0 1
        1 1]
row = 1
col = 1
机器人初始位置为 (1, 1), 往上走到 (0, 1) 清理房间后, 由于前方无路可走, 则右转, 同样
无路可走, 继续右转, 面向 (1, 1), 由于 (1, 1) 已经访问过, 则继续右转, 也是无路可走,
再次右转, 至此针对 (0, 1) 的递归结束, 对于 (1, 1) 来说, 它结束了往上的探索, 现在需要
右转向右探索, 但此时机器人的位置还在 (0, 1) 处, 右转没有意义, 所以需要回溯使机器人回
到原来的位置;

这里复位采用右转两次, 然后前进一格, 然后左转两次的方式; 一个方向探索完成后, 让机器人
右转, 换下一个方向探索;
    """
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # jy: 最开始的遍历的坐标是第二和三个参数组成的 (0, 0), 方向是第四和五个参数组成的 (0, 1),
        #    即机器人朝北(朝上);
        self._dfs(robot, 0, 0, 0, 1, set())

    def _dfs(self, robot, x, y, direction_x, direction_y, visited):
        # jy: 打扫当前坐标系 (x, y), 并将该坐标系加入已访问集合;
        robot.clean()
        visited.add((x, y))
        # jy: 循环四次, 最开始 (direction_x, direction_y) 为 (0, 1), 每次循环时均按以下方式进行变换:
        #    direction_x, direction_y = direction_y, -direction_x
        #    则剩下三次得到的 (direction_x, direction_y) 分别为 (1, 0), (0, -1), (-1, 0), 即当前坐标
        #    位上的四个方位均已涉及;
        for _ in range(4):
            neighbour_x = x + direction_x
            neighbour_y = y + direction_y
            # jy: 如果该坐标位置还未被访问, 且可以朝当前的方位前进, 则向当前方向前进并打扫;
            if (neighbour_x, neighbour_y) not in visited and robot.move():
                self._dfs(robot, neighbour_x, neighbour_y, direction_x, direction_y, visited)
                # jy: 前进打扫完后, 则回到原位置: 右转两次(即右转 180 度)后移动一位(即往刚刚前进的方
                #    向相反处回退一位, 回到原位置), 然后再左转 2 次(即左转 180 度)使得与原先位置的原
                #    先方向相同;
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            # jy: 然后再右转一次(右转 90 度), 每次循环均右转(顺时针) 90 度, 循环 4 次后即四个方向均遍历到;
            robot.turnRight()
            direction_x, direction_y = direction_y, -direction_x

room = [
 [1, 1, 1, 1, 1, 0, 1, 1],
 [1, 1, 1, 1, 1, 0, 1, 1],
 [1, 0, 1, 1, 1, 1, 1, 1],
 [0, 0, 0, 1, 0, 0, 0, 0],
 [1, 1, 1, 1, 1, 1, 1, 1]],
row = 1,
col = 3


