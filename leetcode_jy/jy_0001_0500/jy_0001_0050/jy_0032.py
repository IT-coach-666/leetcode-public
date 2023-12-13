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
title_jy = "Longest-Valid-Parentheses(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "栈 | 暴力求解 | 贪心思路优化暴力求解"


"""
Given a string containing just the characters '(' and ')', return the length
of the longest valid (well-formed) parentheses substring.

 
Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
 

Constraints:
0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.
"""


class Solution:
    """
解法 1: 用栈存储索引, 遍历时, 只要有两个连续索引对应字符可以构成一对括号就出
栈, 因此栈中存储的都是到当前位置暂时不可以构成括号的索引; 时间复杂度 O(n), 空
间复杂度 O(n)


需明确什么样的模式是合格的, 什么样的模式是不合格的; 这两个条件决定了入栈和出
栈的规则; 
a) 合格的模式应该是有序且成对的 "()", 即 "(...)"
b) 不合格的模式应该是无序的, 不管他成对不成对，即 ")...(" 、"(...(" 、")...)"


满足以下条件时, 当前字符不可以与栈顶字符构成匹配的括号:
1) 当前栈为空
2) 当前字符 s[i] 是左括号 "(", 无法跟栈顶元素构成一对括号
3) 栈顶元素是右括号 ")", 无论当前字符是什么, 都无法和栈顶元素构成一对括号

因此栈顶元素必须为 "(", 且当前字符 s[i] 必须为 ")", 这样才能构成一对括号; 构
成一对括号后, 栈顶元素出栈; 因此栈中存储的都是当前暂时不可以构成括号的索引
    """
    def longestValidParentheses_v1(self, s: str) -> int:
        # jy: 构建一个栈记录字符 index
        stack = [] 
        ans = 0
        for i in range(len(s)):
            # jy: 如果栈非空, 且当前为右括号, 且栈顶对应字符为左括号, 则出栈
            if stack and s[i] == ")" and s[stack[-1]] == "(":
                stack.pop()
                # jy: 如果出栈后变成空栈, 说明整个 [0:i] 的区间都合格, 长度为 i+1
                #     如果出栈后非空, 说明区间 [stack[-1]: i] 合格
                ans = max(ans, i - (stack[-1] if stack else -1))
            # jy: 以下 3 个条件中的任一个会触发 else
            #     1) 空栈
            #     2) 当前字符为左括号 "(", 需寻找匹配的右括号 ")"
            #     3) 当前字符为右括号 ")", 且栈顶记录的也是右括号 ")"
            else:
                stack.append(i)
                
        return ans


    """
解法 2: 暴力解法

要找满足匹配规则的子串肯定要以左括号 "(" 开始进行查找; 因此遍历 s 找到所有
左括号的下标, 保存到数组 nums; 如果 nums 长度等于 s, 直接返回 0

遍历 nums, 从每一个左括号开始进行查找:
1) 如果 left == right, 比较最大值 ret = max(ret, left * 2)
2) 如果 right > left, 停止, 从下一个左括号下标继续找起

时间复杂度 O(n^2), 由于要存储 left 所有下标, 所以空间复杂度最大为 O(n)
    """
    def longestValidParentheses_v2(self, s: str) -> int:
        len_s = len(s)
        # jy: 遍历 s 找到所有左括号的下标, 保存到数组 nums; 如果 nums 长度
        #     等于 s, 直接返回 0
        nums = [i for i in range(len_s) if s[i] == '(']
        if len(nums) == len_s:
            return 0

        ret = 0
        # jy: 遍历 nums (即左括号的下标位置)
        for left in nums:
            # jy: a 统计左括号数, b 统计右括号数
            a, b = 0, 0
            # jy: 从每一个左括号开始进行查找
            for i in range(left, len_s):
                if s[i] == '(':
                    a += 1
                else:
                    b += 1
                # jy: 如果左右括号数相等, 则可更新匹配的字符串长度
                if a == b:
                    ret = max(ret, a * 2)
                # jy: 如果右括号数大于左括号数, 则可提前退出循环
                elif b > a:
                    break
        return ret


    """
解法 3: 贪心思路, 性能和内存消耗最佳

暴力解法做了很多重复的查找; 当发现右括号数大于左括号数时, break 后就可以从当
前位置开始找下一个左括号, 减少重复的查找:
1) 初始 left = right = 0, 然后遍历 s
2) 当 left == right 时更新 ret
3) 当 right > left 时, 前面的数据都是报废且计算过最大值的, 全部舍弃掉, 重复
   "1)" 的操作

这样就完了吗? 不是, 我们只判断了 right > left, 那如果 left 一直大于 right 呢?
换位思考是不颠倒左右括号就能实现这种异常场景, 所以从右向左再遍历一次 s 就能解
决这个问题

从左向右、从右向左的代码都是一样的, 只是判断 right > left 和 left > right 的
条件不一样; 有什么办法能复用这套查找代码呢? 可以定义一个标记位, 然后使用异或
运算: order ^ (left > right)

异或运算: 
True  ^ True  = False
False ^ False = False
True  ^ False = True

如果为正序 (order = True), 当 right > left 时才重置 left = right = 0
也只有当 right > left 时的判断条件 order ^ (left > right) 才为 True

如果为反序 (order = False), 当 left > right 时才重置 left = right = 0
也只有当 left > right 时的判断条件 order ^ (left > right) 才为 True
    """
    def longestValidParentheses_v3(self, s: str) -> int:
        def comp(strings, order=True):
            """
            order 为 True 时代表正序, 否则代表反序
            """
            ret = 0
            left = right = 0
            for i in strings:
                if i == '(':
                    left += 1
                else:
                    right += 1
                if left == right:
                    ret = max(ret, left * 2)
                elif order ^ (left > right):
                    left = right = 0
            return ret
        # jy: 如果仅仅返回 comp(s), 则 "(()" 这种情况时得不到正确答案;
        #     s[::-1] 即反转字符串, 如 "(()" 反转为 ")(("
        return max(comp(s), comp(s[::-1], False))




s = "(()"
res = Solution().longestValidParentheses_v1(s)
# jy: 2
print(res)


s = ")()())"
res = Solution().longestValidParentheses_v2(s)
# jy: 4
print(res)


s = ")()())"
res = Solution().longestValidParentheses_v3(s)
# jy: 4
print(res)


s = ""
res = Solution().longestValidParentheses_v3(s)
# jy: 0
print(res)


