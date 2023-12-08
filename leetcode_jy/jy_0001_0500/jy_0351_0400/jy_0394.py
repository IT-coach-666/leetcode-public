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
title_jy = "Decode-String(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an encoded string, return its decoded string. The encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being repeated exactly k times. Note
that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets
are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits
are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"



Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""




class Solution:
    """
解法1: 遍历字符串, 如果遇到左括号, 找到与之相匹配的右括号, 将两个括号之间的内容递归解码;
    """
    def decodeString_v1(self, s: str) -> str:
        # jy: 记录最终 decode 后的结果;
        result = ''
        # jy: 用于保存数值, 因为数值可能会有多位数;
        digit = 0
        i, length = 0, len(s)
        # jy: 遍历字符串;
        while i < length:
            c = s[i]
            # jy: 如果字符串为数值, 则用 digit 记录数值结果(由于数值可能不止一位数)
            if c.isdigit():
                digit = digit * 10 + int(c)
            # jy: 如果字符为 '[', 表明在该字符之前已经获取到了一个有效数值 digit (因
            #    为 Constraints 中已经表明输入的 s 必为有效输入, 故该字符前已经确保
            #    是一个有效数值了), 此时, 需要找出于该 '[' 相匹配的字符 ']' (注意: 不
            #    一定是后续字符中的第一个出现的 ']', 因为可能会再次出现 '[', 使得第一
            #    个出现的 ']' 并不是与当前遍历得到的 '[' 直接匹配的)
            elif c == '[':
                # jy: 设定 j 为当前字符 '[' 后的第一个字符的下标, 将从该下标中开始找与当
                #    前字符匹配的 ']' ; 此处的 brackets 统计遇到的 '[' 的个数, 当遇到 '['
                #    时, brackets 加 1 , 遇到 ']' 时 brackets 减 1, 当 brackets 为 0 时,
                #    表明当前遍历到的 j 下标所对应的 ']' 字符是与最开始的 '[' 配对的
                j = i + 1
                brackets = 1

                while j < length:
                    if s[j] == '[':
                        brackets += 1
                    if s[j] == ']':
                        brackets -= 1
                    if brackets == 0:
                        break
                    j += 1
                # jy: 获取到与 '[' 匹配的 ']' 后, 将这两个中括号中的内容抽取出来(即为 s[i+1: j], 其
                #    中 s[i] 为 '[', s[j] 为 ']', 均不被包含在内), 进行递归调用, 调用得到的结果再乘
                #    以 digit 即为当前片段经过 decode 后的目标结果;
                result += self.decodeString_v1(s[i+1: j]) * digit
                # jy: 此时将 i 设置为 j, 即对应 ']' 的下标, 在后面会使 i 进一步加 1, 跳过该字符下标进
                #    行后续遍历, 后续遍历时的 digit 也应该重新算起, 故此处重新设置 digit 为 0;
                i = j
                digit = 0
            # jy: 如果当前字符既不是数值, 也不是 '[' 和 ']' 囊括起来的内容, 则直接添加到 result 后端即可;
            else:
                result += c
            # jy: 一轮 while 循环结束, 定位到下一个字符后继续循环遍历;
            i += 1

        return result


    """
解法2: 使用一个栈保存字符串对应重复的次数, 遍历字符串, 如果遇到左括号, 则入栈新的一组匹配, 如果遇到
右括号, 则出栈一组匹配, 根据重复次数更新栈顶的元素;
    """
    def decodeString_v2(self, s: str) -> str:
        stack = [['', 1]]
        digit = 0
        # jy: 遍历字符串
        for c in s:
            # jy: 如果字符串为数值类型, 则计算该数值结果(可能是多位数, 最终用 digit 该数值)
            if c.isdigit():
                digit = digit * 10 + int(c)
            # jy: 如果遇到左括号, 则入栈新的一组匹配(入栈值为一个列表, 第一个元素为字符串, 初始值为
            #    空字符串, 后续会进一步遍历将需要重复出现 digit 次的子串补全进来; 第二个元素即 digit,
            #    即表示最终第一个元素需要重复出现的次数)
            elif c == '[':
                stack.append(['', digit])
                digit = 0
            # jy: 如果当前字符为 ']', 则表明栈顶中的值列表的第一个元素已经补充完善要重复的子串了, 直接
            #    出栈, 并将子串与其要出现的次数进行拼接, 随后再补充到新栈顶的值列表的第一个元素中;
            elif c == ']':
                text, count = stack.pop()
                stack[-1][0] += text * count
            # jy: 如果当前字符既不是数值, 也不是括号, 则将该元素更新到栈顶的值列表的第一个元素中去;
            else:
                stack[-1][0] += c

        return stack[0][0]


s = "3[a]2[bc]"
# Output: "aaabcbc"
res = Solution().decodeString_v1(s)
print(res)


s = "3[a2[c]]"
# Output: "accaccacc"
res = Solution().decodeString_v2(s)
print(res)


s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
res = Solution().decodeString_v2(s)
print(res)


s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
res = Solution().decodeString_v1(s)
print(res)"""
Given an encoded string, return its decoded string. The encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being repeated exactly k times. Note
that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets
are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits
are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"



Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""




class Solution:
    """
解法1: 遍历字符串, 如果遇到左括号, 找到与之相匹配的右括号, 将两个括号之间的内容递归解码;
    """
    def decodeString_v1(self, s: str) -> str:
        # jy: 记录最终 decode 后的结果;
        result = ''
        # jy: 用于保存数值, 因为数值可能会有多位数;
        digit = 0
        i, length = 0, len(s)
        # jy: 遍历字符串;
        while i < length:
            c = s[i]
            # jy: 如果字符串为数值, 则用 digit 记录数值结果(由于数值可能不止一位数)
            if c.isdigit():
                digit = digit * 10 + int(c)
            # jy: 如果字符为 '[', 表明在该字符之前已经获取到了一个有效数值 digit (因
            #    为 Constraints 中已经表明输入的 s 必为有效输入, 故该字符前已经确保
            #    是一个有效数值了), 此时, 需要找出于该 '[' 相匹配的字符 ']' (注意: 不
            #    一定是后续字符中的第一个出现的 ']', 因为可能会再次出现 '[', 使得第一
            #    个出现的 ']' 并不是与当前遍历得到的 '[' 直接匹配的)
            elif c == '[':
                # jy: 设定 j 为当前字符 '[' 后的第一个字符的下标, 将从该下标中开始找与当
                #    前字符匹配的 ']' ; 此处的 brackets 统计遇到的 '[' 的个数, 当遇到 '['
                #    时, brackets 加 1 , 遇到 ']' 时 brackets 减 1, 当 brackets 为 0 时,
                #    表明当前遍历到的 j 下标所对应的 ']' 字符是与最开始的 '[' 配对的
                j = i + 1
                brackets = 1

                while j < length:
                    if s[j] == '[':
                        brackets += 1
                    if s[j] == ']':
                        brackets -= 1
                    if brackets == 0:
                        break
                    j += 1
                # jy: 获取到与 '[' 匹配的 ']' 后, 将这两个中括号中的内容抽取出来(即为 s[i+1: j], 其
                #    中 s[i] 为 '[', s[j] 为 ']', 均不被包含在内), 进行递归调用, 调用得到的结果再乘
                #    以 digit 即为当前片段经过 decode 后的目标结果;
                result += self.decodeString_v1(s[i+1: j]) * digit
                # jy: 此时将 i 设置为 j, 即对应 ']' 的下标, 在后面会使 i 进一步加 1, 跳过该字符下标进
                #    行后续遍历, 后续遍历时的 digit 也应该重新算起, 故此处重新设置 digit 为 0;
                i = j
                digit = 0
            # jy: 如果当前字符既不是数值, 也不是 '[' 和 ']' 囊括起来的内容, 则直接添加到 result 后端即可;
            else:
                result += c
            # jy: 一轮 while 循环结束, 定位到下一个字符后继续循环遍历;
            i += 1

        return result


    """
解法2: 使用一个栈保存字符串对应重复的次数, 遍历字符串, 如果遇到左括号, 则入栈新的一组匹配, 如果遇到
右括号, 则出栈一组匹配, 根据重复次数更新栈顶的元素;
    """
    def decodeString_v2(self, s: str) -> str:
        stack = [['', 1]]
        digit = 0
        # jy: 遍历字符串
        for c in s:
            # jy: 如果字符串为数值类型, 则计算该数值结果(可能是多位数, 最终用 digit 该数值)
            if c.isdigit():
                digit = digit * 10 + int(c)
            # jy: 如果遇到左括号, 则入栈新的一组匹配(入栈值为一个列表, 第一个元素为字符串, 初始值为
            #    空字符串, 后续会进一步遍历将需要重复出现 digit 次的子串补全进来; 第二个元素即 digit,
            #    即表示最终第一个元素需要重复出现的次数)
            elif c == '[':
                stack.append(['', digit])
                digit = 0
            # jy: 如果当前字符为 ']', 则表明栈顶中的值列表的第一个元素已经补充完善要重复的子串了, 直接
            #    出栈, 并将子串与其要出现的次数进行拼接, 随后再补充到新栈顶的值列表的第一个元素中;
            elif c == ']':
                text, count = stack.pop()
                stack[-1][0] += text * count
            # jy: 如果当前字符既不是数值, 也不是括号, 则将该元素更新到栈顶的值列表的第一个元素中去;
            else:
                stack[-1][0] += c

        return stack[0][0]


s = "3[a]2[bc]"
# Output: "aaabcbc"
res = Solution().decodeString_v1(s)
print(res)


s = "3[a2[c]]"
# Output: "accaccacc"
res = Solution().decodeString_v2(s)
print(res)


s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
res = Solution().decodeString_v2(s)
print(res)


s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
res = Solution().decodeString_v1(s)
print(res)


