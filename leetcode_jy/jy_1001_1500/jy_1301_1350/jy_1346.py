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
title_jy = "Check-If-N-and-Its-Double-Exist(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array arr of integers, check if there exists two integers N and M such
that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that:
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]



Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:
Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:
Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.



Constraints:
2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
"""


from typing import List


class Solution:
    """
和 001_Two-Sum.py 类似, 使用一个 set 保存至今遇到的数字, 然后遍历数组, 如果当前数字的两倍或
者一半在 set 中, 则返回 True;
    """
    def checkIfExist(self, arr: List[int]) -> bool:
        numbers = set()
        for n in arr:
            if n * 2 in numbers or n / 2 in numbers:
                return True
            numbers.add(n)
        return False


arr = [10,2,5,3]
# Output: true
res = Solution().checkIfExist(arr)
print(res)


arr = [7,1,14,11]
# Output: true
res = Solution().checkIfExist(arr)
print(res)


arr = [3,1,7,11]
# Output: false
res = Solution().checkIfExist(arr)
print(res)


