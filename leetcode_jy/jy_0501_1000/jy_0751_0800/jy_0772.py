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
title_jy = "Basic-Calculator-III(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Implement a basic calculator to evaluate a simple expression string. The expression
string contains only non-negative integers, '+', '-', '*', '/' operators, and open
'(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results
will be in the range of [-2^31, 2^31 - 1].


Example 1:
Input: s = "1+1"
Output: 2

Example 2:
Input: s = "6-4/2"
Output: 4

Example 3:
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21

Example 4:
Input: s = "(2+6*3+5-(3*14/7+2)*5)+3"
Output: -12

Example 5:
Input: s = "0"
Output: 0


Constraints:
1 <= s <= 10^4
``s`` consists of digits, '+', '-', '*', '/', '(', and ')'.
``s`` is a valid expression.


Follow up: Could you solve the problem without using built-in library functions?
"""



class Solution:
    """
遇到左括号时, 找到与之相匹配的右括号, 将两个括号间的内容基于 227_Basic-Calculator-II.py 求解;
    """
    def calculate_v1(self, s: str) -> int:
        # jy: 记录上一个操作符, 默认为 "+";
        last_operator = '+'
        # jy: 记录待加和的数值, 其中除栈顶之外的数值肯定是要加和的数值, 栈顶数值需要结合后续
        #     遍历到下一个操作符时(此时的 digit 已经构建完整), 结合上一个操作符判断是否要对栈
        #     顶元素和此时的 digit 做优先级更高的运算操作(当上一个操作符为 "*" 或 "-" 时, 表
        #     明栈顶元素与此时的 digit 数值结合上一个操作符的操作优先级更高)
        stack = []
        # jy: 记录上一个操作符开始, 截止当前字符为止对应的数值;
        digit = 0
        i = 0
        # jy: 遍历字符串表达式中的每个字符;
        while i < len(s):
            # jy: 如果当前字符为数值字符, 则构造当前的数值;
            if s[i].isdigit():
                digit = digit * 10 + int(s[i])

            # jy: 如果当前字符为 "(", 则从当前字符的下一个字符开始, 找出与之匹配的 ")" 的位
            #     置下标 j, 并递归计算 "(" 和 ")" 中的字符串表达式 (即 s[i+1: j]) 的值, 赋值
            #     给 digit 变量(当前字符 "(" 之前的字符肯定是一个操作符, 在遍历到该操作符时
            #     已经将原先该操作符之前的数值入栈, 且 digit 又经过一轮初始化, 故此处重新对
            #     digit 初始化并不会与原先的 digit 产生冲突); 同时将 i 更新为 j, 即 ")" 字符
            #     对应的下标(i 要更新为当前已经处理完的字符的位置下标, 因为后面会统一在当前
            #     已经处理完的位置下标基础上加 1, 然后进入下一轮循环);
            elif s[i] == '(':
                j = i + 1
                # jy: 用 braces 记录还未找到配对的 "(" 字符的个数;
                braces = 1
                # jy: 从当前字符 "(" 的下一个字符开始, 找到与之匹配的 ")" 的坐标 j (互相匹配
                #     的括号中可能还会内嵌括号);
                while j < len(s):
                    # jy: 如果碰到的字符为 "(", 则 braces 加 1, 如果碰到 ")", 则 braces 减 1;
                    #     当 braces 为 0 时, 表明当前的位置下标 j 对应的 ")" 即为与最初的 "("
                    #     匹配的字符(当 brace 为 0 时, 此时的位置下标 j 对应的字符必定是 ")")
                    if s[j] == '(':
                        braces += 1
                    if s[j] == ')':
                        braces -= 1
                    if braces == 0:
                        break
                    j += 1

                # jy: s[i+1: j] 是 "(" 和 ")" 之间的有效表达式(表达式中也可能存在 "(" 和 ")",
                #     会在不断递归中计算求解)
                digit = self.calculate_v1(s[i+1: j])

                # jy: 以上表明 j 对应位置下标的字符已经处理完成, 因此 i 更新为 j; 后面会统一在
                #     当前已经处理完的位置下标基础上加 1, 然后进入下一轮循环); 此处不能直接将 i
                #     更新为 j+1, 因为如果 j 是字符串中的最后一个字符, 则此时的 digit 需要入栈
                #     如果更新为 j+1, 则不再会有入栈操作;
                i = j

            # jy: 如果当前字符是操作符或已经是字符串的最后一个字符, 此时上一轮操作中保存的 digit
            #     已经确保为上一个操作符与当前操作符之间的一个完整的数值; 此时需要结合上一个操作
            #     符判断栈顶元素和当前的 digit 的运算操作是否优先级更高, 如果优先级更高(如 "*" 和
            #     "/" 操作), 则需要出栈栈顶元素和当前 digit 进行运算操作后再入栈; 如果优先级相同,
            #     则结合上一个操作符将当前的 digit 直接入栈即可(如果上一个操作符为 "-", 则应在当
            #     前字符的前面加个负号后入栈, 因为栈中的元素最终是进行加和的);
            if s[i] in '+-*/' or i == len(s) - 1:
                if last_operator == '+':
                    stack.append(digit)
                elif last_operator == '-':
                    stack.append(-digit)
                elif last_operator == '*':
                    stack.append(stack.pop() * digit)
                elif last_operator == '/':
                    stack.append(int(stack.pop() / digit))

                # jy: 经过以上处理后, 上一个操作符对应的应有操作已经完成, 并且截止当前位置为止
                #     的对应数值也都入栈, 此时 digit 更新为 0, 上一个操作符更新为当前操作符(如
                #     果当前字符已经是最后一个字符, 即 i == len(s)-1, 则 s[i] 不一定为操作符,
                #     但也不影响结果, 因为 last_operator 赋值为 s[i] 后也不会再被使用了);
                digit = 0
                last_operator = s[i]

            # jy: 经过以上逻辑, 表明截止下标位置为 i 的字符已经处理完成, 更新 i 为下一个字符对应的
            #     下标, 供下一轮循环时使用;
            i += 1
        # jy: 最终的栈中保存的都是一些待加和的数值, 直接加和返回;
        return sum(stack)

    """
解法2: 将解法 1 中的栈优化掉(参考 227_Basic-Calculator-II.py  中的解法 2)
    """
    def calculate_v2(self, s: str) -> int:
        # jy: 记录上一个操作符, 默认为 "+";
        last_operator = '+'
        # jy: 用 prev_res 记录除原先的栈顶元素外的其它元素之和, res 记录原先的栈顶元素;
        prev_res = 0
        res = 0
        # jy: 记录上一个操作符开始, 截止当前字符为止对应的数值;
        digit = 0
        i = 0
        # jy: 遍历字符串表达式中的每个字符;
        while i < len(s):
            # jy: 如果当前字符为数值字符, 则构造当前的数值;
            if s[i].isdigit():
                digit = digit * 10 + int(s[i])

            elif s[i] == '(':
                j = i + 1
                # jy: 用 braces 记录还未找到配对的 "(" 字符的个数;
                braces = 1
                # jy: 从当前字符 "(" 的下一个字符开始, 找到与之匹配的 ")" 的坐标 j (互相匹配
                #     的括号中可能还会内嵌括号);
                while j < len(s):
                    if s[j] == '(':
                        braces += 1
                    if s[j] == ')':
                        braces -= 1
                    if braces == 0:
                        break
                    j += 1

                digit = self.calculate_v2(s[i + 1: j])
                i = j

            if s[i] in '+-*/' or i == len(s) - 1:
                if last_operator == '+':
                    res += prev_res
                    prev_res = digit
                elif last_operator == '-':
                    res += prev_res
                    prev_res = -digit
                elif last_operator == '*':
                    prev_res *= digit
                elif last_operator == '/':
                    prev_res = int(prev_res / digit)

                digit = 0
                last_operator = s[i]

            i += 1
        return res + prev_res


s = "1+1"
# Output: 2
res = Solution().calculate_v1(s)
print(res)


s = "6-4/2"
# Output: 4
res = Solution().calculate_v1(s)
print(res)


s = "2*(5+5*2)/3+(6/2+8)"
# Output: 21
res = Solution().calculate_v2(s)
print(res)


s = "(2+6*3+5-(3*14/7+2)*5)+3"
# Output: -12
res = Solution().calculate_v2(s)
print(res)


s = "0"
# Output: 0
res = Solution().calculate_v2(s)
print(res)


