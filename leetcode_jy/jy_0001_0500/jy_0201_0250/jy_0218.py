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
title_jy = "The-Skyline-Problem(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A city's skyline is the outer contour of the silhouette formed by all  the buildings in that city when viewed
from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape
photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

图片: https://www.yuque.com/frederick/dtwi9g/zvq6h7
      https://leetcode-cn.com/problems/the-skyline-problem/

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri
are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is
guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect
rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as:
[[2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8]] .

The output is a list of "key points" (red dots in Figure B) in the format of [[x1,y1], [x2, y2], [x3, y3], ...] that
uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment.  Note that the last key
point, where the rightmost building ends, is  merely used to mark the termination of the skyline, and always has
zero height. Also, the ground in between any two adjacent buildings should be  considered part of the skyline
contour.  For instance, the skyline in Figure B should be represented as:
[[2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0]].

Notes:
1) The number of buildings in any input list is guaranteed to be in the range [0, 10000].
2) The input list is already sorted in ascending order by the left x position Li.
3) The output list must be sorted by the x position.
4) There must be no consecutive horizontal lines of equal height in the output skyline. For instance,
   [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should
   be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
"""

from typing import List

class Solution:
    """
采用分治法, 将问题分为两半分别求解, 然后合并结果集;
    """
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        # jy: 如果只有一个建筑物, 根据要求, 返回建筑物的两个坐标点(左上和右下);
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        # jy: 如果有多个建筑物, 则分而治之(分两半, 各自求解后再将两个组合起来);
        middle = len(buildings) // 2
        # jy: getSkyline 得到的是 skyline 数组结果(即数组元素为轮廓线的左上和右下坐标点)
        left_skyline = self.getSkyline(buildings[:middle])
        right_skyline = self.getSkyline(buildings[middle:])
        # jy:
        return self._merge(left_skyline, right_skyline)

    def _merge(self, left_skyline, right_skyline):
        """对两组 skyline 数组进行合并; skyline 数组的值为轮廓线的左上和右下坐标点"""
        left_height, right_height = 0, 0
        # jy: left 和 right 分别记录 left_skyline 和 right_skyline 中已合并处理完的个数;
        left, right = 0, 0
        result = []
        print("===left_skyline: %s ===right_skyline: %s" % (str(left_skyline), str(right_skyline)))
        while left < len(left_skyline) and right < len(right_skyline):
            # jy: 如果当前的 left_skyline 的横坐标小于 right_skyline 的横坐标, 依据 left_skyline 构造
            #    skyline(准备加入到 result 中), 且 left 加 1;
            if left_skyline[left][0] < right_skyline[right][0]:
                skyline = [left_skyline[left][0], max(left_skyline[left][1], right_height)]
                left_height = left_skyline[left][1]
                left += 1
            # jy: 如果当前的 left_skyline 的横坐标大于 right_skyline 的横坐标, 依据 right_skyline 构造
            #    skyline(准备加入到 result 中), 且 right 加 1;
            elif left_skyline[left][0] > right_skyline[right][0]:
                skyline = [right_skyline[right][0], max(right_skyline[right][1], left_height)]
                right_height = right_skyline[right][1]
                right += 1
            # jy: 如果当前的 left_skyline 的横坐标等于 right_skyline 的横坐标, 依据 left_skyline 构造
            #    skyline(准备加入到 result 中), 且 left 和 right 均加 1;
            else:
                skyline = [left_skyline[left][0], max(left_skyline[left][1], right_skyline[right][1])]
                left_height = left_skyline[left][1]
                right_height = right_skyline[right][1]
                left += 1
                right += 1

            if len(result) == 0 or result[-1][1] != skyline[1]:
                result.append(skyline)
        # jy: 如果仅仅剩余 left_skyline 或 right_skyline, 则将剩余部分直接加入 result;
        result.extend(left_skyline[left:] or right_skyline[right:])

        return result



buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
# output: [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
res = Solution().getSkyline(buildings)
print(res)


