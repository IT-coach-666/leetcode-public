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
title_jy = "Intersection-of-Three-Sorted-Arrays(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order,
return a sorted array of only the integers that appeared in all three arrays.



Example 1:
Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.

Example 2:
Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
Output: []



Constraints:
1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""


from typing import List


class Solution:
    """
解法1: 和 349_Intersection-of-Two-Arrays.py 一样, 不过该题没有说最后返回的结果顺
序随意, 所以要多一步对最终结果的排序;
    """
    def arraysIntersection_v1(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # set1 = set(arr1)
        # set2 = set(arr2)
        # set3 = set(arr3)
        # jy: 对 set1 的结果按 lambda 表达式进行过滤;
        # return sorted(list(filter(lambda x: x in set2 and x in set3, set1)))

        return sorted(list(filter(lambda x: x in arr2 and x in arr3, arr1)))


    """
解法2: 和 350_Intersection-of-Two-Arrays-II.py 的解法 2 一样;
    """
    def arraysIntersection_v2(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i = j = k = 0
        result = []

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            largest = max(arr1[i], arr2[j], arr3[k])

            if arr1[i] < largest:
                i += 1
            elif arr2[j] < largest:
                j += 1
            elif arr3[k] < largest:
                k += 1
            elif arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                i += 1
                j += 1
                k += 1

        return result



arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
# Output: [1,5]
res = Solution().arraysIntersection_v1(arr1, arr2, arr3)
print(res)


arr1 = [197,418,523,876,1356]
arr2 = [501,880,1593,1710,1870]
arr3 = [521,682,1337,1395,1764]
# Output: []
res = Solution().arraysIntersection_v2(arr1, arr2, arr3)
print(res)


