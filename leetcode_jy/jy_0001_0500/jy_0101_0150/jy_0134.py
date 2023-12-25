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
title_jy = "Gas-Station(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There are `n` gas stations along a circular route, where the amount of gas at the i-th station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the i-th station to its next (i+1)-th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

 

Example 1:
Input: gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
Output: 3
Explanation: Start at station 3 (index 3) and fill up with 4 unit of gas.
             Your tank = 0 + 4 = 4
             Travel to station 4. Your tank = 4 - 1 + 5 = 8
             Travel to station 0. Your tank = 8 - 2 + 1 = 7
             Travel to station 1. Your tank = 7 - 3 + 2 = 6
             Travel to station 2. Your tank = 6 - 4 + 3 = 5
             Travel to station 3. The cost is 5. 
             Your gas is just enough to travel back to station 3.
             Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2, 3, 4], cost = [3, 4, 3]
Output: -1
Explanation: You can't start at station 0 or 1, as there is not enough gas
             to travel to the next station. Let's start at station 2 and fill
             up with 4 unit of gas. Your tank = 0 + 4 = 4
             Travel to station 0. Your tank = 4 - 3 + 2 = 3
             Travel to station 1. Your tank = 3 - 3 + 3 = 3
             You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
             Therefore, you can't travel around the circuit once no matter where you start.
 

Constraints:
n == gas.length == cost.length
1 <= n <= 10^5
0 <= gas[i], cost[i] <= 10^4
"""


# 解法1
class Solution:
    """
解法 1: https://leetcode.cn/problems/gas-station/solutions/488622/134-jia-you-zhan-tan-xin-jing-dian-ti-mu-xiang-jie/

    """
    def canCompleteCircuit_v1(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        cur_sum = 0
        min_sum = float('inf')
        
        for i in range(n):
            cur_sum += gas[i] - cost[i]
            min_sum = min(min_sum, cur_sum)
        
        if cur_sum < 0: return -1
        if min_sum >= 0: return 0
        
        for j in range(n - 1, 0, -1):
            min_sum += gas[j] - cost[j]
            if min_sum >= 0:
                return j
        
        return -1


    """
解法 2: 
    """
    def canCompleteCircuit_v2(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        curSum = 0
        totalSum = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                start = i + 1
        if totalSum < 0: return -1
        return start

    
    
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
res = Solution().canCompleteCircuit_v1(gas, cost)
# jy: 3
print(res)


gas = [2, 3, 4]
cost = [3, 4, 3]
res = Solution().canCompleteCircuit_v1(gas, cost)
# jy: -1
print(res)
