# S0020_Valid-Parentheses.py

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:    
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""


class Solution:
    """
栈的典型应用: 首先初始化一个栈, 用于保存遇到的左括号, 然后遍历数组:
1) 如果遇到的是左括号, 则将其入栈
2) 如果遇到的是右括号, 则出栈一个左括号判断两者是否匹配, 如果不匹配
   则返回 false, 否则继续循环;

当循环结束时, 判断栈是否为空, 如果为空则返回 true, 否则说明有左括号未匹配, 返回 false;
    """
    def isValid(self, s: str) -> bool:
        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']'}
        stack = []
        for c in s:
            # jy: 如果为左括号字符, 直接入栈;
            if c in parentheses:
                stack.append(c)
            # jy: 如果为右括号字符, 则需确保栈不为空, 且出栈元素必须为与当前右括号字符对应
            #     的左括号字符, 否则返回 False;
            else:
                if len(stack) == 0 or parentheses[stack.pop()] != c:
                    return False
        return not stack

    def isValid_2022_02_27(self, s: str) -> bool:
        # jy: dict_ 中的 key 为右括号字符, value 为对应的左括号字符;
        dict_ = {")": "(", "}": "{", "]": "["}
        stack = []
        # jy: 遍历字符串中的每个括号字符;
        for char in s:
            # jy: 如果字符为右括号字符, 且栈不为空, 出栈一个元素必须为对应的左括号;
            if char in dict_ and stack:
                if stack.pop() != dict_[char]:
                    return False
            # jy: 如果字符为右括号字符, 且栈为空, 则直接返回 False
            elif char in dict_ and not stack:
                return False
            # jy: 其它情况(即字符为左括号字符)则将字符入栈;
            else:
                stack.append(char)
        return not stack


s = "{[]}"
# Output: true
res = Solution().isValid(s)
print(s, " === ", res)

s = "()"
# Output: true
res = Solution().isValid(s)
print(s, " === ", res)

s = "()[]{}"
# Output: true
res = Solution().isValid(s)
print(s, " === ", res)

s = "(]"
# Output: False
res = Solution().isValid(s)
print(s, " === ", res)

s = "([)]"
# Output: False
res = Solution().isValid(s)
print(s, " === ", res)

