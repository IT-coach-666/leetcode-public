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
title_jy = "Jump-Game-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3

Example 2:
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true
Explanation:
One possible way to reach at index 3 with value 0 is:
index 0 -> index 4 -> index 1 -> index 3

Example 3:
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.


Constraints:
1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length
"""

from typing import List


class Solution:
    """
解法1
使用 visited 标记访问过的位置, 深度优先搜索数组, 如果遇到数组的值为0, 则表示可到达数组值为0的地方;
    """
    def canReach(self, arr: List[int], start: int) -> bool:
        return self._dfs(arr, start, set())

    def _dfs(self, arr, start, visited):
        if start < 0 or start >= len(arr) or start in visited:
            return False

        if arr[start] == 0:
            return True

        visited.add(start)

        return self._dfs(arr, start + arr[start], visited) \
            or self._dfs(arr, start - arr[start], visited)

from collections import deque
from typing import List


class Solution:
    """
解法2:
广度优先搜索版本;
    """
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = set()

        while queue:
            i = queue.popleft()

            if i < 0 or i >= len(arr) or i in visited:
                continue

            if arr[i] == 0:
                return True

            visited.add(i)
            queue.append(i + arr[i])
            queue.append(i - arr[i])

        return False


