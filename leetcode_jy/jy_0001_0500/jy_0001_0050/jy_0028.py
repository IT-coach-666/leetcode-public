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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "find-the-index-of-the-first-occurrence-in-a-string(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "KMP 算法 | sunday 算法 | 巧用字符串内置方法 find | 【IMP】"



"""
Given two strings `needle` and `haystack`, return the index of the first
occurrence of `needle` in `haystack`, or -1 if `needle` is not part of 
`haystack`.


Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
             The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:
1 <= haystack.length, needle.length <= 10^4
`haystack` and `needle` consist of only lowercase English characters.
"""


class Solution:
    """
解法 1: 枚举
    """
    def strStr_v1(self, haystack: str, needle: str) -> int:
        len_n = len(needle)
        len_h = len(haystack)
        for i in range(len_h - len_n + 1):
            if haystack[i: i + len_n] == needle:
                return i
        return -1


    """
解法 2: 巧用字符串内置方法 find

算法题中需明白该方法的具体实现逻辑
    """
    def strStr_v2(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


    """
解法 3: Sunday 算法
    """
    def strStr_v3(self, haystack: str, needle: str) -> int:

        def calShiftMat(st):
            """
            偏移表计算函数
            """
            dict_ = {}
            for i in range(len(st)-1, -1, -1):
                if not dict_.get(st[i]):
                    dict_[st[i]] = len(st) - i
            dict_["ot"] = len(st) + 1
            return dict_


        len_n, len_h = len(needle), len(haystack)
        # jy: 如果模式串 needle 比原字符串还长, 则直接返回 -1
        if len_n > len_h:
            return -1
        # jy: 如果模式串 needle 为空, 则直接返回 0
        if needle == "":
            return 0
       
        # jy: 初始化偏移表   
        dict_ = calShiftMat(needle)
        print("%s 对应的偏移表为: %s" % (needle, dict_))
        # jy: 遍历字符串下标
        idx = 0
        while idx <= len_h - len_n:
            
            # 待匹配字符串
            str_cut = haystack[idx: idx + len_n]
            
            # 判断是否匹配, 如果匹配则直接返回
            if str_cut == needle:
                return idx

            # 边界处理
            if idx + len_n == len_h:
                return -1

            # 如果不匹配, 则根据下一个字符的偏移, 移动 idx
            cur_c = haystack[idx + len_n]
            if dict_.get(cur_c):
                idx += dict_[cur_c]
            else:
                idx += dict_["ot"]
            
        return -1 if idx + len_n >= len_h else idx


    """
解法 4: KMP 算法
    """
    def strStr_v4(self, haystack: str, needle: str) -> int:
        def get_next(needle):
            len_ = len(needle)
            # jy: 初始化 next 数组
            next_ = [0] * len_
            for i in range(1, len_):
                k = next_[i-1]
                while needle[i] != needle[k]:
                    # jy: 比较到首位字符仍与当前字符 needle[i] 不一致, 没办法
                    #     再往前找字符了, 即 needle[0, i] 没有相同前后缀,
                    #     next[i] = 0; 为了和最后的 next[i] = k + 1 一致, k 先
                    #     减 1 等于 -1, 之后再加 1 变成 0
                    if k == 0:
                        k -= 1
                        break
                    # jy: needle[i] 与 needle[k] 不一致, 就要在 needle[0, k-1]
                    #     中找一个更短的相同前后缀, 即更新 k = next[k-1]
                    else:
                        k = next_[k-1]
                # jy: needle[i] 的最长相同前后缀等于已有的 k 值再加 1
                next_[i] = k + 1
            return next_        


        len_n = len(needle)
        # jy: 生成 needle 的 next 数组
        next_ = get_next(needle) 

        # jy: 遍历 haystack 的指针
        i = 0   
        # jy: 指向 needle 的指针
        j = 0
        while i < len(haystack):
            # jy: 字符匹配, 两个指针都后移一位
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            # jy: needle 第一个字符就不匹配, haystack 指针后移一位
            elif j == 0:
                i += 1
            # jy: 找到已匹配的 needle[0, j-1] 的最长相同前后缀, 更
            #     新 j 从这一位开始比较
            else:
                j = next_[j - 1]

            # jy: needle 匹配完成, 返回匹配起点等于 i - n (最后一位匹配完
            #     成后 i 也会后移一位, 即匹配区间为 [i-n, i-1] 长度为 n)
            if j >= len_n:
                return i - len_n
        # jy: 没有找到匹配子串, 返回 -1
        return -1



haystack = "sadbutsad"
needle = "sad"
res = Solution().strStr_v1(haystack, needle)
# jy: 0
print(res)


haystack = "leetcode"
needle = "leeto"
res = Solution().strStr_v2(haystack, needle)
# jy: -1
print(res)


haystack = "sadbutsad"
needle = "sad"
res = Solution().strStr_v3(haystack, needle)
# jy: 0
print(res)


haystack = "leetcode"
needle = "leeto"
res = Solution().strStr_v3(haystack, needle)
# jy: -1
print(res)


haystack = "checkthisout"
needle = "this"
res = Solution().strStr_v4(haystack, needle)
# jy: 5
print(res)



