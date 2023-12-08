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
title_jy = "Max-Chunks-To-Make-Sorted-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an integer array ``arr``. We split ``arr`` into some number of
chunks (i.e., partitions), and individually sort each chunk. After concatenating
them, the result should equal the sorted array. Return the largest number of
chunks we can make to sort the array.


Example 1:
Input: arr = [5,4,3,2,1]
Output: 1
Explanation: Splitting into two or more chunks will not return the required result. For
             example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3],
             which isn't sorted.

Example 2:
Input: arr = [2,1,3,4,4]
Output: 4
Explanation: We can split into two chunks, such as [2, 1], [3, 4, 4]. However, splitting
             into [2, 1], [3], [4], [4] is the highest number of chunks possible.


Constraints:
1 <= arr.length <= 2000
0 <= arr[i] <= 10^8
"""

from typing import List


class Solution:
    """
解法1: 记 right_min[i] 表示 min(arr[i:]), 遍历 arr, 记录至今的最大数字, 如果
至今的最大数字小于等于 right_min[i+1], 说明当前位置可以作为一个切分点;
    """
    def maxChunksToSorted_v1(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)

        right_min = [-1] * n
        # jy: 用 right_min[i] 记录 arr[i:] 中的最小值; i 从倒数第二个数开始向前
        #     遍历(因为最后一个数之后的最小值为最后一个数本身)
        right_min[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            right_min[i] = min(right_min[i+1], arr[i])

        max_so_far = arr[0]
        for i in range(n-1):
            max_so_far = max(max_so_far, arr[i])
            if max_so_far <= right_min[i+1]:
                count += 1

        return count + 1

    def maxChunksToSorted_v2(self, arr: List[int]) -> int:
        # jy: stack 中保留每个排序块的最大值;
        stack = []
        # jy: 遍历数组中的元素;
        for num in arr:
            # jy: 如果栈不为空, 则判断当前元素值是否小于栈顶元素, 如果小于栈顶元素, 则
            #     表明它应该与栈顶属于同一排序块中(由于栈中的每个元素都代表的是独立的每
            #     一块, 如果当前元素不仅小于栈顶元素, 还小于栈顶之下的元素, 则表明栈顶之
            #     下的所有比当前元素大的元素至栈顶元素应该归属于同一块, 不应分开, 故将除
            #     栈顶之外比当前元素值大的元素通通出栈, 随后再次将原栈顶入栈);
            # jy: 以 [2, 3, 4, 1] 为例进行思考;
            if stack and num < stack[-1]:
                head = stack.pop()
                while stack and num < stack[-1]:
                    stack.pop()
                stack.append(head)
            else:
                stack.append(num)
        # jy: 最终栈中有多少个元素即代表最多能分为多少块
        return len(stack)

    def maxChunksToSorted_2022_02_19(self, arr):
        res_count = 0

        ls_right_min = [None] * len(arr)
        ls_right_min[-1] = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            # jy: 注意, 当前下标位置 i 以及之后元素的最小值是通过当前位置的 arr[i] 和
            #     下标为 i+1 以及之后元素的最小值(即 ls_right_min[i+1])进行比较判断得到;
            ls_right_min[i] = min(arr[i], ls_right_min[i+1])

        max_so_far = arr[0]
        for i in range(len(arr)-1):
            max_so_far = max(max_so_far, arr[i])
            if max_so_far <= ls_right_min[i+1]:
                res_count += 1

        return res_count + 1


arr = [5, 4, 3, 2, 1]
# Output: 1
res = Solution().maxChunksToSorted_v1(arr)
print(res)


arr = [2, 1, 3, 4, 4]
# Output: 4
res = Solution().maxChunksToSorted_v2(arr)
print(res)


