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
title_jy = "Daily-Temperatures(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a list of daily temperatures T, return a list such that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature. If there is no
future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output
should be [1, 1, 4, 2, 1, 1, 0, 0].

Note:
The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
"""






from typing import List



class Solution:
    """
jy: 即找出字典当前位置之后的值且其值比当前位置的值还大的值的下标与当前位置的下标差;
使用一个栈保存遇到的温度及其下标, 遍历温度, 如果栈不为空且栈顶的温度小于当前温度, 说明遇
到了升温, 则执行出栈, 因为栈同时保存了温度对应的下标, 所以可以直接计算出升温需要的天数,
一直出栈直到栈为空或者栈顶的温度大于当前的温度, 然后将当前温度压入栈;
    """
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # jy: 先将返回结果初始化为全0
        result = [0] * len(T)
        stack = []
        # jy: 不断往栈中添加元组元素(值与该值对应的下标)
        for i, current in enumerate(T):
            # jy: 当栈不为空, 且当前值比栈顶的值大, 表明栈顶元素遇到了升温(即当前值对应的温度),
            #    此时出栈, 并将当前值的下标减去出栈值的下标, 即为下一个比出栈元素对应的温度还高
            #    的温度距离该栈元素的距离, 在该位置设置符合要去的值后, 即出栈(如果栈中的值一直符
            #    合要求, 则就不断出栈, 直到栈中的值不符合要求, 则当前值也入栈, 随后进行下一轮循
            #    环; 如果找不到符合要求的值, 则 result 数组中的值 0 也即表示没有符合要求的结果;
            while stack and stack[-1][0] < current:
                temperature, index = stack.pop()
                result[index] = i - index

            stack.append((current, i))

        return result

T = [73, 74, 75, 71, 69, 72, 76, 73]
res = Solution().dailyTemperatures(T)
print(res)


