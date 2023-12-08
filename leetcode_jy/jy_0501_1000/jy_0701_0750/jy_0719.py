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
title_jy = "Find-K-th-Smallest-Pair-Distance(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array, return the k-th smallest distance among all the pairs. The
distance of a pair (A, B) is defined as the absolute difference between A and B.


Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.


Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
"""


from typing import List


class Solution:
    """
首先将数组排序, 求出首尾数字的差值作为最大距离, 在 0 和最大距离间进行二分查找;

二分查找时, 根据 middle 判断哪边 (middle 代表的是距离, 距离区间有 [low, middle] 和
[middle+1, high] , 其中目标距离只能在两个区间中的一个) 的距离使得数组元素有超过或等
于 k 对满足条件的差值对 (如: 小于或等于的 middle 的 pair 至少有 k 个, 则表明要获取某
个 pair 的距离, 且小于或等于该距离的 pair 为 k 个的话, 该距离肯定在 [low, middle] 之
间), 即可舍弃另一半的不满足条件的距离;
    """
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # jy: 对数组进行排序, 并计算首尾数字的差值作为最大距离(0 是最小距离, 因为距离是以绝对值的形式表示)
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        # jy: 在 0 和最大距离间进行二分查找,
        while low < high:
            # jy: 二分查找时, 根据 middle 判断有序数组中距离小于或等于 middle 的 pair 的个数是否
            #    大于或等于 k 个 (目标是求某个 pair 的距离 distance, 且小于或等于该 distance 的
            #    pair 总共有 k 个, 即该 distance 是所有的 pair 的距离的第 k 小的):
            #    1) 如果数组中距离小于或等于 middle 的 pair 的个数大于或等于 k 个, 表明目标所求
            #       的距离在 low 和 middle 之间;
            #    2) 如果数组中距离小于或等于 middle 的 pair 的个数小于 k 个, 表明目标所求的距离
            #       在 middle+1 和 high 之间;
            middle = low + (high - low) // 2
            if self._has_more_than_k_pairs(nums, k, middle):
                high = middle
            else:
                low = middle + 1
        # jy: 注意, 最开始的 low 以及循环过程中的 middle 对应的距离不一定正好等于某个 pair 对应的
        #    距离值, 但以上不断循环过程中会最终求得距离等于 low 的 pair 个数大于或等于 k 个(当距
        #    离等于 low 的 pair 有多个时, pair 个数大于 k 个, 否则 pair 的个数正好为 k 个)
        print("================test============", self._has_more_than_k_pairs(nums, k, low))
        return low

    def _has_more_than_k_pairs(self, nums: List[int], k: int, middle_distance: int) -> bool:
        """判断有序数组 nums 中距离小于或等于 middle_distance 的 pair 的个数是否大于或等于 k 个"""
        count = 0
        left = 0
        # jy: 遍历数组下标, 将该下标对应元素看做 pair 中的较大值;
        for right in range(len(nums)):
            # jy: 如果 (nums[left], nums[right]) 组成的 pair 的距离大于 middle_distance, 则
            #    left 向右移, 直到对应的 pair 距离小于或等于 middle_distance; 此时用 count
            #    变量统计距离小于或等于 middle_distance 的 pair 的个数;
            while nums[right] - nums[left] > middle_distance:
                left += 1
            count += right - left
            # jy: 如果距离小于或等于 middle_distance 的 pair 的个数大于或等于 k 个, 则返回 Ture;
            if count >= k:
                print("============== ", count)
                return True

        return False


nums = [1,3,1]
k = 1
# Output: 0
res = Solution().smallestDistancePair(nums, k)
print(res)


nums = [1,2,4,7,11, 16]
k = 8
# Output: 6
res = Solution().smallestDistancePair(nums, k)
print(res)


nums = [1,6,1]
k = 3
# Output: 5
res = Solution().smallestDistancePair(nums, k)
print(res)


