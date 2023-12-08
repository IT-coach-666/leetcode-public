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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Implement-Stack-using-Queues(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Implement the following operations of a stack using queues.
push(x) -- Push element x onto stack.
pop()   -- Removes the element on top of the stack.
top()   -- Get the top element.
empty() -- Return whether the stack is empty.


Example:
MyStack stack = new MyStack();
stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false


Notes:
1) You must use only standard operations of a queue -- which means only push to back,
   peek/pop from front, size, and is empty operations are valid.
2) Depending on your language, queue may not be supported natively.  You may simulate
   a queue by using a list or deque (double-ended queue),  as long as you use only
   standard operations of a queue.
3) You may assume that all operations are valid (for example, no pop or top operations
   will be called on an empty stack).
"""



from collections import deque

"""
解法1: 借助 collections 包下的 deque 实现, 但并不符合题目的要求, 因为额外使用了 pop 方法;
       collections.deque 是为了高效实现插入和删除操作的双向列表, 适合用于队列和栈;
"""
class MyStack_v1:
    def __init__(self):
        self.queue = deque()


    def push(self, x: int) -> None:
        self.queue.append(x)


    def pop(self) -> int:
        if self.empty():
            raise Exception('stack is empty')
        return self.queue.pop()


    def top(self) -> int:
        if self.empty():
            raise Exception('stack is empty')
        return self.queue[-1]


    def empty(self) -> bool:
        return len(self.queue) == 0


"""
解法2: 解法 1 使用了 deque 现成的 api, 如果不能使用 deque 的 pop 方法, 则需要修改下 push 的
实现; 当 push 一个元素时, 首先将这个元素入队, 然后将这个元素之前的所有元素依次出队和入队, 这
样最新 push 的元素就来到了队首, 栈的 pop 操作就等同于队列的出队操作; 相比于解法 1, 解法 2 的
push 的时间复杂度就上升到了 O(n);
"""
class MyStack_v2:
    def __init__(self):
        self.queue = deque()


    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())


    def pop(self) -> int:
        if self.empty():
            raise Exception('stack is empty')
        return self.queue.popleft()


    def top(self) -> int:
        if self.empty():
            raise Exception('stack is empty')
        return self.queue[0]


    def empty(self) -> bool:
        return len(self.queue) == 0


stack = MyStack_v1()
stack.push(1)
stack.push(2)
print(stack.top())    # returns 2
print(stack.pop())    # returns 2
print(stack.empty())  # returns false


stack = MyStack_v2()
stack.push(1)
stack.push(2)
print(stack.top())    # returns 2
print(stack.pop())    # returns 2
print(stack.empty())  # returns false



