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
title_jy = "Jewels-and-Stones(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
You're given strings ``jewels`` representing the types of stones that are jewels,
and ``stones`` representing the stones you have. Each character in ``stones`` is
a type of stone you have. You want to know how many of the stones you have are
also jewels. Letters are case sensitive, so "a" is considered a different type of
stone from "A".


Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0


Constraints:
1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""


class Solution:
    """
使用 Set 保存 jewels, 然后遍历 stones 判断是否在 Set 中; 
    """
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(list(jewels))
        count = 0

        for stone in stones:
            if stone in jewels_set:
                count += 1

        return count


jewels = "aA"
stones = "aAAbbbb"
# Output: 3
res = Solution().numJewelsInStones(jewels, stones)
print(res)


jewels = "z"
stones = "ZZ"
# Output: 0
res = Solution().numJewelsInStones(jewels, stones)
print(res)



