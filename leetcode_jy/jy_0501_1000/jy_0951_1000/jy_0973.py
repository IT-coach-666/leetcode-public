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
title_jy = "K-Closest-Points-to-Origin(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in.)



Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)



Note:
1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""


from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    """
解法1: 根据所有点的距离排序, 然后取前 K 个值;
    """
    def kClosest_v1(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = sorted(points, key=lambda x: pow(x[0], 2) + pow(x[1], 2))

        return distance[:K]


    """
解法2: 类似 703_Kth-Largest-Element-in-a-Stream.py 的解法 2, 维护一个各个点到原点的距
离的最小堆, 遍历坐标, 每次往堆中插入一个距离, 如果堆的大小超过 K, 则删除堆顶的元素, 为
了删除堆顶元素时删除的是距离最大的坐标, 最小堆中存储的数据实际上是距离的相反数以及坐标
的下标所组成的元组;
    """
    def kClosest_v2(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []

        heap = [(-(pow(points[0][0], 2) + pow(points[0][1], 2)), 0)]
        heapify(heap)

        for i in range(1, len(points)):
            heappush(heap, (-(pow(points[i][0], 2) + pow(points[i][1], 2)), i))

            if len(heap) > K:
                heappop(heap)
        # jy: x[1] 为坐标位置的下标;
        return [points[x[1]] for x in heap]



points = [[1,3],[-2,2]]
K = 1
# Output: [[-2,2]]
res = Solution().kClosest_v1(points, K)
print(res)


points = [[3,3],[5,-1],[-2,4]]
K = 2
# Output: [[3,3],[-2,4]]
res = Solution().kClosest_v2(points, K)
print(res)


