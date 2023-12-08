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
title_jy = "Kth-Largest-Element-in-an-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element
in the sorted order, not the kth distinct element.


Example 1:
Input: [3, 2, 1, 5, 6, 4] and k = 2
Output: 5

Example 2:
Input: [3, 2, 3, 1, 2, 4, 5, 5, 6] and k = 4
Output: 4


Note: You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

from typing import List
from heapq import heappush, heappop


class Solution:
    """
解法1: 对数组倒序排序, 然后直接返回下标为 k-1 的元素即可(或正向排序后返回第 len(nums)-k 个);;
    """
    def findKthLargest_v1(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


    """
解法2: 同 703_Kth-Largest-Element-in-a-Stream.py 的解法 2, 维护一个 k 个元素的最小堆来求解;
    """
    def findKthLargest_v2(self, nums: List[int], k: int) -> int:
        heap = []
        # jy: 将列表元素入堆, 如果堆元素大于 k 个, 则将大于 k 部分的出堆(确保堆中只有 k 个),
        #    则堆顶即为第 k 大元素值(堆顶元素为堆中元素的最小值);
        for n in nums:
            heappush(heap, n)
            if len(heap) > k:
                heappop(heap)

        return heap[0]


    """
解法3: 快速排序思想: 在快排中, 会挑选一个 pivot, 然后将数组中小于 pivot 的元素放到它的前面, 将
大于它的元素放到它的后面; 利用这一点, 我们可以对数组执行一次分割, 选择一个 pivot, 由于要求的是
第 k 大的元素, 所以我们将大于 pivot 的元素放到 pivot 的前面, 将小于 pivot 的元素放到它的后面,
同时返回一个数组的下标 p:
如果 p = k-1, 则说明 nums[p] 就是第 k 大的元素;
如果 p > k-1, 说明第 k 大的数在 p 的左侧, 则对数组 nums[0]...nums[p-1] 重新进行分割
如果 p < k-1, 说明第 k 大的数在 p 的右侧, 则对数组 nums[p+1]...nums[L-1] 重新进行分割(L 表示数组长度)
    """
    def findKthLargest_v3(self, nums: List[int], k: int) -> int:
        low, high = 0, len(nums) - 1

        while True:
            p = self._partition(nums, low, high)

            if p == k-1:
                return nums[p]
            elif p > k-1:
                high = p-1
            else:
                low = p+1

    def _partition(self, nums: List[int], low: int, high: int):
        # jy: pivot 是可以任意选取的, 此处选择数组的中间下标作为 pivot;
        pivot = (low + high) // 2
        # jy: 将 pivot 的值暂存起来;
        pivot_value = nums[pivot]
        # jy: 将 pivot 和 high 对应的值替换, 将 pivot_value 换到 nums[high] 中;
        nums[pivot], nums[high] = nums[high], nums[pivot]

        # jy: p 初始化为 low, 以下 for 循环必须从 low 开始(注意, 不能将两者都改成从 low+1 开始);
        p = low
        for i in range(low, high):
            # jy: 如果当前下标 i 对应的值大于或等于 pivot_value, 则将该值与 p 下标值进行替换,
            #    使得大于或等于 pivot_value 的值都被替换到左边;
            if nums[i] >= pivot_value:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        # jy: 经过以上循环后, nums[:p] 都是大于或等于 pivot_value 的值, nums[p] 为小于或等于
        #    pivot_value 的值(因为原先的 pivot_value 被替换到 nums[high] 了, 且大于或等于
        #    pivot_value 的值都已经被放置 p 下标左侧, 注意 nums[high] 没有包括在 以上 for 循
        #    环中, 而是被暂存起来了, 此时已经确保 p 的左侧已经是大于或等于 pivot_value, 则
        #    将原先的 pivot_value, 即 nums[high] 归位到属于它的位置 p)
        # print("========", nums[:p],  pivot_value)  # jy: p 左侧肯定大于或等于 pivot_value
        # print("========", nums[p:],  pivot_value)  # jy: p 以及其右侧肯定小于或等于 pivot_value
        # jy: 将 high(即原先的 pivot 对应的值, 因为原先发生替换) 和 p 的值替换, 实现 pivot_value
        #    的正确定位;
        # print("========", nums[high] == pivot_value)
        nums[high], nums[p] = nums[p], nums[high]
        # print("========", nums[p] == pivot_value)

        return p

nums = [3, 2, 1, 5, 6, 4]
k = 2
# Output: 5
res = Solution().findKthLargest_v2(nums, k)
print(res)


nums = [3, 2, 1, 5, 6, 4]
k = 2
# Output: 5
res = Solution().findKthLargest_v3(nums, k)
print(res)

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
# Output: 4
res = Solution().findKthLargest_v3(nums, k)
print(res)


