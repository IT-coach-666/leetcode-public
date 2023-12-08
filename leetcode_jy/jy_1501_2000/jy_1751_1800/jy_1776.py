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
title_jy = "Car-Fleet-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:
positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.
Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10^-5 of the actual answers are accepted.

Example 1:
Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.

Example 2:
Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]


Constraints:
1 <= cars.length <= 10^5
1 <= positioni, speedi <= 10^6
positioni < positioni+1
"""


import math
from typing import List


class Solution:
    """
从后往前遍历数组(即从距离起点最远的车开始遍历), 使用栈保存每辆车的距离起点的位置, 车速, 和追上前一辆车需要的时间, 如果当前车的速度小于等于栈顶的车, 说明无法追上栈顶的车(因为从后往前遍历, 栈顶的车距离起点更远), 则将栈顶出栈; 或者当前车的速度大于栈顶的车, 但是当前车追上栈顶的车的时间大于等于栈顶的车追上它前面的车的时间, 同样将栈顶出栈, 因为在当前车追上栈顶车的时候, 栈顶的车已经追上前一辆车了, 根据题目描述, 此时栈顶的车的速度会改变(取栈顶的车和前一辆车的速度较小值), 所以当前车追上栈顶车的时间已无效;
    """
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        result = []
        stack = []

        for i in range(len(cars) - 1, -1, -1):
            position, speed = cars[i]

            while stack and (
                    speed <= stack[-1][1]
                    or self._get_collide_time(stack, position, speed)
                    >= stack[-1][2]):
                stack.pop()

            if not stack:
                stack.append((position, speed, math.inf))
                result.append(-1)
            else:
                collide_time = self._get_collide_time(stack, position, speed)
                stack.append((position, speed, collide_time))
                result.append(collide_time)

        result.reverse()

        return result

    def _get_collide_time(self, stack, position, speed):
        return (stack[-1][0] - position) / (speed - stack[-1][1])


