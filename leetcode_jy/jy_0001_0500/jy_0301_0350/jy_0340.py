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
title_jy = "Longest-Substring-with-At-Most-K-Distinct-Characters(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string ``s`` and an integer ``k``, return the length of the longest substring
of ``s`` that contains at most ``k`` distinct characters.


Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.


Constraints:
1 <= s.length <= 5 * 10^4
0 <= k <= 50
"""


import collections


class Solution:
    """
使用 start 和 end 维护一个窗口, 起始 start 和 end 都指向 0, 同时使用字典 counter 记录窗口
中每个字符的个数(字典中元素的个数即为不同类型字符的个数), 不断将 end 向右移动一位并将该位
置对应的字符加入到 counter 中, 如果 counter 中元素的个数超过 k, 则滑动窗口从 start 位置开
始不断右移缩小, 缩小过程中不断将 start 位置对应的字符从 counter 中去除, 直到 counter 的元
素个数不超过 k (即剔除到等于 k 为止);

注意, counter 中的元素个数大于 k 时缩小窗口的操作是为了找下一个可能能更长的窗口; counter 等
于 k 时不能就开始 start 右移缩小窗口, 因为此时 end 的下一个元素可能在 counter 中已经存在, 此
时 end 右移扩大窗口可能是一个更合适的目标窗口;
    """
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = collections.defaultdict(int)
        # jy: 初始化滑动窗口的起始坐标为 0;
        start = 0
        max_window = (0, 0)
        # jy: 遍历字符串 s, 尝试将其中的所有字符对应的下标当做滑动窗口的末尾下标 end, 如果
        #     窗口对应的子串满足要求(不同字符小于或等于 k 个), end 不断右移, 扩大窗口长度,
        #     如果随着 end 不断右移窗口不断扩大, 但窗口中的不同字符一直等于 k, 则表明以当前
        #     窗口是一个更长且符合目标要求的窗口, 则最长窗口会不断被更新; 如果窗口对应的子串
        #     中不同字符大于 k 个, 则表明以当前 start 起始下标的最大窗口已经不满足要求(且满
        #     足要求的最大窗口已经被记录了), 此时在 counter 中将当前 start 对应的字符剔除,
        #     并不断将 start 右移, 直到窗口中的不同字符小于或等于 k 个, 在此基础上找后续的最
        #     大窗口;
        for end in range(len(s)):
            counter[s[end]] += 1
            # jy: 如果窗口中的不同字符大于 k 个, 则在字典中删除当前 start 对应的字符(字符数
            #     减 1, 如果字符个数为 0, 则在字典中删除), 随后 start 进 1, 直到不同字符数小
            #     于等于 k 个为止;
            while len(counter) > k and start < len(s):
                counter[s[start]] -= 1
                if counter[s[start]] == 0:
                    counter.pop(s[start])
                start += 1

            # jy: 经过以上 while 循环, 总是确保当前窗口的字符类型数是小于 k 个的; 此时需判断是否更
            #     新最大窗口;
            max_window = (start, end) if end - start > max_window[1] - max_window[0] else max_window

        print(s[max_window[0]: max_window[1]+1])
        return max_window[1] - max_window[0] + 1


s = "eceba"
k = 2
# Output: 3
res = Solution().lengthOfLongestSubstringKDistinct(s, k)
print(res)


s = "aa"
k = 1
# Output: 2
res = Solution().lengthOfLongestSubstringKDistinct(s, k)
print(res)


