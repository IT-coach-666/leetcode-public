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
title_jy = "Basic-Calculator(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string ``s`` representing an expression, implement a basic calculator to evaluate it.


Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2 - 1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:
1 <= s.length <= 3 * 10^5
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
"""


class Solution:
    """
题解遍历字符串, 如果遇到加号, 则说明当前符号位为正, 否则为负(因为字符串只包含括号, 加减号和空字符);
如果遇到左括号, 则将当前值和符号位压入栈;
如果遇到右括号, 则出栈一个符号位和之前的值, 与当前值和当前符号位进行运算;
如果遇到的是数字, 则将数字和当前符号位进行运算;
    """
    def calculate_v1(self, s: str) -> int:
        result = 0
        # jy: 记录上一个符号开始, 到当前字符截止时的数值;
        digit = 0
        # jy: 记录上一个操作符, 加号为 1 , 减号为 -1(初始化为 1);
        last_sign = 1
        stack = []
        # jy: 遍历字符串;
        for i, char in enumerate(s):
            # jy: 如果当前字符是 " ", 则直接跳过当前循环;
            if char == " ":
                continue
            # jy: 如果当前字符为数值字符, 将其转换为数值;
            if char.isdigit():
                digit = digit * 10 + int(char)
                # jy: 如果当前字符是最后一个字符, 或者其下一个字符非数值, 则表明截止当前字符已经构
                #     成一个完整的数值, 结合 last_sign 判断该数值的正负号并与 result 相加;
                if i == len(s) - 1 or not s[i+1].isdigit():
                    result += last_sign * digit
                    digit = 0
            # jy: 如果当前字符为 "+", 则更新 last_sign 为 1 ("-" 更新为 -1);
            elif char in ['+', '-']:
                last_sign = 1 if char == '+' else -1
            # jy: 如果当前字符为 ")", 则将该字符之前的数值计算结果 result 以及该字符之前的运算符(该字
            #     符的前一个有效非空字符肯定是运算符, 且还没有经过运算)先后入栈(入栈的先后顺序可以颠
            #     倒, 后续出栈时获取操作符和数值结果保持一致即可); 更新 result 为 0, last_sign 为 1
            #     (表示默认为正数值); 因此当前 "(" 到下一个 ")" 之间的字符串算术表达式的运算结果会随
            #     着循环遍历过程更新到 result 值中;
            elif char == '(':
                stack.append(result)
                stack.append(last_sign)
                result = 0
                last_sign = 1
            # jy: 如果是右括号, 则从栈中出两个元素(分别为原先左括号前的操作符和该操作符之前的运算结果,
            #     其出栈的先后顺序取决于入栈时的先后顺序), 并结合当前的 result (即原先左括号到右括号之
            #     间的字符串的运算结果) 进行运算, 更新为新的 result (当对最后一个 ")" 操作完成后, 栈肯
            #     定为空, 此时如果 ")" 之后还有运算字符串, 则会在 result 的基础上进行运算, 最终 result
            #     即为正确运算结果);
            elif char == ')':
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result

        return result


s = "1 + 1"
# Output: 2
res = Solution().calculate_v1(s)
print(res)

s = " 2-1 + 2 "
# Output: 3
res = Solution().calculate_v1(s)
print(res)


s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
res = Solution().calculate_v2(s)
print(res)


