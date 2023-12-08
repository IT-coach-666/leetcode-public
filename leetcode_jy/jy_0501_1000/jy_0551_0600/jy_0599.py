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
title_jy = "Minimum-Index-Sum-of-Two-Lists(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list
of favorite restaurants represented by strings. You need to help them find out their common
interest with the least list index sum. If there is a choice tie between answers, output
all of them with no order requirement. You could assume there always exists an answer.


Example 1:
Input:
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input:
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Example 3:
Input:
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 4:
Input:
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 5:
Input:
list1 = ["KFC"]
list2 = ["KFC"]
Output: ["KFC"]


Constraints:
1 <= list1.length, list2.length <= 1000
1 <= list1[i].length, list2[i].length <= 30
list1[i] and list2[i] consist of spaces ' ' and English letters.
All the stings of list1 are unique.
All the stings of list2 are unique.
"""


import sys
from typing import List


class Solution:
    """
使用 Map 保存 list1 的所有元素及对应的位置, 然后遍历 list2, 判断当前元素是否在 Map 中, 根据
索引位置之和判断是否更新两者都喜欢的餐馆;
    """
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapping = {}
        both_likes = []
        min_sum = sys.maxsize
        # jy: 使用 Map 保存 list1 的所有元素(已确保元素唯一; 其实即使非唯一, 则把下标大的元素
        #    忽略即可)及其对应的位置
        for i, restaurant in enumerate(list1):
            mapping[restaurant] = i
        # jy: 遍历 list2 的下标和元素, 如果元素在 mapping 中, 则计算两个元素的下标之和, 如果下
        #    标和等于当前最小值, 则将其加入到结果列表中, 如果小于当前最小值, 则更新结果列表为
        #    仅含当前元素的结果列表;
        for i, restaurant in enumerate(list2):
            if restaurant in mapping:
                score = mapping[restaurant] + i

                if score == min_sum:
                    both_likes.append(restaurant)
                elif score < min_sum:
                    min_sum = score
                    both_likes = [restaurant]

        return both_likes


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
res = Solution().findRestaurant(list1, list2)
print(res)


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
res = Solution().findRestaurant(list1, list2)
print(res)


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
res = Solution().findRestaurant(list1, list2)
print(res)


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
res = Solution().findRestaurant(list1, list2)
print(res)


list1 = ["KFC"]
list2 = ["KFC"]
# Output: ["KFC"]
res = Solution().findRestaurant(list1, list2)
print(res)


