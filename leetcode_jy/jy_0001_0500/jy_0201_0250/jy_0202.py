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
title_jy = "Happy-Number(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
1) Starting with any positive integer, replace the number by the sum of the squares of its digits.
2) Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a
   cycle which does not include 1.
3) Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false

Constraints:1 <= n <= 2^31 - 1
"""

class Solution:
    """
解法1: 一直循环构建数字, 使用一个 Set 保存遇到的数字, 如果新的数字已经在 Set 中了, 返回 false;
    """
    def isHappy_v1(self, n: int) -> bool:
        visited = set()

        while True:
            # jy: 将数值的每一个数字进行平方加和, 如果结果为 1, 直接返回 True, 如果结果已经出现过, 则
            #    直接返回 False, 否则将结果加入到集合中;
            # n = sum(map(lambda x: int(x) * int(x), str(n)))
            n = sum(map(lambda x: int(x) ** 2, str(n)))

            if n == 1:
                return True
            elif n in visited:
                return False
            else:
                visited.add(n)

    """
解法2: 还可以借鉴快慢指针的思想, fast 每次计算两次, slow 计算一次, 当两者相同时判断其值是否为 1;

JY: 如果最终不能变为 1, 一定是在某几个数之间不断死循环; 使用 slow 和 fast 快慢指针, 数值肯定会相遇;
    """
    def isHappy_v2(self, n: int) -> bool:
        slow = n
        fast = self._square_sum(n)

        while slow != fast:
            print("====slow: %d ====fast: %d" % (slow, fast))
            slow = self._square_sum(slow)
            fast = self._square_sum(fast)
            fast = self._square_sum(fast)
        print("====slow: %d ====fast: %d" % (slow, fast))
        return slow == 1

    def _square_sum(self, n):
        '''将数值的每一个数字进行平方加和'''
        # return sum(map(lambda x: int(x) * int(x), str(n)))
        return sum(map(lambda x: int(x) ** 2, str(n)))


n = 19
# Output: true
res = Solution().isHappy_v1(n)
print(res)

n = 2
# Output: false
res = Solution().isHappy_v2(n)
print(res)


