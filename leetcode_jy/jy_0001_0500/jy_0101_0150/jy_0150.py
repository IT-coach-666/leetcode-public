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
title_jy = "Evaluate-Reverse-Polish-Notation(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Evaluate the value of an arithmetic expression in ``Reverse Polish Notation``. Valid
operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero. It is guaranteed
that the given RPN expression is always valid. That means the expression would always
evaluate to a result, and there will not be any division by zero operation.


Example 1:
Input: tokens = ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
             ((10 * (6 / (12 * -11))) + 17) + 5
             ((10 * (6 / -132)) + 17) + 5
             ((10 * 0) + 17) + 5
             (0 + 17) + 5
             17 + 5
             22


Constraints:
1 <= tokens.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

from typing import List

class Solution:
    """
栈的应用: 遍历 tokens, 如果是数字则入栈, 如果是操作符, 则出栈两个数字(注意这里出栈数字的顺序, 因
为 a-b 与 b-a 是有区别的), 第一个出栈的为操作符右边的数, 第二个出栈的为操作符左边的数, 根据操作符
对两个数字进行计算, 然后将结果入栈, 最后返回栈顶的元素就是最终的结果(最后的栈中只有一个元素);
    """
    def evalRPN(self, tokens: List[str]) -> int:
        digits = []

        for token in tokens:
            # jy: 除了这四种运算符外, 其它字符均为有效数值字符, 将其转换为 int 类型, 加入列表(栈);
            if token not in ['+', '-', '*', '/']:
                digits.append(int(token))
            # jy: 如果是操作符, 则出栈两个元素(注意, 先出栈的元素是后一个元素), 接着判断是哪种操作
            #    符, 进行相应的运算即可;
            else:
                digit2 = digits.pop()
                digit1 = digits.pop()

                if token == '+':
                    digits.append(digit1 + digit2)
                elif token == '-':
                    digits.append(digit1 - digit2)
                elif token == '*':
                    digits.append(digit1 * digit2)
                elif token == '/':
                    digits.append(int(digit1 / digit2))

        return digits[0]


tokens = ["2", "1", "+", "3", "*"]
# Output: 9
res = Solution().evalRPN(tokens)
print(res)


tokens = ["4", "13", "5", "/", "+"]
# Output: 6
res = Solution().evalRPN(tokens)
print(res)


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
res = Solution().evalRPN(tokens)
print(res)


