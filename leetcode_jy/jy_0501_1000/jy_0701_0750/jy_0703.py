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
title_jy = "Kth-Largest-Element-in-a-Stream(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest
element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array
nums, which contains initial elements from the stream. For each call to the method KthLargest.add,
return the element representing the kth largest element in the stream.


Example:
int k = 3;
int[] arr = [4, 5, 8, 2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8


Note: You may assume that nums' length ≥ k-1 and k ≥ 1.
"""

from typing import List
from heapq import heappush, heappop, heapify


"""
解法1: 粗暴的解法是每次添加元素的时候对数组倒序排序, 然后直接返回下标为 k-1 的元素即可
      (或正向排序后返回第 len(nums)-k 个);
"""
class KthLargest_v1:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)

        return self.nums[self.k - 1]


"""
解法2: 最小堆; 维护一个只有 k 个元素的最小堆, 那么堆顶的元素就是第 k 大的元素
      (最小堆的堆顶元素是堆中最小的);
类初始化时: 先将元素加入堆中, 如果堆元素个数大于 k, 则移除堆顶的元素, 此时最小
            堆会将剩余元素中最小的放到堆顶(即始终保证堆顶的元素是第 k 大元素)
add 方法: 如果当前堆的元素数量达到了 k, 并且堆顶的元素大于需要添加的元素, 则无
          需添加, 因为新元素不会影响现有堆的排序;
"""
class KthLargest_v2:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [n for n in nums]
        # jy: 将 self.heap 列表进行堆化, 形成最小堆;
        heapify(self.heap)
        # jy: 如果堆中元素大于 k, 则不断 pop 出堆顶元素, 直到堆元素为 k 个为止;
        while len(self.heap) > self.k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        # jy: 如果最小堆中元素个数为 k 个, 且堆顶元素大于要添加的元素, 则直接返回堆顶元素;
        if len(self.heap) == self.k and self.heap[0] > val:
            return self.heap[0]
        # jy: 如果以上条件不满足, 则将元素入堆, 如果堆中元素大于 k, 则移除多余的元素, 最终
        #    返回堆顶元素(即第 k 大元素, 因为此时的堆有 k 个元素)
        heappush(self.heap, val)

        if len(self.heap) > self.k:
            heappop(self.heap)

        return self.heap[0]


k = 3
arr = [4, 5, 8, 2]
kthLargest = KthLargest_v1(3, arr)
print(kthLargest.add(3))   # returns 4
print(kthLargest.add(5))   # returns 5
print(kthLargest.add(10))  # returns 5
print(kthLargest.add(9))   # returns 8
print(kthLargest.add(4))   # returns 8

k = 3
arr = [4, 5, 8, 2]
kthLargest = KthLargest_v2(3, arr)
print(kthLargest.add(3))   # returns 4
print(kthLargest.add(5))   # returns 5
print(kthLargest.add(10))  # returns 5
print(kthLargest.add(9))   # returns 8
print(kthLargest.add(4))   # returns 8


