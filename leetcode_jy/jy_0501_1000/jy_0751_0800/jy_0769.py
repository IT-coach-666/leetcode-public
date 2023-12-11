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
title_jy = "Max-Chunks-To-Make-Sorted(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
You are given an integer array ``arr`` of length n that represents a permutation
of the integers in the range [0, n-1]. We split ``arr`` into some number of chunks
(i.e., partitions), and individually sort each chunk. After concatenating them,
the result should equal the sorted array.  Return the largest number of chunks we
can make to sort the array.


Example 1:
Input: arr = [4,3,2,1,0]
Output: 1
Explanation: Splitting into two or more chunks will not return the required result.
             For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2],
             which isn't sorted.

Example 2:
Input: arr = [1,0,2,3,4]
Output: 4
Explanation: We can split into two chunks, such as [1, 0], [2, 3, 4]. However, splitting
             into [1, 0], [2], [3], [4] is the highest number of chunks possible.


Constraints:
n == arr.length
1 <= n <= 10
0 <= arr[i] < n
All the elements of arr are unique.
"""


from typing import List


class Solution:
    """
解法1: 记录截止当前为止所遇到的最大值; 由于 arr 中的元素值为 [0, n-1], 即等价于
元素下标的范围, 当截止某下标为止对应的最大值正好等于该下标编号时, 表明在此处可
以做一次分割;
    """
    def maxChunksToSorted_v1(self, arr: List[int]) -> int:
        count = 0
        max_so_far = -1
        for i, n in enumerate(arr):
            max_so_far = max(max_so_far, n)
            if max_so_far == i:
                count += 1
        return count


arr = [4, 3, 2, 1, 0]
# Output: 1
res = Solution().maxChunksToSorted_v1(arr)
print(res)


arr = [1, 0, 2, 3, 4]
# Output: 4
res = Solution().maxChunksToSorted_v1(arr)
print(res)


