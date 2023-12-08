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
title_jy = "Basic-Calculator-II(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string ``s`` which represents an expression, evaluate this expression and return
its value. The integer division should truncate toward zero.


Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5


Constraints:
1 <= s.length <= 3 * 10^5
``s`` consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
``s`` represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 2^31-1].
The answer is guaranteed to fit in a 32-bit integer.
"""


class Solution:
    """
解法1: 遍历字符串, 用 last_operator 记录上一个遇到的操作符; 用 digit 记录上一个操作符开始到当前字
符为止的数值大小, 如果当前字符为一个操作符或者已经是字符串的末尾, 即表明 digit 已经构建完整, 可对
上一个操作符进行相应的运算:
1) 如果上一个操作符是 "+", 将当前 digit 入栈(由于后面有可能有优先级更高的 "*" 或 "/" 运算符, 遇
   到 "+" 时不能直接相加后入栈, 遇到 "-" 同理);
2) 如果上一个操作符是 "-", 则将当前 digit 的相反数入栈;
3) 如果上一个操作符是 "*" 或 "/", 则出栈顶元素和当前数字相乘或相除后入栈;

最后返回栈中元素之和

注意: 这里整数除法要求趋向 0 取整, 而 Python 处理负数除法即 a // b 时是趋向负
无穷取整(即趋向于更小的那个值, 如 -3 // 2 为 -2), 这里要用 int(a / b) 处理;

JY: 该字符串操作不含使用括号改变运算优先级的情况;
    """
    def calculate_v1(self, s: str) -> int:
        # jy: 记录上一个遇到的操作符(默认为 "+");
        last_operator = '+'
        stack = []
        # jy: 记录从上一个操作符开始, 截止当前字符为止对应的数值(初始化为 0);
        digit = 0
        # jy: 遍历字符串中的每个字符以及该字符的位置下标;
        for i, char in enumerate(s):
            # jy: 如果当前字符是数字字符, 则将其转换为截止当前字符为止的数值大小;
            if char.isdigit():
                digit = digit * 10 + int(char)
            # jy: 如果当前字符是操作符或者已经是字符串中的最后一个字符(即从上一个操作符开始, 截
            #     止到当前字符为止的数值 digit 已经构建完整, 可以结合上一个操作符进行运算操作),
            #     则依据上一个操作符以及栈顶元素进行相关运算操作后入栈:
            #     1) 如果上一个操作符是 "+", 则直接将 digit 入栈即可(最终栈中的元素会进行加和);
            #     2) 如果上一个操作符是 "-", 表明要减当前 digit, 则将 digit 的相反数入栈;
            #     3) 如果上一个操作符是 "*" 或 "/", 则从栈顶出一个元素与当前 digit 数值进行相关
            #        的运算操作(相乘或相除), 随后将运算结果继续入栈;
            #     对上一个操作符(last_operator)进行完相关的运算操作后, 将 last_operator 更新为当
            #     前碰到的操作符, 并将 digit 更新为 0, 继续进行下一轮循环;
            if char in '+-*/' or i == len(s) - 1:
                if last_operator == '+':
                    stack.append(digit)
                elif last_operator == '-':
                    stack.append(-digit)
                elif last_operator == '*':
                    stack.append(stack.pop() * digit)
                elif last_operator == '/':
                    # jy: 注意此处要使用 int(a / b) 的形式处理(针对 python3.x); 如果是 python2.x, 则
                    #     需 int(a / float(b)));
                    # jy: a 除以 b 时将小数部分 truncate 掉不能简单的进行 a // b, 针对于均为正数时, 该
                    #     方式符合要求, 但如果一正一负时不满足要求, 如 -3 // 2 的结果为 -2 (python3 中);
                    stack.append(int(stack.pop() / digit))

                digit = 0
                last_operator = char
        # jy: 最终返回栈中的元素值的加和结果;
        return sum(stack)

    """
解法2: 将解法 1 中的栈优化掉(减少内存消耗): 由于 v1 的栈中, 如果累积超过 2 个元
素, 表明前两个元素肯定是要相加的, 因此相加的结果其实还是可以优化为栈中只有 2 个
元素, 那其实可以用两个变量来保存这两个元素, 栈中要相加的结果用 result 记录, 另
一个待处理的元素用 last_digit 记录;
    """
    def calculate_v2(self, s: str) -> int:
        # jy: 记录原先栈中除栈顶元素之外的其它元素的累加结果;
        result = 0
        # jy: 记录上一个操作符之前的那个数值(即原先的栈顶元素数值);
        last_digit = 0

        # jy: 记录上一个操作符;
        last_operator = '+'
        # jy: 记录从上一个操作符开始到当前字符为止的数值;
        digit = 0

        for i, c in enumerate(s):
            if c.isdigit():
                digit = digit * 10 + int(c)

            if c in '+-*/' or i == len(s) - 1:
                if last_operator == '+':
                    # jy: 如果是使用栈的方式, 则需要将 digit 入栈(如果该数值入栈, 原先的栈顶(即 last_digit
                    #     代表的值)将不再是栈顶元素), 即 last_digit 需要将其加入到 result 中, 并将 last_digit
                    #     更新为 digit;
                    result += last_digit
                    last_digit = digit
                elif last_operator == '-':
                    # jy: 原本需要将 -digit 入栈, (如果该数值入栈, 原先的栈顶(即 last_digit 代表的值)将不再是
                    #     栈顶元素), 即 last_digit 需要将其加入到 result 中, 并将 last_digit 更新为 -digit;
                    result += last_digit
                    last_digit = -digit
                elif last_operator == '*':
                    last_digit *= digit
                elif last_operator == '/':
                    last_digit = int(last_digit / digit)

                last_operator = c
                digit = 0
        # jy: result 为原先栈中除栈顶元素之外的其它元素的累加结果, last_digit 为原先的栈顶元素;
        return result + last_digit

    def calculate_2022_02_23(self, s: str) -> int:
        stack = []
        last_operator = "+"
        digit = 0
        for idx, char in enumerate(s):
            # jy: 没有含义的代码补充, 注释掉
            # if char.isspace():
            #     pass

            # jy: 注意, 以下两层外层 if 判断不能将其改造成 if...elif... 结构, 因为假如改成该
            #     结构, 如果最后一个字符为数值字符, 则转换为 digit 后, 不会再进行基于 last_operator
            #     的相关算术运算, 是不符合预期的;
            if char.isdigit():
                digit = digit * 10 + int(char)

            # if char in ["+", "-", "*", "/"] or idx == len(s) - 1:
            if char in "+-*/" or idx == len(s) - 1:
                if last_operator == "+":
                    stack.append(digit)
                elif last_operator == "-":
                    stack.append(-digit)
                elif last_operator == "*":
                    prev_digit = stack.pop()
                    stack.append(prev_digit * digit)
                elif last_operator == "/":
                    prev_digit = stack.pop()
                    stack.append(int(prev_digit / digit))
                digit = 0
                last_operator = char
        return sum(stack)

    def calculate_2022_02_23_v2(self, s: str) -> int:
        prev_sum = 0
        last_val = 0
        last_operator = "+"
        digit = 0
        for idx, char in enumerate(s):
            if char.isdigit():
                digit = digit * 10 + int(char)

            if char in ["+", "-", "*", "/"] or idx == len(s) - 1:
                if last_operator == "+":
                    prev_sum += last_val
                    last_val = digit
                elif last_operator == "-":
                    prev_sum += last_val
                    last_val = -digit
                elif last_operator == "*":
                    last_val = last_val * digit
                elif last_operator == "/":
                    last_val = int(last_val / digit)
                digit = 0
                last_operator = char
        # jy: 注意最后不能只返回 prev_sum, 还要加上 last_val;
        return prev_sum + last_val


s = "3+2*2"
# Output: 7
res = Solution().calculate_v1(s)
print(res)


s = " 3/2 "
# Output: 1
res = Solution().calculate_v2(s)
print(res)


s = " 3+5 / 2 "
# Output: 5
res = Solution().calculate_v1(s)
print(res)


