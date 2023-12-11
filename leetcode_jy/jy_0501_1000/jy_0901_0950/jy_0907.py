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
title_jy = "Sum-of-Subarray-Minimums(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444


Constraints:
1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4
"""


from typing import List


# Time Limit Exceeded!
class Solution:
    """
解法1(超时)
记 dp[i][j] 表示 arr[i:j + 1] 的最小值, 则 dp[i][j] = min(dp[i][j - 1], arr[j]), 不过会超时;
    """
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = arr[i]

            for j in range(i + 1, n):
                dp[i][j] = min(dp[i][j - 1], arr[j])

        return sum(map(sum, dp)) % (pow(10, 9) + 7)


class Solution:
    """
解法2
对于每个元素 arr[i], 找到 arr[i] 左边第一个比他小的元素 arr[left], 和 arr[i] 右边第一个比他小的元素 arr[right], 则 arr[left + 1:right] 是以 arr[i] 为最小元素的连续子数组, 其包含 arr[i] 的子数组个数为 (i - left) * (right - i)  而构造 arr[left] 和 arr[right] 的过程则通过单调栈实现;
    """
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        left = [0] * n
        right = [0] * n
        stack = []
        mod = pow(10, 9) + 7

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            right[i] = stack[-1] if stack else n
            stack.append(i)

        for i in range(n):
            result += (i - left[i]) * (right[i] - i) * arr[i]
            result %= mod

        return result


import sys
from typing import List


class Solution:
    """
解法3
也可以合并为一趟循环, 不过需要额外在原数组的首尾添加负数的最大值避免没有出栈;
    """
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [-sys.maxsize] + arr + [-sys.maxsize]
        n = len(arr)
        stack = []
        result = 0
        mod = pow(10, 9) + 7

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                result += arr[index] * (i - index) * (index - stack[-1]) % mod
                result %= mod

            stack.append(i)

        return result


