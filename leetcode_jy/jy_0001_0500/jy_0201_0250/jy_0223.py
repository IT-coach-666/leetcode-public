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
title_jy = "Rectangle-Area(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

图见: https://www.yuque.com/frederick/dtwi9g/vc8nb6

Example:
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45

Note:Assume that the total area is never beyond the maximum possible value of int.
"""


class Solution:
    """
两个矩形的面积相加然后减去相交部分的面积, 关键在于求相交部分的面积; 观察图可得:
1) 相交部分横轴的左坐标为两个矩形左下角横坐标的较大值
2) 相交部分横轴的右坐标为两个矩形右上角横坐标的较小值
3) 相交部分纵轴的上坐标为两个矩形右上角纵坐标的较小值
4) 相交部分纵轴的下坐标为两个矩形左下角纵坐标的较大值
    """
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = abs((C - A) * (D - B))
        area2 = abs((G - E) * (H - F))
        overlap_area = 0 if not self._is_overlap(A, B, C, D, E, F, G, H) \
                         else (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))

        return area1 + area2 - overlap_area

    def _is_overlap(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> bool:
        '''
        判断 [(A, B) (C, D)] 和 [(E, F) (G, H)] 组成的两个矩形是否相交
        '''
        # return not E >= C or A >= G or B >= H or D <= F
        return E < C and A < G and B < H and D > F

A = -3
B = 0
C = 3
D = 4
E = 0
F = -1
G = 9
H = 2
# Output: 45
res = Solution().computeArea(A, B, C, D, E, F, G, H)
print(res)


