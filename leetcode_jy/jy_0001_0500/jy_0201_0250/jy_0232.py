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
title_jy = "Implement-Queue-using-Stacks(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Implement the following operations of a queue using stacks.
push(x) -- Push element x to the back of queue.
pop()   -- Removes the element from in front of queue.
peek()  -- Get the front element.
empty() -- Return whether the queue is empty.


Example:
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false


Notes:
1) You must use only standard operations of a stack -- which means only push to top,
   peek/pop from top, size, and is empty operations are valid.
2) Depending on your language, stack may not be supported natively.  You may simulate
   a stack by using a list or deque (double-ended queue),  as long as you use only
   standard operations of a stack.
3) You may assume that all operations are valid (for example, no pop or peek operation
   will be called on an empty queue).
"""


"""
解法1: 使用 Python 的 List 实现, 关键的 pop 方法使用了 List 的 pop(0) 方法, 不符合题目要求;
"""
class MyQueue_v1:
    def __init__(self):
        self.stack = []


    def push(self, x: int) -> None:
        self.stack.append(x)


    def pop(self) -> int:
        if self.empty():
            raise Exception('queue is empty')
        # jy: 返回列表中的第一个元素(并两该元素删除);
        return self.stack.pop(0)


    def peek(self) -> int:
        if self.empty():
            raise Exception('queue is empty')
        # jy: 返回列表中的第一个元素(不删除)
        return self.stack[0]


    def empty(self) -> bool:
        return len(self.stack) == 0



"""
解法2: 不同于队列, 栈的入栈和出栈操作是同一个入口, 所以需要一个额外的栈, 在 push 时, 先
将原先栈内的元素移动到辅助栈中, 然后将新元素压栈, 最后将辅助栈中的元素挪回到原来的栈中;
"""
class MyQueue_v2:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # jy: stack2 为辅助栈, 先将 stack1 中的数值全部添加如辅助栈中;
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        # jy: 再将 x 加入 stack1 的栈底(使得后续出栈时, 后加入的元素总是后出);
        self.stack1.append(x)
        # jy: 再将原先栈中的元素入栈, 使其在栈的偏顶部(保证原先先进入栈的元素出栈时先出)
        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        if self.empty():
            raise Exception('queue is empty')

        return self.stack1.pop()

    def peek(self) -> int:
        if self.empty():
            raise Exception('queue is empty')

        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0


"""
解法3: 对解法 2 进行优化(仍使用一个辅助的栈), 所有的入队操作在其中一个栈上, 同时记录一
个 front 变量作为队首元素; 出队时, 如果辅助栈为空, 则将另一个栈中的元素移动到辅助栈中,
然后从辅助栈中进行出栈; peek 操作需要注意, 当辅助栈不为空时直接返回辅助栈的栈顶元素即
可, 当辅助栈为空时则返回 front;

JY: 相对于解法2, 该解法不需要频繁的对辅助栈 stack2 和 stack1 进行来回倒换;
"""
class MyQueue_v3:
    def __init__(self):
        self.front = None
        self.stack1 = []
        self.stack2 = []  # jy: stack2 为辅助栈;

    def push(self, x: int) -> None:
        # jy: 将所有元素入 stack1, 并记录最开始入栈的元素为队首元素(stack1 中的元素靠底
        #    端的应先出);
        if not self.stack1:
            self.front = x
        self.stack1.append(x)

    def pop(self) -> int:
        if self.empty():
            raise Exception('queue is empty')
        # jy: 如果辅助栈 stack2 为空, 则将 stack1 中的元素移动到辅助栈中(使得原先的 stack1 靠
        #    栈顶部分在 stack2 中靠栈底, 原先靠栈底的(即应先出队的元素)现在为 stack2 的靠栈
        #    顶端), 随后从辅助栈 stack2 中进行出栈(即辅助栈 stack2 的栈顶总是应先出的元素);
        if not self.stack2:
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        if self.empty():
            raise Exception('queue is empty')
        # jy: 如果辅助栈 stack2 不为空, 则辅助栈的栈顶元素即为队首元素; 如果辅助栈为空, 则队
        #    首元素为 self.front 所指袁元素;
        return self.stack2[-1] if self.stack2 else self.front

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0



queue = MyQueue_v1()
queue.push(1)
queue.push(2)
print(queue.peek())  # returns 1
print(queue.pop())   # returns 1
print(queue.empty()) # returns false


queue = MyQueue_v2()
queue.push(1)
queue.push(2)
print(queue.peek())  # returns 1
print(queue.pop())   # returns 1
print(queue.empty()) # returns false


queue = MyQueue_v3()
queue.push(1)
queue.push(2)
print(queue.peek())  # returns 1
print(queue.pop())   # returns 1
print(queue.empty()) # returns false


