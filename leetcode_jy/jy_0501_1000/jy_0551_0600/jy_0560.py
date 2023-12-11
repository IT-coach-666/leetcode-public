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
title_jy = "Subarray-Sum-Equals-K(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of integers and an integer k, you need to find the total number of
continuous subarrays whose sum equals to k.


Example 1:
Input: nums = [1,1,1], k = 2
Output: 2


Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""


from typing import List
from collections import deque

class Solution:
    """
解法1 (超时): 由于要求数组中连续元素的和, 所以可以先构建一个数组 sums, 使得;
sums[i] = nums[0] + nums[1] + ... + nums[i]
则:
sums[j] - sums[i] = nums[i+1] + ... + nums[j], 即 nums[i+1] 到 nums[j] 的连续
元素的和; 所以如果存在 sums[j] - sums[i] + nums[i] == k, 则表示找到了连续的数
组元素 nums[i], nums[i+1], ..., nums[j], 其和为 k; 但是由于嵌套遍历数组, 会使此题超时;
    """
    def subarraySum_v1(self, nums: List[int], k: int) -> int:
        sums = [0] * len(nums)
        sum = 0
        count = 0
        # jy: 构建数组 sums, 使得 sums[i] = nums[0] + nums[1] + ... + nums[i]
        for i, value in enumerate(nums):
            sum += value
            sums[i] = sum

        for i in range(len(nums)):
            # jy: 遍历数组 nums, 如果有单独的数值为 k, 则目标方案数 count 加 1;
            #    注意, 此处不能加 continue, 因为当 sums[j] - sums[i] 为 0 时,
            #    如果 nums[i] 为 k, 此时 sums[j] - sums[i] + nums[i] 也为 k, 如
            #    果此处加 continue, 则就少算了一些可能性方案;
            if nums[i] == k:
                count += 1
                # continue

            # jy: 从数组下标从 i+1 开始遍历(主要是为了获取数组 sums[j], 与下标 i 对
            #    应的 sums[i] 进行运算比较), 找出满足 sums[j] - sums[i] + nums[i] == k
            #    的方案, 找到则 count 数加 1;
            for j in range(i+1, len(nums)):
                if sums[j] - sums[i] + nums[i] == k:
                    count += 1
        # jy: 最终返回 count 数即可;
        return count


    """
解法:2 在 001_Two-Sum.py 中使用了哈希表来存放访问过的数组元素, 同时遍历数组判断 target - n 是
否在哈希表中, 此题也可采用类似的思路;

遍历 nums, 对于子数组 nums[0], nums[1], ..., nums[i] 来说:
如果存在 0 <= j <= i 使得:
nums[j] + nums[j+1] + ... + nums[i] = k
(这里为什么不是存在 0 <= j <= p < i, 使得: nums[j] + nums[j+1] + ... + nums[p] = k ? 因为如果存
在 p < i, 则在数组遍历到下标 p 时已经判断过了, 无需再次判断)
则(sums 的定义同解法 1):
nums[0] + nums[1] + ... + nums[j-1] = sums[i] - k

即将问题转换为找出 j (0 <= j <= i) 使得:
sums[j-1] = sums[i] - k
则此时: nums[j] + nums[j+1] + ... + nums[i] = k

为了快速判断 sums[i] - k 是否存在于 sums 中, 可将 sums 中的元素作为键(key)放入哈希表中; 由于最后
需要返回满足条件的子数组的个数, 所以哈希表的值(value)为 sums 中的元素出现的次数;

另外要注意的是, 哈希表的初始元素为 {0: 1}, 因为当 sums[i] - k = 0 时, 正好满足条件 (此时不需要
sums[j-1] 的存在), 为了在哈希表命中 sums[i] - k = 0 的情况, 需要提前初始化 0 到哈希表中;

JY: 如果需要获取符合要求的连续子数组, 需要在字典 sum_mapping 的 value 中记录所有和为 key 的下
标, 可以将 value 的值由数值改为列表记录, 列表的长度即为和为 key 的出现次数;
    """
    def subarraySum_v2(self, nums: List[int], k: int) -> int:
        sum = 0
        count = 0
        sum_mapping = {0: 1}
        # jy: 遍历 nums 数组, 求截止数组当前数值的 sum, 将其作为 key 加入到字典中, 字典中其对应的
        #    值为该 sum 出现的次数; 如果当前 sum 减掉 k 的结果出现在字典中, 则表明出现:
        #    sums[i] - k = sums[j-1]  (其中 0 <= j <= i, 因为提前加入字典中的数值对应的下标肯定
        #    是比当前 sum 值对应的下标小的), 故表明存在 nums[j] + nums[j+1] + ... + nums[i] = k
        #    有多少种这种情况, 则取决于 sums[j-1] (即 sums[i]-k) 的数量有多少;
        for n in nums:
            sum += n
            # jy: 注意, 要先 if 判断后再将当前 sum 加入到字典中, 因为 if 判断中是需要用到先前字典
            #    中积累的值的;
            if sum - k in sum_mapping:
                count += sum_mapping[sum - k]
            sum_mapping[sum] = sum_mapping.get(sum, 0) + 1

        return count


    """
滑动窗口解法: 定义 paths 保存所有符合要求的子数组; 初始化窗口 path 为空列表 [], 遍
历 nums, 不断将元素加入列表, 并统计列表中的元素和 sum_window, 加入当前遍历的元素后:
1) 如果 sum_window 小于目标值 k, 则继续循环遍历;
2) 如果 sum_window 等于目标值 k, 则将等于目标值 k 的 path 加入 paths 中, 并从 path 左
   侧出一元素, 继续循环遍历;
3) 如果 sum_window 大于目标值 k, 则不断从 path 左侧出元素, 直到 path 中的元素小于或等
   于 k, 并进一步判断是否等于 k, 等于则重复步骤 "2)" 中的操作;

以上思路对包含负数的列表可能无效, 如以下示例(待改进):
nums = [-1,-1,1]
k = 0
    """
    def subarraySum_jy(self, nums: List[int], k: int) -> int:
        paths = []
        path = deque([])
        sum_window = 0

        for n in nums:
            path.append(n)
            sum_window += n

            if sum_window < k:
                continue
            elif sum_window == k and len(path) != 0:
                paths.append(path)
                removed = path.popleft()
                sum_window -= removed
            else:
                while sum_window > k:
                    removed = path.popleft()
                    sum_window -= removed
                if sum_window == k and len(path) != 0:
                    paths.append(path)
                    removed = path.popleft()
                    sum_window -= removed

        return len(paths)


nums = [1,1,1]
k = 2
res = Solution().subarraySum_v1(nums, k)
print(res)

res = Solution().subarraySum_v2(nums, k)
print(res)


nums = [1,1,1]
k = 2
res = Solution().subarraySum_jy(nums, k)
print(res)


