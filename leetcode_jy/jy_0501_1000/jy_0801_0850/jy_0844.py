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
title_jy = "Backspace-String-Compare(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two strings S and T, return True if they are equal when both are typed into
empty text editors. # means a backspace character.


Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".


Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(N) time and O(1) space?
"""



class Solution:
    """
解法1: 分别为 S 和 T 建立两个栈, 然后各自遍历 S 和 T, 如果遇到 #, 则执行出栈操作, 否
则执行入栈, 最后比较两个栈内的元素是否相同;
    """
    def backspaceCompare_v1(self, S: str, T: str) -> bool:
        stack_a, stack_b = [], []

        for c in S:
            if c == '#':
                if stack_a:
                    stack_a.pop()
            else:
                stack_a.append(c)

        for c in T:
            if c == '#':
                if stack_b:
                    stack_b.pop()
            else:
                stack_b.append(c)

        if len(stack_a) != len(stack_b):
            return False

        while stack_a:
            a, b = stack_a.pop(), stack_b.pop()
            if a != b:
                return False

        return True


    """
解法2: 解法1 的算法空间复杂度是 O(n), 而题目中最后要求我们使用空间复杂度为 O(1) 的算法;

使用两个指针分别指向 S 和 T 的末尾, 向数组头移动, 同时使用两个 count 变量记录遇到的 '#',
遇到 '#' 则 count 加 1, 如果遇到非 '#' 字符且此时 count 大于 0, 说明当前元素需要删除(即
指针左移并将 count 减 1);

当两个指针停止时, 如果其中有一个指针小于 0, 说明该指针对应的字符串最后为空串, 则判断另一
个指针的值是否与该指针相同, 如果相同则返回 true, 否则返回 false; 如果两个指针都不为 0, 则判断 S 和 T 对应指针的字符是否相等即可;
    """
    def backspaceCompare_v2(self, S: str, T: str) -> bool:
        # jy: i 和 j 指针分别指向 S 和 T 的末尾;
        i, j = len(S) - 1, len(T) - 1
        # jy: count1 和 count2 分别记录 S 和 T 中遇到的 "#";
        count1, count2 = 0, 0

        while i >= 0 or j >= 0:
            # jy: 1) 如果 i 为有效下标, 且当前下标对应的字符为 '#', 则 count1 加 1 后 i 向
            #       左移一位(跳过 '#' 字符)
            #    2) 如果当前字符不是 '#' 且 count1 大于 0, 则 i 向左移一位(删除当前字符),
            #       且 count1 减 1;
            #    经过该操作后, i 对应的是一个有效字符(如果 i 小于 0, 则表示空字符), 且此时
            #    的 count1 为 0(即表示暂没有 '#' 字符用于删除操作);
            while i >= 0 and (S[i] == '#' or count1 > 0):
                count1 = count1 + 1 if S[i] == '#' else count1 - 1
                i -= 1
            # jy: 同理以上;
            while j >= 0 and (T[j] == '#' or count2 > 0):
                count2 = count2 + 1 if T[j] == '#' else count2 - 1
                j -= 1

            # jy: 如果有一个指针小于 0 (即等于 -1), 则表明相应的字符串为空, 则判断另一字符
            #    串是否为空即可(即另一个指针是否也为 -1, 即两个指针是否相等)
            if i < 0 or j < 0:
                return i == j

            # jy: 如果两个指针均还有效, 则判断对应的字符是否相等(不等直接返回 False), 然后
            #    两指针均左移一位后继续判断;
            if S[i] != T[j]:
                return False
            i -= 1
            j -= 1
        return i == j


    """
JY: 同理解法 1, 但更简洁;
    """
    def backspaceCompare_jy(self, s: str, t: str) -> bool:
        def stack_fun(stack_, str_):
            for char in str_:
                if char == "#":
                    if stack_:
                        stack_.pop()
                else:
                    stack_.append(char)
            return stack_

        stack_s = stack_fun([], s)
        stack_t = stack_fun([], t)
        return stack_s == stack_t


S = "ab#c"
T = "ad#c"
# Output: true
res = Solution().backspaceCompare_v1(S, T)
print(res)


S = "ab##"
T = "c#d#"
# Output: true
res = Solution().backspaceCompare_v2(S, T)
print(res)


S = "a##c"
T = "#a#c"
# Output: true
res = Solution().backspaceCompare_jy(S, T)
print(res)


S = "a#c"
T = "b"
# Output: false
res = Solution().backspaceCompare_jy(S, T)
print(res)


