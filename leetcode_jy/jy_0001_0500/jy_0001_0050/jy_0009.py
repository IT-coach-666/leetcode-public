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
from typing import List
import math
# jy: 记录该题的难度系数
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Palindrome-Number(number)"
# jy: 记录不同解法思路的关键词
tag_jy = "字符反转 | 数值反转 | 双指针 | 数值计算技巧（取最高位、去除最高位）"


"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it
             becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:
-2^31 <= x <= 2^31 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""


""" 解题思路: (五种实现方法) 1. 转成字符串: a. 双向队列 b. 双指针 2. 不转字符串: a. 模拟字符串的双向队列(使用math库的log函数 获取整数的位数) b. 反转后面一半的整数(使用math库的log函数 获取整数的位数) c. 反转后面一半的整数(不适用log函数) (通过原整数x 与 reverse_x 的大小判断) """



class Solution:

    """
解法 1: 双向队列; pop(0) 的时间复杂度为 O(n), 总体时间复杂度为 O(n^2)
将 int 转化成 str 类型后, 不断左右两边 pop 后比较
    """
    def isPalindrome_v1(self, x: int) -> bool:
        lst = list(str(x))
        while len(lst) > 1:
            if lst.pop(0) != lst.pop():
                return  False
        return True


    """
解法 2: 双指针; 时间复杂度为 O(n)
    """
    def isPalindrome_v2(self, x: int) -> bool:
        str_ = str(x)
        left, right = 0, len(str_) - 1
        while left < right:
            if str_[left] != str_[right]:
                return  False
            left += 1
            right -= 1
        return True


    """
解法 3 (进阶): 使用 log 计算 x 的位数; 时间复杂度为 O(n)
参照字符串的方法(但无需将整数转为字符串): 分别取数值的最高位和最低位进行对比;
只需对比数值位数的一半即可 (提高性能)
缺点: 频繁计算(整除、取余、幂运算), 导致速度变慢

真实算法场景 log 函数的计算逻辑需自定义实现
    """
    def isPalindrome_v3(self, x: int) -> bool:
        """
        以下代码逻辑可基于 x = 13231 进行理解
        """
        # jy: x 为负值时不可能满足条件, 直接返回 False
        if x < 0:
            return False
        # jy: x 为 0 时, 满足条件, 直接返回 True
        elif x == 0:
            return True
        # jy: x 不为 0 时, 且 x 能被 10 整除(表明最后一位为 0), 则必然不符合
        #     要求, 返回 False
        elif x % 10 == 0:
            return False

        # jy: 以 10 为底的 x 的对数, 即求出满足 10^n = x 的 n 值, 并取整数
        #     部分, 得到的结果加 1 即为数值 x 的位数
        length = int(math.log(x, 10)) + 1
        # jy: 位数减 1, 后续基于 L 值获取最高位数值以及去除最高位后的剩余数
        #     值; L 值始终比当前 x 的位数少 1
        L = length - 1
        # jy: 只需遍历数值位数的一半即可 (类比双指针遍历进行理解)
        for i in range(length // 2):
            # jy: 左侧用于获取 x 的最高位数, 右侧用于取 x 的最低位数
            if x // 10 ** L != x % 10:
                return False
            # jy: ** 的优先级比 % 高, 因此 x % 10 ** L 的结果即去除最高位后
            #     的数值, 再除以 10 (整除) 即表示去除最低位的数值
            x = (x % 10 ** L) // 10
            # jy: x 去除最高位和最低位后, L 值相应减去 2, 使得 L 值始终与 x
            #     的位数少 1
            L -= 2
        return True


    """
解法 4: 只反转后面一半的数字; 使用 log 函数计算 x 的位数, 时间复杂度 O(n)
不需将整数转为字符串
    """
    def isPalindrome_v4(self, x: int) -> bool:
        # jy: x 为负值时不可能满足条件, 直接返回 False
        if x < 0:
            return False
        # jy: x 为 0 时, 满足条件, 直接返回 True
        elif x == 0:
            return True
        # jy: x 不为 0 时, 且 x 能被 10 整除(表明最后一位为 0), 则必然不符合
        #     要求, 返回 False
        elif x % 10 == 0:
            return False

        # jy: 计算 x 的位数
        length = int(math.log(x, 10)) + 1
        # jy: 用于统计反转一半后的数值
        reverse_x = 0
        # jy: 只需反转后面一半的数值, 因此循环次数为位数的一半; 反转过程中后
        #     一半的数值不断反转, 且原数值不断去除后一半的数值
        for i in range(length // 2):
            remainder = x % 10
            x = x // 10
            reverse_x = reverse_x * 10 + remainder
        # jy: 当 x 为奇数时, 需满足 reverse_x == x // 10
        #     当 x 为偶数时, 需满足 reverse_x == x
        if reverse_x == x or reverse_x == x // 10:
            return True
        else:
            return False

    """
解法 5: 不将整数转为字符串, 且不需使用 log 函数计算位数; 时间复杂度 O(n)
同样是反转一半的数值, 只是优化了反转过程中的终止条件
    """
    def isPalindrome_v5(self, x: int) -> bool:
        # jy: x 为负值时不可能满足条件, 直接返回 False
        if x < 0:
            return False
        # jy: x 为 0 时, 满足条件, 直接返回 True
        elif x == 0:
            return True
        # jy: x 不为 0 时, 且 x 能被 10 整除(表明最后一位为 0), 则必然不符合
        #     要求, 返回 False
        elif x % 10 == 0:
            return False

        # jy: 同样是反转数值, 但反转终止条件为 x <= reverse_x
        reverse_x = 0
        while x > reverse_x:
            remainder = x % 10
            reverse_x = reverse_x * 10 + remainder
            x = x // 10

        # jy: 当 x 为奇数时, 以上反转结束后 reverse_x 必定比 x 多一位, 此时
        #     需满足 reverse_x // 10 == x ; 当 x 为偶数时, 反转后 reverse_x
        #     和 x 的位数相等
        if reverse_x == x or reverse_x//10 == x:
            return True
        else:
            return False



x = 10
res = Solution().isPalindrome_v1(x)
print("%s == %s" % (x, res))

x = 10001
res = Solution().isPalindrome_v2(x)
print("%s == %s" % (x, res))


x = 12301
res = Solution().isPalindrome_v3(x)
print("%s == %s" % (x, res))


x = 13231
res = Solution().isPalindrome_v4(x)
print("%s == %s" % (x, res))


x = 1001
res = Solution().isPalindrome_v5(x)
print("%s == %s" % (x, res))

