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
title_jy = "Replace-Elements-with-Greatest-Element-on-Right-Side(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array ``arr``, replace every element in that array with the greatest element
among the elements to its right, and replace the last element with -1. After doing so,
return the array.


Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.


Constraints:
1 <= arr.length <= 104
1 <= arr[i] <= 105
"""


from typing import List
import heapq


class Node(object):

    def __init__(self, value: int, index: int):
        self.value = value
        self.index = index

    def __lt__(self, other):
        return self.value < other.value


class Solution:
    """
解法1(超时):直接两层循环, 不过会超时;
    """
    def replaceElements_v1(self, arr: List[int]) -> List[int]:
        length = len(arr)

        for i in range(length):
            if i == length - 1:
                arr[i] = -1
                break

            max_number = arr[i+1]

            for j in range(i+2, length):
                max_number = max(max_number, arr[j])

            arr[i] = max_number

        return arr


    """
解法2: 从数组第二位到最后一位维护一个最大堆, 遍历数组, 最大堆堆顶的数字就是当前位置的
新值; 需要注意的是, 在维护最大堆的节点时, 除了记录节点的值, 同时还要记录节点值对应数组
中的索引位置, 当最大堆堆顶的元素在数组中的索引值小于等于当前数组位置时, 当前堆顶元素已
无效, 需要弹出堆顶;
    """
    def replaceElements_v2(self, arr: List[int]) -> List[int]:
        length = len(arr)
        # jy: 从数组的第二个位置开始对数值进行取反(取反后最大值即变成了最小值), 并结合其
        #    下标构造 Node; 基于 Node 列表构造最小堆, 堆顶值为最小值, 其相反数即为最大值;
        largest = [Node(-arr[i], i) for i in range(1, length)]
        # jy: 将 largest 数组最小堆化, 该操作后, largest 数组的第一个元素是数组中值最小的,
        #    但不能确保其是从小到大排序, 如果通过 heapq 对其进行操作, 则有最小堆的特性, 如
        #    heapq.heappop(largest) 会出最小值, 并且保证 largest[0] 又为当前最小值;
        heapq.heapify(largest)

        # jy: 如果最小堆的堆顶元素在原数组中的下标比当前位置下标小, 表明其不属于当前位置的后
        #    面的最大值(负最小值), 而是属于当前位置之前的, 将其出堆;
        for i in range(length):
            while largest and largest[0].index <= i:
                heapq.heappop(largest)

            arr[i] = -largest[0].value if largest else -1

        return arr





    """
解法3: 从数组尾往前遍历, 维护至今遇到的最大值, 将其更新到数组当前位置;
    """
    def replaceElements_v3(self, arr: List[int]) -> List[int]:
        # jy: 初始化最后一个数值为 -1;
        largest = -1
        # jy: 从后往前遍历, 先将当前位置的值 arr[i] 赋值为上一轮找到的最大值, 再
        #    更新截止当前位置为止的最大值, 不断循环;
        for i in range(len(arr) - 1, -1, -1):
            arr[i], largest = largest, max(largest, arr[i])

        return arr


arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
res = Solution().replaceElements_v1(arr)
print(res)


arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
res = Solution().replaceElements_v2(arr)
print(res)


arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
res = Solution().replaceElements_v3(arr)
print(res)


