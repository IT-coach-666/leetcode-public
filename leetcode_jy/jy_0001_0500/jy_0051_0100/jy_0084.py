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
title_jy = "Largest-Rectangle-in-Histogram(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given an array of integers ``heights`` representing the histogram's bar height where 
the width of each bar is 1, return the area of the largest rectangle in the histogram.


Example 1:    https://www.yuque.com/frederick/dtwi9g/eohups
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1. The largest rectangle
             is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4


Constraints:
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""


from typing import List


class Solution:
    """
维护一个栈保存递增的高度的索引位置(栈中的位置索引不需要总是确保连续):
1) 如果当前栈为空或当前高度大于栈顶的高度, 则持续入栈;
2) 如果当前高度小于栈顶的高度, 则需要根据栈中的高度计算面积: 先弹出栈顶的元素, 作
   为计算面积的高, 再将当前栈顶距离当前高度所在位置下标相隔的距离作为宽度, 求得面
   积后更新至今遇到的最大面积
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        # jy: 一个栈, 用于保存递增的高度的索引位置(索引不需要连续)
        stack = []
        max_area = 0
        length = len(heights)
        i = 0

        while i <= length:
            # jy-version-1-begin: ----------------------------------------------
            """
            # jy: 如果 i 等于数组长度, 表明数组已经遍历完成, 当前位置的高度为 0;
            current_height = 0 if i == length else heights[i]
            # jy: 如果当前位置高度大于或等于栈顶对应的位置的高度, 则不断将当前位置
            #    入栈, 并将位置进一位;
            if not stack or current_height >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            """
            # jy-version-1-end: ------------------------------------------------

            # jy-version-2-begin: ----------------------------------------------
            if i < length and (not stack or heights[i] >= heights[stack[-1]]):
                stack.append(i)
                i += 1
            # jy: 如果下标 i 等于 length, 且栈为空, 则可终止(如果栈不为空, 则需要不
            #    断出栈并基于该下标 i 计算面积);
            elif i == length and not stack:
                #i += 1
                break
            # jy-version-2-end: ------------------------------------------------

            # jy: 如果当前位置 i 对应的高度小于栈顶高度, 则需要根据栈中的高度计算面积;
            #    该过程位置 i 不递进, 直到栈为空或者当前位置的高度大于栈顶位置对应的
            #    高度后, 再继续将该位置 i 入栈;
            else:
                # jy: 先出栈栈顶位置, 将该位置的值作为计算面积的高;
                high = heights[stack.pop()]
                # jy: 如果出栈后栈为空, 表明当前宽度为当前位置的下标; 否则为当前位置减
                #    去栈顶位置再减 1(以 [1, 2, 3, 1] 为例进行思考);
                width = i if not stack else i-1 - stack[-1]
                max_area = max(max_area, high * width)

        return max_area


heights = [2,1,5,6,2,3]
# Output: 10
res = Solution().largestRectangleArea(heights)
print(res)


heights = [2,4]
# Output: 4
res = Solution().largestRectangleArea(heights)
print(res)




