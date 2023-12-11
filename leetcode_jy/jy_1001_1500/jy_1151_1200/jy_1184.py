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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Distance-Between-Bus-Stops(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.
The bus goes along both directions i.e. clockwise and counterclockwise.
Return the shortest distance between the given start and destination stops.

Example 1:    https://www.yuque.com/frederick/dtwi9g/vgg4ms

Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

Example 2:

Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

Example 3:

Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.


Constraints:
1 <= n <= 10^4
distance.length == n
0 <= start, destination < n
0 <= distance[i] <= 10^4
"""


from typing import List


class Solution:
    """
分别求解顺时针方向 start 到 destination 和逆时针方向 start 到 destination 的距离, 其中逆时针方向 start 到 destination 的距离等价于顺时针方向 destination 到 start 的距离; 因为入参的 start 不一定比 destination 小, 为了处理方便, 需提前处理保证 start 小于 destination;
    """
    def distanceBetweenBusStops(self, distance: List[int],
                                start: int, destination: int) -> int:
        clockwise_distance = 0
        counterclockwise_distance = 0
        start, destination = min(start, destination), max(start, destination)

        for i in range(start, destination):
            clockwise_distance += distance[i]

        i = destination

        while i != start:
            counterclockwise_distance += distance[i]
            i = (i + 1) % len(distance)

        return min(clockwise_distance, counterclockwise_distance)


