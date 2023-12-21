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
title_jy = "Jump-Game-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "动态规划 | 贪心 | IMP | 相似题: 0055"


"""
Given an array of non-negative integers `nums`, you are initially positioned
at the first index of the array. Each element in the array represents your 
maximum jump length at that position. Your goal is to reach the last index 
in the minimum number of jumps. You can assume that you can always reach the
last index.


Example 1:
Input: nums = [2, 3, 1, 1, 4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
             Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2, 3, 0, 1, 4]
Output: 2


Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
"""


class Solution:
    """
解法 1: 动态规划 (超时), 时间复杂度为 O(n^2), 空间复杂度 O(n)

定义 dp[i] 表示跳到下标位置 i 所需要的最小跳跃次数
    """
    def jump_v1(self, nums: List[int]) -> int:
        size = len(nums)
        # jy: 初始化 dp[i] 均为极大值
        dp = [float("inf") for _ in range(size)]
        # jy: 跳到下标 0 需要的最小跳跃次数为 0
        dp[0] = 0
        # jy: 
        for i in range(1, size):
            # jy: 尝试从位置 j 往后跳, 如果能跳到的最远位置大于等于 i, 且
            #     dp[j] + 1 比原先的 dp[i] 更小, 则更新 dp[i] = dp[j] + 1
            for j in range(i):
                if j + nums[j] >= i:
                    # jy: 由于 dp[i] 的求解从前往后, 且 j < i, 因此 dp[j]
                    #     在使用之前已经被求解过
                    dp[i] = min(dp[i], dp[j] + 1)
        # jy: 返回最后一个下标位置所需要跳几次
        return dp[size - 1]


    """
解法 2: 动态规划 + 贪心 (优化解法 1); 时间复杂度 O(n), 空间复杂度 O(n)

如果跳到下标 i 最少需要 5 步, 即 dp[i] = 5, 则必然不可能出现少于 5 步就能
跳到下标 i+1 的情况, 跳到下标 i+1 至少需要 5 步或更多步, 因此 dp[i] 是单调
递增的, 即: dp[i-1] <= dp[i] <= dp[i+1]

因此在更新 dp[i] 时, 可以找最早可以跳到 i 的点 j, 从该点更新 dp[i]; 即找到
满足 j + nums[j] >= i 的第一个 j, 使得 dp[i] = dp[j] + 1, 而查找第一个 j 的
过程可以通过使用一个指针变量 j 从前向后迭代查找
    """
    def jump_v2(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [float("inf") for _ in range(size)]
        dp[0] = 0

        j = 0
        for i in range(1, size):
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1

        return dp[size - 1]


    """
解法 3: 贪心算法; 时间复杂度 O(n), 空间复杂度 O(1)

如果第 i 个位置所能跳到的位置为 [i+1, i + nums[i]], 则有:
1) 第 0 个位置所能跳到的位置就是 [0 + 1, 0 + nums[0]], 即 [1, nums[0]]
2) 第 1 个位置所能跳到的位置就是 [1 + 1, 1 + nums[1]], 即 [2, 1 + nums[1]]
......

对于每一个位置 i 来说, 所能跳到的所有位置都可以作为下一个起跳点, 为了尽可能
使用最少的跳跃次数, 我们应该使得下一次起跳所能达到的位置尽可能的远; 简单来说
就是每次在「可跳范围」内选择可以使下一次跳的更远的位置, 这样才能获得最少跳
跃次数; 具体做法:
1) 维护几个变量: 
   current_end: 当前所能达到的最远位置
   max_end: 下一步所能跳到的最远位置
   jumps: 最少跳跃次数
2) 遍历数组 nums 的前 len(nums) - 1 个元素:
   a) 每次更新第 i 位置下一步所能跳到的最远位置 max_end
   b) 如果下标位置 i 到达 current_end, 则更新 current_end 为新的当前位
      置 max_end, 并令步数 jumps 加 1
3) 最终返回跳跃次数 jumps

在 0055 (Jump-Game) 的基础上补充 current_end 和 jumps 的相关逻辑

以 nums = [2, 3, 1, 1, 4] 作为示例进行思考
    """
    def jump_v3(self, nums: List[int]) -> int:
        # jy: 记录最少跳几次能到末尾位置 (题目中已确保肯定能跳到最后)
        jumps = 0
        # jy: 记录每跳一次之后的所在位置, 初始化为第一个位置 (下标为 0)
        current_end = 0
        # jy: 记录截止当前位置为止, 能往后跳到的最远距离
        max_end = 0
        # jy: 遍历 nums 中的位置至倒数第二个位置 (即 len(nums) - 2)
        # jy: 注意: 必须循环到倒数第二个位置就终止; 如果循环到最后一个位
        #     置 (即 n-1), 则会出错 (0055 中也可以循环到最后一个位置)
        for i in range(len(nums) - 1):
            # jy: 更新截止当前位置 i 为止能跳到的最远距离
            max_end = max(max_end, i + nums[i])
            # jy: 当上一跳所能跳到的最远位置(即 current_end)等于当前位置 i
            #     时, 进行下一跳(jumps 跳数加 1), 同时 current_end 更新为截
            #     止当前位置 i 以及之前的位置, 往后跳一次能跳到的最远位置
            if i == current_end:
                jumps += 1
                #print("i=%s, jumps=%s, current_end=%s, max_end=%s" % (i, jumps, current_end, max_end))
                current_end = max_end

        return jumps


    """
解法 4: 同解法 3, 代码略有区别 (可遍历至最后一个位置)
    """
    def jump_v4(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        max_end = 0
        # jy: 与解法 1 的区别: 循环时必须循环到最后一个位置
        for i in range(len(nums)):
            # jy: 当 current_end 小于 i 时, 表明需要跳下一次了, 并将跳下一次
            #     能跳到的最远距离赋值给 current_end
            if current_end < i:
                jumps += 1
                current_end = max_end

            # jy: 更新截止当前位置为止所能跳到的最远距离
            max_end = max(max_end, i + nums[i])
        return jumps



nums = [2, 3, 1, 1, 4]
# Output: 2
res = Solution().jump_v1(nums)
print(res)


nums = [2, 3, 0, 1, 4]
# Output: 2
res = Solution().jump_v2(nums)
print(res)


nums = [2, 3, 0, 1, 4]
# Output: 2
res = Solution().jump_v3(nums)
print(res)


nums = [2, 3, 0, 1, 4]
# Output: 2
res = Solution().jump_v4(nums)
print(res)

