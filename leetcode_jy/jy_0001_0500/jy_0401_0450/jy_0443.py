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
title_jy = "String-Compression(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of characters, compress it in-place. The length after compression must always
be smaller than or equal to the original array. Every element of the array should be a character
(not int) of length 1. After you are done modifying the input array in-place, return the new
length of the array.

Follow up:  Could you solve it using only O(1) extra space?


Example 1:
Input:  ["a","a","b","b","c","c","c"]
Output:  Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation:  "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

Example 2:
Input:  ["a"]
Output:  Return 1, and the first 1 characters of the input array should be: ["a"]
Explanation:  Nothing is replaced.

Example 3:
Input:  ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is
             replaced by "b12". Notice each digit has it's own entry in the array.


Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
"""

from typing import List



class Solution:
    """
使用两个指针 i 和 j, 一开始 i 和 j 指向相同的元素, 然后 j 开始移动直到遇到和 i 指向的元素不同,
计算 i 和 j 的距离, 如果距离大于 1, 则需要压缩数组, 然后 i 又移动到和 j 一样的位置开始新的循环
    """
    def compress(self, chars: List[str]) -> int:
        # jy: 记录压缩后的数组的长度(初始值为 0);
        length = 0
        # jy: 一开始 i 和 j 指向相同的元素;
        i, j = 0, 0

        while i < len(chars):
            # jy: 依据已压缩的数组的长度, 将当前待压缩的字符加入到压缩数组中, 然后压缩数组的长度加 1;
            chars[length] = chars[i]
            length += 1

            # jy: 移动 j, 直到遇到和 i 指向的元素不同, 此时计算 i 和 j 的距离;
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            # jy: 如果距离大于 1, 表明 chars[i] 有重复, 需要压缩;
            if j-i > 1:
                # jy: 将 j-i 的结果字符串化(使得如果非个位数的情况下, 也能将所有数值字符逐个加入到压缩数
                #    组), 并添加到压缩数组中;
                for c in str(j-i):
                    chars[length] = c
                    length += 1

            i = j

        return length


chars = ["a", "a", "b", "b", "c", "c", "c"]
# Output:  Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
res = Solution().compress(chars)
print(res, " ===== ", chars[:res])


chars = ["a"]
# Output:  Return 1, and the first 1 characters of the input array should be: ["a"]
res = Solution().compress(chars)
print(res, " ===== ", chars[:res])


chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
res = Solution().compress(chars)
print(res, " ===== ", chars[:res])


