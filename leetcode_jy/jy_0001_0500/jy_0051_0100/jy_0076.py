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
tag_jy = "滑动窗口 + 巧用字典 | IMP2"



"""
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the
minimum window substring of `s` such that every character in `t` (including
duplicates) is included in the window. If there is no such substring, return
the empty string "".

The test cases will be generated such that the answer is unique.


Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
             from string `t`.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string `s` is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from `t` must be included in the window. Since the
             largest window of `s` only has one 'a', return empty string.


Constraints:
1) m == s.length
2) n == t.length
3) 1 <= m, n <= 10^5
4) `s` and `t` consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


import collections


class Solution:
    """
解法 1: 暴力求解 (超时)

遍历 s 的每一个下标位置, 以当前下标位置为滑动窗口的起始下标, 向后遍历
字符串, 直到当前窗口中的字符串包含 t 的所有字符, 表明在指定起始下标中
找到了一个满足要求的最小窗口, 如果该窗口比之前的窗口小, 则更新最小窗口
    """
    def minWindow_v1(self, s: str, t: str) -> str:
        min_window = ''
        min_window_length = sys.maxsize
        len_s = len(s)

        # jy: 尝试以字符串的每个位置下标为窗口的起始下标
        start = 0
        while start < len_s:
            # jy: 统计目标字符串 t 的各个字符的个数
            char_counter = collections.Counter(t)

            # jy: 优化: 满足要求的最小子串的起始下标 start 对应的字符必定
            #     在 t 中, 如果 start 对应的字符不在 t 中, 直接后移 start,
            #     减少后续不必要的 while 逻辑
            while start < len_s and s[start] not in char_counter:
                start += 1

            # jy: 初始化窗口的末尾下标
            end = start
            # jy: 末尾下标 end 不断右移, 在有效的末尾下标中不断查找, 当 end 下标位置对应
            #     的字符在 char_counter 中且该字符的个数仍大于 1 时, 将其个数减 1, 直到
            #     char_counter 中所有字符的个数总和为 0, 此时表示 s[start: end+1] 包含
            #     了所有 t 中的字符, 跳出当前 while 循环;
            while end < len_s:
                if s[end] in char_counter and char_counter[s[end]] >= 1:
                    char_counter[s[end]] -= 1
                # jy: 如果找到一个满足要求的窗口, 即为以 start 开头的滑动窗口中的最小窗
                #     口, 如果该窗口比之前的窗口小, 则更新最小窗口, 并退出循环, 遍历下
                #     一个滑动窗口
                if sum(char_counter.values()) == 0:
                    if end - start + 1 < min_window_length:
                        min_window_length = end - start + 1
                        min_window = s[start: end + 1]
                    break
                end += 1
            start += 1
        return min_window


    """
解法 2: 滑动窗口 (IMP)
1) start 不断右移, 直到对应的字符在 t 中, 将其作为窗口的起始下标
2) 找窗口的末尾下标, 使得窗口能满足条件; 找到后判断是否更新最小窗口; (即固定 start, 找
   出该情况下满足条件的 end 最小下标, 使得窗口是以 start 作为起始下标时的最小窗口)
3) 更新 start, 确保 start 得到更新, 且其对应的字符仍在 t 中, 继续循环以上操作, 找新的 end;
   (该更新方式较为粗糙, 导致执行效率不如方法 3)
    """
    def minWindow_v2(self, s: str, t: str) -> str:
        len_s = len(s)
        # jy: 理解该题的关键要先理解 char_counter 和 count:
        #     char_counter: 统计当前窗口对应的子串中, 目标字
        #                   符串 t 中每个类型的字符缺几个
        #     count: 统计还缺几个字符就能包含所有目标字符串
        # jy: 注意: 因为后续的逻辑中 char_counter 字典中某些字符对应的值
        #     可能是负数 (表示对于某些字符已经找到超过目标个数多少个了)
        char_counter = collections.Counter(t)
        count = len(t)

        # jy: 记录窗口的首末下标位置, 初始化为一个极大值
        min_window = (0, sys.maxsize)

        # jy: 找出滑动窗口的起始下标 (满足要求的滑动窗口的起始下标位置
        #     对应的字符必定在 t 中存在)
        start = 0
        while start < len_s and s[start] not in char_counter:
            start += 1

        # jy: 从 start 下标位置开始尝试将字符串的各个字符下标作为滑动窗
        #     口的末尾下标
        for end in range(start, len_s):
            print(start, end)
            # jy: 如果当前下标对应的字符不在 char_counter 中, 表明当前
            #     end 不可能满足要求, end 直接跳到下一位
            if s[end] not in char_counter:
                continue

            # jy: 执行到此处表明当前字符为 t 中的一员, 在 char_counter 中
            #     将该字符的个数减 1, 表明将当前字符加入到滑动窗口后, 目
            #     标字符串中该字符的缺失数量少 1:
            #     1) 如果该字符在 char_counter 中的记录个数大于等于 0, 表
            #        明当前的该字符是 t 的组成部分, count 数也相应减 1
            #     2) 如果该字符在 char_counter 中的记录个数小于 0, 表明当
            #        前滑动窗口中的该字符虽然在 t 中出现, 但已找到足够的
            #        该字符, 此时 count 不能减 1, 当前 end 对应的字符不能
            #        使得滑动窗口满足要求, 仍需继续向后遍历找其它类型的字符
            char_counter[s[end]] -= 1
            if char_counter[s[end]] >= 0:
                count -= 1
                while count == 0:
                    # jy: 如果 count 为 0, 表明当前 (start, end) 是一个满足条件
                    #     的窗口, 判断该窗口是否比之前的窗口记录小, 小则更新
                    if end - start < min_window[1] - min_window[0]:
                        min_window = (start, end)

                    # jy: 恢复原 start 下标位置的字符 (该字符存在于 t 中) 在
                    #     char_counter 和 count 中的统计信息, 并同时让 count
                    #     加 1, 表明下一个窗口中差一个字符才满足要求
                    char_counter[s[start]] += 1
                    # UNDO
                    if char_counter[s[start]] > 0:
                        count += 1

                    # jy: 更新 start 下标, 要求 start 对应的字符必须出现在 t 中
                    #     (该更新方式较为粗糙, 使得执行效率不如方法 3)
                    start += 1
                    while start < len_s and s[start] not in char_counter:
                        start += 1

        # jy: 返回最小滑动窗口对应的字符串
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


