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
title_jy = "Max-Points-on-a-Line(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of `points` where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1: 图示: https://www.yuque.com/it-coach/leetcode/rem5z0ic071pngnu
Input: points = [[1, 1], [2, 2], [3, 3]]
Output: 3

Example 2: 图示: https://www.yuque.com/it-coach/leetcode/rem5z0ic071pngnu
Input: points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
Output: 4
 

Constraints:
1) 1 <= points.length <= 300
2) points[i].length == 2
3) -10^4 <= xi, yi <= 10^4
4) All the points are unique.
"""


class Solution:
    """
解法 1: 枚举直线 + 枚举统计, 时间复杂度 O(n^3), 空间复杂度 O(1)
https://leetcode.cn/problems/max-points-on-a-line/solutions/842391/gong-shui-san-xie-liang-chong-mei-ju-zhi-u44s/
    """
    def maxPoints_v1(self, points: List[List[int]]) -> int:
        n, ans = len(points), 1
        for i, x in enumerate(points):
            for j in range(i + 1, n):
                y = points[j]
                # 枚举点对 (i,j) 并统计有多少点在该线上, 起始 cnt = 2 代表只有 i 和 j 两个点在此线上
                cnt = 2
                for k in range(j + 1, n):
                    p = points[k]
                    s1 = (y[1] - x[1]) * (p[0] - y[0])
                    s2 = (p[1] - y[1]) * (y[0] - x[0])
                    if s1 == s2: cnt += 1
                ans = max(ans, cnt)
        return ans

    """
解法 2: 枚举直线 + 哈希表统计

根据「朴素解法」的思路，枚举所有直线的过程不可避免，但统计点数的过程可以优化。

具体的，我们可以先枚举所有可能出现的 直线斜率（根据两点确定一条直线，即枚举所有的「点对」），使用「哈希表」统计所有 斜率 对应的点的数量，在所有值中取个 maxmaxmax 即是答案。

一些细节：在使用「哈希表」进行保存时，为了避免精度问题，我们直接使用字符串进行保存，同时需要将 斜率 约干净。


枚举所有直线的复杂度为 O(n^2), 令坐标值的最大差值为 m, gcd 复杂度为 O(log ⁡m), 整体复杂度为 O(n^2 × log ⁡m); 空间复杂度 O(n)
    """
    def maxPoints_v2(self, points):
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        
        n, ans = len(points), 1
        for i in range(n):
            mapping = {}
            maxv = 0
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                a, b = x1 - x2, y1 - y2
                k = gcd(a, b)
                key = str(a // k) + "_" + str(b // k)
                mapping[key] = mapping.get(key, 0) + 1
                maxv = max(maxv, mapping[key])
            ans = max(ans, maxv + 1)    
        return ans

    
points = [[1, 1], [2, 2], [3, 3]]
res = Solution().maxPoints_v1(points)
# jy: 3
print(res)


points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
res = Solution().maxPoints_v2(points)
# jy: 4
print(res)
