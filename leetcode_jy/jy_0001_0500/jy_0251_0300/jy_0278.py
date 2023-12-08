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
title_jy = "First-Bad-Version(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since
each version is developed based on the previous version, all the versions after
a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad
one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is
bad. Implement a function to find the first bad version. You should minimize the
number of calls to the API.



Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1



Constraints:   1 <= bad <= n <= 2^31 - 1
"""


class Solution:
    """
二分查找的应用, 如果 middle 对应版本号没问题, 则将 low 设置为 middle + 1, 否则将 high 
指向 middle, 循环终止条件为 low == high, 最后返回 low;
    """
    def firstBadVersion(self, n):
        low, high = 1, n

        while low < high:
            middle = low + (high - low) // 2

            if not isBadVersion(middle):
                low = middle + 1
            else:
                high = middle

        return low


# jy: have problem

n = 5
bad = 4
# Output: 4
res = Solution().firstBadVersion(n)
print(res)


n = 1
bad = 1
# Output: 1
res = Solution().firstBadVersion(n)
print(res)


