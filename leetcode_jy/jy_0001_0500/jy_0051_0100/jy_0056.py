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
tag_jy = ""



"""
Given a collection of intervals, merge all overlapping intervals.


Example 1:
Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
output = [[1, 6], [8, 10], [15, 18]]
Explanation: Since intervals [1, 3] and [2, 6] overlaps, merge them into [1, 6].

Example 2:
Input: [[1, 4], [4, 5]]
output = [[1, 5]]
Explanation: Intervals [1, 4] and [4, 5] are considered overlapping.


NOTE: input types have been changed on April 15, 2019. Please reset to
default code definition to get new method signature.
"""



from typing import List
class Solution:
    """
将区间按照起点排序, 然后将第一个区间放入一个栈, 从第二个区间开始遍历, 如果当前区间和栈顶
的区间相交, 则更新栈顶区间的终点, 否则当前区间入栈;
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # jy: 区间列表排序, 依据区间的起始位进行排序(sort 方法中的 key 参数指定可迭代对象中
        #    的一个元素来进行排序);
        intervals.sort(key=lambda x: x[0])
        # jy: 将第一组区间入栈;
        stack = [intervals[0]]
        # jy: 从第二组区间开始遍历;
        for i in range(1, len(intervals)):
            # jy: 获取栈顶(即一个最后入栈的区间)
            top = stack[-1]
            # jy: 获取当前区间
            current = intervals[i]
            # jy: 如果栈顶的区间开始值 <= 当前区间开始值 <= 当前区间末尾值, 则更新栈顶的区
            #    间末尾值为当前区间的末尾值(如果当前区间末尾值较大的话);  实际上, 如果区间
            #    值都是正确无误的, 即末尾值大于开始值, 则经过排序后 top[0] <= current[0] 是
            #    确保成立的;
            #if top[0] <= current[0] <= top[1]:
            if top[1] >= current[0]:
                stack[-1][1] = max(stack[-1][1], current[1])
            else:
                stack.append(current)
        return stack

    def merge_jy(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= res[-1][1]:
                if i[1] > res[-1][1]:
                    res[-1][1] = i[1]
            else:
                res.append(i)
        # print(res)
        return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# output = [[1, 6], [8, 10], [15, 18]]
res = Solution().merge(intervals)
print(res)


intervals = [[1, 4], [4, 5]]
# output = [[1, 5]]
res = Solution().merge_jy(intervals)
print(res)


