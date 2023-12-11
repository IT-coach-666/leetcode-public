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
title_jy = "Different-Ways-to-Add-Parentheses(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string expression of numbers and operators, return all possible results from computing all
the different possible ways to group numbers and operators. You may return the answer in any order.


Example 1:
Input: expression = "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
(2*((3-4)*5)) = -10
((2*(3-4))*5) = -10
(((2*3)-4)*5) = 10
((2*3)-(4*5)) = -14


Constraints:
1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
"""


from typing import List

class Solution:
    """
遍历表达式, 如果遇到 +-*, 则以运算符为界, 分别递归调用计算运算符左边的值, 和运算符右边的值, 然后
根据运算符计算整个表达式的值;
    """
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        # jy: 循环遍历字符串表达式, 将每个运算符的左右两侧进行递归求解;
        for i, c in enumerate(expression):
            if c not in '+-*':
                continue
            # jy: 如果遍历的字符为运算符之一('+-*'中的一个), 则递归求解运算符左侧与运算符右侧的运算结果;
            #    如果运算符的一侧对应的表达式中仍含有多个运算符, 计算的结果会有多个, 会放入列表中返回;
            part1 = self.diffWaysToCompute(expression[0:i])
            part2 = self.diffWaysToCompute(expression[i+1:])
            # jy: 依据运算符左右两侧的运算结果计算最终的结果;
            for n1 in part1:
                for n2 in part2:
                    if c == '+':
                        result.append(n1 + n2)
                    elif c == '-':
                        result.append(n1 - n2)
                    elif c == '*':
                        result.append(n1 * n2)

        if not result:
            result.append(int(expression))

        return result


expression = "2-1-1"
# Output: [0, 2]
res = Solution().diffWaysToCompute(expression)
print(res)

expression = "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
res = Solution().diffWaysToCompute(expression)
print(res)


