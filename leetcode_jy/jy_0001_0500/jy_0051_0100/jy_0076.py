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
title_jy = "Minimum-Window-Substring(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given two strings ``s`` and ``t`` of lengths ``m`` and ``n`` respectively, return
the minimum window substring of ``s`` such that every character in ``t`` (including
duplicates) is included in the window. If there is no such substring, return the
empty string "".

The test cases will be generated such that the answer is unique. A substring is a
contiguous sequence of characters within the string.


Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from
             string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from ``t`` must be included in the window. Since the largest
             window of ``s`` only has one 'a', return empty string.


Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


import collections
import sys


# Time Limit Exceeded!
class Solution:
    """
解法1(超时): 暴力求解, 遍历 s, 以当前字符串为起始, 向后遍历字符串, 直到当前字符串中
每个字符的个数能够组成 t, 更新符合条件的窗口;
    """
    def minWindow_v1(self, s: str, t: str) -> str:
        min_window = ''
        min_window_length = sys.maxsize
        len_s = len(s)
        # jy-version-1-Begin------------------------------------------------------
        # jy: 尝试以字符串的每个位置下标为窗口的起始下标;
        for start in range(len_s):
            # jy: 统计目标字符串 t 的各个字符的个数;
            char_counter = collections.Counter(t)
            # jy: 记录满足要求的窗口的 end 下标位置是否已找到;
            is_end_finded = False

            # jy: 窗口的末尾下标 end 初始化为与起始下标相同;
            end = start
            # jy: 末尾下标 end 不断右移, 在有效的末尾下标中不断查找, 当 end 下标位置对应
            #     的字符在 char_counter 中且该字符的个数仍大于 1 时, 将其个数减 1, 直到
            #     char_counter 中所有字符的个数总和为 0, 此时表示 s[start: end+1] 包含
            #     了所有 t 中的字符, 跳出当前 while 循环;
            while end < len_s:
                if s[end] in char_counter and char_counter[s[end]] >= 1:
                    char_counter[s[end]] -= 1
                if sum(char_counter.values()) == 0:
                    is_end_finded = True
                    break
                end += 1
            # jy: 如果以上退出 while 循环后的 end 下标满足要求, 且窗口长度小于之前记录的最
            #     小窗口长度, 则更新最小窗口长度;
            if is_end_finded and end - start + 1 < min_window_length:
                min_window_length = end - start + 1
                min_window = s[start: end + 1]
        # jy-version-1-End--------------------------------------------------------
        # jy-version-2-Begin------------------------------------------------------
        '''
        # jy: 对以上 version-1 进行优化: 
        #     1) 满足要求的最小子串的起始下标 start 对应的字符必定是在 t 中的字符, 因此如
        #        果 start 对应的字符不在 t 中, 直接后移 start, 减少后续不必要的 while 逻
        #        辑;
        #     2) 在找到满足要求的 end 下标时, 直接判断此时的窗口是否更小, 是否应更新; 减少
        #        不必要的代码量;
        start = 0
        while start < len_s:
            char_counter = collections.Counter(t)

            while start < len_s and s[start] not in char_counter:
                start += 1

            end = start
            while end < len_s:
                if s[end] in char_counter and char_counter[s[end]] >= 1:
                    char_counter[s[end]] -= 1
                if sum(char_counter.values()) == 0 and \
                        end - start + 1 < min_window_length:
                    min_window_length = end - start + 1
                    min_window = s[start: end + 1]
                    break
                end += 1
            start += 1
        '''
        # jy-version-2-End--------------------------------------------------------
        return min_window

    """
解法2: 滑动窗口; 
1) start 不断右移, 直到对应的字符在 t 中, 将其作为窗口的起始下标;
2) 找窗口的末尾下标, 使得窗口能满足条件; 找到后判断是否更新最小窗口; (即固定 start, 找
   出该情况下满足条件的 end 最小下标, 使得窗口是以 start 作为起始下标时的最小窗口)
3) 更新 start, 确保 start 得到更新, 且其对应的字符仍在 t 中, 继续循环以上操作, 找新的 end;
   (该更新方式较为粗糙, 导致执行效率不如方法 3)
    """
    def minWindow_v2(self, s: str, t: str) -> str:
        len_s = len(s)
        # jy: 记录目标字符串的字符及其出现个数
        char_counter = collections.Counter(t)
        # jy: 记录窗口的起止下标位置, 初始化为一个极大值;
        min_window = (0, sys.maxsize)
        # jy: 记录滑动窗口的起始下标位置, 满足要求的滑动窗口的起始下标位置对应的字符必定在
        #     t 中出现;
        start = 0
        while start < len_s and s[start] not in char_counter:
            start += 1
        # jy: 记录剩余待查找的目标字符个数;
        count = len(t)
        # jy: 从 start 下标位置开始尝试将字符串的各个字符下标作为滑动窗口的末尾下标;
        for end in range(start, len_s):
            print(start, end)
            # jy: 如果当前下标对应的字符不在 char_counter 中, 表明当前 end 不可能满足要求,
            #     直接进行下一轮 for 循环(end + 1);
            if s[end] not in char_counter:
                continue

            # jy: 执行到此处表明当前字符在 t 中, 在 char_counter 中将该字符的个数减 1;
            #     1) 如果该字符在 char_counter 中的记录个数大于等于 0, 表明当前的该字符
            #        是 t 的组成部, count 数也相应减 1;
            #     2) 如果该字符在 char_counter 中的记录个数小于 0, 表明虽然该字符在 t 中
            #        出现, 但 t 中已找到足够的该字符, 此时 count 不能减 1, 当前 end 下标
            #        对应的字符并非目标查找字符;
            char_counter[s[end]] -= 1
            if char_counter[s[end]] >= 0:
                count -= 1
                # jy: 如果 count 为 0, 表明当前 (start, end) 是一个满足条件的窗口, 判断
                #     该窗口是否比之前的窗口记录小, 小则更新; 由于需要寻找下一个滑动窗口,
                #     因此 start 下标位置要得到更新(更新为下一个出现在 t 中的下标位置),
                #     在更新之前需要先将原 start 对应的字符(必定是在 t 中的)的信息恢复到
                #     char_counter 和 count 中;
                while count == 0:
                    min_window = (start, end) if \
                        end - start < min_window[1] - min_window[0] else min_window
                    # jy: 恢复原 start 下标位置的字符在 char_counter 和 count 中的统计信
                    #     息;
                    char_counter[s[start]] += 1
                    if char_counter[s[start]] > 0:
                        count += 1
                    # jy: 更新 start 下标为下一个出现在 t 中的下标位置(该更新方式较为粗糙,
                    #     导致执行效率不如方法 3);
                    start += 1
                    while start < len_s and s[start] not in char_counter:
                        start += 1

        return "" if min_window[1] > len_s else s[min_window[0]: min_window[1]+1]

    """
解法 3: 思路同解法 2, 代码执行效率更高;
1) 找到满足条件的初始窗口 [start, end]
2) start 不断右移, 在确保满足条件的情况下不断缩小窗口, 随后判断是否更新最小窗口;
   (即固定满足条件时的 end, 通过 start 不断右移缩小窗口)
3) start 加 1 (该操作后新的窗口必定不满足条件, 因为原先的以 end 结尾的窗口已经是满足条件
   的最小窗口), 则此时窗口中缺少一个原先 start 对应的字符才能满足条件, 进入下一轮循环, 继
   续找新的满足条件的 end 下标;  
    """
    def minWindow_v3(self, s: str, t: str) -> str:
        len_s = len(s)
        # jy: 记录窗口需要包含的字符串 t 中的各个字符以及出现次数;
        need_char_count = collections.defaultdict(int)
        for c in t:
            # jy: 由于使用的是带默认值为 int 的字典(默认为 0), 可以直接统计字符个数;
            need_char_count[c] += 1
        # jy: 记录剩余待查找的目标字符串中的字符个数;
        need_count = len(t)
        # jy: 记录滑动窗口的起始下标;
        start = 0
        min_window = (0, float('inf'))
        # jy: 尝试以字符串的每个字符位置下标作为滑动窗口的末尾下标;
        for end in range(start, len_s):
            # jy: 如果当前 end 对应的字符在 t 中, 当 need_char_count 中该字符数大于 0 时,
            #     表明该字符是 t 中的组成部分, 将 need_count 减 1; (need_char_count 中的
            #     字符对应的个数可能是负值, 如果是负值, 表明当前窗口中的该字符大于 t 中该
            #     字符的个数);
            if s[end] in need_char_count:
                if need_char_count[s[end]] > 0:
                    need_count -= 1
                need_char_count[s[end]] -= 1

            # jy: 如果 need_count 为 0, 表明当前窗口 (start, end) 满足条件;
            if need_count == 0:
                # jy: 尝试在确保满足条件的情况下不断右移 start, 缩小窗口; 每当 start 右移
                #     时, 如果 start 对应的字符在 need_char_count 中, 则该字符的统计信息
                #     是否为 0, 如果是, 则不能继续右移, 如果不为 0 (则必定是小于 0, 因为当
                #     前的窗口是满足条件的了), 则 start 可以右移, 右移时将
                #     need_char_count 中该字符的个数加 1 即可;
                while True:
                    if s[start] in need_char_count:
                        if need_char_count[s[start]] == 0:
                            break
                        need_char_count[s[start]] += 1
                    start += 1
                # jy: 经过以上操作后, 以 end 结尾的满足条件的窗口已经是最小窗口, 与之前的最
                #     小窗口记录比较, 判断是否更新当前最小窗口;
                min_window = (start, end) if \
                    end - start < min_window[1] - min_window[0] else min_window
                # jy: start 加 1, 寻找下一个满足条件的窗口; 在 start 加 1 之前需要将原先的
                #     start 位置对应的字符(必定是在 t 中的字符) 在 need_char_count 和
                #     need_count 中的统计信息恢复, 以表明窗口的 end 下标需要继续向右寻找到
                #     1 个出现该字符的位置;
                need_char_count[s[start]] += 1
                need_count += 1
                start += 1
        return '' if min_window[1] > len_s else s[min_window[0]: min_window[1] + 1]


s = "ADOBECODEBANC"
t = "ABC"
# Output: "BANC"
res = Solution().minWindow_v1(s, t)
print(res)
res = Solution().minWindow_v2(s, t)
print(res)


s = "a"
t = "a"
# Output: "a"
res = Solution().minWindow_v2(s, t)
print(res)


s = "a"
t = "aa"
# Output: ""
res = Solution().minWindow_v2(s, t)
print(res)


s = "aaaaaABC"
t = "ABC"
# Output: "ABC"
res = Solution().minWindow_v3(s, t)
print(res)



