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
2) 基于 need_char_counter 字典和 need_count (这两个变量的含义参见以下代码注
   解), 寻找滑动窗口的末尾下标, 使得窗口能满足条件, 随后判断滑动窗口是否更小
3) 移动 start (确保新的 start 对应的字符在 t 中), 并更新 need_char_counter 字
   典, 必要时更新 need_count, 继续寻找下一个有效的滑动窗口

注意: 该题的关键在于每一轮新滑动窗口的寻找过程中, 更新 need_char_counter 和
need_count 中的技巧 (need_char_counter 无需总是重复统计)
    """
    def minWindow_v2(self, s: str, t: str) -> str:
        len_s = len(s)
        # jy: 理解该题的关键要先理解 need_char_counter 和 need_count:
        #     need_char_counter: 统计当前窗口对应的子串中, 目标字
        #                        符串 t 中每个类型的字符缺几个
        #     need_count: 统计还缺几个字符就能包含所有目标字符串
        # jy: 注意: 因为后续的逻辑中 need_char_counter 字典中某些字符对应的值
        #     可能是负数 (表示此类字符已经找到超过目标个数多少个)
        need_char_counter = collections.Counter(t)
        need_count = len(t)

        # jy: 记录窗口的首末下标位置, 初始化为一个极大值
        min_window = (0, sys.maxsize)

        # jy: 找出滑动窗口的起始下标 (满足要求的滑动窗口的起始下标位置
        #     对应的字符必定在 t 中存在)
        start = 0
        while start < len_s and s[start] not in need_char_counter:
            start += 1

        # jy: 从 start 下标位置开始尝试将字符串的各个字符下标作为滑动窗
        #     口的末尾下标
        for end in range(start, len_s):
            #print(start, end)
            # jy: 如果当前下标对应的字符不在 need_char_counter 中, 表明当前
            #     end 不可能满足要求, end 直接跳到下一位
            if s[end] not in need_char_counter:
                continue

            # jy: 执行到此处表明当前字符为 t 中的一员, 在 need_char_counter
            #     中将该字符的个数减 1, 表明将当前字符加入到滑动窗口后, 目
            #     标字符串中该字符的缺失数量少 1:
            #     1) 如果该字符在 need_char_counter 中的记录个数大于等于 0,
            #        表明当前的该字符是 t 的组成部分, need_count 数也相应减 1
            #     2) 如果该字符在 need_char_counter 中的记录个数小于 0, 表明
            #        当前滑动窗口中的该字符虽然在 t 中出现, 但已找到足够的该
            #        字符, 此时 need_count 不能减 1, 当前 end 对应的字符不能
            #        使得滑动窗口满足要求, 仍需继续向后遍历找其它类型的字符
            need_char_counter[s[end]] -= 1
            if need_char_counter[s[end]] >= 0:
                need_count -= 1

            # jy: 如果 need_count 为 0, 表明当前 (start, end) 是一个满足
            #     条件的窗口 (如果循环过程中移动 start 后 need_count 仍
            #     为 0, 表明窗口仍满足条件)
            while need_count == 0:
                # jy: 如果 need_count 为 0, 表明当前 (start, end) 是一个满足
                #     条件的窗口, 判断该窗口是否比之前的窗口记录小, 小则更新
                if end - start < min_window[1] - min_window[0]:
                    min_window = (start, end)

                # jy: need_char_counter 中 start 下标位置的字符 (该字符存在
                #     于 t 中) 恢复加 1, 因为 start 准备往前移动了, 因此在
                #     need_char_counter 中该位置对应的字符的需求数需加回 1
                # jy: 注意, 当 s[start] 在 need_char_counter 中为负数时, 表
                #     明当前滑动窗口中 start 对应的字符已经超过目标字符串中
                #     该字符的数量了, 此时移动 start 恢复该字符的需求数后
                #     (即加 1), need_char_counter 中的该字符对应的值仍小于
                #     或等于 0, 表明即使 start 前进一步, 缩小后的滑动窗口仍
                #     为满足要求的, 会继续当前的 while 循环更新最小滑动窗口
                need_char_counter[s[start]] += 1
                if need_char_counter[s[start]] > 0:
                    need_count += 1

                # jy: 更新 start 下标, start 对应的字符必须出现在 t 中
                #     (该更新方式较为粗糙, 使得执行效率不如方法 3)
                start += 1
                while start < len_s and s[start] not in need_char_counter:
                    start += 1

        # jy: 返回最小滑动窗口对应的字符串
        return "" if min_window[1] > len_s else s[min_window[0]: min_window[1]+1]


    """
解法 3: 思路同解法 2, 代码执行效率更高
1) 找到满足条件的初始窗口 [start, end]
2) start 不断右移, 在确保满足条件的情况下不断缩小窗口, 随后判断是否更新最小窗口;
   (即固定满足条件时的 end, 通过 start 不断右移缩小窗口)
3) start 加 1 (该操作后新的窗口必定不满足条件, 因为原先的以 end 结尾的窗口已经是满足条件
   的最小窗口), 则此时窗口中缺少一个原先 start 对应的字符才能满足条件, 进入下一轮循环, 继
   续找新的满足条件的 end 下标;  
    """
    def minWindow_v3(self, s: str, t: str) -> str:
        len_s = len(s)
        need_char_count = collections.defaultdict(int)
        for c in t:
            need_char_count[c] += 1
        need_count = len(t)

        # jy: 记录滑动窗口的起始下标;
        start = 0
        min_window = (0, float('inf'))
        for end in range(start, len_s):

            if s[end] not in need_char_count:
                continue

            need_char_count[s[end]] -= 1
            if need_char_count[s[end]] >= 0:
                need_count -= 1
 
            # jy: 以下部分开始与解法 2 中的略有区别 (效率更高)
            if need_count == 0:
                # jy: 在确保满足条件的情况下不断右移 start, 缩小窗口: 由于
                #     need_count 为 0, 因此 need_char_count 中的字符对应的
                #     数值均小于或等于 0, 表明所有字符都不缺了 (有的甚至还
                #     多过头了); 此时不断尝试右移 start, 确保 start 对应的
                #     字符在 need_char_count 中 (即在目标字符串中):
                #     1) 如果此时 start 对应的字符在 need_char_count 中记录
                #        的值为 0, 表明当前的 start 不能再往前移了, 否则又
                #        会使当前的滑动窗口中缺少一个目标字符
                #     2) 如果此时 start 对应的字符在 need_char_count 中记录
                #        的值不为 0, 则其值必定为负值, 因为结合当前 need_count
                #        的值为 0 可知, 当前不缺 s[start] 字符, 该字符只能是
                #        过多了, 因此 need_char_count 中该字符对应的值为负值;
                #        因此, 表明当前 start 位置可以跳过, 并在 need_char_count
                #        中更新跳过该字符后的值
                while True:
                    while s[start] not in need_char_count:
                        start += 1
                    if need_char_count[s[start]] == 0:
                        break
                     need_char_count[s[start]] += 1
                     start += 1

                # jy: 经过以上操作后, 以 end 结尾的满足条件的窗口已经是最小窗
                #     口, 如果当前窗口更小, 则更新最小窗口记录
                if end - start < min_window[1] - min_window[0]:
                    min_window = (start, end)
                # jy: start 加 1, 寻找下一个满足条件的窗口; 在 start 加 1 之前
                #     需将原先的 start 位置对应的字符 (必定是在 t 中的字符) 在
                #     need_char_count 和 need_count 中的统计信息恢复, 以表明窗
                #     口的 end 下标需要继续向右寻找到 1 个出现该字符的位置
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


