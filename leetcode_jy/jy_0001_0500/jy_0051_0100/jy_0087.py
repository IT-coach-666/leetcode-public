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
title_jy = "Scramble-String(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 + 缓存 | 动态规划"


"""
We can scramble a string `s` to get a string `t` using the following algorithm:
1) If the length of the string is 1, stop.
2) If the length of the string is > 1, do the following:
   a) Split the string into two non-empty substrings at a random index, i.e.,
      if the string is `s`, divide it to `x` and `y` where `s = x + y`.
   b) Randomly decide to swap the two substrings or to keep them in the same
      order. i.e., after this step, `s` may become `s = x + y` or `s = y + x`.
   c) Apply step 1 recursively on each of the two substrings `x` and `y`.

Given two strings `s1` and `s2` of the same length, return `true` if `s2` is
a scrambled string of `s1`, otherwise, return `false`.

 
Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on `s1` is:
  # divide at random index:
  "great" --> "gr/eat"

  # random decision is not to swap the two substrings and keep them in order:
  "gr/eat" --> "gr/eat" 

  # apply the same algorithm recursively on both substrings. divide at random
  # index each of them:
  "gr/eat" --> "g/r / e/at"

  # random decision was to swap the first substring and to keep the second
  # substring in the same order:
  "g/r / e/at" --> "r/g / e/at"

  # again apply the algorithm recursively, divide "at" to "a/t":
  "r/g / e/at" --> "r/g / e/ a/t"

  # random decision is to keep both substrings in the same order:
  "r/g / e/ a/t" --> "r/g / e/ a/t"

  The algorithm stops now, and the result string is "rgeat" which is `s2`.
  As one possible scenario led `s1` to be scrambled to `s2`, we return `true`.


Example 2:
Input: s1 = "abcde", s2 = "caebd"
Output: false


Example 3:
Input: s1 = "a", s2 = "a"
Output: true
 

Constraints:
1) s1.length == s2.length
2) 1 <= s1.length <= 30
3) `s1` and `s2` consist of lowercase English letters.
"""


class Solution:
    """
解法 1: 递归 (超时)
    """
    def isScramble_v1(self, s1: str, s2: str) -> bool:
        # jy: 如果字符串长度不同, 直接返回 False, 终止递归
        if len(s1) != len(s2):
            return False

        # jy: 字符串相等则直接返回 True
        if s1 == s2:
            return True

        # jy: 如果字符串长度相等, 但排序后不等, 表明构成的字符存在差异,
        #     直接返回 False (注意: 排序后相等并不能确保一定满足要求)
        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            option_1 = self.isScramble_v1(s1[:i], s2[:i]) and self.isScramble_v1(s1[i:], s2[i:])
            option_2 = self.isScramble_v1(s1[:i], s2[-i:]) and self.isScramble_v1(s1[i:], s2[:-i])
            if option_1 or option_2:
                return True
        return False


    """
解法 2: 递归 + 缓存 (在解法 1 的基础上添加缓存)
    """
    dict_ = {}
    def isScramble_v2(self, s1: str, s2: str) -> bool:

        # jy: 优先判断是否命中缓存
        if s1 + s2 in self.dict_:
            return self.dict_[s1 + s2]

        # jy: 如果字符串长度不同, 直接返回 False, 终止递归
        if len(s1) != len(s2):
            return False

        # jy: 字符串相等则直接返回 True
        if s1 == s2:
            return True

        # jy: 如果字符串长度相等, 但排序后不等, 表明构成的字符存在差异,
        #     直接返回 False (注意: 排序后相等并不能确保一定满足要求)
        if sorted(s1) != sorted(s2):
            self.dict_[s1 + s2] = False
            return False
            

        for i in range(1, len(s1)):
            option_1 = self.isScramble_v2(s1[:i], s2[:i]) and self.isScramble_v2(s1[i:], s2[i:])
            option_2 = self.isScramble_v2(s1[:i], s2[-i:]) and self.isScramble_v2(s1[i:], s2[:-i])
            if option_1 or option_2:
                self.dict_[s1 + s2] = True
                return True
        self.dict_[s1 + s2] = False
        return False


    """
解法 3: 动态规划

dp[i][j][len_] = True 表明 s1[i: i + len_] 与 s2[j: j + len_] 可以通过扰乱得到

例如: s1 = "abcde", s2 = "deabc", 则 dp[0][2][3] 为 True, 因为 s1[0: 3] 扰乱后
可变成 s2[2: 5]


对与两个字符串是否可以通过扰乱互相转换，我们可以一层一层的看，最高层就是整个字符串，最底层是字符。每一层都可以把这个串拆成两个子串。

对于每一层可以归纳为两种情况：一是当前层的两个子串经过交换，第二种当前层未经过交换。

对于这每一种情况，都要检查每一种子串划分的方法
    """
    def isScramble_v3(self, s1: str, s2: str) -> bool:
        len_ = len(s1)
        # jy: 如果长度不等, 则直接返回 False
        if len_ != len(s2):
            return False

        # jy: 先初始化 dp 为全 False
        dp = [[None for _ in range(len_)] for _ in range(len_)]
        for i in range(len_):
            for j in range(len_):
                # jy: dp 的第三个维度的长度取决于 i 和 j 的值, 因为需确
                #     保 i 或 j 下标位置之后存在相应长度的字符数, 否则字
                #     符数都不相等, 必然为 False (当 i 和 j 均为 0 时, 
                #     dp[0][0] 的值为 len_ + 1 个, 第三维最大下标为 len_)
                dp[i][j] = [False] * (min(len_ - i, len_ - j) + 1)
                # jy: 第三维度的值拉满也不影响后续逻辑, 但浪费存储空间
                #dp[i][j] = [False] * (len_ + 1)

        # jy: 所有 len_ 为 1 的情况必须是对应字符相等, 因此 dp[i][j][1] 的值
        #     等价于 s1[i] == s2[j], 即: 如果两个字符相等, 则表明可扰乱得到
        for i in range(len_):
            for j in range(len_):
                dp[i][j][1] = s1[i] == s2[j]

        # jy: 长度从 2 开始逐步动态规划求解至长度为 len_
        for k in range(2, len_ + 1):
            # jy: 当确定长度为 k 时, i 和 j 的下标范围只能在 [0, len_ - k]
            #     范围之内, 超过该范围内的下标位置之后的字符个数少于 k 个
            for i in range(len_ - k + 1):
                for j in range(len_ - k + 1):
                    # jy: sep 是分割点, 此处即检查每一种子串划分的方法
                    for sep in range(1, k):
                        # jy: 第一种情况: 当前层两个子串未经过交换 (S1 -> T1, S2 -> T2)
                        #     即 s1 和 s2 的左半部分的长度为 sep, 右半部分的长度为 k - sep
                        if dp[i][j][sep] and dp[i + sep][j + sep][k - sep]:
                            dp[i][j][k] = True
                            break
                        # jy: 第二种情况: 当前层的两个子串经过交换 (S1 -> T2, S2 -> T1)
                        #     即 s1 的左半部分和 s2 的右半部分的长度为 sep, s1 的右半部
                        #     分和 s2 的左半部分的长度为 k - sep
                        if dp[i][j + k - sep][sep] and dp[i + sep][j][k - sep]:
                            dp[i][j][k] = True
                            break

        # jy: 【仅供调试使用】k 为 0 的位置不需做任何处理, 一直为 False
        """
        for i in range(len_):
            for j in range(len_):
                # jy: 均为 False
                print("k=0 : %s" % dp[i][j][0])
        """

        return dp[0][0][len_]



s1 = "great"
s2 = "rgeat"
res = Solution().isScramble_v1(s1, s2)
# jy: true
print(res)


s1 = "abcde"
s2 = "caebd"
res = Solution().isScramble_v2(s1, s2)
# jy: false
print(res)


s1 = "a"
s2 = "a"
res = Solution().isScramble_v3(s1, s2)
# jy: true
print(res)


s1 = "abcde"
s2 = "caebd"
res = Solution().isScramble_v3(s1, s2)
# jy: false
print(res)

