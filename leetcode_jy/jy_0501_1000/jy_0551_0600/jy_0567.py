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
title_jy = "Permutation-in-String(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given two strings ``s1`` and ``s2``, write a function to return true if ``s2`` contains the permutation
of ``s1``. In other words, one of the first string's permutations is the substring of the second string.


Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False


Constraints:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

import collections


class Solution:
    """
解法1: 首先遍历 s1, 计算出 s1 中各字符出现的次数, 然后遍历 s2, 如果 s2 当前的字符在 s1 中
出现了, 则从当前位置开始遍历 s1.length() 个字符, 判断其字符个数是否与 s1 中各字符个数相等;
    """
    def checkInclusion_v1(self, s1: str, s2: str) -> bool:
        # jy: 统计 s1 中各字符出现的次数;
        counts = collections.Counter(s1)
        # jy: 从头开始遍历 s2, 只需要遍历到下标为 len(s2) - len(s1) 的字符即可(因为下标
        #    为 len(s2) - len(s1) + 1 到 len(s2)-1 的字符个数已经不足 len(s1) 个, 肯定
        #    不满足条件了);
        for i in range(len(s2) - len(s1) + 1):
            # jy: 如果 s2 中的字符不在 s1 中, 则跳过;
            if s2[i] not in counts:
                continue
            # jy: 如果 s2 中的字符在 s1 中, 则从该字符的位置 i 开始, 循环遍历 s2 中的 len(s1)
            #    个字符, 并将该字符及其出现的次数加入到一个字典中, 等遍历完 len(s1) 个字符后,
            #    判断该字典与 s1 中字符对应的字典是否相等, 相等则返回 True;
            current_counts = {}

            for j in range(i, i + len(s1)):
                current_counts[s2[j]] = current_counts.get(s2[j], 0) + 1

            if counts == current_counts:
                return True

        return False

    """
对解法 1 进行代码优化(但实际上执行时间可能反而增加)
    """
    def checkInclusion_jy(self, s1: str, s2: str) -> bool:
        counts = collections.Counter(s1)
        # jy: 从头开始遍历 s2, 只需要遍历到下标为 len(s2) - len(s1) 的字符即可(因为下标
        #    为 len(s2) - len(s1) + 1 到 len(s2)-1 的字符个数已经不足 len(s1) 个, 肯定
        #    不满足条件了);
        len_ = len(s2) - len(s1) + 1
        i = 0
        while i < len_:
            # jy: 如果 s2 中的字符不在 s1 中, 则跳过;
            if s2[i] not in counts:
                i += 1
                continue
            # jy: 如果 s2 中的字符在 s1 中, 则从该字符的位置 i 开始, 循环遍历 s2 中的 len(s1)
            #    个字符, 并将该字符及其出现的次数加入到一个字典中, 等遍历完 len(s1) 个字符后,
            #    判断该字典与 s1 中字符对应的字典是否相等, 相等则返回 True;
            current_counts = {}

            for j in range(i, i + len(s1)):
                # jy: 经 LeetCode 执行验证, 多了以下 if 判断可能反而会使执行时间增加;
                if s2[j] not in s1:
                    i = j
                    break
                current_counts[s2[j]] = current_counts.get(s2[j], 0) + 1

            if counts == current_counts:
                return True

            i += 1

        return False


    """
解法2: 维护一个窗口表示 s2 的子串下各字符的个数, 遍历 s2, 更新当前字符在窗口中的个数, 如果当
前窗口的大小超过了 s1 的长度, 则从窗口中将第一个字符的个数减 1, 如果该字符个数为 0, 则剔除该
字符; 如果当前窗口中各字符的个数等于 s1 中各字符的个数, 则返回 True;
    """
    def checkInclusion_v2(self, s1: str, s2: str) -> bool:
        # jy: 统计 s1 中各字符的个数;
        counts1 = collections.Counter(s1)
        counts2 = {}
        # jy: 遍历 s2 字符串, 每一轮 for 循环结束后, 都能确保 counts2 中字符的个数
        #    是小于或等于 counts1 中的字符个数的(即该字典中统计了一个窗口中的字符
        #    以及其出现的次数)
        for i, c in enumerate(s2):
            # jy: 将遍历得到的字符加入 counts2 字典中, 并记录其出现次数;
            counts2[c] = counts2.get(c, 0) + 1
            # jy: i 是 s2 中的字符的下标; 如果 i 大于等于 len(s1) 了, 表明 counts2 中的字符
            #   个数开始超出 counts1 中的个数(第一次出现 i 等于 len(s1) 时, 即超出 1 个, 因
            #   此在 counts2 中去除 s2 的最先加入到 counts2 中的字符, 使得 counts2 中字符保
            #   持为 len(s1) 个, 此时判断 counts2 是否等于 count1, 相等则返回 True; 否则下
            #   一轮循环中又从 s2 中加入一个字符, 加入后又是 counts2 中字符个数比 counts1 中
            #   多 1 个, 此时将 s2 中左侧的那个字符从 counts2 中去除, 使得 counts2 中字符个数
            #   不断保持在 len(s1) 个, 即包含了 s2 中一个长度为 len(s1) 的窗口的字符)
            if i >= len(s1):
                # jy: 获取待从 counts2 中移除的字符(当 s2 中的窗口不断右移时, 其 s2 窗口左侧的
                #    元素逐个被剔除, 并有右侧元素加入代替, 使得 counts2 总保持为 len(s1) 长度,
                #    记录的是滑动窗口中的字符及其对应出现的次数)
                removed = s2[i - len(s1)]
                counts2[removed] -= 1

                if counts2[removed] == 0:
                    del counts2[removed]
            # jy: 当 i 大于等于 len(s1)-1 时, counts2 中的元素个数总是与 count1 中的个数相等, 但
            #    是各个字符及其出现的个数是否都一一相等, 需要通过字典是否相等判断;
            if counts1 == counts2:
                return True

        return False

s1 = "ab"
s2 = "eidbaooo"
# Output: True
res = Solution().checkInclusion_v1(s1, s2)
print(res)

s1= "ab"
s2 = "eidboaoo"
# Output: False
res = Solution().checkInclusion_v1(s1, s2)
print(res)


