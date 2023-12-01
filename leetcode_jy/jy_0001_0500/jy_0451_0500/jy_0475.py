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
title_jy = "Heaters(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.
Every house can be warmed, as long as the house is within the heater's warm radius range.
Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.
Notice that all the heaters follow your radius standard, and the warm radius will the same.

Example 1:
Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:
Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

Example 3:
Input: houses = [1,5], heaters = [2]
Output: 3


Constraints:
1 <= houses.length, heaters.length <= 3 * 10^4
1 <= houses[i], heaters[i] <= 10^9
"""


import bisect
from typing import List


class Solution:
    """
先将加热器排序, 然后遍历房子, 对当前房子使用二分查找搜索房子在加热器中应该插入的
位置, 来计算加热器的范围, 注意处理插入的位置在两端的情况
    """
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius = 0
        n = len(heaters)
        sorted_heaters = sorted(heaters)

        for house in houses:
            i = bisect.bisect_left(sorted_heaters, house)

            if i == 0:
                radius = max(radius, abs(house - sorted_heaters[0]))
            elif i == n:
                radius = max(radius, abs(house - sorted_heaters[-1]))
            else:
                radius = max(radius, min(abs(house - sorted_heaters[i - 1]),
                                         abs(house - sorted_heaters[i])))

        return radius


