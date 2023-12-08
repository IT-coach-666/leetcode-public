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
title_jy = "Guess-Number-Higher-or-Lower(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked. Every time you guess
wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:
-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).

Return the number that I picked.


Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

Example 4:
Input: n = 2, pick = 2
Output: 2


Constraints:
1 <= n <= 2^31 - 1
1 <= pick <= n
"""


class Solution:
    """
二分查找;
    """
    def guessNumber(self, n: int, pick: int) -> int:
        def guess(guess_num, real_num):
            if guess_num == real_num:
                return 0
            elif guess_num < real_num:
                return 1
            else:
                return -1

        low, high = 1, n

        while low <= high:
            middle = low + (high - low) // 2
            compare = guess(middle, pick)

            if compare == 1:
                low = middle + 1
            elif compare == -1:
                high = middle - 1
            else:
                return middle


#JY: undo
n = 10
pick = 6
# Output: 6
res = Solution().guessNumber(n, pick)
print(res)

n = 1
pick = 1
# Output: 1
res = Solution().guessNumber(n, pick)
print(res)


n = 2
pick = 1
# Output: 1
res = Solution().guessNumber(n, pick)
print(res)


n = 2
pick = 2
# Output: 2
res = Solution().guessNumber(n, pick)
print(res)


