# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
from typing import List
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Container-With-Most-Water(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "双指针 (结合对题目的理解进行指针移动)"


"""
Given `n` non-negative integers a1, a2, ..., an , where each represents a
point at coordinate (i, ai). `n` vertical lines are drawn such that the two
endpoints of the line `i` is at (i, ai) and (i, 0). Find two lines, which,
together with the x-axis forms a container, such that the container contains
the most water.

Notice that you may not slant the container.


Example 1: 
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array. In this case,
             the max area of water (blue section) the container can contain is 49.
图片参考: https://www.yuque.com/it-coach/leet-code/etktv3


Example 2:
Input: height = [1,1]
Output: 1


Example 3:
Input: height = [4,3,2,1,4]
Output: 16


Example 4:
Input: height = [1,2,1]
Output: 2


Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""


class Solution:
    """
解法1: 双指针法
使用两个指针从数组的两端向中间靠拢, 当两个指针在数组的首尾时组成的矩阵的宽
(即为数组两指针之差) 最大, 移动指针时如果想要获得更大面积的矩阵, 则需要更高
的高度; 将高度较低的一端向目标方向移动, 才可能获得更高的高度, 依据此来移动
两个指针;

注意: 此题的含义是相邻两个直方图之间的宽度为 1, 可以用来蓄水; 目标即找到不
同位置的两个直方图 (只能使用 2 个直方图进行蓄水) 进行蓄水, 使得蓄水量最大;
(相邻位置的两个高度均为 1 的直方图的蓄水量即为 1, 因为最小高度为 1, 相邻位
置宽度为 1)
    """
    def maxArea_v1(self, height: List[int]) -> int:
        low, high, max_water = 0, len(height) - 1, 0
        max_height = max(height)
        while low < high:
            if height[low] < height[high]:
                # jy: 短板作为高, 结合底的长度求出蓄水面积
                max_water = max(max_water, height[low] * (high - low))
                low += 1
            else:
                max_water = max(max_water, height[high] * (high - low))
                high -= 1

            # jy: 进一步优化 (极大提高运行效率): 如果当前所求的最大蓄水量大于
            #     最大高度乘以此时的宽度, 则 low 和 high 没必要进一步缩小范围
            #     了, 直接跳出循环 (因为后续收缩后底更小, 高也不会超过最大高
            #     度, 因此蓄水面积肯定只会更小了)
            if max_water >= max_height * (high - low):
                break

        return max_water


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
res = Solution().maxArea_v1(height)
print(res)


height = [1, 1]
# Output: 1
res = Solution().maxArea_v1(height)
print(res)


height = [4, 3, 2, 1, 4]
# Output: 16
res = Solution().maxArea_v1(height)
print(res)


height = [1, 2, 1]
# Output: 2
res = Solution().maxArea_v1(height)
print(res)


