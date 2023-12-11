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
title_jy = "Car-Fleet(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.
You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).
A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.
The distance between these two cars is ignored (i.e., they are assumed to have the same position).
A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.
If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
Return the number of car fleets that will arrive at the destination.

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1


Constraints:
n == position.length == speed.length
1 <= n <= 10^5
0 < target <= 10^6
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 10^6
"""

from typing import List


class Solution:
    """
首先将位置和速度组合按照升序排序, 使用栈保存每辆车到达 target 的时间, 如果当前车到达 target 需要的时间小于栈顶的时间, 说明当前车会和栈顶的车在某一时刻相遇, 两者合并为一个 fleet, 如果需要的时间大于栈顶的元素, 说明当前车无法追赶上前面的车, 最终会成为一个 fleet, 则将当前时间入栈, 最后栈的大小就是要求的个数;
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) \
            -> int:
        stack = []

        for position, car_speed in sorted(zip(position, speed), reverse=True):
            distance = target - position

            if not stack:
                stack.append(distance / car_speed)
            elif distance / car_speed > stack[-1]:
                stack.append(distance / car_speed)

        return len(stack)


