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
title_jy = "Palindrome-Partitioning(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string ``s``, partition ``s`` such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of ``s``. A palindrome string
is a string that reads the same backward as forward.


Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]


Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""


from typing import List


class Solution:
    """
解法1: 暴力搜索, 遍历字符串判断第一个字符到当前字符是否是回文, 如果是则对剩余的字符串递归搜索
    """
    def partition_v1(self, s: str) -> List[List[str]]:
        result = []
        self._search_v1(s, 0, [], result)
        return result

    def _search_v1(self, s, start, partition, result):
        """
        从字符串 s 的 start 下标开始分割, 将其分割为回文, 回文子串加入到 partition 列表中,
        当字符串全部分割完毕后, 将所有分割结果 partition 加入结果列表 result 中;
        """
        # jy: 如果字符串的起始下标 start 已经等于字符串 s 的长度, 表明分割完成, 如果分割结果列表
        #     partition 不为空, 则将其加入 result 列表中;
        # jy: 实际代码逻辑中 partition 不可能是空, 故以下 if 判断可将 partition 去除;
        if start == len(s):
        # if start == len(s) and partition:
            result.append(partition)
            return
        # jy: 遍历 start 到字符串的最后一个字符下标, 不断将其作为子串的末尾下标, 判断
        #     其构成的子串是否是回文:
        #     1) 如果不是回文, 则跳过;
        #     2) 如果是回文, 则将下标为 start 到 end 对应的子串加入 partition 列表中,
        #        并递归从 end + 1 的位置开始切分子串;
        for end in range(start, len(s)):
            if not self._is_palindrome(s, start, end):
                continue

            self._search_v1(s, end + 1, partition + [s[start:end + 1]], result)

    def _is_palindrome(self, s, low, high):
        # jy: 如果 low 小于 high 且两指针对应的字符相等, 则 low 进 1 high 退 1;
        #     退出 while 循环时有两种可能(只有当是情况 1 时才确保是回文):
        #     1) low >= high
        #     2) low < high 但 s[low] != s[high]
        while low < high and s[low] == s[high]:
            low += 1
            high -= 1
        return low >= high

    """
解法2: 在解法 1 的基础上增加一层缓存避免重复判断字符串子串是否是回文
    """
    def partition_v2(self, s: str) -> List[List[str]]:
        result = []
        # jy: 在解法 1 的基础上增加缓存 cache, 并作为递归函数的参数传入;
        #     避免重复判断字符子串是否是回文;
        cache = {}
        self._search_v2(s, 0, [], result, cache)
        return result

    def _search_v2(self, s, start, partition, result, cache):
        if start == len(s) and partition:
            result.append(partition)
            return

        for end in range(start, len(s)):
            # jy: 优先从缓存 cache 中获取子串(下标从 start 到 end 的子串), 如果缓存中存在, 则
            #     表明该子串已经确认是回文, 无需再次判断是否是回文;
            is_cached, palindrome = cache.get((start, end), (False, ''))

            if is_cached and palindrome:
                self._search_v2(s, end + 1, partition + [s[start:end + 1]], result, cache)
            elif not is_cached:
                is_palindrome = self._is_palindrome(s, start, end)
                palindrome = s[start:end + 1] if is_palindrome else ''
                cache[(start, end)] = (True, palindrome)

                if is_palindrome:
                    self._search_v2(s, end + 1, partition + [palindrome], result, cache)

    """
解法3: 对解法 2 中的 cache 进行优化;
    """
    def partition_jy(self, s: str) -> List[List[str]]:
        result = []
        # jy: 在解法 1 的基础上增加缓存 cache, 并作为递归函数的参数传入;
        #     避免重复判断字符子串是否是回文;
        cache = {}
        self._search_v3(s, 0, [], result, cache)
        return result

    def _search_v3(self, s, start, partition, result, cache):
        if start == len(s) and partition:
            result.append(partition)
            return

        for end in range(start, len(s)):
            # jy: 优先从缓存 cache 中获取子串(下标从 start 到 end 的子串), 如果缓存中存在, 则
            #     表明该子串已经确认是回文, 无需再次判断是否是回文;
            is_cached = cache.get((start, end), False)

            if is_cached:
                self._search_v3(s, end + 1, partition + [s[start:end + 1]], result, cache)
            else:
                is_palindrome = self._is_palindrome(s, start, end)
                palindrome = s[start:end + 1] if is_palindrome else ''
                if is_palindrome:
                    cache[(start, end)] = True
                    self._search_v3(s, end + 1, partition + [palindrome], result, cache)


s = "aab"
# Output: [["a","a","b"],["aa","b"]]
res = Solution().partition_v1(s)
print(res)


s = "a"
# Output: [["a"]]
res = Solution().partition_v2(s)
print(res)


s = "aab"
# Output: [["a","a","b"],["aa","b"]]
res = Solution().partition_jy(s)
print(res)


