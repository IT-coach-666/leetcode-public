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
title_jy = "Jump-Game(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 循环 | 相似题: 0045"


"""
Given an array of non-negative integers `nums`, you are initially positioned
at the first index of the array. Each element in the array represents your 
maximum jump length at that position. Determine if you are able to reach the
last index.


Example 1:
Input: nums = [2, 3, 1, 1, 4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3, 2, 1, 0, 4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump
             length is 0, which makes it impossible to reach the last index.


Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""



class Solution:
    """
解法 1: 递归搜索 (超时, 解法 4 中进行了优化)

对于 nums 中的每个数字 nums[i], 尝试走 1 至 nums[i] 步 (递归方法中的第 2 个
参数记录当前已走到的位置)
    """
    def canJump_v1(self, nums: List[int]) -> bool:
        # jy: 从 nums[0] 的位置开始尝试走, 尝试走 1 至 nums[0] 步:
        #     走 1 步时, 后续递归过程会从 nums[1] 的位置开始走, 走 1 至 nums[1] 步
        #     走 2 步时, 后续递归过程会从 nums[1] 的位置开始走, 走 1 至 nums[2] 步
        return self._dfs(nums, 0)

    def _dfs(self, nums, start):
        """
        从 nums[start] 的位置开始走, 不断尝试走 1 到 nums[start] 步, 看是
        否能走到终点位置
        """
        # jy: 如果已经递归到从最后一个位置的下一个位置开始走, 表明上一个递归
        #     过程已经走到最后一个位置了, 直接返回 True, 终止递归
        if start == len(nums):
            return True

        # jy: 不断尝试走 1 到 nums[start] 步 (假设为 step 步), 则下一轮递归将
        #     从 nums[start + step] 位置开始走, 走 1 到 nums[start + step] 步
        for step in range(1, nums[start] + 1):
            if self._dfs(nums, start + step):
                return True

        # jy: 以下不能直接 "return False", 否则当传入的 nums = [0] 时, 以上的
        #     for 循环不会走任何一步, 因此缺少了递归调用过程, 但此时已经到最后
        #     一个位置了, 应返回 True; 当 nums = [2, 0, 0] 时同理, 因此需使用
        #     以下返回逻辑
        return nums[start] == 0 and start == len(nums) - 1


    """
解法 2: 遍历 nums, 记录至今能走到的最远位置, 如果该位置小于 nums 的下标, 则
说明无法到达后面的位置, 否则根据当前步长更新能走到的最远位置
    """
    def canJump_v2(self, nums: List[int]) -> bool:
        # jy: 记录截止 nums[i] 为止能走到的最远位置 (位置均用列表下标表示, 初
        #     始化为第一个位置下标 0)
        end = 0
        n = len(nums)
        # jy: 遍历列表的下标位置 i, 从该位置最多能往后跳 nums[i] 步, 假设截止
        #     下标位置 i 时能跳到的最远距离为 end, 则有 end = i + nums[i], 如
        #     果 end 已经大于或等于最后一个下标位置, 表明能跳到最后一个位置;
        #     如果在准备遍历下一个位置 i 时, 上一轮能跳到的最远距离 end 比 i 
        #     还小, 表明上一轮不能跳到 i 位置, 无法跳的更远, 故不能跳到最后,
        #     因此直接返回 False
        # jy: 实际上只需要遍历到倒数第二个位置即可, 因为如果能跳到倒数第二个
        #     位置 (下标为 n-2), 即可计算从该位置往后能跳多远, 从而判断是否
        #     能跳到最后一个位置
        for i in range(n-1):
            # jy: 如果上一轮能跳到的最远距离 end 不能到达当前位置 i, 则一定
            #     不呢跳转到最后一个位置
            if i > end:
                return False
            # jy: 基于当前能走的最大步数更新从位置 i 能跳到的最远位置
            end = max(end, i + nums[i])
            # jy: 优化, 提前终止
            if end >= n-1:
                return True
        return end >= n-1


    """
解法 3: 解法 2 的更简洁写法
    """
    def canJump_v3(self, nums: List[int]) -> bool:
        # jy: 初始化当前能到达最远的位置
        max_idx = 0
        # jy: i 为当前位置, jump 是当前位置的跳数
        for i, jump in enumerate(nums):
            # jy: 如果当前位置能到达 (max_idx >= i), 且 i + jump > max_idx,
            #     则更新 max_idx
            # if max_i >= i and i + jump > max_i:
            if i + jump > max_idx >= i:
                max_idx = i + jump
        return max_idx >= i


    """
解法 4: 结合解法 2 中的思路, 优化解法 1 中的递归逻辑
    """
    def canJump_v4(self, nums: List[int]) -> bool:
        return self._dfs4(nums, 0, 0)

    def _dfs4(self, nums, cur_idx, max_idx):
        if max_idx < cur_idx:
            return False
        if max_idx >= len(nums):
            return True

        if cur_idx + nums[cur_idx] > max_idx:
            return self._dfs4(nums, cur_idx+1, cur_idx + nums[cur_idx])
        if self._dfs4(nums, cur_idx+1, max_idx):
            return True
        return nums[cur_idx] == 0 and cur_idx == len(nums) - 1


nums = [2, 3, 1, 1, 4]
# Output: true
res = Solution().canJump_v1(nums)
print(res)


nums = [3, 2, 1, 0, 4]
# Output: false
res = Solution().canJump_v2(nums)
print(res)


nums = [3, 2, 1, 0, 4]
# Output: false
res = Solution().canJump_v3(nums)
print(res)


nums = [3, 2, 1, 0, 4]
# Output: false
res = Solution().canJump_v4(nums)
print(res)

