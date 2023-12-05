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
title_jy = "Maximum-Length-of-a-Concatenated-String-with-Unique-Characters(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of strings ``arr``. String ``s`` is a concatenation of a sub-sequence
of ``arr`` which have unique characters. Return the maximum possible length of s.


Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
             Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26


Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""


from typing import List, Set


class Solution:
    """
深度优先搜索: 使用一个 Set 来保存当前遇到的字符, 遍历数组, 如果当前字符串和 Set 中的字
符不冲突, 则将该字符串加入到 Set 中, 然后递归调用求解, 递归结束后从 Set 移除该字符串;
    """
    def maxLength(self, arr: List[str]) -> int:
        visited = set()
        # jy: 从 arr 数组中的第 0 个位置开始递归深度优先搜索;
        return self._dfs(arr, 0, visited)

    def _dfs(self, arr: List[str], start: int, visited: Set[str]) -> int:
        # jy: 最长长度为 visited 中的元素个数, 如果 start 等于数组 arr 的长度, 表明已经遍历
        #    完所有数组元素, 直接返回 max_length;
        max_length = len(visited)
        if start == len(arr):
            return max_length
        # jy: 从数组 arr 的下标为 start 的位置开始循环遍历;
        for i in range(start, len(arr)):
            # jy: 如果 arr[i] 中的字符串有重复, 或者与 visited 中的有相同, 则跳过当前循环;
            if not self._is_unique(arr[i], visited):
                continue

            visited.update(list(arr[i]))

            max_length = max(self._dfs(arr, i+1, visited), max_length)

            visited.difference_update(list(arr[i]))

        return max_length

    def _is_unique(self, word: str, visited: Set[str]) -> bool:
        """判断 word 字符串是否与 visited 集合不冲突(即 word 中的字符不存在于 visited 中)"""
        for c in word:
            if c in visited:
                return False
        # jy: 如果 word 中含有相同字符, 则返回 False;
        return len(word) == len(set(list(word)))


arr = ["un","iq","ue"]
# Output: 4
res = Solution().maxLength(arr)
print(res)


arr = ["cha","r","act","ers"]
# Output: 6
res = Solution().maxLength(arr)
print(res)


arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
res = Solution().maxLength(arr)
print(res)


