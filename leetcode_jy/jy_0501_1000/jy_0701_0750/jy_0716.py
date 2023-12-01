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
title_jy = "Max-Stack(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design a max stack data structure that supports the stack operations and supports
finding the stack's maximum element. Implement the ``MaxStack`` class:
MaxStack() :       Initializes the stack object.
void push(int x) : Pushes element x onto the stack.
int pop() :        Removes the element on top of the stack and returns it.
int top() :        Gets the element on the top of the stack without removing it.
int peekMax() :    Retrieves the maximum element in the stack without removing it.
int popMax() :     Retrieves the maximum element in the stack and removes it. If there
                   is more than one maximum element, only remove the top-most one.


Example 1:
MaxStack stk = new MaxStack();
stk.push(5)    # [5] the top of the stack and the maximum number is 5.
stk.push(1)    # [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5)    # [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top()      # return 5, [5, 1, 5] the stack did not change.
stk.popMax()   # return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top()      # return 1, [5, 1] the stack did not change.
stk.peekMax()  # return 5, [5, 1] the stack did not change.
stk.pop()      # return 1, [5] the top of the stack and the max element is now 5.
stk.top()      # return 5, [5] the stack did not change.


Constraints:
-10^7 <= x <= 10^7
At most 10^4 calls will be made to push, pop, top, peekMax, and popMax.
There will be at least one element in the stack when pop, top, peekMax, or popMax is called.


Follow up: Could you come up with a solution that supports O(1) for each top call and O(logn)
for each other call?
"""


"""
解法1: 参照 155_Min-Stack.py 并补充 popMax: 先弹出在最大值上方的数字, 随后弹出最大值, 最后再
将弹出的数字重新压入栈, 时间复杂度是 O(n);
"""
class MaxStack:
    def __init__(self):
        self.stack = []

    # jy: 入栈为一个元组, 前一位是当前入栈的数值, 后一位记录栈底到当前位置的最大值;
    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, max(x, self.stack[-1][1])))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        # jy: 获取当前栈中的最大元素;
        max_element = self.stack[-1][1]
        tmp_stack = []
        # jy: 将非最大节点逐个先出栈, 保存到  poped 临时栈中(保存到临时栈中的值不是元组类型, 不含
        #     最大值, 因为后续剔除最大值重新入栈时, 新的最大值会有所变化, 故没必要保留原有的最大值);
        while self.stack and self.stack[-1][0] != max_element:
            tmp_stack.append(self.stack.pop()[0])
        # jy: 经过以上, self.stack 的栈顶即为待删除的最大元素, 弹出即可;
        self.stack.pop()

        # jy: 重新将原先最大值位置之后的数值入栈(注意, 入栈时需要调用 self.push 方法, 其会重新更新入
        #     栈元素的最大值)
        while tmp_stack:
            self.push(tmp_stack.pop())
        return max_element


stk = MaxStack()
stk.push(5)           # [5] the top of the stack and the maximum number is 5.
stk.push(1)           # [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5)           # [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
print(stk.top())      # return 5, [5, 1, 5] the stack did not change.
print(stk.popMax())   # return 5, [5, 1] the stack is changed now, and the top is different from the max.
print(stk.top())      # return 1, [5, 1] the stack did not change.
print(stk.peekMax())  # return 5, [5, 1] the stack did not change.
print(stk.pop())      # return 1, [5] the top of the stack and the max element is now 5.
print(stk.top())      # return 5, [5] the stack did not change.


