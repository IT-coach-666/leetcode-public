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
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Longest-Palindromic-Substring(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "动态规划 | 双指针"


"""
Given a string ``s``, find the longest palindromic substring in ``s``. 
You may assume that the maximum length of ``s`` is 1000.


Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""


class Solution:
    """
解法1: 动态规划, 时间复杂度和空间复杂度均较差
定义 dp[i][j]=True 表示 s[i:j+1] (其中 j > i) 为回文, 则: 
    dp[i][j] = (s[i] == s[j]) and (j-i == 1 or dp[i+1][j-1])
解析:
    1) j-i == 1 即两字符相邻, 此时如果 s[i] == s[j] 则可确
       认 s[i:j+1] 是回文
    2) dp[i][j] 的求解依赖于 dp[i+1][j-1], 且要求 j > i, 因此
       求解时 i 要从后往前遍历, j 要从 i 往后遍历
       (或者: j 从前往后遍历, i 从前往 j 遍历)
    """
    def longestPalindrome_v1(self, s: str) -> str:
        length = len(s)
        # jy: 记录最大回文子串的首尾下标
        start, end = 0, 0
        longest_ = s[0]
        # jy: 初始化 dp[i][j] 均为 False
        dp = [[False for _ in range(length)] for _ in range(length)]
        # jy: dp[i][i] 后续会赋值为 True, 表示由一个字符构成的回文; 也可在此
        #     处进行 dp[i][i] 的更新赋值, 后续的则注释掉
        '''
        for i in range(length):
            dp[i][i] = True
        '''

        # jy: 遍历方式一: j 从前往后遍历, i 从前至 j 遍历 --------------------
        #     该遍历方式确保 j > i, 且求解 dp[i][j] 时每新的一轮外层 j 循环时,
        #     都能确保上一轮中 dp[i][j] 都已经求解得到 (i 为 0 到 j), 因此新的
        #     一轮循环中需要使用到的 dp[i+1][j-1] 肯定是在上一轮循环中已经求解
        #     得到
        for j in range(length):
            # jy: 如果初始化时已经设置, 则此处可注释掉
            dp[j][j] = True
            for i in range(j):
                # jy: 注意, j-i == 1 or dp[i+1][j-1] 中 or 的前面最好是
                #     j-i==1, 否则会出现 i+1 > j-1 的情况, 使得 dp 取值
                #     为 dp 矩阵的下三角, 值总是为 False, 毫无意义 (执行
                #     过程并不会出现下标越界问题)
                dp[i][j] = s[i] == s[j] and (j-i == 1 or dp[i+1][j-1])
                # jy: 如果 dp[i][j] 为 True, 表明 s[i: j+1] 是回文, 则判断
                #     是否更新最长回文;
                if dp[i][j] and j-i+1 > len(longest_):
                    longest_ = s[i: j+1]
                    start, end = i, j

        # jy: 遍历方式二: i 从后往前遍历, j 从 i 往后遍历 --------------------
        '''
        for i in range(length - 1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, length):
                dp[i][j] = s[i] == s[j] and (j-i == 1 or dp[i+1][j-1])
                if dp[i][j] and j-i+1 > len(longest_):
                    longest_ = s[i: j+1]
                    start, end = i, j
        '''

        print("原字符串: %s, 构成最长回文的起止下标: [%s, %s]" % (s, start, end))
        return longest_


    """
解法2: 双指针法
尝试以字符串中的每个字符为中心, 使用左右指针向左右方向移动, 判断由中心向两边
扩充的子串是否是回文

初始化左右指针时, 以下标位置 i 为中心, 左右指针均初始化为下标位置 i, 初始化
时如果右指针 i 的下一个字符与当前字符相同, 则右指针需移动到重复字符的最右端;
如 noon 或 nooon, 当遍历到第一个 o 时, 左右指针开始时都在第一个 o 处, 然后
右指针需要移动到最右侧的 o, 此时才完成左右指针的初始化, 左右指针才能开始向
左右移动判断是否是回文

注意: 下一轮的字符中心应选择在上一轮左右指针初始化后的右指针的下一个位置, 这
样可以减少不必要的重复判断; 如判断 nooon 时, 没必要将中间的 3 个 'o' 都作为字
符中心进行判断一遍, 因为结果都是相同的
    """
    def longestPalindrome_v2(self, s: str) -> str:
        length = len(s)
        longest_ = s[0]
        # jy: 当前的初始回文中心, 后续的双指针会基于该初始中心进一步初始化
        i = 0
        while i < length:
            # jy: left 和 right 用于记录基于当前初始回文的中心进行初始化的
            #     双指针; 初始化时左右指针指向同一个位置, 并将右指针移动到
            #     相同字符的最右端, 即后续双指针的左右移动均以当前的回文
            #     s[left: right+1] 为中心
            left, right = i, i
            while right < length - 1 and s[right] == s[right + 1]:
                right += 1

            # jy: 更新下一轮的初始回文中心, 将其设置为当前轮初始右指针的下
            #     一个位置 (注意: 必须在此处就做更新, 因为后续的 right 值
            #     会发生改变)
            i = right + 1

            # jy: 双指针法获取当前中心的最长回文长度: 在确保左右指针的左右
            #     两边字符均相等的情况下, 不断往左右两边移动, 直到左右两边
            #     的字符不相等为止, 此时就可以获取到最长回文
            while right < length - 1 and left > 0 and s[right + 1] == s[left - 1]:
                left -= 1
                right += 1
            # jy: 如果得到的回文比当前的回文长, 则进行替换
            if right - left + 1 > len(longest_):
                longest_ = s[left: right+1]
        return longest_

    """
jy: 暴力求解(超时): 两层 for 循环模拟所有子串
    """
    def longestPalindrome_v3(self, s: str) -> str:
        def isPalindrome(str_):
            """
            双指针法判断字符串 s 是否是回文 
            (也可以判断字符串反转后是否等于其本身)
            """
            low, high = 0, len(str_) - 1
            while low < high:
                if str_[low] != str_[high]:
                    return False
                low += 1
                high -= 1
            return True

        length = len(s)
        longest_ = s[0]
        # jy: j 从前往后遍历, i 从前至 j 遍历, 确保 j > i
        for j in range(length):
            for i in range(j):
                # jy: 如果构成回文, 判断回文长度是否更长
                if isPalindrome(s[i: j+1]):
                    if len(s[i: j+1]) > len(longest_):
                        longest_ = s[i: j+1] 
        return longest_



s = "babad"
res = Solution().longestPalindrome_v1(s)
print(res)

s = "baccabad"
res = Solution().longestPalindrome_v2(s)
print(res)

s = "cbbd"
res = Solution().longestPalindrome_v2(s)
print(res)

s = "abc1234321ab"
res = Solution().longestPalindrome_v3(s)
print(res, len(res))

