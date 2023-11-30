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
title_jy = "Min-Stack(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design a stack that supports push, pop, top, and retrieving the minimum element in
constant time. Implement the ``MinStack`` class:
MinStack()      initializes the stack object.
void push(val)  pushes the element val onto the stack.
void pop()      removes the element on the top of the stack.
int top()       gets the top element of the stack.
int getMin()    retrieves the minimum element in the stack.


Example 1:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())    # return -3
minStack.pop()
print(minStack.top())       # return 0
print(minStack.getMin())    # return -2


Constraints:
1) -2^31 <= val <= 2^31 - 1
2) At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
3) Methods pop, top and getMin operations will always be called on non-empty stacks.
"""


"""
添加数字到栈时，同时放入当前元素以及当前元素到栈底的最小值。
"""
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        # jy: 如果栈为空, 则截止当前值的最小值就是当前值, 将 (当前值, 最小值) 入栈;
        if not self.stack:
            self.stack.append((val, val))
        # jy: 如果栈不为空, 则获取截止当前值 val 的最小值, 并将其与当前值组成一个元
        #     组入栈;
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class MinStack_2022_03_02:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            # jy: 注意, 是与元组中的第 2 个元素比较;
            self.stack.append((val, min(val, self.stack[-1][1])))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        poped = self.stack.pop()
        return poped[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())    # return -3
minStack.pop()
print(minStack.top())       # return 0
print(minStack.getMin())    # return -2


