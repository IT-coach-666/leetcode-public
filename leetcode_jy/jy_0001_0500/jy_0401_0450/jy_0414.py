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
title_jy = "Third-Maximum-Number(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).


Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
             Both numbers with value 2 are both considered as second maximum.
"""


import sys
from typing import List


class Solution:
    """
和 215_K-th-Largest-Element-in-an-Array.py 有点不同, 这道题的第三大需要排除重复的元素;

首先初始化三个变量 max1, max2, max3 分表表示第一大, 第二大, 第三大的数; 然后遍历数组:
1) 如果元素大于 max1, 则更新 max3 为 max2, 更新 max2 为 max1, 更新 max1 为当前元素;
2) 如果元素大于 max2 且小于 max1, 则更新 max3 为 max2, 更新 max2 为当前元素;
3) 如果元素大于 max3 且小于 max2, 则更新 max3 为当前元素;
    """
    def thirdMax(self, nums: List[int]) -> int:
        max1, max2, max3 = -sys.maxsize, -sys.maxsize, -sys.maxsize

        for n in nums:
            # jy: 如果 n 比第一大的还大, 则更新第一大的为 n, 第二大则更新为原先的
            #    第一大, 同理第三大则更新为原先的第二大;
            if n > max1:
                max3, max2, max1 = max2, max1, n
            # jy: 如果 n 比第二大还大(但比第一大小), 则更新第二大为 n, 并将第三大
            #    更新为原先的第二大; 由于当 n
            #    此处要明确指出比第一大的小, 因为其可能等于第一大的值, 此时仍将 n 视为是第一大
            #    的, 不能直接更新其为第二大, 因此第三大爷无需更新;
            elif max2 < n < max1:
                max3, max2 = max2, n
            # jy: 如果 n 比第三大还大, 但比第二大小, 则仅更新第三大为 n;
            #    此处要明确指出比第二大的小, 因为其可能等于第二大的值, 此时仍将 n 视为是第二大
            #    的, 不能直接更新其为第三大;
            elif max3 < n < max2:
                max3 = n

        return max3 if max3 != -sys.maxsize else max1


nums = [3, 2, 1]
# Output: 1
res = Solution().thirdMax(nums)
print(res)


nums = [1, 2]
# Output: 2
res = Solution().thirdMax(nums)
print(res)


nums = [2, 2, 3, 1]
# Output: 1
res = Solution().thirdMax(nums)
print(res)


