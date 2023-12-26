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
title_jy = "Merge-Intervals(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "区间排序 + 栈 | 相似题: 0057"



"""
Given an array of `intervals` where intervals[i] = [start_i, end_i], merge all
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.


Example 1:
Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
output = [[1, 6], [8, 10], [15, 18]]
Explanation: Since intervals [1, 3] and [2, 6] overlaps, merge them into [1, 6].

Example 2:
Input: [[1, 4], [4, 5]]
output = [[1, 5]]
Explanation: Intervals [1, 4] and [4, 5] are considered overlapping.


Constraints:
1) 1 <= intervals.length <= 10^4
2) intervals[i].length == 2
3) 0 <= start_i <= end_i <= 10^4
"""



class Solution:
    """
解法 1: 区间排序 + 栈

将区间按起点排序, 然后将第一个区间放入一个栈, 从第二个区间开始遍历, 如果当前
区间和栈顶的区间相交, 则更新栈顶区间的终点, 否则当前区间入栈
    """
    def merge_v1(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # jy: 区间列表排序, 依据区间的起始位进行排序 (列表内置的 sort 方法中
        #     的 key 参数指定可迭代对象中的元素进行排序)
        intervals.sort(key=lambda x: x[0])
        #intervals = sorted(intervals, key = lambda x: x[0])
        # jy: 将第一组区间入栈
        stack = [intervals[0]]
        # jy: 从第二组区间开始遍历
        for i in range(1, len(intervals)):
            # jy: 获取栈顶(即一个最后入栈的区间)
            top = stack[-1]
            # jy: 获取当前区间
            current = intervals[i]
            # jy: 如果栈顶区间的末尾值大于当前区间开始值, 表明当前区间与栈顶区
            #     间有重合, 此时:
            #     1) 如果当前区间的末尾值大于栈顶区间的末尾值, 则更新栈顶区间的
            #        末尾值为当前区间的末尾值
            #     2) 如果当前区间的末尾值小于或等于栈顶区间的末尾值, 则表明当前
            #        区间完全被栈顶区间包含
            if top[1] >= current[0]:
                stack[-1][1] = max(stack[-1][1], current[1])
            # jy: 如果栈顶区间的末尾值小于当前区间开始值, 说明当前区间与栈顶区
            #     间没有重合, 直接将当前区间入栈
            else:
                stack.append(current)
        return stack




intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
res = Solution().merge_v1(intervals)
# jy: [[1, 6], [8, 10], [15, 18]]
print(res)


intervals = [[1, 4], [4, 5]]
res = Solution().merge_v1(intervals)
# jy: [[1, 5]]
print(res)


