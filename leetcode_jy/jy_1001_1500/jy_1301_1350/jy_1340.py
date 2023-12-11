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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Jump-Game-V(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers arr and an integer d. In one step you can jump from index i to index:
i + x where: i + x < arr.length and 0 < x <= d.
i - x where: i - x >= 0 and 0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).
You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.
Notice that you can not jump outside of the array at any time.

Example 1:    https://www.yuque.com/frederick/dtwi9g/sbi55c

Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.

Example 2:
Input: arr = [3,3,3,3,3], d = 3
Output: 1
Explanation: You can start at any index. You always cannot jump to any index.

Example 3:
Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indicies.

Example 4:
Input: arr = [7,1,7,1,7,1], d = 2
Output: 2

Example 5:
Input: arr = [66], d = 1
Output: 1


Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 10^5
1 <= d <= arr.length
"""


from typing import List


class Solution:
    """
记 dp[i] 表示从 i 位置开始最多可以访问到的位置个数, 遍历 arr, 以当前位置为中心, 分别向左右两边进行搜索;
    """
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n
        max_jumps = 0

        for i in range(n):
            max_jumps = max(max_jumps, self._dfs(arr, n, d, i, dp))

        return max_jumps

    def _dfs(self, arr, n, d, start, dp):
        if dp[start] != 0:
            return dp[start]

        max_jumps = 1
        j = start + 1

        while j <= min(start + d, n - 1) and arr[j] < arr[start]:
            max_jumps = max(max_jumps, 1 + self._dfs(arr, n, d, j, dp))
            j += 1

        j = start - 1

        while j >= max(start - d, 0) and arr[j] < arr[start]:
            max_jumps = max(max_jumps, 1 + self._dfs(arr, n, d, j, dp))
            j -= 1

        dp[start] = max_jumps

        return dp[start]


