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
title_jy = "Print-in-Order(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Suppose we have a class:
public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of ``Foo`` will be passed to three different threads. Thread ``A`` will
call ``first()``, thread ``B`` will call ``second()``, and thread ``C`` will call ``third()``.
Design a mechanism and modify the program to ensure that ``second()`` is executed after
``first()``, and ``third()`` is executed after ``second()``.

Note:
We do not know how the threads will be scheduled in the operating system, even though the
numbers in the input seem to imply the ordering. The input format you see is mainly to ensure
our tests' comprehensiveness.

 
Example 1:
Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread
             ``A`` calls ``first()``, thread ``B`` calls ``second()``, and thread ``C`` calls
             ``third()``. "firstsecondthird" is the correct output.

Example 2:
Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C
             calls second(). "firstsecondthird" is the correct output.
 

Constraints:
nums is a permutation of [1, 2, 3].
"""

from typing import Callable
from threading import Lock


"""
参考: 
https://leetcode-cn.com/problems/print-in-order/solution/an-xu-da-yin-by-leetcode/
https://leetcode-cn.com/problems/print-in-order/solution/1114-an-xu-da-yin-python3de-5chong-jie-fa-by-tuotu/
"""


class Foo_v1:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        with self.firstJobDone:
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # Wait for the second job to be done.
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()


"""

"""
class Foo_v2:
    def __init__(self):
        self.d = {}

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.d[0] = printFirst
        self.res()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.d[1] = printSecond
        self.res()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.d[2] = printThird
        self.res()

    def res(self) -> None:
        if len(self.d) == 3:
            self.d[0]()
            self.d[1]()
            self.d[2]()



