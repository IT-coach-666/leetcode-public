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
title_jy = "Height-Checker(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students to be
standing in non-decreasing order of height.

Notice that when a group of students is selected they can reorder in any possible way
between themselves and the non selected students remain on their seats.



Example 1:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation:
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.

Example 2:
Input: heights = [5,1,2,3,4]
Output: 5

Example 3:
Input: heights = [1,2,3,4,5]
Output: 0



Constraints:
1 <= heights.length <= 100
1 <= heights[i] <= 100
"""


from typing import List
import collections


class Solution:
    """
解法1: 比较原数组和排序后的数组, 如果相同位置的数字不同, 则说明当前位置的数字需要调整顺序;
    """
    def heightChecker_v1(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0

        for i, n in enumerate(heights):
            if n != sorted_heights[i]:
                count += 1

        return count


    """
解法2: 借助 Counting sort (计数排序) 的思想:
1) 首先遍历 heights 计算出每个高度出现的次数, 记为 counts, 记 current_height 为在 heights
   有序的情况下的当前高度
2) 然后遍历 heights, 如果 current_height 和实际的当前高度不同, 说明当前位置的数字需要调整
   顺序, 每次遍历的同时更新 counts 中对应 current_height 的次数;
    """
    def heightChecker_v2(self, heights: List[int]) -> int:
        # jy: 遍历 heights 计算出每个高度出现的次数;
        counts = collections.Counter(heights)
        # jy: 当前高度初始化为 1(即 1 是最低的);
        current_height, count = 1, 0
        # jy: 遍历 heights;
        for height in heights:
            # jy: 如果当前高度不存在于 counts 中, 则不断增加当前高度, 直到当前高度在 counts 中,
            #    该高度即为 heights 中的当前最低高度;
            while counts[current_height] == 0:
                current_height += 1
            # jy: 如果当前最低高度不等于 heights 中的第一个位置的高度, 说明第一个位置的高度不是
            #    最终排序的位置, 此时 count 加 1;
            if current_height != height:
                count += 1
            # jy: 当前高度确认后, 其在 counts 中的个数减 1;
            counts[current_height] -= 1

        return count


heights = [1,1,4,2,1,3]
# Output: 3
res = Solution().heightChecker_v1(heights)
print(res)


heights = [5,1,2,3,4]
# Output: 5
res = Solution().heightChecker_v1(heights)
print(res)


heights = [1,2,3,4,5]
# Output: 0
res = Solution().heightChecker_v1(heights)
print(res)


