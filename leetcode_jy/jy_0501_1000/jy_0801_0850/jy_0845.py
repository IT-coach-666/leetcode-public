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
title_jy = "Longest-Mountain-in-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You may recall that an array ``arr`` is a ``mountain array`` if and only if:
1) arr.length >= 3
2) There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
   a) arr[0] < arr[1] < ... < arr[i-1] < arr[i]
   b) arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Given an integer array ``arr``, return the length of the longest subarray, which
is a mountain. Return 0 if there is no mountain subarray.



Example 1:
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:
Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.



Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^4


Follow up:
Can you solve it using only one pass?
Can you solve it in O(1) space?
"""


from typing import List


class Solution:
    """
先从数组第一位开始找到第一座山, 记 start 为左山脚, top 为山顶, end 为右山脚,
end - start + 1 即为当前山的跨度, 然后从 end 处开始寻找下一座山 (因为下一座山的
左山脚不可能存在于 start + 1 和 end - 1 之间; 假设存在, 计为 k, k 要么小于等于
top, 要么大于 top, 如果 k 小于等于 top, 则 k-top-end 组成一座山, 但是这座山不是
局部最优解, 因为有 start-top-end 这座跨度更大的山; 如果 k 大于 top, 由于 top 到
end 是递减的, 所以这种情况不存在满足条件的山);

寻找山顶和山脚的过程同 941_Valid-Mountain-Array.py
    """
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0

        max_length = 0
        length = len(arr)
        i = 0

        while i < length:
            start, top, end = i, i, i
            # jy: while 循环, 找出真正的 top 下标;
            while top + 1 < length:
                if arr[top + 1] <= arr[top]:
                    break
                top += 1
            # jy: end 先更新为 top;
            end = top
            # jy: while 循环, 找出真正的 end 下标;
            while end + 1 < length:
                if arr[end + 1] >= arr[end]:
                    break
                end += 1
            # jy: 如果 start 跟 top 不相同, 且 top 跟 end 不相同, 则表示 start-top-end 是一座
            #    真正的 mountain, 此时判断当前 mountain 的跨度, 看是否是更长的 mountain, 是则
            #    更新;
            if start != top and top != end:
                max_length = max(max_length, end - start + 1)
            # jy: 如果当 top 跟 end 位置相等时, i 赋值为 end+1 (否则还是赋值为 end 的话, 可能会
            #    进入死循环, 如以下的第一个示例中, 此处改为 i = end 会进入死循环); 且按理解, 如
            #    果 end == top, 那么它不可能是下一座 mountain 的 start, 故如果 top == end 时, 下
            #    一座 mountain 应从 end+1 开始;
            i = end + 1 if top == end else end
            # i = end

        return max_length


arr = [2,1,4,7,3,2,5]
# Output: 5
res = Solution().longestMountain(arr)
print(res)


arr = [2,2,2]
# Output: 0
res = Solution().longestMountain(arr)
print(res)


# jy: 这种情况的最大 moutain 长度仍为 5, 因为数组后的 6 个数值单向递增, 不能视
#    为 mounatin (代码逻辑中不能符合此要求: start != top and top != end, 故不
#     视为 mountain)
arr = [2,1,4,7,3,2,5,6,7,8,9]
# Output: 5
res = Solution().longestMountain(arr)
print(res)


