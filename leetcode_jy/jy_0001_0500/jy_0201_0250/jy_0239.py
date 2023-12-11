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
title_jy = "Sliding-Window-Maximum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array
to the very right. You can only see the k numbers in the window. Each time the sliding window moves right
by one position. Return the max sliding window.


Example:
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], and k = 3
Output: [3, 3, 5, 5, 6, 7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


Note: You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up: Could you solve it in linear time?
"""



from heapq import heapify, heappop, heappush
from collections import deque
from typing import List

class Solution:
    """
解法1: 类似 703_Kth-Largest-Element-in-a-Stream.py, 都是求动态数组中的最大值, 在窗口滑动时, 维护一个
最大堆, 堆顶的元素就是当前窗口的最大值; 由于 Python 的 heapq 是最小堆, 我们可以将数组的元素取反再加入
堆中, 这样堆顶的最小值取反后就是当前窗口的最大值;

在窗口滑动时, 窗口左侧会移除一个元素, 同时窗口右侧进入一个元素, 这里并不需要从堆中删除移出的元素, 只要
判断堆顶元素的下标是否还在窗口中, 如果堆顶元素落在了窗口外, 则需要删除堆顶元素, 直到堆顶元素再次落到窗
口中;

算法时间复杂度分析: 初始 k 个元素的堆化需要 O(k), 循环时遇到的最坏的情况是数组按升序排列, 这样堆顶的
元素永远是刚进入滑动窗口的元素, 堆内元素的大小一直在增加, 堆中加入元素的时间复杂度为 O(lgn), 所以循环
体的时间复杂度为 lg(k) + lg(k+1) + ... + lg(n) = lg(n!/(k-1)!), 整体时间复杂度为 k + lg(n!/(k-1)!), 当
k = 2 时, 复杂度变为 2 + lg(n!);
相关证明见 167_Two-Sum-II-Input-array-is-sorted.py 中的解法1, 即算法的时间复杂度存在不是线性的情况;
    """
    def maxSlidingWindow_v1(self, nums: List[int], k: int) -> List[int]:
        # jy: 对原数组中的前 k 个数值进行取反后最小堆化(这样堆顶的最小值就是原先的最大值);
        #    注意此时堆中的数值为原数组数值以及其对应的下标所组成的元组;
        heap = [(-nums[i], i) for i in range(k)]
        heapify(heap)
        # jy: result 的第一个数值即初始化时的堆顶元素的相反数;
        result = [-heap[0][0]] if heap else []
        # jy: 总共有 len(nums)-k+1 个滑动窗口, 且初始下标为 0 的滑动窗口已经完成, 现在只需完成初始
        #    下标为 1 开始的剩余滑动窗口;
        for i in range(1, len(nums) - k+1):
            # jy: 如果堆顶元素(最小值, 相反数为最大值)对应的下标小于当前窗口的起始下标, 则需将该元
            #    素从堆中剔除, 因为它不属于当前窗口范围之内的元素(剔除后自然会有新的最小值成为堆顶);
            while heap and heap[0][1] < i:
                heappop(heap)
            # jy: 将当前窗口的末尾下标(即下标为 i+k-1 的元素)对应的元素入堆;
            heappush(heap, (-nums[i+k-1], i+k-1))
            # jy: 经过以上, 当前窗口元素已经全在堆中, 且堆顶元素值的相反数即为当前窗口中的最大值;
            result.append(-heap[0][0])

        return result


    """
解法2: 巧妙地利用了双端队列: 遍历数组, 然后判断队列右侧的元素是否小于等于当前元素, 如果是则将
这些元素从队列右侧出队(因为这些出队的元素不影响最大值的判断), 并将当前元素从队列右侧入队, 这样
就保证了队列左侧的队首元素始终是最大的, 即队列左侧的队首元素就是每个滑动窗口的最大值;

实际代码中双端队列存储的是元素在数组中的下标, 因为循环数组时还需要先判断队列左侧的队首的元素是否
已经位于滑动窗口之外, 如果是则需要将队首元素出队;

双端队列的入队和出队都是的时间复杂度 O(1), 而从队列右侧的出队这个操作来说每个元素至多只会出队一
次, 所以整个循环的时间复杂度为 O(n);
    """
    def maxSlidingWindow_v2(self, nums: List[int], k: int) -> List[int]:
        # jy: 队列, 记录的是数组元素的下标
        queue = deque()
        result = []

        for i, value in enumerate(nums):
            # jy: 如果数组元素下标大于或等于 k 且队尾元素(记录的是数组元素的下标)小于或等于当前窗口
            #    的起始下标的前一个下标(即 i-k), 则将队尾元素剔除(即从队列左侧删除);
            # jy: 此处 i >= k 可以去掉, 去掉后 i-k 有可能小于 0, 但小于 0 时后半部分肯定是不满足的;
            #    当要使得后半部分满足, 也必然有 i >= k 了;
            # if i >= k and queue[0] <= i-k:
            if queue and queue[0] <= i-k:
                queue.popleft()
            # jy: 如果队列不为空, 且队首元素小于或等于当前元素, 则将队首元素出队, 直到队首元素大于
            #    当前元素为止才停止出队, 并将当前数组元素的下标入队(右侧入队); 该逻辑确保了队首的
            #    元素一定是小于队尾的元素, 且从队首到队尾(从右到左)是升序排序的;
            while queue and nums[queue[-1]] <= value:
                queue.pop()
            queue.append(i)
            # jy: 当 i 大于 k-1 的时候(即初始化第一个滑动窗口之后), 开始每次循环都将队尾(队列左侧)
            #    的元素(最大值)加入 result 中(i 从 k-1 到 len(num)-1 都会往 result 中加入元素, 共
            #    加入 len(nums)-k+1 个值);
            if i >= k-1:
                result.append(nums[queue[0]])

        return result


    """
jy: 依据数组大小和 k , 可以确定最终返回的数组的元素个数, 即可作为循环的次数, 并每次确定出滑动窗口的起始下标,
同时根据 k 可知滑动窗口的末尾下标, 每次循环都从 nums 中截取滑动窗口部分, 并求得 max 值加入 result 数组中;

该方法提交 LeetCode 会超时;
    """
    def maxSlidingWindow_jy(self, nums: List[int], k: int) -> List[int]:
        len_ = len(nums)
        # jy: 返回的数组中共有 len_ - k + 1 个数值;
        result = []
        # jy: 第一个窗口的起始下标为 0, 最后一个窗口的起始下标为 (len_ - k)
        for i in range(len_ - k+1):
            # print("=======", i)
            result.append(max(nums[i: i + k]))
        return result






nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# Output: [3, 3, 5, 5, 6, 7]
res = Solution().maxSlidingWindow_v1(nums, k)
print(res)

res = Solution().maxSlidingWindow_v2(nums, k)
print(res)

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# print(max(nums[0:k+1]))
res = Solution().maxSlidingWindow_jy(nums, k)
print(res)


