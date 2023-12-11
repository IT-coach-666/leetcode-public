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
title_jy = "Jump-Game-IV(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers arr, you are initially positioned at the first index of the array.
In one step you can jump from index i to index:
i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.
Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

Example 2:
Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.

Example 3:
Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Example 4:
Input: arr = [6,1,9]
Output: 2

Example 5:
Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3


Constraints:
1 <= arr.length <= 5 * 10^4
-108 <= arr[i] <= 10^8
"""

import collections
from typing import List


class Solution:
    """
在 1306. Jump Game III 的基础上增加了跳跃的方式, 需要先处理 arr 中所有值相同的元素的位置, 将其保存在一个 Map 中, 在搜索时, 除了 i + 1 和 i - 1 以外, 还要搜索元素值与当前元素相同的位置, 当将一组值相同的元素位置都添加到队列后, 则可以从 Map 中删除该元素, 避免后续重复搜索;
    """
    def minJumps(self, arr: List[int]) -> int:
        if not arr:
            return 0

        n = len(arr)
        positions = collections.defaultdict(list)

        for i, step in enumerate(arr):
            positions[step].append(i)

        queue = collections.deque([(0, 0)])
        visited = set()

        while queue:
            steps, i = queue.popleft()

            if i < 0 or i >= len(arr) or i in visited:
                continue

            if i == n - 1:
                return steps

            visited.add(i)
            queue.append((steps + 1, i + 1))
            queue.append((steps + 1, i - 1))

            if arr[i] in positions:
                for neighbour in positions[arr[i]]:
                    queue.append((steps + 1, neighbour))

                positions.pop(arr[i])


