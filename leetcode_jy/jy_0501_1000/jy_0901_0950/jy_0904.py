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
title_jy = "Fruit-Into-Baskets(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are visiting a farm that has a single row of fruit trees arranged from left to
right. The trees are represented by an integer array ``fruits`` where fruits[i] is
the type of fruit the ith tree produces. You want to collect as much fruit as possible.
However, the owner has some strict rules that you must follow:
1) You only have two baskets, and each basket can only hold a single type of fruit.
   There is no limit on the amount of fruit each basket can hold.
2) Starting from any tree of your choice, you must pick exactly one fruit from every
   tree (including the start tree) while moving to the right. The picked fruits must
   fit in one of your baskets.
3) Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array ``fruits``, return the maximum number of fruits you can pick.



Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.


Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2]. If we had started at the first tree, we
             would only pick from trees [0,1].


Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2]. If we had started at the first tree,
             we would only pick from trees [1,2].


Example 4:
Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can pick from trees [1,2,1,1,2].




Constraints:
1 <= fruits.length <= 10^5
0 <= fruits[i] < fruits.length
"""


import collections
from typing import List


class Solution:
    """
典型的滑动窗口问题, 维护一个滑动窗口表示遇到的果树, 当窗口的长度大于2时, 说明需要剔除窗口起始位置的果树;
    """
    def totalFruit(self, fruits: List[int]) -> int:
        counter = collections.defaultdict(int)
        start = 0
        max_count = 0

        for end, n in enumerate(fruits):
            counter[n] += 1

            while len(counter) > 2:
                counter[fruits[start]] -= 1

                if counter[fruits[start]] == 0:
                    counter.pop(fruits[start])

                start += 1

            max_count = max(max_count, end - start + 1)

        return max_count


