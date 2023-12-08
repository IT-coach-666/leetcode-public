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
title_jy = "Distribute-Candies(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array with even length, where different numbers in this array
represent different kinds of candies. Each number means one candy of the corresponding
kind. You need to distribute these candies equally in number to brother and sister.

Return the maximum number of kinds of candies the sister could gain.

Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.

Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.


Note:
The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].
"""


from typing import List


class Solution:
    """
使用一个 Set 保存所有糖果的种类, 然后和糖果总数的一半比较, 返回较小值;
    """
    def distributeCandies(self, candies: List[int]) -> int:
        # jy: 集合长度代表数组中的所有种类, 数组长度的一半代表每人分到的糖果数;
        #    1) 如果种类数小于数组长度的一半, 表明 sister 可以分配到所有种类
        #       数, 并且个别种类数会分配到多于 1 个, 才能确保其分到一半;
        #    2) 如果种类数大于数组长度的一半, 则 sister 分配到的一半中, 可以分
        #       配均为不同的种类的糖果(每种均只出现一次), 此时分配到的种类数为
        #       其分配到的糖果的数量;
        return min(len(set(candies)), len(candies) // 2)


candies = [1,1,2,2,3,3]
# Output: 3
res = Solution().distributeCandies(candies)
print(res)


candies = [1,1,2,3]
# Output: 2
res = Solution().distributeCandies(candies)
print(res)


