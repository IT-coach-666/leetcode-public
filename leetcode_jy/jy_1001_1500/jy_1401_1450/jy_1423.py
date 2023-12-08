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
title_jy = "Maximum-Points-You-Can-Obtain-from-Cards(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.

Example 4:
Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1.

Example 5:
Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202


Constraints:
1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""

import sys
from typing import List


class Solution:
    """
从数组首尾取 k 个数使其和最大等价于从数组中找到一个长度为 len(cardPoints) - k 的连续子数组的和的最小值;
    """
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_window_length = len(cardPoints) - k
        start, end = 0, 0
        min_score = sys.maxsize
        sum_so_far = 0
        total_sum = sum(cardPoints)

        if max_window_length <= 0:
            return total_sum

        for end in range(len(cardPoints)):
            sum_so_far += cardPoints[end]
            current_window_length = end - start + 1

            if current_window_length < max_window_length:
                continue
            elif current_window_length > max_window_length:
                sum_so_far -= cardPoints[start]
                start += 1

            min_score = min(min_score, sum_so_far)

        return total_sum - min_score



