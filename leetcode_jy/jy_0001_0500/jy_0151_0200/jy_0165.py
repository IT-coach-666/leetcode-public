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
title_jy = "Compare-Version-Numbers(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Compare two version numbers version1 and version2.
If version1 > version2, return 1;
if version1 < version2, return -1;
otherwise return 0.


You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth
second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example,
version number 3.4 has a revision number of 3 and 4 for its first and second level revision number.
Its third and fourth level revision number are both 0.



Example 1:
Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1

Example 4:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both  "01"  and  "001" represent the same number  "1"

Example 5:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means
             its third level revision number is default to "0"



Note:Version strings are composed of numeric strings separated by dots . and this numeric strings
may have leading zeroes. Version strings do not start or end with dots, and they will not be two
consecutive dots.
"""

from typing import List

class Solution:
    """
先对版本号以 . 分隔, 然后逐个比较, 对剩下较长的版本号判断是否都是 0, 如果都是 0 则返回相等, 否则返回较大
    """
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n1, n2 = len(v1), len(v2)

        n = min(n1, n2)
        for i in range(n):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1

        # jy: 如果 v2 中第 n 之后的元素都为 0, 表明版本相等, 否则表明 v1 < v2 (因
        #    为 v2 长度更长, 且长的部分的值不全是 0)
        if n1 < n2:
            return 0 if self._is_all_zero(v2, n) else -1
        # jy: 同理如上;
        elif n1 > n2:
            return 0 if self._is_all_zero(v1, n) else 1
        # jy: 此处表明 v1 和 v2 的长度相等, 且经过以上 for 循环没有返回, 表明数值也都相等;
        else:
            return 0

    # jy: 判断列表 v 的第 i 个元素开始之后的元素是否都为 0;
    def _is_all_zero(self, v: List[str], i: int) -> bool:
        for j in range(i, len(v)):
            if int(v[j]) != 0:
                return False
        return True




version1 = "0.1"
version2 = "1.1"
# Output: -1
res = Solution().compareVersion(version1, version2)
print(res)


version1 = "1.0.1"
version2 = "1"
# Output: 1
res = Solution().compareVersion(version1, version2)
print(res)


version1 = "7.5.2.4"
version2 = "7.5.3"
# Output: -1
res = Solution().compareVersion(version1, version2)
print(res)


version1 = "1.01"
version2 = "1.001"
# Output: 0
res = Solution().compareVersion(version1, version2)
print(res)


version1 = "1.0"
version2 = "1.0.0"
# Output: 0
res = Solution().compareVersion(version1, version2)
print(res)


