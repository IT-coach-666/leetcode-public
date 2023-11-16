# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Longest-Substring-Without-Repeating-Characters(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "动态规划 | 滑动窗口 + 巧用字典"


"""
Given a string, find the length of the longest substring without repeating
characters.


Example 1:
Input: "abcabcbb"
Output: 3  (The answer is "abc", with the length of 3.)

Example 2:
Input: "bbbbb"
Output: 1

Example 3:
Input: "pwwkew"
Output: 3  (The answer is "wke", with the length of 3. Note that the answer
            must be a  substring, "pwke" is a subsequence and not a substring.)
"""


class Solution:
    """
解法1: 动态规划 (超时、超出内存限制, 因为 dp 是一个 n^2 二维数组)

设 dp[i][j] = True 表示 s[i:j+1] 为一个无重复子串, 则 dp[i][j] = True 需满足:
1) s[j] 不在 s[i:j] 中
2) dp[i][j-1] = True

求解过程即计算 dp 二维数组的过程, 最终返回使得 dp[i][j] = True 且使得 j-i+1 值
最大的结果 (实际长度比下标值的差大 1)

求解时, 仅需求解 dp 矩阵的上三角对应的值即可(因为要求 j > i)
    """
    def lengthOfLongestSubstring_v1(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        # jy: 初始化 dp 均为 False（dp[i][i] 后续会设置为 True）
        dp = [[False for _ in range(n)] for _ in range(n)]
        # jy: 记录最长目标子串长度（初始值设置为 1）
        max_length = 1
        # jy: i 从 0 开始遍历, j 从 i 的下一个值开始遍历（因为求解矩阵上三角,
        #     要求 j > i）
        for i in range(0, n):
            # jy: dp[i][i] 必定为 True
            dp[i][i] = True
            for j in range(i+1, n):
                # jy: 更新 d[i][j] 的值, 如果 dp[i][j] 为 True, 则判断是否更
                #     新 max_length
                dp[i][j] = dp[i][j-1] and s[j] not in s[i:j]
                if dp[i][j]:
                    max_length = max(max_length, j-i+1)
                # jy: 如果当前的 dp[i][j] 为 False, 则后续的 j 都不再使得
                #     dp[i][j] 满足条件, 因此可提前退出当前内循环、加速查找过程
                else:
                    break
        return max_length


    """
解法2: 滑动窗口 + 字典 (记录无重复子串)

维护一个无重复字串滑动窗口, i 和 j 分别表示滑动窗口的首尾下标, 初始均指向
字符串的第一个字符; j 不断往后移动遍历 s, 当 s[j] 存在于 s[i:j] 中时, 假
设 s[j] 在 s[i:j] 中的下标为 k, 则需更新 i 的位置为 k+1, 使得新的 
s[k+1: j+1] 为无重复子串滑动窗口; 

每次遍历完成后均统计无重复字串滑动窗口的长度, 如果比之前的记录更长, 则更新
最长滑动窗口的长度

JY: 由于涉及滑动窗口对应的字典 window_item 中删除元素(硬删除策略), 性能普通
    """
    def lengthOfLongestSubstring_v2(self, s: str, is_v1=True) -> int:
        # jy: 滑动窗口的起始下标
        i = 0
        max_length = 0
        # jy: 记录当前滑动窗口中的已有字符以及字符在 s 中的下标位置
        window_item = {}
        # jy: 滑动窗口的末尾下标 j 不断后移
        for j, c in enumerate(s):
            # jy: 如果当前 j 对应的字符 c 在滑动窗口(即在 window_item
            #     字典)中, 则找出 c 在 s 中的位置下标 index, 并将 window_item
            #     中的 s[i: index + 1] 字符删除, 新的滑动窗口的起始下标也需更
            #     新为 index + 1, 此时新的 j 成为当前滑动窗口的末尾下标, 并将
            #     其对应的字符 c 和下标位置 j 记录到 window_item 字典中 (使得
            #     后续可判断其它字符是否与字典中的字符重复)
            # jy: is_v1=True 表明使用第一种删除策略
            if c in window_item and is_v1:
                index = window_item[c]
                for k in range(i, index + 1):
                    del window_item[s[k]]
                i = index + 1
            # jy: is_v1=False 表明使用第二种删除策略: 不需用到 window_item 中
            #     字符对应的下标, 因此可以将 window_item 字典换为 set() 进行
            #     操作(效果更优)
            while c in window_item and not is_v1:
                del window_item[s[i]]
                i += 1

            # jy: 将当前位置 j 对应的字符及其下标位置添加到 window_item 字典中
            window_item[c] = j

            # jy: 以上操作确保 window_item 中总是记录无重复滑动窗口元素, 且 i 
            #     和 j 分别为当前有效滑动窗口的首末位置下标; 每次更新滑动窗口,
            #     都判断是否更新 max_length
            if j-i+1 > max_length:
                max_length = j-i+1
        return max_length


    """
解法3: 解法 2 中每次更新滑动窗口的起始下标时的硬删除可以修改为软删除:
1) substring 字典记录遍历 s 时遇到的每一字符及其对应的下标; 如果该字符为重
   复字符, 该字符在 substring 中记录的下标是最近一次访问到的下标)
2) 如果当前字符在 substring 中, 且下标为 k, 由于滑动窗口必须是从 k+1 或之
   后位置开始, 因此需判断 k+1 是否大于滑动窗口的起始下标 i (即判断重复字符
   是否落在当前滑动窗口之中):
   a) 如果大于则说明重复字符落在当前滑动窗口中, 需更新滑动窗口的起始下标为 k+1
   b) 如果小于说明重复字符落在当前滑动窗口之外, 不需要更新
    """
    def lengthOfLongestSubstring_v3(self, s: str) -> int:
        # jy: 无重复字串滑动窗口的起始下标, 初始化为 0
        i = 0
        max_length = 0
        # jy: 记录遍历 s 时遇到的每一个字符及其对应的下标 (如果该字符为重复字
        #     符, 则记录的下标会是最近一次访问到的下标)
        substring = {}
        # jy: 将滑动窗口的末尾下标 j 不断右移, 如果其对应的字符 c 在 substring
        #     中且下标为 k, 则判断 k+1 是否大于 i (即判断重复字符是否落在当前
        #     滑动窗口中); 因为接下来的有效滑动窗口必须是从 k+1 或之后的位置开
        #     始):
        #     a) 如果 k+1 大于 i 则说明重复字符落在当前滑动窗口中, 需更新滑动
        #        窗口的起始下标为 k+1
        #     b) 如果 k+1 小于 i 则说明重复字符落在当前滑动窗口之外, 不需要更新
        for j, c in enumerate(s):
            if c in substring:
                i = max(substring[c] + 1, i)
            # jy: 记录遍历 s 时遇到的每一个字符及其对应的下标 (如果该字符为重复
            #     字符, 记录的下标会是最近一次访问到的下标)
            substring[c] = j

            # jy: 每轮更新滑动窗口的起始或末尾下标都判断是否更新 max_length
            max_length = max(max_length, j-i+1)
        return max_length


    """
JY: 暴力求解 (超时)
    """
    def lengthOfLongestSubstring_jy(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        # jy: 记录最长目标子串长度
        max_length = 1
        # jy: i 从当前位置开始往后遍历, j 从最后一个位置开始往前遍历, 直到
        #     与 i 相遇, 遍历过程中判断 s[i: j+1] 是否为无重复子串
        for i in range(0, n):
            for j in range(n-1, i, -1):
                # jy: 如果遍历至某个位置 j 时产生无重复的字串, 则该字串即为从
                #     位置 i 开始的最长无重复子串, 因此可跳出当前 j 的遍历; 但
                #     此时还不能确定 i 之后位置的最长无重复子串是否更长, 因此
                #     仍需遍历 i 查找其它最长无重复字串, 挑选最长的一个
                if len(s[i:j+1]) == len(set(s[i:j+1])) and j-i+1 > max_length:
                    max_length = j-i+1
                    break
        return max_length



res = Solution().lengthOfLongestSubstring_v1("abcabcbb")
print(res)

res = Solution().lengthOfLongestSubstring_v2("abcabcbb")
print(res)

res = Solution().lengthOfLongestSubstring_v3("abcabcbb")
print(res)

res = Solution().lengthOfLongestSubstring_v4("abcabcbb")
print(res)


