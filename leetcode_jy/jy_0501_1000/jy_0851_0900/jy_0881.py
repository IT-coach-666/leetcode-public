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
title_jy = "Boats-to-Save-People(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.

Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)


Constraints:
1 <= people.length <= 5 * 10^4
1 <= people[i] <= limit <= 3 * 10^4
"""


from typing import List


class Solution:
    """
将人按重量排序后, 使用两个指针分别指向数组的首尾, 当 low 处和 high 处的人重量加起来小于等于 limit 时, 将其两人放入一条船并移动 low 和 high 指针, 否则就只能将 high 处的一个人单独放入一条船;
    """
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        sorted_people = sorted(people)
        low, high = 0, len(people) - 1

        while low <= high:
            if sorted_people[low] + sorted_people[high] <= limit:
                low += 1
                high -= 1
            else:
                high -= 1

            count += 1

        return count


